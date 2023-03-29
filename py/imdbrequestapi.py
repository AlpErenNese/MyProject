import requests
import tkinter as tk

def search():
    keyword = entry.get()
    url = "http://www.omdbapi.com/?s={}&apikey=23b09716".format(keyword)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get("Search", [])
        listbox.delete(0, tk.END)
        for result in results:
            listbox.insert(tk.END, result["Title"])
    else:
        print("Error:", response.status_code)

root = tk.Tk()
root.title("IMDB Film Arama")
root.geometry("500x400")

label = tk.Label(root, text="Film Adı:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Ara", command=search)
button.pack()

listbox = tk.Listbox(root)
listbox.pack(expand=True, fill=tk.BOTH)

root.mainloop()