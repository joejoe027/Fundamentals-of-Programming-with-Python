from collections import defaultdict

def sign_up(users):
    username = input("Create a username: ")
    password = input("Create a password: ")
        
    if username not in users:
        users[username] = password
        print("You have successfully Signed Up!")
        return username
    else:
        print("Username already exists")
        sign_up()

def log_in(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if (username not in users) and (users[username] != password):
        print("Username does not exist and password is incorrect")
        log_in(users)
    if username not in users:
        print("Username does not exist")
        log_in(users)
    elif users[username] != password:
        print("Password is incorrect")
        log_in(users)
    else:
        print("You have successfully Logged In!")
        return username

def browse_profiles(currentUser,users,network):
    users_list = set(users.keys())
    
    # remove yourself and users you already follow
    remove_list = network[currentUser].copy()
    remove_list.append(currentUser)
    users_list = list(users_list.difference(set(remove_list)))
    
    if(len(users_list) != 0):
        for i in range(len(users_list)):
            print(str(i + 1) + ". " + users_list[i])
            
        chose_to_follow = int(input("Pick a person to follow: "))
        
        network[currentUser].append(users_list[chose_to_follow - 1])
    else:
        print("You follow everyone!!")

def following_list(currentUser,network):
    for user in network[currentUser]:
        print(user)

def followers_list(currentUser,network):
    for user in network:
        if user != currentUser and currentUser in network[user]:
            print(user)

def friends_list(currentUser,network):
    for user in network[currentUser]:
        if currentUser in network[user]:
            print(user)

def main_menu():
    users = {}
    network = defaultdict(list)
    currentUser = None
    exit = False
    
    while not exit:
        if currentUser == None:
            print("1. Sign Up")
            print("2. Log In")
            print("3. Exit")
            command = input("Please pick a command: ")
                
            if(command == "1"):
                currentUser = sign_up(users)
            elif(command == "2"):
                currentUser = log_in(users)
            elif(command == "3"):
                exit = True
        else:
            print("1. Find someone to follow")
            print("2. Find who you follow")
            print("3. Find who follows you")
            print("4. Find those who you follow and they follow you back")
            print("5. Log Out")
            command = input("Welcome "+currentUser+" please pick a command: ")
            
            if(command == "1"):
                browse_profiles(currentUser,users,network)
            elif (command == "2"):
                following_list(currentUser,network)
            elif (command == "3"):
                followers_list(currentUser,network)
            elif (command == "4"):
                friends_list(currentUser,network)
            elif(command == "5"):
                currentUser = None

main_menu()


