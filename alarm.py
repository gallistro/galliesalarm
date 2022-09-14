import time
import webbrowser
from audioplayer import AudioPlayer

alarm = (str(input("Enter the time you would like to wake up\n"
                  "(should be in 24 hr format; example:\n"
                  "00:30 = 12:30AM, 14:30 = 2:30PM, etc.)\n"
                  ">>> ")))

print("You have set the alarm.")

now = None # traditional not yet initialized value
while now != alarm:
    now = time.strftime("%H:%M") # update the now variable with the current time. 
    print("The current time is: " + now)
    time.sleep(60)

# this does not need an if block; if the code reaches this point it was already checked by the while loop.
print("Time to wake up!")
AudioPlayer("YOURNEWMORNINGALARM.mp3").play(loop=True, block=True)
