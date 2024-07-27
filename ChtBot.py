import tkinter as tk
from tkinter import scrolledtext

# Function for the bot response
def bot_response(user_input):
    # Extended example of responses
    responses = {
        "hello": "Hello! How can I help you?",
        "how are you?": "I'm a bot, so I'm always good. How about you?",
        "what is your name?": "I'm ChatBot. Nice to meet you!",
        "bye": "Goodbye! Have a great day!",
        "what time do you wake up in the morning?": "I usually wake up at 6:30 AM.",
        "do you eat breakfast?": "Yes, I have breakfast every morning.",
        "what do you typically have for breakfast?": "I usually have oatmeal or eggs and toast.",
        "how do you get to work or school?": "I drive to work/school.",
        "what time do you start working or attending classes?": "I start at 9:00 AM.",
        "do you take a lunch break?": "Yes, I take a lunch break around 12:30 PM.",
        "what do you usually do during your lunch break?": "I eat lunch and take a short walk.",
        "what time do you finish work or classes?": "I finish at 5:00 PM.",
        "do you exercise regularly?": "Yes, I try to exercise at least three times a week.",
        "what type of exercise do you do?": "I usually go for a run or do a workout at the gym.",
        "what time do you usually have dinner?": "I usually have dinner around 7:00 PM.",
        "do you cook dinner yourself?": "Yes, I cook dinner most of the time.",
        "what’s your favorite dinner dish to make?": "I like making pasta or stir-fry.",
        "how do you spend your evenings?": "I like to read, watch TV, or spend time with family.",
        "what time do you usually go to bed?": "I usually go to bed around 10:30 PM.",
        "do you have a bedtime routine?": "Yes, I read a book and then turn off the lights.",
        "how often do you check your email or messages?": "I check them a few times throughout the day.",
        "do you drink coffee or tea?": "Yes, I drink coffee in the morning.",
        "how many hours of sleep do you usually get?": "I usually get about 7 to 8 hours of sleep.",
        "do you make your bed every morning?": "Yes, I make my bed as soon as I get up.",
        "how often do you do laundry?": "I do laundry once a week.",
        "do you have any hobbies you practice daily?": "Yes, I like to practice playing the guitar.",
        "what time do you typically take a shower?": "I usually shower in the morning after I wake up.",
        "do you prefer to work in the morning or evening?": "I prefer to work in the morning.",
        "how often do you go grocery shopping?": "I go grocery shopping once a week.",
        "do you listen to music while working or studying?": "Yes, I often listen to music to help me concentrate.",
        "what’s one thing you always do before going to bed?": "I always brush my teeth before bed.",
        "do you have any pets?": "Yes, I have a dog.",
        "how do you unwind before bed?": "I usually watch a TV show or read a book.",
        "do you set an alarm to wake up?": "Yes, I set an alarm to wake up in the morning."
    }
    return responses.get(user_input.lower(), "I don't understand that. Can you please rephrase?")

# Function to send the user input to the chat window and get bot response
def send_message():
    user_input = entry.get()
    if user_input.strip():
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        bot_reply = bot_response(user_input)
        chat_window.insert(tk.END, "Bot: " + bot_reply + "\n")
        chat_window.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

# Main window setup
root = tk.Tk()
root.title("ChatBot")
root.geometry("400x500")

# Chat window
chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Entry widget for user input
entry = tk.Entry(root, width=80)
entry.pack(pady=10, padx=10, fill=tk.X)
entry.bind("<Return>", lambda event: send_message())

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10, padx=10)

# Start the Tkinter event loop
root.mainloop()
