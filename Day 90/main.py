import tkinter as tk
from tkinter import messagebox
import time

APP_TITLE = "Dangerous Writer"
INACTIVITY_SECONDS = 5


class DangerousWriter:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("800x500")

        self.last_key_time = None
        self.running = False

        top = tk.Frame(root, pady=8)
        top.pack(fill=tk.X)

        self.status_var = tk.StringVar(
            value="Start typing… your fate awaits ⏳")
        self.timer_lbl = tk.Label(
            top, textvariable=self.status_var, font=("Segoe UI", 12, "bold"))
        self.timer_lbl.pack(side=tk.LEFT, padx=10)

        self.reset_btn = tk.Button(
            top, text="Reset", command=self.reset_document)
        self.reset_btn.pack(side=tk.RIGHT, padx=6)

        self.pause = False
        self.pause_btn = tk.Button(
            top, text="Pause", command=self.toggle_pause)
        self.pause_btn.pack(side=tk.RIGHT, padx=6)

        self.text = tk.Text(root, wrap=tk.WORD, font=(
            "Segoe UI", 12), undo=False)
        self.text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        self.text.bind("<KeyRelease>", self.on_key)
        self.text.bind("<Button-1>", self.on_click)

        self.watchdog()

    def on_click(self, _):

        if not self.running and self.text_compare_with_empty() == False:
            self.running = True
            self.last_key_time = time.time()

    def on_key(self, event):

        if event.keysym in ("Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R", "Caps_Lock", "Escape", "Tab"):
            return

        if not self.running:
            self.running = True
        self.last_key_time = time.time()

    def text_compare_with_empty(self):
        content = self.text.get("1.0", tk.END).strip()
        return len(content) == 0

    def toggle_pause(self):
        self.pause = not self.pause
        self.pause_btn.config(text="Resume" if self.pause else "Pause")
        if not self.pause:

            self.last_key_time = time.time()

    def reset_document(self):
        self.text.delete("1.0", tk.END)
        self.flash_bg("#ffdddd")
        self.running = False
        self.last_key_time = None
        self.status_var.set("Reset. Start typing to begin again ⏳")

    def nuke_text(self):

        self.text.delete("1.0", tk.END)
        self.flash_bg("#ffb3b3")
        self.status_var.set(
            "You stopped. All progress lost. Type to try again.")
        self.running = False
        self.last_key_time = None

    def flash_bg(self, color):
        original = self.text.cget("background")
        self.text.config(background=color)
        self.root.after(180, lambda: self.text.config(background=original))

    def watchdog(self):

        try:
            if self.running and not self.pause:
                now = time.time()
                if self.last_key_time is None:
                    self.last_key_time = now
                elapsed = now - self.last_key_time
                remaining = max(0, INACTIVITY_SECONDS - elapsed)

                if self.text_compare_with_empty():
                    self.status_var.set("Start typing… your fate awaits ⏳")
                else:
                    self.status_var.set(
                        f"Keep typing! Deleting in {remaining:0.1f}s if you stop…")

                if elapsed >= INACTIVITY_SECONDS and not self.text_compare_with_empty():
                    self.nuke_text()
            else:

                if self.pause:
                    self.status_var.set("Paused. No deletion while paused.")
                elif self.text_compare_with_empty():
                    self.status_var.set("Start typing… your fate awaits ⏳")
                else:
                    self.status_var.set("Type to continue the challenge.")
        finally:

            self.root.after(100, self.watchdog)


def main():
    root = tk.Tk()
    DangerousWriter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
