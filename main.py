from tkinter import *

# Create the main window
window = Tk()
window.title("Mile to KM Converter")  # Set the title of the window
window.config(padx=100, pady=150)  # Add padding around the window
window.minsize(width=500, height=500)  # Set minimum size for the window

# Function to perform the conversion when the button is clicked
def action():
    miles_data = float(entry.get())  # Get the value from the input field and convert it to float
    km_data = miles_data * 1.60934  # Convert miles to kilometers
    labelkm.config(text=km_data)  # Update the label to display the result

# Entry widget to take input from the user
entry = Entry(window)
entry.grid(row=0, column=1)  # Place the entry widget in the grid

# Label for the unit "miles"
label2 = Label(window, text="miles")
label2.grid(row=0, column=2)  # Place the label in the grid

# Label to display the text "is equal to"
label1 = Label(window, text="is equal to")
label1.grid(row=1, column=0)  # Place the label in the grid

# Label to show the result in kilometers, initially set to "0"
labelkm = Label(window, text="0")
labelkm.grid(row=1, column=1)  # Place the label in the grid

# Label for the unit "km"
label3 = Label(window, text="km")
label3.grid(row=1, column=2)  # Place the label in the grid

# Button to trigger the conversion
button = Button(window, text="Calculate", command=action)
button.grid(row=3, column=1)  # Place the button in the grid

# Start the Tkinter event loop
window.mainloop()
