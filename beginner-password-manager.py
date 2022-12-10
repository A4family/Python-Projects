from cryptography.fernet import Fernet
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key 

master_pwd = input("What is the master password ?")
key = load_key() + master_pwd.encode()
fer = Fernet(key)



mode = input("Woud you like to add a new password or view existing one (view, add) ? Press to quit ").lower()

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key",'wb') as key_file:
#         key_file.write(key)



def view():
    with open('passwords.txt','r') as f: ## with will auto matically closes file
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split('|')
            print("Username:",user, " && Password: ",fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name :")
    pwd = input("Password: ")
    with open('passwords.txt','a') as f: ## with will auto matically closes file
        f.write(name  + " | " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    if mode == 'q':
        break

    if mode == 'view':
        view()
        break
    elif mode == 'add':
        add()
        break
    else:
        print("Invalid mode.")
        continue