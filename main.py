from random import choice

possibleOptions = ['R', 'P', 'S']

userInput = input('enter R,P or S: ')

killOptions = {
    "R": "S",
    "S": "P",
    "P": "R"
}

while True:
    while userInput not in possibleOptions:
        print ('incorrect selection.Pls enter R,P or S')
        userInput = input('enter R,P or S: ')

    computerInput = choice(possibleOptions)

    print(f"Player {userInput} : CPU {computerInput}")

    if userInput == computerInput:
        userInput = None
        continue
    if killOptions[userInput] == computerInput:
        print("Player wins")
    else:
        print("CPU wins")
    break
