import pyttsx3
import random
#import convtodeva as deva
#When user runs the prog, this func should be called
#Also should be called every time a new number is to be drawn

globalnum = 0

def obtainNumber(retry):
    global globalnum
    if (retry == 0):
        numberToWrite = random.randint(0,9)
        globalnum = numberToWrite
    else:
        numberToWrite = globalnum


    engine = pyttsx3.init()

    #engine.setProperty('rate', 150)
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[1].id)

    if numberToWrite == 0:
        engine.say("Zero")
        engine.runAndWait()
    elif numberToWrite == 1:
        engine.say("One")
        engine.runAndWait()
    elif numberToWrite == 2:
        engine.say("Two")
        engine.runAndWait()
    elif numberToWrite == 3:
        engine.say("Three")
        engine.runAndWait()
    elif numberToWrite == 4:
        engine.say("Four")
        engine.runAndWait()
    elif numberToWrite == 5:
        engine.say("Five")
        engine.runAndWait()
    elif numberToWrite == 6:
        engine.say("Six")
        engine.runAndWait()
    elif numberToWrite == 7:
        engine.say("Seven")
        engine.runAndWait()
    elif numberToWrite == 8:
        engine.say("Eight")
        engine.runAndWait()
    elif numberToWrite == 9:
        engine.say("Nine")
        engine.runAndWait()

    return numberToWrite

def retryInstruction() :
    engine = pyttsx3.init()
    engine.say("Try again")
    engine.runAndWait()


#number that is to be drawn is now stored and audio work is done

#So, what number is to be drawn is generated at random and the student is asked to draw
#Number to be drawn
#Submit clicked by the user
#OnSubmit event to be triggered
#Accuracy checked by Mugdhas method
#mag he pudcha function call karaycha

#number to be drawn and accuracy of resultant drawing to be passed as parameters


# if 1 is returned, then valid drawing. So will print spelling (and Devanagari writing)? on the main screen
# if 0 is returned, then drawing is invalid. So will print Wrong Drawing on the screen. Then will give a new number?
