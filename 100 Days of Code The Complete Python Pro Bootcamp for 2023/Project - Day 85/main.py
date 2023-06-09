import tkinter as tk
import time
 
class TypingSpeedApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed App")
        self.geometry("400x300")
 
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.current_text = tk.StringVar()
        self.start_time = None
        self.total_words = 0
 
        self.create_widgets()
 
    def create_widgets(self):
        self.sample_label = tk.Label(self, text="Sample Text:", font=("Arial", 12))
        self.sample_label.pack(pady=10)
 
        self.sample_text_label = tk.Label(self, text=self.sample_text, wraplength=350)
        self.sample_text_label.pack()
 
        self.typing_label = tk.Label(self, text="Start typing:", font=("Arial", 12))
        self.typing_label.pack(pady=10)
 
        self.entry = tk.Entry(self, font=("Arial", 12), textvariable=self.current_text)
        self.entry.pack()
 
        self.start_button = tk.Button(self, text="Start", command=self.start_typing)
        self.start_button.pack(pady=10)
 
        self.result_label = tk.Label(self, text="", font=("Arial", 12))
        self.result_label.pack()
 
    def start_typing(self):
        self.start_time = time.time()
        self.entry.delete(0, tk.END)
        self.entry.config(state=tk.NORMAL)
        self.entry.focus()
        self.start_button.config(state=tk.DISABLED)
        self.entry.bind("<KeyRelease>", self.check_typing)
 
    def check_typing(self, event):
        typed_text = self.current_text.get()
        if typed_text == self.sample_text:
            elapsed_time = time.time() - self.start_time
            words_per_minute = int((self.total_words / elapsed_time) * 60)
            self.result_label.config(text=f"Words per minute: {words_per_minute}")
            self.entry.unbind("<KeyRelease>")
            self.entry.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)
        else:
            typed_words = typed_text.split()
            self.total_words = len(typed_words)
 
app = TypingSpeedApp()
app.mainloop()