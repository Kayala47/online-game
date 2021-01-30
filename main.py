# this file's objective is to send data to a Cloudflare Worker in order to host our game

# lets first install the package we need: requests
import requests

# constants: URL of our website
URL = "https://josh-game.kayala.workers.dev/"

# make a function to send information to our website


def sendMessage(type: str, user: str, message: str):
    if (typeofMsg == "GET"):
        response = requests.get(URL)
        print(response.text)
    else:
        # POST

        # first, let's make the JSON object
        json = "{user:" + user + ",message:" + message + "}"

        response = requests.post(URL, data=json)


def main():
    print("This is josh's hw!")

    # take information using input()

    # 1. ask the user whether they're doing a POST or a GET and write down the response as the variable "type"
    typeofMsg = input("What type of message do you want to send?")
    if (typeofMsg.capitalize() == "GET"):
        print("This is a GET message")
    elif (typeofMsg.capitalize == "POST"):
        print("This is a POST message")
        # POST
    # 2. ask the user what their name is and write it down as the variable "user"
    user = input("What is your username?")

    # 3. ask the user what their message is and write it down as the variable "message"
    if (typeofMsg == "POST"):
        msg = input("What message do you want to send?")

    print("Sent message of type: " + typeofMsg +
          ". The message was from username " + user + " and said: " + msg)


# don't touch this :)
if __name__ == "__main__":
    main()
