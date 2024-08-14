import sys

from db import DB

class Flipkart:
    def __init__(self):
        self.db = DB()



        self.menu()
    

    def menu(self):
        user_input = input(""" 
        Enter 1 to register
        Enter 2 to login
        Enter any number to leave
        """)

        if(user_input == "1") :
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(500)
    

    def register(self):

        name = input("Enter your Name : ")
        email = input("Enter your Email : ")
        password = input("Enter your Password : ")
        # pass
        res  = self.db.register(name, email, password)

        if res:
            print("Registration successfull")
        else:
            print("Registration failed")



        self.menu()

    def login(self):

        email = input("Enter your email: ")
        password = input("Enter your password : ")

        data = self.db.search(email, password)

        if (len(data) == 0):
            print("Inavalid Credentials")
            self.login()
        else:

            id, n, e, p = data[0];

            print("Hello ", data[0][1]) 
            print("name :- ", n)
            print("Your Email Id is - " , e)
            print("Have your password :- ", p)

            self.login_menu()
            # print(n)
            # for i in range(1, len(data), 1):
            #     print(data[i])

        # print(data)
        # pass

        def login_menu():
            user_val = input("""
            1. Enter 1 to see profile
            2. ENTER 2 TO EDIT PROFILE
            3. ENTER 3 TO DELETE PROFILE
            4. ENTER 4 TO LOGOUT
        
            """)

            # if(user_val == 1):

            # elif user_val == 2:

            # elif user_val == 3:

            # else:

# print("satya")   

if __name__ == "__main__":
    app = Flipkart()
