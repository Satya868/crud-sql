import mysql.connector
import psycopg2 as pg


class DB:

    def __init__(self):
        try:
            self.conn = pg.connect(
                host='localhost',
                database='crud',
                port=5432,
                user='postgres',
                password='password'
            )
            self.cursor = self.conn.cursor()
            print("Connection established.")
        
        except Exception as err:
            print("Something went wrong.")
            print(err)
    

    def register(self, name, email, password):
        try:
            # Use a parameterized query to safely insert data
            self.cursor.execute("""
                INSERT INTO users (name, email, password) 
                VALUES (%s, %s, %s)
            """, (name, email, password))

            self.conn.commit()
        except Exception as err:
            print("Error occurred during registration.")
            print(err)
            return 0
        else:
            return 1
    

    def search(self, email, password):
        try:
            self.cursor.execute("""
            SELECT * FROM users WHERE email LIKE %s AND password LIKE %s
            """, (email, password))

            data = self.cursor.fetchall()  # Correcting the typo here

            print(data)
            return data

        except Exception as err:
            print("Error occurred during search.")
            print(err)
            return None
            # self.cursor.execute("""
            # SELECT * from users where email LIKE '{}' AND password LIKE '{}'

            # """).format(email, password)

            # data = self.cursor.fethall()

            # print(data); 

# # Example usage
# # db = DB()
# # result = db.register("John Doe", "john.doe@example.com", "securepassword")
# # if result == 1:
# #     print("User registered successfully.")
# # else:
# #     print("User registration failed.")
# ~