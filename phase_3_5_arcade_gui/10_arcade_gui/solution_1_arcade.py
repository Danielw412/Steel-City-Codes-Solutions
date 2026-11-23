"""Arcade GUI solution: a tkinter window that launches the class projects.

The arcade has three kinds of pages:
- a welcome page
- a menu page with one button per project
- a project page with instructions, the creator's name, and a Launch button

Launch runs the project's Python file in the terminal the arcade was started
from. The arcade window hides while you play and comes back when you finish.
"""

import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from arcade_projects import projects


# This file is in phase_3_5_arcade_gui/10_arcade_gui, so the top folder of the
# repository is two folders above this one.
REPO_FOLDER = Path(__file__).resolve().parent.parent.parent

TITLE_FONT = ("Arial", 24, "bold")
TEXT_FONT = ("Arial", 13)
BUTTON_FONT = ("Arial", 13)


class ArcadeApp:
    """The arcade window and its pages."""

    def __init__(self, root):
        self.root = root
        self.root.title("Steel City Codes Arcade")
        self.root.geometry("520x620")

        # Every page is drawn inside this frame. Changing pages clears it.
        self.page = tk.Frame(self.root, padx=20, pady=20)
        self.page.pack(fill="both", expand=True)

        self.show_welcome_page()

    def clear_page(self):
        """Remove everything from the current page."""
        for widget in self.page.winfo_children():
            widget.destroy()

    def show_welcome_page(self):
        """Show the first page the player sees."""
        self.clear_page()

        tk.Label(self.page, text="Welcome to the Arcade!", font=TITLE_FONT).pack(pady=20)
        tk.Label(
            self.page,
            text="Every game here was built by our class.\nPick one and press Launch to play.",
            font=TEXT_FONT,
        ).pack(pady=10)
        tk.Button(
            self.page,
            text="See the projects",
            font=BUTTON_FONT,
            command=self.show_menu_page,
        ).pack(pady=20)
        tk.Button(self.page, text="Quit", font=BUTTON_FONT, command=self.root.destroy).pack()

    def show_menu_page(self):
        """Show one button for every project in the list."""
        self.clear_page()

        tk.Label(self.page, text="Projects", font=TITLE_FONT).pack(pady=10)

        for project in projects:
            tk.Button(
                self.page,
                text=project["name"],
                font=BUTTON_FONT,
                width=24,
                command=lambda project=project: self.show_project_page(project),
            ).pack(pady=3)

        tk.Button(
            self.page,
            text="Back to welcome page",
            font=BUTTON_FONT,
            command=self.show_welcome_page,
        ).pack(pady=15)

    def show_project_page(self, project):
        """Show one project's instructions, creator, and Launch button."""
        self.clear_page()

        tk.Label(self.page, text=project["name"], font=TITLE_FONT).pack(pady=10)
        tk.Label(self.page, text="Made by " + project["creator"], font=TEXT_FONT).pack()
        tk.Label(
            self.page,
            text=project["instructions"],
            font=TEXT_FONT,
            wraplength=460,
            justify="left",
        ).pack(pady=20)
        tk.Button(
            self.page,
            text="Launch",
            font=BUTTON_FONT,
            width=12,
            command=lambda: self.launch(project),
        ).pack(pady=5)
        tk.Button(
            self.page,
            text="Back to projects",
            font=BUTTON_FONT,
            command=self.show_menu_page,
        ).pack(pady=5)

    def launch(self, project):
        """Run the project's Python file and wait until it finishes."""
        script = REPO_FOLDER / project["script"]

        if not script.exists():
            messagebox.showerror("Project not found", "Could not find:\n" + str(script))
            return

        print()
        print("Starting", project["name"] + ". Play in this terminal window.")

        # Hide the arcade while the game runs, then bring it back.
        self.root.withdraw()
        self.root.update()

        # sys.executable is the same Python that is running the arcade.
        # cwd makes the game run from its own folder.
        subprocess.run([sys.executable, str(script)], cwd=str(script.parent))

        print("Finished", project["name"] + ". Back to the arcade window.")
        self.root.deiconify()


def main():
    root = tk.Tk()
    ArcadeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
