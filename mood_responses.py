# 1. Python Modules and Data Handling Assignment

# Objective: The aim of this assignment is to assess your understanding and ability to implement Python modules, both built-in and custom, and to apply data handling techniques using Python's data structures and error handling. This assignment will help solidify your grasp on creating and using modules, as well as manipulating and processing data effectively in Python.

# Task 1: Your Mood Today

# Problem Statement: Create a Python program using a custom module holding a function that asks the user how they are feeling today and responds with a custom message based on the mood entered. This function should then be imported and used in another file "main.py".
# Code Example:

# mood_responses.py

#def mood_response(mood):
    #responses = {
        #'happy': "That's great to hear! :)",
        #'excited': "That's awesome! Keep up the excitement! :D",
        #'sad': "I'm sorry to hear that. I hope things get better soon. :()",
        #'angry': "Take a deep breath. It's going to be okay. v_v",
        #'bored': "Maybe try something new to spice things up! 0_0",
        #'tired': "Make sure to get some rest and take care of yourself! z_z"
    #}
    #return responses.get(mood.lower(), "I'm not sure how to respond to that, but I hope you have a good day! :D")

# Task 1

def mood_response(mood):
    mood = mood
    if mood == "happy":
        return "\nThats Great To Hear! :D"
    elif mood == "sad":
        return "\nI'm sorry to hear that. I hope your day gets better soon. :("
    elif mood == "angry":
        return "\nIt's okay, just take a deep breath. v_v "
    elif mood == "bored":
        return "\nGo outside and enjoy life! :P"
    elif mood == "annoyed":
        return "\nEverything will be fine just relax. 0_0 "
    elif mood == "tired":
        return "\nMake sure to get some rest and take care of yourself! z_z "
    else:
        return "\nSorry Please Type In Valid Response! :/ "

