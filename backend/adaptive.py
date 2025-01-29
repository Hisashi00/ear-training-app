class AdaptiveDifficulty:
    def __init__(self):
        self.correct_streak = 0  # Tracks consecutive correct answers
        self.difficulty = "medium"  # Default difficulty

    def update_difficulty(self, correct: bool):
        """Adjust difficulty based on user performance."""
        if correct:
            self.correct_streak += 1
        else:
            self.correct_streak = max(0, self.correct_streak - 2)  # Penalize for mistakes

        if self.correct_streak >= 3:
            self.difficulty = "hard"
        elif self.correct_streak >= 1:
            self.difficulty = "medium"
        else:
            self.difficulty = "easy"

        return self.difficulty
