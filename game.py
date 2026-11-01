# ---------- GUI support functions (add at END of game.py) ----------
_current = {}


def gui_start_round(difficulty):
    """GUI theke ek round shuru kore."""
    settings = config.DIFFICULTIES[difficulty]
    _current["difficulty"] = difficulty
    _current["max_num"] = settings["max_num"]
    _current["max_attempts"] = settings["attempts"]
    _current["secret"] = random.randint(1, settings["max_num"])
    _current["low"] = 1
    _current["high"] = settings["max_num"]
    _current["attempts"] = 0
    _current["start_time"] = time.time()

    ui.show_game_start(_current["max_num"], _current["max_attempts"])


def gui_handle_guess(raw):
    """GUI guess button theke call hobe."""
    try:
        guess = int(raw)
    except ValueError:
        ui.show_invalid_input()
        return

    if guess < 1 or guess > _current["max_num"]:
        ui.show_invalid_input()
        return

    _current["attempts"] += 1
    attempts = _current["attempts"]
    max_attempts = _current["max_attempts"]
    secret = _current["secret"]

    if guess == secret:
        elapsed = time.time() - _current["start_time"]
        points = calculate_points(_current["difficulty"], attempts, max_attempts, elapsed)
        ui.show_win(attempts, elapsed, points)
        storage.save_high_score(points)
        unlocked = achievements.check_achievements(
            True, attempts, elapsed, _current["difficulty"], max_attempts
        )
        ui.show_achievements(unlocked)
        stats = storage.update_stats(True, points, attempts, elapsed)
        storage.show_stats(stats)
        return

    if guess < secret:
        _current["low"] = max(_current["low"], guess + 1)
    else:
        _current["high"] = min(_current["high"], guess - 1)

    ui.show_hint(guess, secret, config.CLOSE_RANGE, config.WARM_RANGE)
    ui.show_range_hint(_current["low"], _current["high"])

    if attempts >= max_attempts:
        ui.show_lose(secret)
        storage.update_stats(False, 0, attempts, time.time() - _current["start_time"])