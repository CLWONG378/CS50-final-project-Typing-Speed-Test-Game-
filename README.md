CS50-final-project-Typing-Speed-Test-Game

Made by WONG Chun Lung, Juno


#### Video Demo: <URL HERE>

#### Description:
The Typing Speed Test Game is an interactive Python program designed to help players improve their typing speed and accuracy while providing a fun and engaging experience. The game challenges players to type sentences of varying difficulty within a timed environment, calculates their performance metrics, awards achievements, and maintains a persistent scoreboard for all-time high scores.

The game includes three difficulty levels: Easy, Medium, and Hard. Each level contains a predefined set of sentences, and for each session, five random sentences are selected for the player to type. The player's name is requested at the start of the session, and their performance is tracked throughout the game. After each round, the program provides detailed feedback on typing accuracy, highlighting correct characters in green and mistakes in red. A countdown timer is included before each sentence to give players a moment to prepare.

#### How the Game Works:
1. **Player Setup**: The player enters their name and chooses a difficulty level.
2. **Round Gameplay**: For each of the five sentences:
   - The sentence is displayed in blue.
   - A three-second countdown appears before typing starts.
   - The player types the sentence, and the program measures the elapsed time.
   - Words per minute (WPM) and accuracy percentage are calculated.
   - Mistakes are highlighted using color-coded feedback.
3. **Session Summary**: At the end of five rounds, the program computes the average WPM and accuracy. Achievements such as "Accuracy Master," "Speed Demon," or "Persistent Typist" are awarded based on performance.
4. **Scoreboard**: The player's score is saved in a JSON file, ensuring persistence across sessions. A high score table displays all previous scores, highlighting the top three performers.
5. **Replay Option**: The player can choose to play again or exit the game.

#### Function Descriptions:
- `get_player_name()`: Prompts the user for their name, defaults to "Player" if empty.
- `choose_difficulty()`: Allows the player to select a difficulty level (Easy, Medium, Hard).
- `select_sentences(difficulty)`: Randomly selects five sentences from the chosen difficulty.
- `calculate_wpm(elapsed_time, typed_text)`: Calculates words per minute based on the typed text and elapsed time.
- `calculate_accuracy(original, typed)`: Computes the percentage of correctly typed characters compared to the original sentence.
- `show_mistakes(original, typed)`: Provides color-coded feedback highlighting correct and incorrect characters.
- `countdown()`: Displays a countdown before each sentence starts.
- `play_game()`: Runs a complete game session, calculates statistics, and awards achievements.
- `save_score(score, filename="scores.json")`: Saves the player's score to a JSON file for persistent tracking.
- `load_scores(filename="scores.json")`: Loads all saved scores from the JSON file.
- `display_session_scoreboard(session_scores)`: Displays all-time scores, sorted by accuracy and WPM, with the top three highlighted.
- `main()`: The main loop controlling the game flow, handling replay options, and integrating scoring.

#### Design Choices:
- **Persistent JSON Score Storage**: Ensures players can track progress over multiple sessions.
- **Color Feedback**: Correct characters are shown in green, mistakes in red, improving visual clarity.
- **Achievements**: Motivates players to improve accuracy and speed.
- **Difficulty Levels**: Provides a gradual challenge for beginners to advanced typists.
- **Countdown Timer**: Prepares players for each round, simulating a real typing test environment.
- **Top 3 Highlighting**: Encourages competition and engagement by visually emphasizing top performers.


## Files

`project.py` – main program

`test_project.py` – pytest tests

`requirements.txt` – dependencies

`README.md` – project description

## How to Run

```bash

python project.py
```



