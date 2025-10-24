import random
import time
import json
import os

SCORES_FILE = "scores.json"

# ---------------- Functions ----------------

def get_player_name():
    """Prompt player to enter their name."""
    name = input("Enter your name: ").strip()
    if not name:
        name = "Player"
    return name

def select_sentence():
    """Return a random sentence for typing."""
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
    return random.choice(sentences)

def calculate_wpm(elapsed_time, typed_text):
    """Calculate words per minute."""
    words = len(typed_text.split())
    minutes = elapsed_time / 60
    if minutes == 0:
        return 0
    return words / minutes

def calculate_accuracy(original, typed):
    """Calculate accuracy percentage of typed text."""
    if not original:
        return 0
    correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
    return (correct_chars / len(original)) * 100

def play_round(round_num):
    """Play a single typing round and return WPM and accuracy."""
    print(f"\nRound {round_num}/10:")
    sentence = select_sentence()
    print(sentence)
    start = time.time()
    typed = input("> ")
    end = time.time()
    elapsed = end - start
    wpm = calculate_wpm(elapsed, typed)
    accuracy = calculate_accuracy(sentence, typed)
    print(f"Time: {elapsed:.2f}s, WPM: {wpm:.2f}, Accuracy: {accuracy:.2f}%")
    return wpm, accuracy

def load_scores():
    """Load scores from file, return as list."""
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_scores(scores):
    """Save scores list to file."""
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def update_scores(player_name, avg_wpm, avg_accuracy):
    """Add current player score to scoreboard."""
    scores = load_scores()
    scores.append({"name": player_name, "wpm": avg_wpm, "accuracy": avg_accuracy})
    scores.sort(key=lambda x: x["wpm"], reverse=True)
    save_scores(scores)
    return scores  # Return updated scores for display

def display_scoreboard(current_player=None):
    """Display top 5 scores with current player highlighted."""
    scores = load_scores()
    if not scores:
        print("\nNo scores yet.")
        return

    print("\nHigh Scores:")
    print(f"{'Rank':<5} {'Player':<15} {'WPM':>8} {'Accuracy (%)':>15}")
    print("-" * 45)

    for i, entry in enumerate(scores[:5], start=1):
        name_display = entry['name']
        if current_player and entry['name'] == current_player:
            name_display = f"*{name_display}*"  # highlight current player
        print(f"{i:<5} {name_display:<15} {entry['wpm']:>8.2f} {entry['accuracy']:>15.2f}")

# ---------------- Main ----------------

def main():
    print("Welcome to the Typing Speed Test!")
    player_name = get_player_name()

    total_wpm = 0
    total_accuracy = 0

    for round_num in range(1, 11):
        wpm, accuracy = play_round(round_num)
        total_wpm += wpm
        total_accuracy += accuracy

    avg_wpm = total_wpm / 10
    avg_accuracy = total_accuracy / 10

    print(f"\nSession Summary for {player_name}:")
    print(f"Average WPM: {avg_wpm:.2f}")
    print(f"Average Accuracy: {avg_accuracy:.2f}%")

    update_scores(player_name, avg_wpm, avg_accuracy)
    display_scoreboard(current_player=player_name)

if __name__ == "__main__":
    main()
