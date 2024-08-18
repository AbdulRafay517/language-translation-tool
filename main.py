import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Define the translation function
def translate_text_deep():
    source_text = text_input.get("1.0", tk.END).strip()
    src_lang = source_lang_var.get()
    dest_lang = target_lang_var.get()

    if not source_text:
        messagebox.showinfo("Input Error", "Please enter some text to translate.")
        return

    try:
        translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(source_text)
        result_var.set(translated_text)
    except Exception as e:
        result_var.set(f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x650")
root.configure(bg='#2b2b2b')  # Set background color to dark

# Custom style for dark mode
style = ttk.Style(root)
style.theme_use("clam")

# Customize the ttk widgets for dark mode
style.configure("TLabel", background="#2b2b2b", foreground="#ffffff", font=("Helvetica", 12))
style.configure("TButton", background="#444444", foreground="#ffffff", font=("Helvetica", 12, "bold"))
style.map("TButton", background=[("active", "#555555")])
style.configure("TCombobox", fieldbackground="#3c3c3c", background="#3c3c3c", foreground="#ffffff")
style.map("TCombobox", fieldbackground=[("readonly", "#3c3c3c")])

# Title Label
title_label = ttk.Label(root, text="Language Translator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Source Language Dropdown
source_lang_var = tk.StringVar(value="auto")
source_lang_label = ttk.Label(root, text="Source Language:")
source_lang_label.pack(pady=5)
source_lang_dropdown = ttk.Combobox(root, textvariable=source_lang_var, state="readonly")
source_lang_dropdown['values'] = ["auto", "en", "fr", "es", "de", "it", "ja", "zh-cn", "ru"]  # Add more languages as needed
source_lang_dropdown.pack(pady=5)

# Text Input
text_input = tk.Text(root, height=8, width=50, bg="#3c3c3c", fg="#ffffff", insertbackground="#ffffff", bd=0, padx=10, pady=10)
text_input.pack(pady=10)

# Target Language Dropdown
target_lang_var = tk.StringVar(value="en")
target_lang_label = ttk.Label(root, text="Target Language:")
target_lang_label.pack(pady=5)
target_lang_dropdown = ttk.Combobox(root, textvariable=target_lang_var, state="readonly")
target_lang_dropdown['values'] = ["en", "fr", "es", "de", "it", "ja", "zh-cn", "ru"]  # Add more languages as needed
target_lang_dropdown.pack(pady=5)

# Translate Button
translate_button = ttk.Button(root, text="Translate", command=translate_text_deep)
translate_button.pack(pady=10)

# Translation Result Label
result_label = ttk.Label(root, text="Translated Text:")
result_label.pack(pady=5)
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, state="readonly", width=60, font=("Helvetica", 12), bg="#3c3c3c", fg="#ffffff", bd=0)
result_entry.pack(pady=5)

# Run the application
root.mainloop()