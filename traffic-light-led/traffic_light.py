from gpiozero import LED
from time import sleep
import threading

loop = True
set_color = "none"

# Define GPIO for LEDs
green = LED(17)
red = LED(22)
yellow = LED(24)

# Define functions for the threads
def loop_colors():
    global loop
    # Loop through colors of the LED while variable is True 
    # the loop must complete 1 cycle once the final color is set and the loop variable is set to False
    while loop:
        green.on()
        sleep(1)
        green.off()
        sleep(1)
        yellow.on()
        sleep(1)
        yellow.off()
        sleep(1)
        red.on()
        sleep(1)
        red.off()
        sleep(1)

def ask_for_color():
    global loop
    global set_color
    while True:
        color = input("Enter color:")
        # Once user enters one of the 3 valid inputs, end the loop and set the final LED color
        if color == "green":
            loop = False
            set_color = "green"
            break
        elif color == "yellow":
            loop = False
            set_color = "yellow"
            break
        elif color == "red":
            loop = False
            set_color = "red"
            break

if __name__ == "__main__":
    # Turn off all lights at the start
    green.off()
    yellow.off()
    red.off()

    # Create threading
    t1 = threading.Thread(target=loop_colors)
    t2 = threading.Thread(target=ask_for_color)

    t1.daemon = True
    t2.daemon = True

    # Start both threads
    t1.start()
    t2.start()

    # Wait until both threads complete
    t1.join()
    t2.join()

    # Set final LED color based on user input
    if set_color == "green":
        green.on()
        yellow.off()
        red.off()
    elif set_color == "yellow":
        green.off()
        yellow.on()
        red.off()
    elif set_color == "red":
        green.off()
        yellow.off()
        red.on()
