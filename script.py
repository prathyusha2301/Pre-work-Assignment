import sqlite3


def connect_db(db_name):
    try:
        connectionn = sqlite3.connect(db_name)
        return connectionn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def get_total_and_average(connectionn):
    while True:
        ss = input("Enter search string (or 'exit'): ").strip().lower()
        
        if ss == 'exit':
            break
        
        if ss == "":
            print("Please enter a search string")
            continue
        
        try:
            qry = "SELECT name, marks FROM students WHERE lower(name) LIKE ?"
            search_param = f"%{ss}%"
            
            cursor = connectionn.execute(qry, (search_param,))
            rows = cursor.fetchall()
            
            if len(rows) == 0:
                print("No matching records found. Search String it not available in table")
            else:
                sum = 0
                for row in rows:
                    name, marks = row
                    print(f"Name: {name}, Marks: {marks}")
                    sum += marks
                
                nrows = len(rows)
                average_marks = sum / nrows if nrows > 0 else 0
                
                print(f"Total Marks: {sum}")
                print(f"Average Marks: {average_marks}")
        
        except sqlite3.Error as e:
            print(f"Error executing SQL query: {e}")
    
    connectionn.close()

if __name__ == "__main__":
    db_name = "assignment.db"
    connectionn = connect_db(db_name)
    
    if connectionn:
        get_total_and_average(connectionn)
    else:
        print("Failed to connect to database. Exiting.")
