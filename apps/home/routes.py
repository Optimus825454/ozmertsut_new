from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from apps.models import (
    MilkDelivery, MilkSupplier, FeedDelivery, Expense, Account, AccountType,
    Factory, FeedSupplier, Vehicle, FeedType, District, Village, Users, ReportTemplate,
    MilkFactoryDelivery
)
from datetime import datetime, timedelta
import json
from apps import db
from apps.home import blueprint
from sqlalchemy.sql import func

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
@login_required
def index():
    try:
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        first_day_of_month = today.replace(day=1)
        
        # Bugünkü süt miktarını hesapla
        today_milk = db.session.query(func.sum(MilkFactoryDelivery.quantity)).filter(
            func.date(MilkFactoryDelivery.delivery_date) == today
        ).scalar() or 0
        
        # Dünkü süt miktarını hesapla
        yesterday_milk = db.session.query(func.sum(MilkFactoryDelivery.quantity)).filter(
            func.date(MilkFactoryDelivery.delivery_date) == yesterday
        ).scalar() or 0
        
        # Yüzde değişimi hesapla
        milk_percentage = ((today_milk - yesterday_milk) / yesterday_milk * 100) if yesterday_milk > 0 else 0
        
        # Aylık yem gideri
        monthly_feed = FeedDelivery.query.filter(
            FeedDelivery.delivery_date >= first_day_of_month
        ).with_entities(db.func.sum(FeedDelivery.total_amount)).scalar() or 0
        
        # Geçen ayın yem gideri
        last_month_start = (first_day_of_month - timedelta(days=1)).replace(day=1)
        last_month_feed = FeedDelivery.query.filter(
            FeedDelivery.delivery_date.between(last_month_start, first_day_of_month)
        ).with_entities(db.func.sum(FeedDelivery.total_amount)).scalar() or 0
        
        # Yem gideri artış/azalış yüzdesi
        feed_percentage = 0
        if last_month_feed > 0:
            feed_percentage = ((monthly_feed - last_month_feed) / last_month_feed) * 100

        # Aktif tedarikçi sayısı
        supplier_count = MilkSupplier.query.filter_by(is_active=True).count()
        
        # Bu ay eklenen tedarikçi sayısı
        new_suppliers = MilkSupplier.query.filter(
            MilkSupplier.created_at >= first_day_of_month
        ).count()

        # Aylık toplam gider
        monthly_expense = Expense.query.filter(
            Expense.date >= first_day_of_month
        ).with_entities(db.func.sum(Expense.amount)).scalar() or 0
        
        # Geçen ayın gideri
        last_month_expense = Expense.query.filter(
            Expense.date.between(last_month_start, first_day_of_month)
        ).with_entities(db.func.sum(Expense.amount)).scalar() or 0
        
        # Gider artış/azalış yüzdesi
        expense_percentage = 0
        if last_month_expense > 0:
            expense_percentage = ((monthly_expense - last_month_expense) / last_month_expense) * 100

        # Son teslimatlar
        recent_deliveries = MilkFactoryDelivery.query.order_by(
            MilkFactoryDelivery.delivery_date.desc()
        ).limit(5).all()

        # Son 30 günlük süt alımı grafiği için veriler
        thirty_days_ago = today - timedelta(days=30)
        
        # Araçlara göre süt miktarı ve yağ oranı verileri
        vehicle_data = MilkFactoryDelivery.query.filter(
            MilkFactoryDelivery.delivery_date >= thirty_days_ago
        ).with_entities(
            db.func.date(MilkFactoryDelivery.delivery_date),
            MilkFactoryDelivery.vehicle_plate,
            db.func.sum(MilkFactoryDelivery.quantity),
            db.func.sum(db.func.coalesce(MilkFactoryDelivery.fat_ratio * MilkFactoryDelivery.quantity, 0)) / db.func.nullif(db.func.sum(MilkFactoryDelivery.quantity), 0)
        ).group_by(
            db.func.date(MilkFactoryDelivery.delivery_date),
            MilkFactoryDelivery.vehicle_plate
        ).order_by(
            db.func.date(MilkFactoryDelivery.delivery_date)
        ).all()

        # Benzersiz tarihleri ve araçları al
        dates = sorted(set(d[0].strftime('%d.%m') for d in vehicle_data)) if vehicle_data else []
        vehicles = sorted(set(d[1] for d in vehicle_data)) if vehicle_data else []

        # Grafik renkleri
        colors = [
            'rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 206, 86)', 
            'rgb(75, 192, 192)', 'rgb(153, 102, 255)', 'rgb(255, 159, 64)'
        ]

        # Süt miktarı veri setleri
        milk_datasets = []
        for idx, vehicle in enumerate(vehicles):
            color = colors[idx % len(colors)]
            data = []
            for date in dates:
                quantity = 0
                for d in vehicle_data:
                    if d[0].strftime('%d.%m') == date and d[1] == vehicle:
                        quantity = float(d[2]) if d[2] is not None else 0
                        break
                data.append(quantity)
            
            milk_datasets.append({
                'label': vehicle,
                'data': data,
                'borderColor': color,
                'backgroundColor': color.replace('rgb', 'rgba').replace(')', ', 0.1)'),
                'tension': 0.4,
                'borderWidth': 2,
                'pointRadius': 2,
                'fill': True
            })

        # Yağ oranı veri setleri
        fat_datasets = []
        for idx, vehicle in enumerate(vehicles):
            color = colors[idx % len(colors)]
            data = []
            for date in dates:
                fat_ratio = 0
                for d in vehicle_data:
                    if d[0].strftime('%d.%m') == date and d[1] == vehicle:
                        fat_ratio = float(d[3]) if d[3] is not None else 0
                        break
                data.append(fat_ratio)
            
            fat_datasets.append({
                'label': vehicle,
                'data': data,
                'borderColor': color,
                'backgroundColor': color.replace('rgb', 'rgba').replace(')', ', 0.1)'),
                'tension': 0.4,
                'borderWidth': 2,
                'pointRadius': 2,
                'fill': True
            })

        # Son 30 günlük ortalama yağ oranı ve toplam süt miktarı
        milk_stats = db.session.query(
            func.avg(MilkFactoryDelivery.fat_ratio).label('avg_fat'),
            func.sum(MilkFactoryDelivery.quantity).label('total_milk')
        ).filter(
            func.date(MilkFactoryDelivery.delivery_date) >= thirty_days_ago
        ).first()

        average_fat_ratio = milk_stats.avg_fat or 0
        total_milk = milk_stats.total_milk or 0

        # Aylık yem satış adedi
        monthly_feed_count = FeedDelivery.query.filter(
            FeedDelivery.delivery_date >= first_day_of_month
        ).with_entities(
            db.func.sum(FeedDelivery.quantity)
        ).scalar() or 0

        # Geçen ayın yem satış adedi
        last_month_feed_count = FeedDelivery.query.filter(
            FeedDelivery.delivery_date.between(last_month_start, first_day_of_month)
        ).with_entities(
            db.func.sum(FeedDelivery.quantity)
        ).scalar() or 0

        # Yem satış artış/azalış yüzdesi
        feed_count_percentage = 0
        if last_month_feed_count > 0:
            feed_count_percentage = ((monthly_feed_count - last_month_feed_count) / last_month_feed_count) * 100

        return render_template('home/index.html',
                            daily_milk=today_milk,
                            milk_percentage=milk_percentage,
                            average_fat_ratio=average_fat_ratio,
                            total_milk=total_milk,
                            monthly_feed_count=monthly_feed_count,
                            feed_percentage=feed_percentage,
                            monthly_expense=monthly_expense,
                            expense_percentage=expense_percentage,
                            recent_deliveries=recent_deliveries,
                            dates=dates,
                            milk_datasets=milk_datasets,
                            fat_datasets=fat_datasets)
    except Exception as e:
        print(f"Hata: {str(e)}")  # Hatayı konsola yazdır
        import traceback
        traceback.print_exc()  # Hata stack trace'ini yazdır
        return render_template('home/page-500.html'), 500

# Süt İşlemleri
@blueprint.route('/milk-collection')
@login_required
def milk_collection():
    return render_template('home/milk-collection.html')

@blueprint.route('/milk-deliveries')
@login_required
def milk_deliveries():
    factories = Factory.query.filter_by(is_active=True).all()
    vehicles = Vehicle.query.filter_by(is_active=True).all()
    deliveries = MilkFactoryDelivery.query.order_by(MilkFactoryDelivery.delivery_date.desc()).all()
    
    # Tarihleri formatla
    unique_dates = sorted(set(delivery.delivery_date.strftime('%Y-%m-%d') for delivery in deliveries), reverse=True)
    
    return render_template('home/milk-delivery.html',
                         segment='milk-deliveries',
                         factories=factories,
                         vehicles=vehicles,
                         deliveries=deliveries,
                         unique_dates=unique_dates)

@blueprint.route('/milk-suppliers')
@login_required
def milk_suppliers():
    suppliers = MilkSupplier.query.all()
    return render_template('home/milk-suppliers.html', suppliers=suppliers)

# Yem İşlemleri
@blueprint.route('/feed-stock')
@login_required
def feed_stock():
    return render_template('home/feed-stock.html')

@blueprint.route('/feed-delivery')
@login_required
def feed_delivery():
    return render_template('home/feed-delivery.html')

@blueprint.route('/feed-suppliers')
@login_required
def feed_suppliers():
    return render_template('home/feed-suppliers.html')

# Finans İşlemleri
@blueprint.route('/accounts')
@login_required
def accounts():
    return render_template('home/accounts.html')

@blueprint.route('/expenses')
@login_required
def expenses():
    return render_template('home/expenses.html')

@blueprint.route('/reports')
@login_required
def reports():
    return render_template('home/reports.html')

# Ayarlar
@blueprint.route('/settings')
@login_required
def settings():
    factories = Factory.query.all()
    feed_types = FeedType.query.all()
    feed_suppliers = FeedSupplier.query.all()
    vehicles = Vehicle.query.all()
    milk_suppliers = MilkSupplier.query.all()
    districts = District.query.all()
    users = Users.query.all()
    report_templates = ReportTemplate.query.all()
    
    return render_template('home/settings.html',
                         segment='settings',
                         factories=factories,
                         feed_types=feed_types,
                         feed_suppliers=feed_suppliers,
                         vehicles=vehicles,
                         milk_suppliers=milk_suppliers,
                         districts=districts,
                         users=users,
                         report_templates=report_templates)

@blueprint.route('/api/districts/<int:district_id>/villages')
@login_required
def get_district_villages(district_id):
    villages = Village.query.filter_by(district_id=district_id).all()
    return jsonify({
        'villages': [{'id': v.id, 'name': v.name} for v in villages]
    })

# Hata sayfaları
@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403

@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404

@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500

# API Endpoints
@blueprint.route('/api/suppliers', methods=['POST'])
@login_required
def create_supplier():
    try:
        data = request.json
        
        # Önce cari hesap oluştur
        account = Account(
            name=data['name'],
            account_type=AccountType.MILK_SUPPLIER,
            balance=0
        )
        db.session.add(account)
        db.session.flush()  # ID almak için flush
        
        # Tedarikçiyi oluştur
        supplier = MilkSupplier(
            name=data['name'],
            district_id=data.get('district_id'),
            village_id=data.get('village_id'),
            phone=data.get('phone'),
            credit_limit=float(data.get('credit_limit', 0)),
            account_id=account.id,
            notes=data.get('notes'),
            is_active=data.get('is_active', 'true') == 'true'
        )
        
        db.session.add(supplier)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Tedarikçi başarıyla eklendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/milk-deliveries/<int:id>/deliver', methods=['POST'])
@login_required
def mark_delivery_as_delivered(id):
    try:
        delivery = MilkDelivery.query.get_or_404(id)
        delivery.is_delivered = True
        delivery.delivery_date = datetime.now()
        db.session.commit()
        
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/milk-deliveries/<int:id>', methods=['GET'])
@login_required
def get_delivery_details(id):
    try:
        delivery = MilkDelivery.query.get_or_404(id)
        
        return jsonify({
            'id': delivery.id,
            'date': delivery.date.strftime('%d.%m.%Y %H:%M'),
            'supplier': {
                'id': delivery.supplier.id,
                'name': delivery.supplier.name
            },
            'quantity': delivery.quantity,
            'fat_ratio': delivery.fat_ratio,
            'ph_value': delivery.ph_value,
            'vehicle_plate': delivery.vehicle_plate,
            'driver_name': delivery.driver_name,
            'receipt_number': delivery.receipt_number,
            'is_delivered': delivery.is_delivered,
            'delivery_date': delivery.delivery_date.strftime('%d.%m.%Y %H:%M') if delivery.delivery_date else None
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

# API Endpoints - Fabrikalar
@blueprint.route('/api/factories', methods=['GET'])
@login_required
def get_factories():
    factories = Factory.query.all()
    return jsonify([{
        'id': f.id,
        'name': f.name,
        'address': f.address,
        'phone': f.phone,
        'is_active': f.is_active
    } for f in factories])

@blueprint.route('/api/factories/<int:id>', methods=['GET'])
@login_required
def get_factory(id):
    try:
        factory = Factory.query.get_or_404(id)
        return jsonify({
            'success': True,
            'id': factory.id,
            'name': factory.name,
            'address': factory.address,
            'phone': factory.phone,
            'is_active': factory.is_active
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@blueprint.route('/api/factories', methods=['POST'])
@login_required
def create_factory():
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        data = request.json
        factory = Factory(
            name=data['name'],
            address=data.get('address'),
            phone=data.get('phone'),
            is_active=True
        )
        db.session.add(factory)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Fabrika başarıyla eklendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/factories/<int:id>', methods=['PUT'])
@login_required
def update_factory(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        factory = Factory.query.get_or_404(id)
        data = request.json
        
        factory.name = data['name']
        factory.address = data.get('address')
        factory.phone = data.get('phone')
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Fabrika başarıyla güncellendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/factories/<int:id>', methods=['DELETE'])
@login_required
def delete_factory(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        factory = Factory.query.get_or_404(id)
        factory.is_active = False
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Fabrika başarıyla pasife alındı'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

# API Endpoints - Yem Çeşitleri
@blueprint.route('/api/feed-types', methods=['GET'])
@login_required
def get_feed_types():
    feed_types = FeedType.query.all()
    return jsonify([{
        'id': ft.id,
        'name': ft.name,
        'description': ft.description,
        'unit': ft.unit,
        'is_active': ft.is_active
    } for ft in feed_types])

@blueprint.route('/api/feed-types/<int:id>', methods=['GET'])
@login_required
def get_feed_type(id):
    try:
        feed_type = FeedType.query.get_or_404(id)
        return jsonify({
            'success': True,
            'id': feed_type.id,
            'name': feed_type.name,
            'description': feed_type.description,
            'unit': feed_type.unit,
            'is_active': feed_type.is_active
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@blueprint.route('/api/feed-types', methods=['POST'])
@login_required
def create_feed_type():
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        data = request.json
        unit = data.get('unit', 'KG')
        
        # Birim kontrolü
        if unit not in ['KG', 'ADET']:
            return jsonify({'success': False, 'message': 'Birim sadece KG veya ADET olabilir'}), 400
        
        feed_type = FeedType(
            name=data['name'],
            description=data.get('description'),
            unit=unit,
            is_active=True
        )
        db.session.add(feed_type)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Yem çeşidi başarıyla eklendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/feed-types/<int:id>', methods=['PUT'])
@login_required
def update_feed_type(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        feed_type = FeedType.query.get_or_404(id)
        data = request.json
        unit = data.get('unit', feed_type.unit)
        
        # Birim kontrolü
        if unit not in ['KG', 'ADET']:
            return jsonify({'success': False, 'message': 'Birim sadece KG veya ADET olabilir'}), 400
        
        feed_type.name = data['name']
        feed_type.description = data.get('description')
        feed_type.unit = unit
        feed_type.is_active = data.get('is_active', 'true') == 'true'
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Yem çeşidi başarıyla güncellendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/feed-types/<int:id>', methods=['DELETE'])
@login_required
def delete_feed_type(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        feed_type = FeedType.query.get_or_404(id)
        feed_type.is_active = False  # Sadece yem çeşidini pasife al
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Yem çeşidi başarıyla pasife alındı'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

# API Endpoints - Rapor Şablonları
@blueprint.route('/api/report-templates', methods=['GET'])
@login_required
def get_report_templates():
    templates = ReportTemplate.query.all()
    return jsonify([{
        'id': t.id,
        'name': t.name,
        'description': t.description,
        'report_type': t.report_type,
        'is_active': t.is_active
    } for t in templates])

@blueprint.route('/api/report-templates/<int:id>', methods=['GET'])
@login_required
def get_report_template(id):
    template = ReportTemplate.query.get_or_404(id)
    return jsonify({
        'id': template.id,
        'name': template.name,
        'description': template.description,
        'report_type': template.report_type,
        'is_active': template.is_active
    })

@blueprint.route('/api/report-templates', methods=['POST'])
@login_required
def create_report_template():
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        data = request.json
        template = ReportTemplate(
            name=data['name'],
            description=data.get('description'),
            report_type=data.get('report_type', 'daily'),
            is_active=True
        )
        db.session.add(template)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Rapor şablonu başarıyla eklendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/report-templates/<int:id>', methods=['PUT'])
@login_required
def update_report_template(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        template = ReportTemplate.query.get_or_404(id)
        data = request.json
        
        template.name = data['name']
        template.description = data.get('description')
        template.report_type = data.get('report_type', template.report_type)
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Rapor şablonu başarıyla güncellendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/report-templates/<int:id>', methods=['DELETE'])
@login_required
def delete_report_template(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        template = ReportTemplate.query.get_or_404(id)
        template.is_active = False
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Rapor şablonu başarıyla pasife alındı'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

# API Endpoints - Süt Tedarikçileri
@blueprint.route('/api/milk-suppliers', methods=['GET'])
@login_required
def get_milk_suppliers():
    suppliers = MilkSupplier.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'phone': s.phone,
        'district_id': s.district_id,
        'village_id': s.village_id,
        'credit_limit': s.credit_limit,
        'notes': s.notes,
        'is_active': s.is_active
    } for s in suppliers])

@blueprint.route('/api/milk-suppliers/<int:id>', methods=['GET'])
@login_required
def get_milk_supplier(id):
    try:
        supplier = MilkSupplier.query.get_or_404(id)
        return jsonify({
            'success': True,
            'id': supplier.id,
            'name': supplier.name,
            'phone': supplier.phone,
            'district_id': supplier.district_id,
            'village_id': supplier.village_id,
            'credit_limit': supplier.credit_limit,
            'notes': supplier.notes,
            'is_active': supplier.is_active
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@blueprint.route('/api/milk-suppliers', methods=['POST'])
@login_required
def create_milk_supplier():
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        data = request.json
        
        # Önce cari hesap oluştur
        account = Account(
            name=data['name'],
            account_type=AccountType.MILK_SUPPLIER,
            balance=0
        )
        db.session.add(account)
        db.session.flush()  # ID almak için flush
        
        # Tedarikçiyi oluştur
        supplier = MilkSupplier(
            name=data['name'],
            phone=data.get('phone'),
            district_id=data.get('district_id'),
            village_id=data.get('village_id'),
            credit_limit=float(data.get('credit_limit', 0)),
            account_id=account.id,
            notes=data.get('notes'),
            is_active=True
        )
        
        db.session.add(supplier)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Tedarikçi başarıyla eklendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/milk-suppliers/<int:id>', methods=['PUT'])
@login_required
def update_milk_supplier(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        supplier = MilkSupplier.query.get_or_404(id)
        data = request.json
        
        supplier.name = data['name']
        supplier.phone = data.get('phone')
        supplier.district_id = data.get('district_id')
        supplier.village_id = data.get('village_id')
        supplier.credit_limit = float(data.get('credit_limit', 0))
        supplier.notes = data.get('notes')
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Tedarikçi başarıyla güncellendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/milk-suppliers/<int:id>', methods=['DELETE'])
@login_required
def delete_milk_supplier(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        supplier = MilkSupplier.query.get_or_404(id)
        supplier.is_active = False
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Tedarikçi başarıyla pasife alındı'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

# API Endpoints - Araçlar
@blueprint.route('/api/vehicles', methods=['GET'])
@login_required
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([{
        'id': v.id,
        'plate': v.plate,
        'driver_name': v.driver_name,
        'is_active': v.is_active
    } for v in vehicles])

@blueprint.route('/api/vehicles/<int:id>', methods=['GET'])
@login_required
def get_vehicle(id):
    try:
        vehicle = Vehicle.query.get_or_404(id)
        return jsonify({
            'success': True,
            'id': vehicle.id,
            'plate': vehicle.plate,
            'driver_name': vehicle.driver_name,
            'is_active': vehicle.is_active
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@blueprint.route('/api/vehicles', methods=['POST'])
@login_required
def create_vehicle():
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        data = request.json
        vehicle = Vehicle(
            plate=data['plate'],
            driver_name=data.get('driver_name'),
            is_active=True
        )
        db.session.add(vehicle)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Araç başarıyla eklendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/vehicles/<int:id>', methods=['PUT'])
@login_required
def update_vehicle(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        vehicle = Vehicle.query.get_or_404(id)
        data = request.json
        
        vehicle.plate = data['plate']
        vehicle.driver_name = data.get('driver_name')
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Araç başarıyla güncellendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/vehicles/<int:id>', methods=['DELETE'])
@login_required
def delete_vehicle(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        vehicle = Vehicle.query.get_or_404(id)
        vehicle.is_active = False
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Araç başarıyla pasife alındı'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

# API Endpoints - Yem Tedarikçileri
@blueprint.route('/api/feed-suppliers', methods=['GET'])
@login_required
def get_feed_suppliers():
    suppliers = FeedSupplier.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'address': s.address,
        'phone': s.phone,
        'is_active': s.is_active
    } for s in suppliers])

@blueprint.route('/api/feed-suppliers/<int:id>', methods=['GET'])
@login_required
def get_feed_supplier(id):
    try:
        supplier = FeedSupplier.query.get_or_404(id)
        return jsonify({
            'success': True,
            'id': supplier.id,
            'name': supplier.name,
            'address': supplier.address,
            'phone': supplier.phone,
            'is_active': supplier.is_active
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@blueprint.route('/api/feed-suppliers', methods=['POST'])
@login_required
def create_feed_supplier():
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        data = request.json
        
        # Önce cari hesap oluştur
        account = Account(
            name=data['name'],
            account_type=AccountType.FEED_SUPPLIER,
            balance=0
        )
        db.session.add(account)
        db.session.flush()  # ID almak için flush
        
        # Yem tedarikçisini oluştur
        supplier = FeedSupplier(
            name=data['name'],
            address=data.get('address'),
            phone=data.get('phone'),
            account_id=account.id,  # Oluşturulan hesabın ID'sini kullan
            is_active=True
        )
        db.session.add(supplier)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Yem tedarikçisi başarıyla eklendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/feed-suppliers/<int:id>', methods=['PUT'])
@login_required
def update_feed_supplier(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403
    
    try:
        supplier = FeedSupplier.query.get_or_404(id)
        data = request.json
        
        supplier.name = data['name']
        supplier.address = data.get('address')
        supplier.phone = data.get('phone')
        supplier.is_active = data.get('is_active', 'true') == 'true'
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Yem tedarikçisi başarıyla güncellendi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})

@blueprint.route('/api/feed-suppliers/<int:id>', methods=['DELETE'])
@login_required
def delete_feed_supplier(id):
    if not current_user.is_superadmin:
        return jsonify({'success': False, 'message': 'Yetkiniz yok'}), 403

# API Endpoints - Süt Fabrika Teslimatları
@blueprint.route('/api/milk-factory-deliveries', methods=['POST'])
@login_required
def create_milk_factory_delivery():
    try:
        data = request.json
        
        # Yeni teslimat oluştur
        delivery = MilkFactoryDelivery(
            delivery_date=datetime.strptime(data['delivery_date'], '%Y-%m-%d %H:%M'),
            quantity=float(data['quantity']),
            factory_name=data['factory_name'],
            vehicle_plate=data.get('vehicle_plate'),
            driver_name=data.get('driver_name'),
            receipt_number=data.get('receipt_number'),
            fat_ratio=float(data.get('fat_ratio', 0)),
            ph_value=float(data.get('ph_value', 0)),
            notes=data.get('notes')
        )
        
        db.session.add(delivery)
        db.session.commit()
        
        return jsonify({
            'success': True, 
            'message': 'Süt teslimatı başarıyla kaydedildi',
            'delivery': {
                'id': delivery.id,
                'delivery_date': delivery.delivery_date.strftime('%Y-%m-%d %H:%M'),
                'quantity': delivery.quantity,
                'factory_name': delivery.factory_name,
                'vehicle_plate': delivery.vehicle_plate,
                'driver_name': delivery.driver_name,
                'receipt_number': delivery.receipt_number,
                'fat_ratio': delivery.fat_ratio,
                'ph_value': delivery.ph_value,
                'notes': delivery.notes
            }
        })
    except ValueError as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'Geçersiz veri formatı: ' + str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@blueprint.route('/api/milk-factory-deliveries/<int:id>', methods=['PUT'])
@login_required
def update_milk_factory_delivery(id):
    try:
        delivery = MilkFactoryDelivery.query.get_or_404(id)
        data = request.json
        
        # Teslimatı güncelle
        if 'delivery_date' in data:
            delivery.delivery_date = datetime.strptime(data['delivery_date'], '%Y-%m-%d %H:%M')
        if 'quantity' in data:
            delivery.quantity = float(data['quantity'])
        if 'factory_name' in data:
            delivery.factory_name = data['factory_name']
        if 'vehicle_plate' in data:
            delivery.vehicle_plate = data['vehicle_plate']
        if 'driver_name' in data:
            delivery.driver_name = data['driver_name']
        if 'receipt_number' in data:
            delivery.receipt_number = data['receipt_number']
        if 'fat_ratio' in data:
            delivery.fat_ratio = float(data['fat_ratio'])
        if 'ph_value' in data:
            delivery.ph_value = float(data['ph_value'])
        if 'notes' in data:
            delivery.notes = data['notes']
        
        db.session.commit()
        
        return jsonify({
            'success': True, 
            'message': 'Süt teslimatı başarıyla güncellendi',
            'delivery': {
                'id': delivery.id,
                'delivery_date': delivery.delivery_date.strftime('%Y-%m-%d %H:%M'),
                'quantity': delivery.quantity,
                'factory_name': delivery.factory_name,
                'vehicle_plate': delivery.vehicle_plate,
                'driver_name': delivery.driver_name,
                'receipt_number': delivery.receipt_number,
                'fat_ratio': delivery.fat_ratio,
                'ph_value': delivery.ph_value,
                'notes': delivery.notes
            }
        })
    except ValueError as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'Geçersiz veri formatı: ' + str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@blueprint.route('/api/milk-factory-deliveries/<int:id>', methods=['DELETE'])
@login_required
def delete_milk_factory_delivery(id):
    try:
        delivery = MilkFactoryDelivery.query.get_or_404(id)
        db.session.delete(delivery)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Süt teslimatı başarıyla silindi'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@blueprint.route('/api/milk-factory-deliveries', methods=['GET'])
@login_required
def get_milk_factory_deliveries():
    try:
        # Tarih filtresi
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        query = MilkFactoryDelivery.query
        
        if start_date:
            query = query.filter(MilkFactoryDelivery.delivery_date >= datetime.strptime(start_date, '%Y-%m-%d'))
        if end_date:
            query = query.filter(MilkFactoryDelivery.delivery_date <= datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1))
        
        deliveries = query.order_by(MilkFactoryDelivery.delivery_date.desc()).all()
        
        return jsonify({
            'success': True,
            'deliveries': [{
                'id': d.id,
                'delivery_date': d.delivery_date.strftime('%Y-%m-%d %H:%M'),
                'quantity': d.quantity,
                'factory_name': d.factory_name,
                'vehicle_plate': d.vehicle_plate,
                'driver_name': d.driver_name,
                'receipt_number': d.receipt_number,
                'fat_ratio': d.fat_ratio,
                'ph_value': d.ph_value,
                'notes': d.notes
            } for d in deliveries]
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@blueprint.route('/api/milk-factory-deliveries/<int:id>', methods=['GET'])
@login_required
def get_milk_factory_delivery(id):
    try:
        delivery = MilkFactoryDelivery.query.get_or_404(id)
        
        return jsonify({
            'success': True,
            'delivery': {
                'id': delivery.id,
                'delivery_date': delivery.delivery_date.strftime('%Y-%m-%d %H:%M'),
                'quantity': delivery.quantity,
                'factory_name': delivery.factory_name,
                'vehicle_plate': delivery.vehicle_plate,
                'driver_name': delivery.driver_name,
                'receipt_number': delivery.receipt_number,
                'fat_ratio': delivery.fat_ratio,
                'ph_value': delivery.ph_value,
                'notes': delivery.notes
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

