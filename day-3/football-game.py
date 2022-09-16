print('''
        ___________________________
       |             |             |
       |___          |          ___|
       |_  |         |         |  _|
      .| | |.       ,|.       .| | |.
      || | | )     ( | )     ( | | ||
      '|_| |'       `|'       `| |_|'
       |___|         |         |___|
       |             |             |
       |_____________|_____________|
''')

print("Welcome to the football game. Let's try and score a goal!")
print("")
goalkeeper = input("Your goalkeeper has the ball with the opposition closing down the left back. What way do you pass it? Type Left or Right. ").lower()
if goalkeeper == "left":
    print("You have been tackled and the opposition have scored.")
    exit()
elif goalkeeper == "right":
    print("Great pass to the right back who is being closed down quickly.")
else:
    print("Wrong selection. Game over.")
    exit()
defender = input("Your defender gets the ball and is pressed by the opposition. Do you play it back to the goalkeeper of hoof it forward? Type Back or Forward. ").lower()
if defender == "back":
    print("The goalkeeper wasn't expecting the back pass and has conceded a goal.")
    exit()
elif defender == "forward":
    print("Big hoof up top and the striker is hunting down the ball.")
else:
    print("Wrong selection. Game over.")
    exit()
striker = input("Your striker chases down the long ball. Do you go for goal, play it to the winger on the overlap or carry on dribbling? Type shoot, pass or dribble. ").lower()
if striker == "shoot":
    print("The shot was hit perfectly and nestles in the top corner. You have just won the match!!!")
    exit()
elif striker == "pass":
    print("Unlucky, the pass was intercepted by the opposition who ran up the field and scored.")
elif striker == "dribble":
    print("You were not able to take it around the defender and the opposition have the ball.")
else:
    print("Wrong selection. Game over.")
    exit()