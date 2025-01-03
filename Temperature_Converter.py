import tkinter as tk

def convert_temperature():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_label.config(text=f"Celsius: {celsius:.2f} °C")
    except ValueError:
        celsius_label.config(text="Invalid input")

window = tk.Tk()
window.title("Temperature Converter")

fahrenheit_label = tk.Label(window, text="Enter Fahrenheit temperature:")
fahrenheit_label.pack()

fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.pack()

convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

celsius_label = tk.Label(window, text="")
celsius_label.pack()

# Start the Tkinter main loop
window.mainloop()
