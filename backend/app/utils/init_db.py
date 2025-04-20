import psycopg2

def init_database():
    # Connect to default postgres database to create our database
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="7895123"  # Replace with your actual password
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Create database if it doesn't exist
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'image_processing'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute("CREATE DATABASE image_processing")
        print("Database created successfully")
    else:
        print("Database already exists")
    
    cursor.close()
    conn.close()
    
    # Connect to our database and create tables
    conn = psycopg2.connect(
        host="localhost",
        database="image_processing",
        user="postgres",
        password="7895123"  # Replace with your actual password
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Create images table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS images (
        id SERIAL PRIMARY KEY,
        original_path VARCHAR(255) NOT NULL,
        enhanced_path VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    print("Tables created successfully")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_database()