# storage.py
# Ei file e sob file save/load er kaj — high score, stats, history

import json
import config


def load_high_score():
    """High score file theke load kore. Na thakle None dey."""
    try:
        with open(config.HIGHSCORE_FILE, "r") as f:
            data = json.load(f)
            return data.get("best_score")
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def save_high_score(score):
    """Notun score jodi purono theke boro hoy, tobe save kore."""
    current = load_high_score()
    if current is None or score > current:
        with open(config.HIGHSCORE_FILE, "w") as f:
            json.dump({"best_score": score}, f, indent=2)
        return True
    return False


def load_stats():
    """Stats load kore. Na thakle default dey."""
    try:
        with open(config.STATS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "games_played": 0,
            "wins": 0,
            "losses": 0,
            "total_points": 0,
            "best_attempts": None,
            "fastest_time": None,
        }


def save_stats(stats):
    """Stats file e save kore."""
    with open(config.STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2)


def update_stats(won, points, attempts, elapsed_time):
    """Ek game shesh hole stats update kore."""
    stats = load_stats()
    stats["games_played"] += 1
    stats["total_points"] += points

    if won:
        stats["wins"] += 1
        if stats["best_attempts"] is None or attempts < stats["best_attempts"]:
            stats["best_attempts"] = attempts
        if stats["fastest_time"] is None or elapsed_time < stats["fastest_time"]:
            stats["fastest_time"] = round(elapsed_time, 1)
    else:
        stats["losses"] += 1

    save_stats(stats)
    return stats


def add_history(entry):
    """History file e ek line add kore."""
    with open(config.HISTORY_FILE, "a") as f:
        f.write(entry + "\n")


def show_stats(stats):
    """Stats print kore (formatted)."""
    print("\n📊 Tomar Statistics:")
    print(f"   Games played : {stats['games_played']}")
    print(f"   Wins         : {stats['wins']}")
    print(f"   Losses       : {stats['losses']}")
    print(f"   Total points : {stats['total_points']}")
    if stats["best_attempts"] is not None:
        print(f"   Best attempts: {stats['best_attempts']}")
    if stats["fastest_time"] is not None:
        print(f"   Fastest time : {stats['fastest_time']}s")