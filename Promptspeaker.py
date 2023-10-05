import os

if __name__ == "__main__":
    print("Welcome to PromptSpeaker 1.1 Created by Akhil")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "exit":
            os.system("ba bye friend , thank you for using prompspeaker 1.1")
            break
        command = f"say{x}"
        os.system(command)
