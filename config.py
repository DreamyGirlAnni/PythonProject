# config.py
# Ei file e sudhu settings ar constant thake — kono logic na

# Difficulty settings
# proti difficulty er jonno: maximum number, attempts, ar bonus point
DIFFICULTIES = {
    "easy": {
        "max_num": 50,
        "attempts": 10,
        "bonus": 10,
        "label": "Easy (1-50, 10 attempts)",
    },
    "medium": {
        "max_num": 100,
        "attempts": 7,
        "bonus": 25,
        "label": "Medium (1-100, 7 attempts)",
    },
    "hard": {
        "max_num": 500,
        "attempts": 9,
        "bonus": 50,
        "label": "Hard (1-500, 9 attempts)",
    },
    "insane": {
        "max_num": 1000,
        "attempts": 10,
        "bonus": 100,
        "label": "Insane (1-1000, 10 attempts)",
    },
}

# File names — data save korar jonno
HIGHSCORE_FILE = "highscore.json"
STATS_FILE = "stats.json"
HISTORY_FILE = "history.txt"

# Hint thresholds
CLOSE_RANGE = 5      # difference <= 5 hole "onek kache"
WARM_RANGE = 15      # difference <= 15 hole "kache kache"