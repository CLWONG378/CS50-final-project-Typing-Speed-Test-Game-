import string
import pytest
from project import select_sentence, calculate_wpm, calculate_accuracy

def test_select_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python programming is fun and educational.",
        "CS50P final project is exciting!",
        "Always write clean and readable code.",
        "Practice makes perfect in coding and typing."
    ]
    sentence = select_sentence()
    assert sentence in sentences

def test_calculate_wpm():
    typed = "This is a test"
    elapsed = 30  # 30 seconds
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
    # 4/5 correct
    assert abs(acc - 80) < 1e-6
