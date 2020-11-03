import random

def timeGenerator():
    minutes = str(random.randint(25,30))
    seconds = (random.randint(0,59))
    if seconds < 10:
        seconds = ("0" + str(seconds))
    else:
        seconds = str(seconds)
        
    print("Your pomodoro is " + minutes + ":" + seconds + " long. Get to it!")

def breakGenerator():
    minutes = str(random.randint(5,8))
    seconds = (random.randint(0,59))
    if seconds < 10:
        seconds = ("0" + str(seconds))
    else:
        seconds = str(seconds)
        
    print("Your break is " + minutes + ":" + seconds + " long. Go do something fun!")

oneMore = 'yes'                  
while oneMore == 'yes':
    timeGenerator()
    breakGenerator()
    print("Would you like another pomodoro? (yes / no)")
    oneMore = input()
    if oneMore == "no":
        break
    else:
        continue

