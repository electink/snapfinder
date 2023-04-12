import requests
print("press Ctrl C at any time to escape")
print()

while True:
	name = input("enter a username: ")

	url = requests.get("http://snapchat.com/add/" + name)
	htmltext = url.text


	if "Add me on Snapchat!" in htmltext:
	    print("user found")
	else:
	    print("sorry user not found")
