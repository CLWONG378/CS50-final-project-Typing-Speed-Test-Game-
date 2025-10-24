import pytest
from project import calculate_wpm, calculate_accuracy, select_sentence

def test_calculate_wpm():
    typed = "This is a test"
    elapsed = 30  # seconds
    wpm = calculate_wpm(elapsed, typed)
    expected = len(typed.split()) / (elapsed / 60)
    assert abs(wpm - expected) < 1e-6

def test_calculate_accuracy_perfect():
    original = "Hello"
    typed = "Hello"
    acc = calculate_accuracy(original, typed)
    assert acc == 100

def test_calculate_accuracy_partial():
    original = "Hello"
    typed = "Hillo"
    acc = calculate_accuracy(original, typed)
    assert abs(acc - 80) < 1e-6

def test_select_sentence_in_list():
    sentences_list = [
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
    sentence = select_sentence()
    assert sentence in sentences_list
