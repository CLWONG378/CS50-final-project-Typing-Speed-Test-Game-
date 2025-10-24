#!/usr/bin/env python3
"""
Typing Speed Test - Keep session records, Play Again, Top 3 Highlighted
"""

import random
import time

NUM_ROUNDS = 5  # 5 rounds per session

# ---------------- Functions ----------------

def get_player_name():
    """Prompt player to enter their name."""
    name = input("Enter your name: ").strip()
    if not name:
        name = "Player"
    return name

def select_sentences_for_session():
    """Return a list of NUM_ROUNDS unique short sentences."""
    sentences = [
        "Hello world",
        "Python is fun",
        "CS50P rocks",
        "Typing test game",
        "Code and test",
        "Fast and accurate",
        "Keep learning",
        "Test your skills",
        "Try again",
        "Win the game"
    ]
    random.shuffle(sentences)
    return sentences[:NUM_ROUNDS]

def calculate_wpm(elapsed_time, typed_text):
    words = len(typed_text.split())
    minutes = elapsed_time / 60
    if minutes == 0:
        return 0
    return words / minutes

def calculate_accuracy(original, typed):
    if not original:
        return 0
    correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
    return (correct_chars / len(original)) * 100

def play_game():
    """Run a single session of the typing game and return session scores."""
    player_name = get_player_name()
    total_wpm = 0
    total_accuracy = 0

    session_sentences = select_sentences_for_session()

    for round_num, sentence in enumerate(session_sentences, start=1):
        print(f"\nRound {round_num}/{NUM_ROUNDS}:")
        print(sentence)
        start = time.time()
        typed = input("> ")
        end = time.time()
        elapsed = end - start
        wpm = calculate_wpm(elapsed, typed)
        accuracy = calculate_accuracy(sentence, typed)
        print(f"Time: {elapsed:.2f}s, WPM: {wpm:.2f}, Accuracy: {accuracy:.2f}%")
        total_wpm += wpm
        total_accuracy += accuracy

    avg_wpm = total_wpm / NUM_ROUNDS
    avg_accuracy = total_accuracy / NUM_ROUNDS

    # Display thanks page and session results
    print("\n" + "="*40)
    print(f"Thank you for playing, {player_name}!")
    print("Session Results:")
    print(f"Average WPM: {avg_wpm:.2f}")
    print(f"Average Accuracy: {avg_accuracy:.2f}%")
    print("="*40 + "\n")

    return {"name": player_name, "wpm": avg_wpm, "accuracy": avg_accuracy}

def display_session_scoreboard(session_scores):
    """Display scoreboard for current session with top 3 highlighted."""
    if not session_scores:
        print("No scores yet in this session.")
        return

    print("\nSession Scoreboard (Top Players this session):")
    print(f"{'Rank':<5} {'Player':<15} {'WPM':>8} {'Accuracy (%)':>15}")
    print("-"*45)

    # Sort scores descending by WPM
    sorted_scores = sorted(session_scores, key=lambda x: x["wpm"], reverse=True)

    for i, entry in enumerate(sorted_scores, start=1):
        name_display = entry["name"]
        # Highlight top 3
        if i == 1:
            name_display = f"🥇 {name_display}"
        elif i == 2:
            name_display = f"🥈 {name_display}"
        elif i == 3:
            name_display = f"🥉 {name_display}"
        print(f"{i:<5} {name_display:<15} {entry['wpm']:>8.2f} {entry['accuracy']:>15.2f}")

# ---------------- Main Loop ----------------

def main():
    session_scores = []  # Keep all records for current runtime
    while True:
        player_score = play_game()
        session_scores.append(player_score)

        display_session_scoreboard(session_scores)

        # Play again option
        print("\nOptions:")
        print("1. Play Again")
        print("2. Exit")
        choice = input("Enter choice: ").strip()
        if choice != "1":
            print("\nExiting the game. Goodbye!")
            break

if __name__ == "__main__":
    main()
