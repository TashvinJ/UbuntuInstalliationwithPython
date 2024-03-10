import getpass
import time

print("Welcome to ubuntu installiation!")

print("Ok lets start our ubuntu installiation")

print("God: Hey yo")
time.sleep(2)
print("Programmer: Yes God")
time.sleep(4)
print(
    "God: Are you sure you are goint to make a ubuntu installiation process with python?"
)
time.sleep(2)
print("God: Even thow you are just 9 years old!")
time.sleep(1)
print("Programmer: Yes God")
time.sleep(1)
print("God: Then start!")


print("")
print("")


while True:
    username = input("Enter username: ")
    password = getpass.getpass(prompt="Enter password: ")
    passwordlenth = len(password)

    if passwordlenth > 6:
        print("Setting up System...")
        time.sleep(10)
        print("Botting up System...")
        time.sleep(8)
        while True:
            print(
                "Your System has been botted up but not completely installed, please type sudo shutdown to shutdown the system, so it can install the main things."
            )
            shutdown = input(f"{username}linux-system-installiation$ ")
            
            if shutdown == "sudo shutdown" or "sudo shutdown":
                sudopassword = getpass.getpass(prompt="sudo password: ")
                if sudopassword == password:
                
                  print("Shutting down the System...")
                  time.sleep(4)
                  print("Shutdown completed succfully...")
                  time.sleep(1)
                  print("The main installiation has been started")
                  break
                else:
                    print("Wrong password! please try again")
                    continue
            
            else:
                print("Wrong command")
                print("Please try again")
                continue

    else:
        print(
            "Password is less than 6 characters, it should be 6 or more than 6 characters long."
        )
        continue
    
    break
