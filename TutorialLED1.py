##The commented out code below turns the LED on
'''import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.output(7,True) ##Turn on GPIO pin 7'''
####

##Making LED blink
import RPi.GPIO as GPIO ##Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
 
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ##Setup GPIO Pin 7 to OUT
 
##Define a function named Blink()
def Blink(numTimes, speed):
    for i in range(0, numTimes): ##Run loop numTimes
        print "Iteration " + str(i+1) ##Print current loop
        GPIO.output(7, True) ##Switch on Pin 7
        time.sleep(speed)##Wait
        GPIO.output(7, False) ##Switch off Pin 7
        time.sleep(speed) ##Wait
    print "Done" ##When loop is complete, print "Done"
    GPIO.cleanup()
 
##Ask user for total number of blinks and length of each blink
def start():
    iterations = raw_input("Enter total number of times to blink: ")
    speed = raw_input("Enter length of each blink(seconds): ")
 
##Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
    Blink(int(iterations), float(speed))
    start()
start()
##NOTE: Indentation is very important in python. Use TAB to match formatting