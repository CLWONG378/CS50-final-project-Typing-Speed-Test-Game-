import pytest
from project import calculate_wpm, calculate_accuracy, select_sentences_for_session

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

def test_select_sentences_unique_and_count():
    sentences = select_sentences_for_session()
    # Check that we have exactly 5 sentences
    assert len(sentences) == 5
    # Check that all sentences are unique
    assert len(sentences) == len(set(sentences))
