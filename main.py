
def forest():
    print("youhave been wandering for a while, and are now lost in the forrest. the trees only let you go north or east.")
    forest = input("where would you like to go next? north or east? ")
    if forest == "north":
        print("you find a cave and intruiged, go inside. in there you find the treasure that sent you on this quest! hurrah! youve sucseeded!")
        end()
    elif forest == "east":
        print("you journy for some time, and stumble upon a river.")
        river()

def river():
    print("you are on a riverbank in a forest. alone. the trees only get thicker on the otherside of the river, making crossing pointless. ")
    river = input("would you like to go back to the forest, or swim in the river? ")
    if river == "go back":
        forest()
    elif river == "swim":
        print("you jump in the river and swimm with the current. it feels very nice and you loose track of your surrondings. suddenly, you see that the river becomes a waterfall. too late, you try to grab on but end up falling to your death. you lose")
        end()

def end():
    next = input("would you like to play again? ")
    if next == "yes":
        forest()
    elif next == "no":
        print("so long adventurer!")

forest()