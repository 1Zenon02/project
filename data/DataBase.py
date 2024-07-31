import sqlite3


conn = sqlite3.connect('database.db')

cur = conn.cursor()


qry = '''
CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT (20),
    last_name TEXT (20),
    age INTEGER,
    sex TEXT (1),
    income float
);

'''

try:
    cur.execute(qry)
    print('Table created successfully')
except:
    print('Error in creating table')

# Close the connection
conn.close()

def insert_data(first_name, last_name, age, sex, income):
    conn = sqlite3.connect('user_data.db')
    cur = conn.cursor()
    qry = '''
    INSERT INTO users (first_name, last_name, age, sex, income)
    VALUES (?, ?, ?, ?, ?);
    '''
    try:
        cur.execute(qry, (first_name, last_name, age, sex, income))
        conn.commit()
        print('Record inserted successfully')
    except:
        print('Error in inserting data')
    finally:
        conn.close()


def update_data(id, income):
    conn = sqlite3.connect('user_data.db')
    cur = conn.cursor()
    qry = '''
    UPDATE users SET income = ? WHERE id = ?;
    '''
    try:
        cur.execute(qry, (income, id))
        conn.commit()
        print('Record updated successfully')
    except:
        print('Error in updating data')
    finally:
        conn.close()

def delete_data(id):
    conn = sqlite3.connect('user_data.db')
    cur = conn.cursor()
    qry = '''
    DELETE FROM users WHERE id = ?;
    '''
    try:
        cur.execute(qry, (id,))
        conn.commit()
        print('Record deleted successfully')
    except:
        print('Error in deleting data')
    finally:
        conn.close()

        def query_data():
            conn = sqlite3.connect('user_data.db')
            cur = conn.cursor()
            qry = '''
            SELECT * FROM users;
            '''
            try:
                cur.execute(qry)
                results = cur.fetchall()
                for row in results:
                    print('id: {}, first_name: {}, last_name: {}, age: {}, sex: {}, income: {}'.
                        format(row[0], row[1],
                        row[2], row[3],
                        row[4], row[5]))
            except:
                print('Error in querying data')
            finally:
                conn.close()

                def insert_data_securely(first_name, last_name, age, sex, income):
                    conn = sqlite3.connect('user_data.db')
                    cur = conn.cursor()
                    qry = '''
                    INSERT INTO users (first_name, last_name, age, sex, income)
                    VALUES (?, ?, ?, ?, ?);
                    '''
                    try:
                        cur.execute(qry, (first_name, last_name, age, sex, income))
                        conn.commit()
                        print('Record inserted successfully')
                    except:
                        conn.rollback()
                        print('Error in inserting data')
                    finally:
                        conn.close()
