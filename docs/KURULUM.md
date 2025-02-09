# cPanel Hosting Üzerinde CYBERPUNKT Kurulum Rehberi

Bu rehber, CYBERPUNKT projesinin cPanel hosting üzerinde kurulumu için adım adım talimatları içermektedir.

## Git Terimleri ve Temel Kavramlar

### Repository (Depo)
Projenizin tüm dosyalarını ve sürüm geçmişini içeren ana dizindir. İki tür repository vardır:
- **Local Repository**: Bilgisayarınızda bulunan kopya
- **Remote Repository**: Sunucuda (cPanel'de) bulunan kopya

### Branch (Dal)
Projenizin farklı sürümlerini yönetmek için kullanılan dallardır. Ana dal genellikle "main" veya "master" olarak adlandırılır.

### Commit
Projenizde yaptığınız değişikliklerin kaydedilmiş bir anlık görüntüsüdür.

### Push & Pull
- **Push**: Yerel değişikliklerinizi uzak sunucuya (cPanel) gönderme
- **Pull**: Uzak sunucudaki değişiklikleri yerel bilgisayarınıza alma

## Kurulum Adımları

### 1. Gereksinimler

- cPanel hosting hesabı
- Python 3.x desteği
- MySQL veritabanı desteği
- Git erişimi
- SSH erişimi (önerilen)

### 2. Git Repository Hazırlığı

1. Yerel bilgisayarınızda repository oluşturun:
```bash
# Repository'i klonlama
git clone [PROJE_REPO_URL]
cd cyberpunkt

# veya yeni repository oluşturma
git init
git remote add origin [PROJE_REPO_URL]
```

2. Deployment yapılandırması için `.cpanel.yml` oluşturun:
```yaml
---
deployment:
  tasks:
    - export DEPLOYPATH=/home/kullanici_adi/public_html/cyberpunkt/
    - /bin/cp -R * $DEPLOYPATH
```

3. İlk commit ve push:
```bash
git add .
git commit -m "İlk commit"
git push -u origin main
```

### 3. cPanel'de Git Kurulumu

1. cPanel'de "Git™ Version Control" bölümüne gidin
2. "Create" butonuna tıklayın
3. Repository bilgilerini girin:
   - **Clone URL**: Projenizin Git URL'i
   - **Repository Path**: `cyberpunkt`
   - **Repository Name**: `cyberpunkt`

### 4. Veritabanı Kurulumu

1. cPanel'de "MySQL® Databases" bölümüne gidin
2. Veritabanı oluşturun:
   ```sql
   CREATE DATABASE kullanici_cyberpunkt CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'kullanici_cybuser'@'localhost' IDENTIFIED BY 'guclu_parola';
   GRANT ALL PRIVILEGES ON kullanici_cyberpunkt.* TO 'kullanici_cybuser'@'localhost';
   FLUSH PRIVILEGES;
   ```

### 5. Deployment Yapılandırması

1. `.env` dosyası oluşturun:
```
FLASK_APP=run.py
FLASK_ENV=production
DEBUG=False
SECRET_KEY=guclu_bir_gizli_anahtar
DATABASE_URL=mysql://kullanici_cybuser:parola@localhost/kullanici_cyberpunkt
```

2. `.htaccess` dosyası oluşturun:
```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ run.py/$1 [L]
</IfModule>

<Files run.py>
    SetHandler wsgi-script
    Options ExecCGI
</Files>

AddHandler wsgi-script .py
```

### 6. Python Uygulama Kurulumu

1. cPanel'de "Setup Python App" bölümüne gidin
2. Yeni uygulama oluşturun:
   - Python Sürümü: 3.x
   - Uygulama Dizini: `/home/kullanici_adi/public_html/cyberpunkt`
   - WSGI Yapılandırması:
```python
import sys
sys.path.insert(0, '/home/kullanici_adi/public_html/cyberpunkt')
from run import app as application
```

### 7. Uygulama Deployment

1. SSH veya cPanel Terminal ile bağlanın
2. Python ortamını hazırlayın:
```bash
cd ~/public_html/cyberpunkt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Veritabanı migrasyonları:
```bash
flask db init
flask db migrate
flask db upgrade
```

4. Süper kullanıcı oluşturun:
```bash
python create_superuser.py
```

## Otomatik Deployment

### Push-Based Deployment
1. Yerel değişikliklerinizi commit edin:
```bash
git add .
git commit -m "Değişiklik açıklaması"
```

2. cPanel repository'sine push yapın:
```bash
git push origin main
```

### Pull-Based Deployment
1. cPanel Git arayüzünde "Pull or Deploy" sekmesine gidin
2. "Update from Remote" tıklayın
3. "Deploy HEAD Commit" tıklayın

## Güvenlik ve Bakım

### Dosya İzinleri
- Dizinler: `755` (drwxr-xr-x)
- Dosyalar: `644` (rw-r--r--)
- Çalıştırılabilir Dosyalar: `755` (rwxr-xr-x)

### Güvenlik Önlemleri
1. SSH Anahtarları:
   ```bash
   # SSH anahtarı oluşturma
   ssh-keygen -t rsa -b 4096
   # Anahtarı cPanel'e yükleme
   ```

2. SSL Sertifikası:
   - Let's Encrypt kurulumu
   - AutoSSL aktivasyonu

### Düzenli Bakım
1. Log Kontrolleri:
   ```bash
   tail -f ~/logs/error.log
   ```

2. Veritabanı Yedekleme:
   ```bash
   mysqldump -u kullanici_cybuser -p kullanici_cyberpunkt > yedek_$(date +%Y%m%d).sql
   ```

## Sorun Giderme

### Git Hataları
1. **Repository Erişim Hataları**
   - SSH anahtarlarını kontrol edin
   - Repository URL'ini doğrulayın

2. **Push/Pull Hataları**
   - Working tree temiz olmalı
   - Branch'leri senkronize edin

### Deployment Hataları
1. **500 Internal Server Error**
   - Python hata loglarını kontrol edin
   - WSGI yapılandırmasını kontrol edin

2. **Veritabanı Hataları**
   - Bağlantı bilgilerini kontrol edin
   - Kullanıcı izinlerini kontrol edin

---

Bu rehberle ilgili sorularınız veya sorunlarınız olursa, lütfen iletişime geçmekten çekinmeyin.
