import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from exa_py import Exa

def search():
    query = search_entry.get()
    response = exa.search(
        query=query,
        num_results=10,
        type='keyword',
        include_domains=['twitter.com'],
    )
    results_text.delete(1.0, tk.END)
    if response.results:
        for result in response.results:
            results_text.insert(tk.END, f'Title: {result.title}\n')
            results_text.insert(tk.END, f'URL: {result.url}\n\n')
    else:
        results_text.insert(tk.END, "No results found.")

# Initialize the Exa API
exa = Exa('71f70d74-0393-403d-aa22-156486ac6354')

# Create the main window
root = tk.Tk()
root.title("Social Search")


# Create a label for the search entry

search_label = tk.Label(root, text="Search here:",)
search_label.pack()


# Create a text entry widget for the search query
search_entry = tk.Entry(root, width=50)
search_entry.pack()

# Create a search button
search_button = tk.Button(root, text="Search",  command=search)
search_button.pack()

# Create a scrolled text widget to display the results
results_text = scrolledtext.ScrolledText(root, width=50, height=20)
results_text.pack()


# Start the Tkinter event loop
root.mainloop()
