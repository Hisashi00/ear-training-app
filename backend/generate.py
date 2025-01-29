import random

# Define note frequencies (A4 = 440 Hz, using MIDI numbers)
notes = ["C", "D", "E", "F", "G", "A", "B"]
intervals = {
    "Unison": 0, "Minor 2nd": 1, "Major 2nd": 2, "Minor 3rd": 3,
    "Major 3rd": 4, "Perfect 4th": 5, "Tritone": 6, "Perfect 5th": 7,
    "Minor 6th": 8, "Major 6th": 9, "Minor 7th": 10, "Major 7th": 11, "Octave": 12
}

def generate_interval(difficulty_level):
    """Generate a random interval based on difficulty."""
    root_note = random.choice(notes)
    interval_list = list(intervals.keys())

    if difficulty_level == "easy":
        interval = random.choice(interval_list[:5])  # Unison to Perfect 4th
    elif difficulty_level == "medium":
        interval = random.choice(interval_list[:9])  # Unison to Major 6th
    else:  # hard
        interval = random.choice(interval_list)  # All intervals

    return {"root": root_note, "interval": interval}
