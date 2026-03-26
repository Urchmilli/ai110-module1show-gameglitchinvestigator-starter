def get_range_for_difficulty(difficulty: str):
    # FIX: Refactored difficulty range mapping from app.py using Copilot
    """Return (low, high) inclusive range for a given difficulty."""
    ranges = {
        "Easy": (1, 50),
        "Normal": (1, 100),
        "Hard": (1, 200),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    # FIX: Implemented input validation and parsing logic with Copilot assistance
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    try:
        guess_int = int(raw.strip())
        return True, guess_int, None
    except ValueError:
        return False, None, f"❌ '{raw}' is not a valid number. Please enter an integer."


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    # FIX: Implemented score calculation logic (points inversely proportional to attempts)
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # Award points inversely proportional to attempts (fewer attempts = more points)
        points = max(100 - (attempt_number * 10), 10)
        return current_score + points
    return current_score
