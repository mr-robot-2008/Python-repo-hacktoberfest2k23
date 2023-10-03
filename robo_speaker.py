import os

if __name__ == '__main__':
    print("welcome to the Robot speaker")
    while True:
        x = input("Write your message: ")
        if x == "q":
            break
        command = f"say {x}"
        os.system(command)