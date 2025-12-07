import random

def start_new_game(config):
    """Initialize a new game using difficulty settings."""
    return {
        "low": config["low"],
        "high": config["high"],
        "max_attempts": config["max_attempts"],
        "secret": random.randint(config["low"], config["high"]),
        "attempts": 0,
        "active": True,
    }

def check_guess(secret, guess):
    """Return comparison result."""
    if guess == secret:
        return "correct"
    elif guess < secret:
        return "low"
    else:
        return "high"
