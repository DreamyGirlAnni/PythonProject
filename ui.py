# ui.py
# Ei file e sob "dekhanor" kaj — print, color, message, decoration

from colorama import Fore, Style, init

init(autoreset=True)   # proti print er por color auto reset hobe


def print_header():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + Style.BRIGHT + "🎮  NUMBER GUESSING GAME  🎮")
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)


def show_difficulty_menu(difficulties):
    print(Fore.YELLOW + "\n🎚️  Difficulty choose koro:")
    keys = list(difficulties.keys())
    for i, key in enumerate(keys, start=1):
        print(f"  {i}. {difficulties[key]['label']}")
    print(Style.RESET_ALL)


def show_game_start(max_num, attempts):
    print(Fore.GREEN + f"\n✅ Range: 1 to {max_num}")
    print(Fore.GREEN + f"✅ Attempts: {attempts}")
    print(Style.RESET_ALL)


def show_attempt_prompt(attempt, max_attempts):
    return input(Fore.WHITE + f"\nAttempt {attempt}/{max_attempts} — Tomar guess: " + Style.RESET_ALL)


def show_invalid_input():
    print(Fore.RED + "⚠️  Number dao (1-100 er moddhe), onno kichu na!" + Style.RESET_ALL)


def show_hint(guess, secret, close_range, warm_range):
    difference = abs(guess - secret)

    if difference <= close_range:
        print(Fore.RED + Style.BRIGHT + "🔥 Onek kache! Ar ektu!" + Style.RESET_ALL)
    elif difference <= warm_range:
        print(Fore.YELLOW + "🌡️  Kache kache..." + Style.RESET_ALL)
    elif guess < secret:
        print(Fore.BLUE + "📈 Choto! Aro boro number try koro." + Style.RESET_ALL)
    else:
        print(Fore.BLUE + "📉 Boro! Aro choto number try koro." + Style.RESET_ALL)


def show_range_hint(low, high):
    print(Fore.MAGENTA + f"   💡 Ekhon range: {low} – {high}" + Style.RESET_ALL)


def show_win(attempts, elapsed_time, points):
    print(Fore.GREEN + Style.BRIGHT + "\n" + "╔" + "═" * 40 + "╗")
    print("║" + "🎉  YOU WIN!  🎉".center(40) + "║")
    print("╚" + "═" * 40 + "╝" + Style.RESET_ALL)
    print(Fore.GREEN + f"⏱️  Time: {elapsed_time:.1f} second")
    print(Fore.GREEN + f"🎯 Attempts: {attempts}")
    print(Fore.GREEN + f"💰 Points: +{points}" + Style.RESET_ALL)


def show_lose(secret):
    print(Fore.RED + Style.BRIGHT + "\n😢 Attempt shesh! Tumi harle." + Style.RESET_ALL)
    print(Fore.RED + f"🔍 Number ta chilo: {secret}" + Style.RESET_ALL)


def show_high_score(score):
    if score is None:
        print(Fore.CYAN + "🏆 High Score: ekhono kono record nei!" + Style.RESET_ALL)
    else:
        print(Fore.CYAN + f"🏆 Best score: {score} points" + Style.RESET_ALL)


def show_achievements(achievements):
    if not achievements:
        return
    print(Fore.YELLOW + "\n🏅 Achievements Unlocked:" + Style.RESET_ALL)
    for a in achievements:
        print(Fore.YELLOW + f"   {a}" + Style.RESET_ALL)


def ask_replay():
    answer = input(Fore.CYAN + "\n🔁 Abar khelte chao? (y/n): " + Style.RESET_ALL)
    return answer.strip().lower() == "y"


def show_goodbye():
    print(Fore.CYAN + "\n👋 Khela sesh! Abar asho!" + Style.RESET_ALL)