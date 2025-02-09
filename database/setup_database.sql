
    -- Mevcut veritabanını sil ve yeniden oluştur
    DROP DATABASE IF EXISTS cybetpunkt;
    CREATE DATABASE cybetpunkt;
    USE cybetpunkt;

    -- Users Tablosu
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(64) UNIQUE NOT NULL,
        email VARCHAR(64) UNIQUE NOT NULL,
        password VARCHAR(500) NOT NULL,
        is_superadmin BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Tedarikçi Kategorileri
    CREATE TABLE supplier_categories (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL UNIQUE,
        description TEXT,
        credit_limit FLOAT DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );

    -- Müstahsil Hesapları
    CREATE TABLE accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        balance FLOAT DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Müstahsiller (Süt Tedarikçileri)
    CREATE TABLE milk_suppliers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20),
        address TEXT,
        category_id INT,
        account_id INT UNIQUE,
        credit_limit FLOAT DEFAULT 0,
        feed_credit_limit FLOAT DEFAULT 0,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (category_id) REFERENCES supplier_categories(id),
        FOREIGN KEY (account_id) REFERENCES accounts(id)
    );

    -- Süt Teslimatları
    CREATE TABLE milk_deliveries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        supplier_id INT NOT NULL,
        quantity FLOAT NOT NULL,
        fat_ratio FLOAT,
        ph_value FLOAT,
        unit_price FLOAT NOT NULL,
        total_amount FLOAT NOT NULL,
        vehicle_plate VARCHAR(20),
        driver_name VARCHAR(100),
        receipt_number VARCHAR(50),
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_delivered BOOLEAN DEFAULT FALSE,
        delivery_date TIMESTAMP NULL,
        available_quantity FLOAT,
        notes TEXT,
        FOREIGN KEY (supplier_id) REFERENCES milk_suppliers(id)
    );

    -- Fabrika Teslimatları
    CREATE TABLE milk_factory_deliveries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        factory_name VARCHAR(100) NOT NULL,
        quantity FLOAT NOT NULL,
        unit_price FLOAT NOT NULL,
        total_amount FLOAT NOT NULL,
        vehicle_plate VARCHAR(20),
        driver_name VARCHAR(100),
        receipt_number VARCHAR(50),
        delivery_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        fat_ratio FLOAT,
        ph_value FLOAT,
        payment_status ENUM('PENDING', 'PAID') DEFAULT 'PENDING',
        payment_date TIMESTAMP NULL,
        notes TEXT
    );

    -- Yem Tedarikçileri
    CREATE TABLE feed_suppliers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20),
        address TEXT,
        account_id INT UNIQUE,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (account_id) REFERENCES accounts(id)
    );

    -- Araç Yem Stokları
    CREATE TABLE vehicle_feed_stocks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        vehicle_plate VARCHAR(20) NOT NULL,
        feed_type VARCHAR(50) NOT NULL,
        quantity FLOAT NOT NULL,
        purchase_price FLOAT NOT NULL,
        feed_supplier_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (feed_supplier_id) REFERENCES feed_suppliers(id)
    );

    -- Yem Teslimatları
    CREATE TABLE feed_deliveries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        vehicle_stock_id INT NOT NULL,
        milk_supplier_id INT NOT NULL,
        quantity FLOAT NOT NULL,
        unit_price FLOAT NOT NULL,
        total_amount FLOAT NOT NULL,
        payment_type ENUM('CASH', 'CREDIT') NOT NULL,
        delivery_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        notes TEXT,
        FOREIGN KEY (vehicle_stock_id) REFERENCES vehicle_feed_stocks(id),
        FOREIGN KEY (milk_supplier_id) REFERENCES milk_suppliers(id)
    );

    -- Hesap Hareketleri
    CREATE TABLE account_transactions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        account_id INT NOT NULL,
        transaction_type ENUM('DEBIT', 'CREDIT') NOT NULL,
        amount FLOAT NOT NULL,
        balance_after FLOAT NOT NULL,
        description TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        related_model VARCHAR(50),
        related_id INT,
        FOREIGN KEY (account_id) REFERENCES accounts(id)
    );

    -- Giderler
    CREATE TABLE expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category VARCHAR(50) NOT NULL,
        amount FLOAT NOT NULL,
        description TEXT,
        payment_method ENUM('CASH', 'BANK') NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        created_by INT,
        FOREIGN KEY (created_by) REFERENCES users(id)
    );

    -- Kredi Limitleri
    CREATE TABLE credit_limits (
        id INT AUTO_INCREMENT PRIMARY KEY,
        supplier_category_id INT NOT NULL,
        cash_limit FLOAT DEFAULT 0,
        feed_limit FLOAT DEFAULT 0,
        warning_threshold FLOAT DEFAULT 80,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (supplier_category_id) REFERENCES supplier_categories(id)
    );

    -- Sistem Ayarları
    CREATE TABLE settings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        setting_key VARCHAR(50) NOT NULL UNIQUE,
        setting_value TEXT,
        description TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );

    -- İndeksler
    CREATE INDEX idx_milk_deliveries_date ON milk_deliveries(date);
    CREATE INDEX idx_milk_deliveries_supplier ON milk_deliveries(supplier_id);
    CREATE INDEX idx_feed_deliveries_date ON feed_deliveries(delivery_date);
    CREATE INDEX idx_feed_deliveries_supplier ON feed_deliveries(milk_supplier_id);
    CREATE INDEX idx_account_transactions_date ON account_transactions(date);
    CREATE INDEX idx_account_transactions_account ON account_transactions(account_id);
    CREATE INDEX idx_expenses_date ON expenses(date);
    CREATE INDEX idx_expenses_category ON expenses(category);
    CREATE INDEX idx_milk_suppliers_category ON milk_suppliers(category_id);

    -- Varsayılan ayarları ekle
    INSERT INTO settings (setting_key, setting_value, description) VALUES
    ('milk_entry_type', 'collection_first', 'Süt giriş yöntemi (collection_first/delivery_first)'),
    ('default_credit_limit', '5000', 'Varsayılan kredi limiti'),
    ('default_feed_credit_limit', '3000', 'Varsayılan yem kredi limiti'),
    ('warning_threshold', '80', 'Kredi limit uyarı eşiği (%)');

    -- Admin kullanıcısı oluştur
    INSERT INTO users (username, email, password, is_superadmin) VALUES
    ('admin', 'admin@cybetpunkt.com', 'pbkdf2:sha256:260000$zY2z8Z2p$d2d78f6e9a52b8b78f5d7c95b3613e7b7c8e8f9c', TRUE);
