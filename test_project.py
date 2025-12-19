import pytest
from project import calculate_wpm, calculate_accuracy, select_sentences, SENTENCES

# ---------------- Tests for calculate_wpm ----------------

def test_wpm_basic():
    assert calculate_wpm(60, "hello world") == 2  # 2 words per minute in 60s

def test_wpm_zero_time():
    assert calculate_wpm(0, "hello world") == 0  # Avoid division by zero

def test_wpm_multiple_words():
    assert calculate_wpm(30, "one two three four") == 8  # 4 words in 0.5 minutes = 8 WPM

# ---------------- Tests for calculate_accuracy ----------------

def test_accuracy_perfect():
    assert calculate_accuracy("hello", "hello") == 100

def test_accuracy_partial():
    assert calculate_accuracy("hello", "hxllo") == 80  # 4/5 correct

def test_accuracy_none():
    assert calculate_accuracy("hello", "abcde") == 0  # 0 correct

def test_accuracy_empty_original():
    assert calculate_accuracy("", "abc") == 0  # Original empty

# ---------------- Tests for select_sentences ----------------

def test_select_sentences_length():
    sentences = select_sentences("Easy")
    assert len(sentences) == 5  # Always returns NUM_ROUNDS sentences

def test_select_sentences_content():
    sentences = select_sentences("Medium")
    for s in sentences:
        assert s in SENTENCES["Medium"]  # All sentences are from correct difficulty

def test_select_sentences_randomness():
    # Test that repeated calls may return different order (not guaranteed but likely)
    first_call = select_sentences("Hard")
    second_call = select_sentences("Hard")
    assert isinstance(first_call, list) and isinstance(second_call, list)
    assert len(first_call) == len(second_call) == 5
