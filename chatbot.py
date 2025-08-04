class chatbot_res:
    def __init__(self):
        self.user="" 
        self.password=""
        self.login=False
        self.main_menu()

    def main_menu(self):
        user_input= input("""Welcome..! Choose the following to proceed
                                            1. Sign in
                                            2. Sign up
                                            3. Text a Friend
                                            4. write a post 
                                            5. Press any key to exit \n""")
        
        if user_input=='1':
            self.sign_in()
        elif user_input=='2':
            self.sign_up()
        elif user_input=='3':
            self.send_txt()
        elif user_input=='4':
            self.write_post()
        else:
            exit

    def sign_up(self):
        self.user=input("Enter email -> \n ")
        self.password=input("Enter password -> \n")
        print(f"Welcome {self.user} you have signed in")
        self.main_menu()

    def sign_in(self):
        if self.user=='' and self.password=='':
            print("Sorry try signing up ")

        else:
            user_name=input("Enter the email -> \n")
            pwd=input("Enter password \n")
            if self.user==user_name and self.password==pwd:
                print(f"Welcome {self.user}")
                self.login=True
            else:
                print("Invalid credentials")

        self.main_menu()

    def write_post(self):
        if self.login:
            content=input("Enter the content to post")
            print(f"Post  written by {self.user}")
            print(content)
        else:
            print("Please try to login")

        self.main_menu()

    def send_txt(self):
        friend=input("enter the friend's name")
        text=input("please enter the message you want to send")
        print(f"Message sent to your friend {friend}")

        self.main_menu()

    
chatbot_res()