class User:
    def __init__(self, login, passw):
        self.login = login
        self.password = passw

users = [User("fimma", "123f1i1m2a1321"), User("henrys", "tumZAEbi"), User("maryus", "59qiIC3B"),
        User("cartol", "VgAhZjV6"), User("StephenSuper", "e1cP3SyA87ak")]

def main():
    flag = False
    input_login = input("Enter login: ")
    for user in users:
        if user.login == input_login:
            print(f"Login: {user.login} Password: {user.password}")
            flag = True
            break
    
    if not flag:
        print("\033[31mUser not found\033[0m")
        main()

if __name__ == "__main__":
    main()