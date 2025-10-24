#!/usr/bin/env python3
"""
Advanced Typing Speed Test Game
Features:
- Difficulty levels
- Countdown timer
- Mistake feedback
- Session stats
- Colored output
- Achievements
- Session scoreboard with top 3
- Play Again option
"""

import random
import time
from colorama import init, Fore, Style

init(autoreset=True)  # initialize colorama

NUM_ROUNDS = 5

# Sample sentences categorized by difficulty
SENTENCES = {
    "Easy": [
        "Hello world",
        "Python is fun",
        "CS50P rocks",
        "Typing test game",
        "Code and test",
        "Keep learning",
        "Try again",
        "Win the game"
    ],
    "Medium": [
        "Python programming is very useful",
        "Learning new skills is fun",
        "Practice makes perfect every day",
        "Testing your typing improves speed",
        "Consistency is key to success",
        "Focus on accuracy before speed",
        "Intermediate challenges are good",
        "Debugging code is essential"
    ],
    "Hard": [
        "The quick brown fox jumps over the lazy dog",
        "Complex sentences include commas, semicolons; and colons",
        "Accuracy and speed are both critical for advanced typists",
        "Mastering keyboard shortcuts can save valuable time",
        "Programming challenges enhance problem-solving abilities",
        "Python lists, dictionaries, and sets have unique properties",
        "Efficiency in coding can reduce runtime errors significantly",
        "Persistent practice builds muscle memory and skill"
    ]
}

# ---------------- Utility Functions ----------------

def get_player_name():
    name = input("Enter your name: ").strip()
    if not name:
        name = "Player"
    return name

def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter choice (1-3): ").strip()
    if choice == "2":
        return "Medium"
    elif choice == "3":
        return "Hard"
    return "Easy"

def select_sentences(difficulty):
    sentences = SENTENCES[difficulty][:]
    random.shuffle(sentences)
    return sentences[:NUM_ROUNDS]

def calculate_wpm(elapsed_time, typed_text):
    words = len(typed_text.split())
    minutes = elapsed_time / 60
    return 0 if minutes == 0 else words / minutes

def calculate_accuracy(original, typed):
    if not original:
        return 0
    correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
    return (correct_chars / len(original)) * 100

def show_mistakes(original, typed):
    mistakes = []
    for i, o in enumerate(original):
        if i < len(typed):
            if typed[i] != o:
                mistakes.append(Fore.RED + typed[i] + Style.RESET_ALL)
            else:
                mistakes.append(Fore.GREEN + typed[i] + Style.RESET_ALL)
        else:
            mistakes.append(Fore.RED + "_" + Style.RESET_ALL)
    if len(typed) > len(original):
        extra = typed[len(original):]
        mistakes += [Fore.RED + c + Style.RESET_ALL for c in extra]
    print("Mistakes/Feedback: " + "".join(mistakes))

def countdown():
    for i in range(3, 0, -1):
        print(f"{Fore.YELLOW}{i}...{Style.RESET_ALL}")
        time.sleep(1)
    print(Fore.CYAN + "Go!" + Style.RESET_ALL)

# ---------------- Gameplay ----------------

def play_game():
    player_name = get_player_name()
    difficulty = choose_difficulty()
    session_sentences = select_sentences(difficulty)

    total_wpm = 0
    total_accuracy = 0
    round_stats = []

    print(f"\nStarting {difficulty} game for {player_name}!\n")

    for i, sentence in enumerate(session_sentences, start=1):
        print(f"\nRound {i}/{NUM_ROUNDS}:")
        print(Fore.BLUE + sentence + Style.RESET_ALL)
        countdown()
        start_time = time.time()
        typed = input("> ")
        elapsed = time.time() - start_time
        wpm = calculate_wpm(elapsed, typed)
        acc = calculate_accuracy(sentence, typed)
        total_wpm += wpm
        total_accuracy += acc
        round_stats.append({"wpm": wpm, "accuracy": acc})
        print(f"Time: {elapsed:.2f}s, WPM: {wpm:.2f}, Accuracy: {acc:.2f}%")
        show_mistakes(sentence, typed)

    avg_wpm = total_wpm / NUM_ROUNDS
    avg_acc = total_accuracy / NUM_ROUNDS

    # Achievements
    achievements = []
    if avg_acc == 100:
        achievements.append("Accuracy Master 🏆")
    if avg_wpm >= 60:
        achievements.append("Speed Demon ⚡")
    if NUM_ROUNDS >= 5:
        achievements.append("Persistent Typist 💪")

    print("\n" + "="*50)
    print(f"Thank you for playing, {player_name}!")
    print(f"Average WPM: {avg_wpm:.2f}")
    print(f"Average Accuracy: {avg_acc:.2f}%")
    if achievements:
        print("Achievements earned: " + ", ".join(achievements))
    print("="*50 + "\n")

    return {"name": player_name, "wpm": avg_wpm, "accuracy": avg_acc}

def display_session_scoreboard(session_scores):
    """Sort by accuracy then WPM, top 3 highlighted."""
    if not session_scores:
        print("No scores yet in this session.")
        return

    print("\nSession Scoreboard:")
    print(f"{'Rank':<5} {'Player':<20} {'WPM':>8} {'Accuracy (%)':>15}")
    print("-"*55)

    sorted_scores = sorted(
        session_scores,
        key=lambda x: (x["accuracy"], x["wpm"]),
        reverse=True
    )

    for i, entry in enumerate(sorted_scores, start=1):
        name_display = entry["name"]
        if i == 1:
            name_display = f"🥇 {name_display}"
        elif i == 2:
            name_display = f"🥈 {name_display}"
        elif i == 3:
            name_display = f"🥉 {name_display}"
        print(f"{i:<5} {name_display:<20} {entry['wpm']:>8.2f} {entry['accuracy']:>15.2f}")

# ---------------- Main Loop ----------------

def main():
    session_scores = []

    while True:
        score = play_game()
        session_scores.append(score)
        display_session_scoreboard(session_scores)

        print("\nOptions:")
        print("1. Play Again")
        print("2. Exit")
        choice = input("Enter choice: ").strip()
        if choice != "1":
            print("\nExiting the game. Goodbye!")
            break

if __name__ == "__main__":
    main()
