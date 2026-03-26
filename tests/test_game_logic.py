from ../logic_utils import check_guess

def test_winning_guess():
    # FIX: Updated tests to properly unpack tuple return value (outcome, message) with Copilot
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_check_guess_returns_tuple():
    # FIX: Added regression test for tuple return type with Copilot
    """Verify check_guess returns a tuple of (outcome, message)"""
    result = check_guess(50, 50)
    assert isinstance(result, tuple)
    assert len(result) == 2
    outcome, message = result
    assert isinstance(outcome, str)
    assert isinstance(message, str)
