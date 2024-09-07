import tkinter as tk
from tkinter import scrolledtext


def create_gui():
    window = tk.Tk()
    window.title("Chatbot")

    
    conversation = scrolledtext.ScrolledText(window, state='disabled', wrap='word', height=20, width=60)
    conversation.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    
   
    user_input = tk.Entry(window, width=60)
    user_input.grid(row=1, column=0, padx=10, pady=10)
    
   
    def send_message():
        user_message = user_input.get()
        if user_message:
            conversation.config(state='normal')
            conversation.insert(tk.END, f"You: {user_message}\n")
            response = get_response(user_message)
            conversation.insert(tk.END, f"Bot: {response}\n")
            conversation.config(state='disabled')
            user_input.delete(0, tk.END)
            conversation.yview(tk.END)
    
    # send button
    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.grid(row=1, column=1, padx=10, pady=10)
    
    # Start the GUI loop
    window.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
