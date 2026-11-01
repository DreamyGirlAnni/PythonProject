# achievements.py
# Ei file e achievement check er kaj

def check_achievements(won, attempts, elapsed_time, difficulty, max_attempts):
    """Game shesh hole kon achievement unlock hobe seta return kore (list)."""
    unlocked = []

    if not won:
        return unlocked

    # Prothom attempt e jit
    if attempts == 1:
        unlocked.append("🍀 Lucky First Try — prothom guess e jite gecho!")

    # Kom attempt e jit (3 ba tar kom)
    if attempts <= 3:
        unlocked.append("⚡ Speed Demon — matro 3 attempt er moddhe!")

    # Kom somoy e jit (10 second er kom)
    if elapsed_time <= 10:
        unlocked.append("🚀 Lightning Fast — 10 second er kom e!")

    # Hard/Insane difficulty e jit
    if difficulty in ("hard", "insane"):
        unlocked.append(f"🔥 {difficulty.capitalize()} Master — kothin level e jite gecho!")

    # Sob attempt use kore jit (last attempt e jit)
    if attempts == max_attempts:
        unlocked.append("😰 Comeback King — last attempt e jite gecho!")

    # Perfect game — 1 attempt, kom somoy
    if attempts == 1 and elapsed_time <= 5:
        unlocked.append("👑 Perfect Game — ek attempt, 5 second er kom!")

    return unlocked