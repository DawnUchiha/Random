from os import path

class PassManager():
    import cryptography 
    key = 'key'
    def __init__(self):
        pass
    
    def main():
        pasw = 'passwords.txt'
        print("Hello what is the key?")
       
        key = input('Key: ')
        if key == 'key':
            print("_________________\nCreate(c) or View(v)\n")
            option = input('Enter: ')
            if option == 'c':
                print('Creating...\n')
                user = input("Account Name: ")
                psw = input("\nPassword: ")
                psw = psw
                print("Submitting...")
                pasw.append(user + " | " + psw, "wt")
                
                
            elif option == 'v':
                print('Viewing...\n')
                
            else:
                print("Did you put the correct thing?\n")
        
start = True    
while start:
    PassManager.main()
    stop = input('Do you want to Quit(q)?\n Enter: ')
    if stop == 'q':
        start = False
    else:
        pass
            