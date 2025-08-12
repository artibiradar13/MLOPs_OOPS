class chatbook:
    def __init__(self):
        self.username =''
        self.password =''
        self.SIGNINNED = False
        self.loggegin =False
        self.menu()

    def menu(self):
        user_input =input("""Welcome to chatbook,pleasse enter the following:
                     -> ENTER 1 to SIGNUP
                     -> ENTER 2 to SIGNIN
                     -> ENTER 3 to POST A MSG
                     -> ENTER 4 to MSG A FRND
                     -> PRESS ANYTHING TO EXIT
                          
                     -> """)
        if user_input=='1':
            self.SIGNUP()
        elif user_input=='2':
            self.SIGNIN()
        elif user_input=='3':
            self.POST_MSG()
        elif user_input=='4':
            self.MSG_FRND()
        else:
            print("Logged Out Successfully")

    def SIGNUP(self):
        self.username=input("SET your Username: ")
        self.password =input("SEt your password: ")
        print(f"Account created for {self.username}")
        self.SIGNINNED=True
        self.menu()

    def SIGNIN(self):
        if self.SIGNINNED==False:
            print("Sign UP First")
        else:    
            uname =input("ENTER YOUR USERNAME: ")
            pwd =input("Enter Password: ")
            if uname==self.username and pwd==self.password:
                self.loggegin=True
                print("LOGGED IN SUCCESSFULLY")
            else:
                print("incorrecorect creandiatials!")
        self.menu()
        
    def POST_MSG(self):
        if self.loggegin==True:
            msg=input("Write your msg: ")
            print(f"your msg is post : {msg}")
        else:
            print("Sign IN FIRST")
        self.menu()

    def MSG_FRND(self):
        if self.loggegin==True:
            friend=input("Enter Friend's name : ")
            msg=input(f"Enter your msg to {friend}  ")
            print(f"MSG sent to {friend}")
        else:
            print("SIGNIN FIRST")
        self.menu()
#object----
user=chatbook()


    







