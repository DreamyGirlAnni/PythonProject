# gui.py
# Tkinter GUI — terminal er bodole sundor window

import tkinter as tk
from tkinter import messagebox
import config


# ---------- Global window state ----------
_root = None
_widgets = {}


def init_gui():
    """Window create kore — main_gui.py theke call hobe."""
    global _root, _widgets

    _root = tk.Tk()
    _root.title("🎮 Number Guessing Game")
    _root.geometry("500x600")
    _root.configure(bg="#1e1e2e")
    _root.resizable(False, False)

    # Title
    tk.Label(
        _root, text="🎮  NUMBER GUESSING GAME  🎮",
        font=("Segoe UI", 16, "bold"),
        fg="#89b4fa", bg="#1e1e2e"
    ).pack(pady=15)

    # High score label
    _widgets["high_score"] = tk.Label(
        _root, text="", font=("Segoe UI", 10),
        fg="#a6e3a1", bg="#1e1e2e"
    )
    _widgets["high_score"].pack()

    # Difficulty frame
    diff_frame = tk.Frame(_root, bg="#1e1e2e")
    diff_frame.pack(pady=10)

    tk.Label(
        diff_frame, text="Difficulty:",
        font=("Segoe UI", 11, "bold"),
        fg="#cdd6f4", bg="#1e1e2e"
    ).pack()

    _widgets["difficulty_var"] = tk.StringVar(value="medium")
    for key in config.DIFFICULTIES:
        tk.Radiobutton(
            diff_frame, text=config.DIFFICULTIES[key]["label"],
            variable=_widgets["difficulty_var"], value=key,
            font=("Segoe UI", 9), fg="#cdd6f4", bg="#1e1e2e",
            selectcolor="#313244", activebackground="#1e1e2e",
            activeforeground="#89b4fa"
        ).pack(anchor="w")

    # Start button
    _widgets["start_btn"] = tk.Button(
        _root, text="▶  Start Game",
        font=("Segoe UI", 12, "bold"),
        bg="#a6e3a1", fg="black", activebackground="#94e2d5",
        command=_on_start
    )
    _widgets["start_btn"].pack(pady=10, ipadx=20)

    # Info label (range, attempts)
    _widgets["info"] = tk.Label(
        _root, text="", font=("Segoe UI", 10),
        fg="#f9e2af", bg="#1e1e2e"
    )
    _widgets["info"].pack(pady=5)

    # Guess entry + button
    guess_frame = tk.Frame(_root, bg="#1e1e2e")
    guess_frame.pack(pady=5)

    _widgets["entry"] = tk.Entry(
        guess_frame, font=("Segoe UI", 14), width=10, justify="center",
        bg="#313244", fg="white", insertbackground="white"
    )
    _widgets["entry"].pack(side="left", padx=5)
    _widgets["entry"].bind("<Return>", lambda e: _on_guess())

    _widgets["guess_btn"] = tk.Button(
        guess_frame, text="Guess!",
        font=("Segoe UI", 11, "bold"),
        bg="#89b4fa", fg="black",
        command=_on_guess, state="disabled"
    )
    _widgets["guess_btn"].pack(side="left", padx=5)

    # Message area
    _widgets["message"] = tk.Label(
        _root, text="", font=("Segoe UI", 11),
        fg="#f9e2af", bg="#1e1e2e", wraplength=460, justify="center"
    )
    _widgets["message"].pack(pady=10)

    # Replay button
    _widgets["replay_btn"] = tk.Button(
        _root, text="🔁 Play Again",
        font=("Segoe UI", 10),
        bg="#f38ba8", fg="black",
        command=_on_replay, state="disabled"
    )
    _widgets["replay_btn"].pack(pady=5, ipadx=15)

    return _root


# ---------- Internal callbacks ----------
def _on_start():
    import game
    diff = _widgets["difficulty_var"].get()
    _widgets["start_btn"].config(state="disabled")
    for child in _root.winfo_children():
        if isinstance(child, tk.Frame):
            for c in child.winfo_children():
                if isinstance(c, tk.Radiobutton):
                    c.config(state="disabled")

    _widgets["entry"].focus()
    game.gui_start_round(diff)


def _on_guess():
    import game
    raw = _widgets["entry"].get()
    _widgets["entry"].delete(0, tk.END)
    game.gui_handle_guess(raw)


def _on_replay():
    _widgets["entry"].delete(0, tk.END)
    _widgets["entry"].focus()
    _widgets["guess_btn"].config(state="normal")
    _widgets["replay_btn"].config(state="disabled")
    _on_start()


# ---------- UI functions (same naam jei game.py use kore) ----------
def print_header():
    pass


def show_high_score(score):
    if score is None:
        text = "🏆 High Score: ekhono kono record nei!"
    else:
        text = f"🏆 Best score: {score} points"
    _widgets["high_score"].config(text=text)


def show_game_start(max_num, attempts):
    _widgets["info"].config(text=f"Range: 1–{max_num}  |  Attempts: {attempts}")
    _widgets["message"].config(text="Guess koro!", fg="#cdd6f4")
    _widgets["guess_btn"].config(state="normal")


def show_attempt_prompt(attempt, max_attempts):
    _widgets["info"].config(text=f"Attempt {attempt}/{max_attempts}")
    return _widgets["entry"].get()


def show_invalid_input():
    _widgets["message"].config(text="⚠️  Number dao (valid range e)!", fg="#f38ba8")


def show_hint(guess, secret, close_range, warm_range):
    difference = abs(guess - secret)
    if difference <= close_range:
        text, color = "🔥 Onek kache! Ar ektu!", "#f38ba8"
    elif difference <= warm_range:
        text, color = "🌡️  Kache kache...", "#f9e2af"
    elif guess < secret:
        text, color = "📈 Choto! Aro boro try koro.", "#89b4fa"
    else:
        text, color = "📉 Boro! Aro choto try koro.", "#89b4fa"
    _widgets["message"].config(text=text, fg=color)


def show_range_hint(low, high):
    _widgets["info"].config(text=f"💡 Range: {low} – {high}")


def show_win(attempts, elapsed_time, points):
    _widgets["message"].config(
        text=f"🎉 YOU WIN!\n⏱️ {elapsed_time:.1f}s  |  🎯 {attempts} attempts  |  💰 +{points} points",
        fg="#a6e3a1"
    )
    messagebox.showinfo("You Win!", f"Attempts: {attempts}\nTime: {elapsed_time:.1f}s\nPoints: {points}")
    _widgets["guess_btn"].config(state="disabled")
    _widgets["replay_btn"].config(state="normal")


def show_lose(secret):
    _widgets["message"].config(text=f"😢 Harle! Number chilo: {secret}", fg="#f38ba8")
    _widgets["guess_btn"].config(state="disabled")
    _widgets["replay_btn"].config(state="normal")


def show_achievements(achievements):
    if not achievements:
        return
    text = "\n".join(achievements)
    _widgets["message"].config(text=f"🏅 Achievements:\n{text}", fg="#f9e2af")


def ask_replay():
    return False


def show_goodbye():
    pass


def show_difficulty_menu(difficulties):
    pass