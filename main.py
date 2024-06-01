from tkinter import *
from gtts import gTTS
import playsound

# Initialize Tkinter window
root = Tk()
root.title("Text to Speech Converter")  # Set window title

# Calculate the center position for the window
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")  # Set window size and position
root.configure(bg='light blue')  # Set background color of window

# Heading label
Label(root, text="TEXT TO SPEECH", font="arial 20 bold", bg='light blue').pack(pady=10)

# Label for input field with bigger font size
Label(root, text="Enter Text", font='arial 18 bold', bg='light blue').pack()

# Frame to contain the text widget and make it responsive
text_frame = Frame(root, bg='light blue')
text_frame.pack(pady=10, padx=20, expand=True, fill=BOTH)

# Text widget for user input with word wrapping and fitting the window
text_widget = Text(text_frame, wrap=WORD, font='Arial 14')
text_widget.pack(side=LEFT, expand=True, fill=BOTH)

# Scrollbar for the text widget
scrollbar = Scrollbar(text_frame, command=text_widget.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_widget.config(yscrollcommand=scrollbar.set)

# Frame to contain the buttons and make them responsive
button_frame = Frame(root, bg='light blue')
button_frame.pack(pady=10)

# Function to convert text to speech
def Text_to_speech():
    Message = text_widget.get("1.0", END)
    speech = gTTS(text=Message)
    speech.save('ConvertedSpeech.mp3')
    playsound.playsound('ConvertedSpeech.mp3')

# Function to exit the application
def Exit():
    root.destroy()

# Function to reset the input field
def Reset():
    text_widget.delete("1.0", END)

# Buttons for play, exit, and reset
Button(button_frame, text="PLAY", font='arial 15 bold', command=Text_to_speech, width=6, bg='green').pack(side=LEFT, padx=10)
Button(button_frame, font='arial 15 bold', text='EXIT', width=6, command=Exit, bg='red').pack(side=LEFT, padx=10)
Button(button_frame, font='arial 15 bold', text='RESET', width=6, command=Reset, bg='blue').pack(side=LEFT, padx=10)

# Label at the bottom
Label(root, text="Text Converter", font='arial 15 bold', bg='light blue', width='20').pack(side=BOTTOM, pady=10)

# Run the Tkinter event loop
root.mainloop()
