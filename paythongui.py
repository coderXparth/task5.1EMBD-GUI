import RPi.GPIO as GPIO
import tkinter as tk

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
LED_PINS = {'red': 17, 'white': 27, 'green': 22}

for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to turn on the selected LED
def turn_on_led(selected_color):
    for color, pin in LED_PINS.items():
        if color == selected_color:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)

# Function to exit the GUI and clean up GPIO
def exit_app():
    GPIO.cleanup()
    root.destroy()

# Create the GUI
root = tk.Tk()
root.title("LED Controller")

# Add radio buttons for selecting the LED
led_var = tk.StringVar(value='red')

tk.Radiobutton(root, text="Red LED", variable=led_var, value='red', command=lambda: turn_on_led('red')).pack(anchor=tk.W)
tk.Radiobutton(root, text="White LED", variable=led_var, value='white', command=lambda: turn_on_led('white')).pack(anchor=tk.W)
tk.Radiobutton(root, text="Green LED", variable=led_var, value='green', command=lambda: turn_on_led('green')).pack(anchor=tk.W)

# Add an exit button
tk.Button(root, text="Exit", command=exit_app).pack()

# Start the GUI main loop
root.mainloop()