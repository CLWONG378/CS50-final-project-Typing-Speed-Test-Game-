#!/usr/bin/env python3
"""
Typing Speed Test
"""

import random
import time

def select_sentence():
    """Return a random sentence for the user to type."""
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python programming is fun and educational.",
        "CS50P final project is exciting!",
        "Always write clean and readable code.",
        "Practice makes perfect in coding and typing."
    ]
    return random.choice(sentences)

def calculate_wpm(elapsed_time, typed_text):
    """Calculate words per minute."""
    words = len(typed_text.split())
    minutes = elapsed_time / 60
    if minutes == 0:
        return 0
    return words / minutes

def calculate_accuracy(original, typed):
    """Calculate percentage of correctly typed characters."""
    if not original:
        return 0
    correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
    return (correct_chars / len(original)) * 100

def play_round():
    """Play one round of typing test."""
    sentence = select_sentence()
    print("Type the following sentence:")
    print(sentence)
    start = time.time()
    typed = input("> ")
    end = time.time()
    elapsed = end - start
    wpm = calculate_wpm(elapsed, typed)
    accuracy = calculate_accuracy(sentence, typed)
    print(f"\nResults:")
    print(f"Time: {elapsed:.2f} seconds")
    print(f"Words per minute: {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

def main():
    """Main CLI for Typing Speed Test."""
    print("Welcome to the Typing Speed Test!")
    while True:
        play_round()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
