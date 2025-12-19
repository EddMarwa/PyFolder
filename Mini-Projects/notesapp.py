import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

"""
notesapp.py
-----------
Simple Tkinter notes application (tabs per note).

Data contract:
 - notes.json is a JSON object mapping title -> content
 - Titles must be unique (used as dictionary keys)

Functions:
 - add_note_tab(title, content): create a read-only tab showing content
 - add_note(): open a 'New Note' tab for entering a title & content and saving
 - delete_note(): delete currently selected note (asks for confirmation)
 - load_notes(): read notes.json and create tabs for each saved note

Edge cases handled:
 - Missing/malformed notes.json -> starts with empty notes
 - Prevent saving notes without title or content (shows warning)
 - Deleting unsaved 'New Note' simply removes its tab

This file adds comments to help a learner understand each section.
"""

# Path to notes.json stored next to this script
ROOT_DIR = os.path.dirname(__file__)
NOTES_FILE = os.path.join(ROOT_DIR, "notes.json")

# Create the main application window
root = tk.Tk()
root.title("Notes App")
root.geometry("600x400")

# The Notebook widget (tabbed interface) will hold one tab per note
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# In-memory dictionary of notes. Keys are titles,
#  values are note contents.
notes = {}


def add_note_tab(title=None, content=""):
    """Create and add a read-only tab to the notebook.

    Parameters:
    - title: string displayed on the tab (if None -> 'Untitled')
    - content: text to show inside the tab

    Returns the (frame, text_widget) for reference if needed.
    """
    # Each tab is a Frame containing a Text widget
    frame = ttk.Frame(notebook, padding=10)
    text = tk.Text(frame, wrap=tk.WORD)

    # Insert content at the start of the text widget
    text.insert("1.0", content)

    # We keep the text widget editable for simplicity; if you want it
    # read-only, set state=tk.DISABLED after insertion.
    text.config(state=tk.NORMAL)
    text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Add the frame as a new tab. If title is falsy, label it 'Untitled'
    notebook.add(frame, text=title or "Untitled")
    return frame, text


def add_note():
    """Open a 'New Note' tab with fields for title and content and a Save button.

    Workflow:
    - User enters title and content.
    - On Save: validate inputs, update the in-memory dict, persist to notes.json,
      remove the 'New Note' tab and replace it with a proper note tab (title).
    """
    frame = ttk.Frame(notebook, padding=10)

    # Title label + entry (single line)
    title_label = ttk.Label(frame, text="Title:")
    title_label.grid(row=0, column=0, sticky=tk.W, pady=4)
    title_entry = ttk.Entry(frame, width=40)
    title_entry.grid(row=0, column=1, sticky=tk.W, pady=4)

    # Content label + multi-line Text widget
    content_label = ttk.Label(frame, text="Content:")
    content_label.grid(row=1, column=0, sticky=tk.NW, pady=4)
    content_text = tk.Text(frame, wrap=tk.WORD, width=50, height=15)
    content_text.grid(row=1, column=1, pady=4, sticky=tk.W)

    def save_note():
        """Validate inputs and save the note to disk and UI.

        Important details:
        - Title cannot be empty (used as key in notes dict)
        - Content cannot be empty
        - If a note with the same title exists, it will be overwritten.
        """
        title = title_entry.get().strip()
        content = content_text.get("1.0", tk.END).rstrip()

        # Basic validation with user feedback
        if not title:
            messagebox.showwarning("Missing Title", "Please enter a title for the note.")
            return
        if not content:
            messagebox.showwarning("Missing Content", "Please enter some content for the note.")
            return

        # Update in-memory notes dictionary
        notes[title] = content

        # Persist the notes dictionary to disk (overwrites the file)
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=2)

        # Replace the 'New Note' tab with a regular note tab showing the content
        try:
            idx = notebook.index(frame)
            notebook.forget(idx)
        except Exception:
            # If we can't find the frame index, just ignore and continue
            pass

        # Add the saved note as a normal tab
        add_note_tab(title, content)

    # Save button placed below the input fields
    save_btn = ttk.Button(frame, text="Save Note", command=save_note)
    save_btn.grid(row=2, column=1, sticky=tk.E, pady=8)

    # Add the frame to the notebook and select it so the user sees it immediately
    notebook.add(frame, text="New Note")
    notebook.select(frame)

def delete_note():
    """Delete the currently selected note tab.
    - If the selected tab is the unsaved 'New Note' tab, it is simply removed.
    - Otherwise the user is asked to confirm; if confirmed the note is removed
      from the in-memory dict, saved to disk, and the tab is removed from UI.
    """
    sel = notebook.select()
    if not sel:
        # Nothing selected
        return
    idx = notebook.index(sel)

    # Tab label (title) is stored in the 'text' option of the tab
    title = notebook.tab(idx, "text")

    # Unsaved new note tabs are labeled 'New Note' and shouldn't prompt.
    if title == "New Note":
        notebook.forget(idx)
        return

    # Ask the user to confirm deletion
    confirm = messagebox.askyesno("Delete Note", f"Are you sure you want to delete '{title}'?")
    if confirm:
        # Remove from in-memory dict and persist updated dict
        notes.pop(title, None)
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=2)
        # Remove the tab from the UI
        notebook.forget(idx)


def load_notes():
    """Load notes from NOTES_FILE and create tabs for each saved note.

    If the file does not exist, the application starts with an empty notes dict.
    If the file is malformed, we silently fallback to an empty dict.
    """
    global notes
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, "r", encoding="utf-8") as f:
                notes = json.load(f)
        except Exception:
            # If reading/parsing fails, proceed with an empty notes dict
            notes = {}

    # Create a tab for every saved note.
    for title, content in notes.items():
        add_note_tab(title, content)


# --- UI: toolbar with New and Deletion buttons ---
toolbar = ttk.Frame(root)
toolbar.pack(fill=tk.X, padx=10)
new_btn = ttk.Button(toolbar, text="New Note", command=add_note)
new_btn.pack(side=tk.LEFT, padx=5)
del_btn = ttk.Button(toolbar, text="Delete Note", command=delete_note)
del_btn.pack(side=tk.LEFT, padx=5)

# ----- Appplication Startup ----


# Load notes from disk and start the Tk event loop

# fct check 

load_notes()
root.mainloop()