#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"


def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()

    user_choice_label.config(
        text=f"You chose {user_choice}", background="blue")
    computer_choice_label.config(
        text=f"Computer chose {computer_choice}", background="red")

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)


window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

instruction_label = tk.Label(window, text="Choose your move:")
instruction_label.pack()

user_choice_var = tk.StringVar()
user_choice_var.set("rock")
rock_radio = tk.Radiobutton(
    window, text="Rock", variable=user_choice_var, value="rock")
paper_radio = tk.Radiobutton(
    window, text="Paper", variable=user_choice_var, value="paper")
scissors_radio = tk.Radiobutton(
    window, text="Scissors", variable=user_choice_var, value="scissors")
rock_radio.pack()
paper_radio.pack()
scissors_radio.pack()
play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()
user_choice_label = tk.Label(window, text="", background="lightblue")
user_choice_label.pack()
computer_choice_label = tk.Label(window, text="", background="lightcoral")
computer_choice_label.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()


# In[ ]:




