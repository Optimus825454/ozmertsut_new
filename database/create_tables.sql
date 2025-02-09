
-- Tedarikçi Kategorileri Tablosu
CREATE TABLE supplier_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    credit_limit FLOAT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Müstahsil (Süt Tedarikçisi) Tablosu
CREATE TABLE milk_suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INT,
    credit_limit FLOAT DEFAULT 0,
    feed_credit_limit FLOAT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES supplier_categories(id)
);

-- Süt Teslimatları Tablosu
CREATE TABLE milk_deliveries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT NOT NULL,
    quantity FLOAT NOT NULL,
    fat_ratio FLOAT,
    ph_value FLOAT,
    vehicle_plate VARCHAR(20),
    driver_name VARCHAR(100),
    receipt_number VARCHAR(50),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_delivered BOOLEAN DEFAULT FALSE,
    delivery_date TIMESTAMP NULL,
    available_quantity FLOAT,
    FOREIGN KEY (supplier_id) REFERENCES milk_suppliers(id)
);

-- Fabrika Teslimatları Tablosu
CREATE TABLE milk_factory_deliveries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    factory_name VARCHAR(100) NOT NULL,
    quantity FLOAT NOT NULL,
    vehicle_plate VARCHAR(20),
    receipt_number VARCHAR(50),
    delivery_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fat_ratio FLOAT,
    ph_value FLOAT,
    notes TEXT
);

-- Yem Tedarikçileri Tablosu
CREATE TABLE feed_suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Araç Yem Stokları Tablosu
CREATE TABLE vehicle_feed_stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_plate VARCHAR(20) NOT NULL,
    feed_type VARCHAR(50) NOT NULL,
    quantity FLOAT NOT NULL,
    purchase_price FLOAT NOT NULL,
    feed_supplier_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (feed_supplier_id) REFERENCES feed_suppliers(id)
);

-- Yem Teslimatları Tablosu
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

-- Hesap Hareketleri Tablosu
CREATE TABLE account_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    transaction_type ENUM('DEBIT', 'CREDIT') NOT NULL,
    amount FLOAT NOT NULL,
    description TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    related_model VARCHAR(50),
    related_id INT
);

-- Giderler Tablosu
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    amount FLOAT NOT NULL,
    description TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Kredi Limitleri Tablosu
CREATE TABLE credit_limits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_category_id INT NOT NULL,
    cash_limit FLOAT DEFAULT 0,
    feed_limit FLOAT DEFAULT 0,
    warning_threshold FLOAT DEFAULT 80,
    FOREIGN KEY (supplier_category_id) REFERENCES supplier_categories(id)
);

-- Ayarlar Tablosu
CREATE TABLE settings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    milk_entry_type ENUM('collection_first', 'delivery_first') DEFAULT 'collection_first',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- İndeksler
CREATE INDEX idx_milk_deliveries_date ON milk_deliveries(date);
CREATE INDEX idx_feed_deliveries_date ON feed_deliveries(delivery_date);
CREATE INDEX idx_account_transactions_date ON account_transactions(date);
CREATE INDEX idx_expenses_date ON expenses(date);
CREATE INDEX idx_milk_suppliers_category ON milk_suppliers(category_id);
