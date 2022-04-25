# import sub

# print(f"Index file's name is {__name__}")

# Sau khi chay
# Sub file's name is sub
# Index file's name is __main__



def welcome():
    print("Welcome to my class")

def function_test():
    print("Do something ....")

def main():
    email = input("Please enter your email address: ").strip()
    username, domain = emailProcess(email=email)
    print(f"username: {username} and doamin: {domain}")

def emailProcess(email):
    username = email[0:email.index("@")]
    domain = email[email.index("@")+1:]
    return [username, domain]


if __name__ == "__main__":
    main()