# Python 2.7.12
#
#Author:    Nikki Yoke
#
# Purpose:  The Tech Academy - Python Course, Drill 1
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember, function name(variable) _means that we passs in the variable.
#           return variable _means that we are returning the variable to
#           the calling function.







def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)



def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, ge the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    if name != "": # meaning, if we do not already have this user's name, then they are a new player and we need to get their name
                 print("\nThanks for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
             if name =="":
                 name = raw_input("\nWhat is your name? ").capitalize()
             if name != "":
                print("\nGreeting, {}!".format(name))
                print("\nIn this game, you will be greeted by several different people. \nYou can be nice or mean.")
                print("At the end of the game your fate will be determined based upon your actions.")
                stop = False
    return name



def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = raw_input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? n/m:").lower()
        if pick == "n":
            print("\nThey smile, wave, and skip off.")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly, and abruptly stores off...")
            mean = (mean + 1)
            stop = False
        score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, you currently have ({}, Nice) and ({} Mean) points.".format(name,nice,mean))


def score(nice,mean,name):
    # score function is being passed the values stores within the 3 variables
    if nice > 5:  # if condition is valid, call win frunction passing the variables so it can use them
        win(nice,mean,name)
    if mean > 5:  # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:         # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    print("\nNice job, {}. you win! \nEveryone loves you, and you now live in a spectacular villa in Italy. You also own a Ferrari.".format(name)) # substiture the {} wildcards with our variables
    again(nice,mean,name) # call again function and pass in our variables


def lose(nice,mean,name):
    print("\nYou really need to work on your social skills, {}. You are now a hobo, and live in a cardboard box under a bridge.".format(name)) #substiture the {} wildcards with our variables
    again(nice,mean,name) # call agina function an pass in our variables


def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to paly again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSee ya later, alligator.")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'YES' or 'n' for 'NO.'")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # notice, I do not reset the name variable, as that name user has elected to place again.
    start(nice,mean,name)
          
        


















if __name__ == "__main__":
    start()
