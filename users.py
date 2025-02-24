import re
class User:
    users_file="usersDB.txt"
    current_user=""
    def __init__(self, first_name, last_name, email, password, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile = mobile
        self.is_active = False

    @staticmethod
    def register(first_name, last_name, email, password, confirm_password, mobile):
        if not User.validate_email(email):
            return "incorrect Email !!"
    
        if not User.validate_password(password,confirm_password):
            return "Password does not match !!"
        
        if not User.validate_mobile(mobile):
            return "Mobile number incorrect !!"
        
        user=User.load_emails() 
        if email in user :
            return "this Email is Exist! please login.."
        
        new_user = User(first_name, last_name, email, password, mobile)
        User.save_in_file(new_user)
        return("Registration successful")

    @staticmethod
    def login(email,password):
        users=User.load_users()
        if not email in users:
            print("this email not Exist !! please regester..")
            return False
        if users[email][0]=="False":
            print("Your account is not activated !!")
            return False
        if users[email][1]!=password :
            print("password incorrect !!")
            return False
        User.current_user=email
        print("login successful")
        return True
          

    @staticmethod
    def validate_email(email):
        reg= r'^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$'
        return re.match(reg, email) is not None

    @staticmethod
    def validate_mobile(mobile):
        reg = r'^01[0-9]{9}$'
        return re.match(reg, mobile) is not None
    
    @staticmethod
    def validate_password(password, confirm_password):
        return password == confirm_password
    
    @staticmethod
    def save_in_file(user):
        f=open(User.users_file,'a')
        f.write(f"{user.email};{user.is_active};{user.first_name};{user.last_name};{user.password};{user.mobile}\n")
        f.close()
        return True

    @staticmethod
    def load_emails ():
        emails=[]
        f=open(User.users_file,'r')
        for line in f:
            emails.append(line.split(";")[0])
        f.close()
        return emails

    @staticmethod 
    def load_users():
        users={}
        f=open(User.users_file,'r')
        for line in f:
            k=line.split(";")[0] #email
            users[k]=[line.split(";")[1] ,line.split(";")[4]] # 1 activation 4 password
        f.close()
        return users      

    def activation(email):
        new_version=[]
        f=open(User.users_file,'r')
        for l in f:
            line=l.strip().split(";")
            if line[0]==email:
                line[1]="True"
            new_version.append(";".join(line))
            
        f1=open(User.users_file,'w')
        f1.write("\n".join(new_version) + "\n")
        f1.close()
        return f"{email} has been successfully activated!"
                    
       