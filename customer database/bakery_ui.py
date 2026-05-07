import sqlite3

def init_db():
    # Database file renamed for the new system name
    conn = sqlite3.connect("customer_system.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            favorite_order TEXT,
            points INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    return conn

def add_customer(conn):
    print("\n--- ADD NEW CUSTOMER ---")
    name = input("Enter Name: ")
    order = input("Enter Favorite Order: ")
    points = input("Initial Loyalty Points: ")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, favorite_order, points) VALUES (?, ?, ?)", 
                   (name, order, points))
    conn.commit()
    print(f"\n✅ {name} successfully registered in the Customer Database System!")

def view_customers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    
    print("\n================ CUSTOMER DATABASE SYSTEM ================")
    print(f"{'ID':<5} {'Name':<20} {'Favorite Order':<20} {'Points':<10}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<20} {row[3]:<10}")
    print("==========================================================")

def main():
    conn = init_db()
    
    while True:
        print("\n🖥️  CUSTOMER DATABASE SYSTEM - MAIN MENU")
        print("1. View All Customer Records")
        print("2. Register New Customer")
        print("3. Exit System")
        
        choice = input("\nSelect an option (1-3): ")
        
        if choice == '1':
            view_customers(conn)
        elif choice == '2':
            add_customer(conn)
        elif choice == '3':
            print("Shutting down system. Data saved.")
            conn.close()
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

