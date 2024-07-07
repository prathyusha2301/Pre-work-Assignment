import sqlite3


def connect_db(database_name):
    try:
        conn = sqlite3.connect(database_name)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def get_total_and_average(conn):
    while True:
        search_string = input("Enter search string (or 'exit'): ").strip().lower()
        
        if search_string == 'exit':
            break
        
        if search_string == "":
            print("Please enter a search string")
            continue
        
        try:
            query = "SELECT name, marks FROM students WHERE lower(name) LIKE ?"
            search_param = f"%{search_string}%"
            
            cursor = conn.execute(query, (search_param,))
            rows = cursor.fetchall()
            
            if len(rows) == 0:
                print("No matching records found. Text it not available in table")
            else:
                total_marks = 0
                for row in rows:
                    name, marks = row
                    print(f"Name: {name}, Marks: {marks}")
                    total_marks += marks
                
                num_rows = len(rows)
                average_marks = total_marks / num_rows if num_rows > 0 else 0
                
                print(f"Total Marks: {total_marks}")
                print(f"Average Marks: {average_marks}")
        
        except sqlite3.Error as e:
            print(f"Error executing SQL query: {e}")
    
    conn.close()

if __name__ == "__main__":
    database_name = "assignment.db"
    conn = connect_db(database_name)
    
    if conn:
        get_total_and_average(conn)
    else:
        print("Failed to connect to database. Exiting.")
