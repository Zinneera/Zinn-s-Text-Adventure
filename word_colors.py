
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Modules.colors_module import bcolors


def print_colored_sentence(sentence, word_colors):
    """
    Prints a sentence with individual words in different colors.
    
    Args:
        sentence (str): The full sentence.
        word_colors (dict): A dictionary where keys are words, and values are the color codes.
    """
    words = sentence.split()  # Split the sentence into words
    colored_sentence = ""

    for word in words:
        # Check if the word should be colored
        if word in word_colors:
            colored_sentence += word_colors[word] + word + bcolors.ENDC + " "
        else:
            colored_sentence += word + " "

    print(colored_sentence.strip())

# Example Usage
#sentence = "Second test for colors"
#word_colors = {
#    "Second": bcolors.OKGREEN,
#    "test": bcolors.OKCYAN,
#    "for": bcolors.OKBLUE,
#    "colors": bcolors.MAGENTA,
#}

#print_colored_sentence(sentence, word_colors)
