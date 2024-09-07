import tkinter as tk
from tkinter import messagebox
import requests


CLIENT_ID = "qQzl6KdnVTmJ0hD_VcJzVmY1GdlRqLB8Rm2WpKOrFgm8Y-bgmXIM3fqr1ZmHdLzz"
CLIENT_SECRET = "7apjCgqB8tBSY4y_maTvV8JR-0SZ8ZnI2W8Wc_9dUlrVIxH2N3Go4Q9gQsrw1kkQaq1AJUHU1cN1p9MTRhmDug"


def get_access_token():
    auth_url = "https://api.genius.com/oauth/token"
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': qQzl6KdnVTmJ0hD_VcJzVmY1GdlRqLB8Rm2WpKOrFgm8Y-bgmXIM3fqr1ZmHdLzz,
        'client_secret': "7apjCgqB8tBSY4y_maTvV8JR-0SZ8ZnI2W8Wc_9dUlrVIxH2N3Go4Q9gQsrw1kkQaq1AJUHU1cN1p9MTRhmDug"
    }
    response = requests.post(auth_url, data=auth_data)
    response_data = response.json()
    return response_data.get("access_tokeQtjelEzQ8T13VI8TtlML5Iv-1dwKYmKEDGL29NbZ04RXbrIh-3eEP_3OEnzB3gZm")


def get_lyrics():
    song_title = title_entry.get()
    artist_name = artist_entry.get()
    access_token = get_access_token()

    if song_title and artist_name:
        try:
            headers = {'Authorization': f'Bearer {access_token}'}
            search_url = f"https://api.genius.com/search?q={song_title} {artist_name}"
            search_response = requests.get(search_url, headers=headers)
            search_data = search_response.json()

            # Extract song path from search results
            song_path = search_data['response']['hits'][0]['result']['path']
            song_url = f"https://genius.com{song_path}"

            # Fetch lyrics page
            lyrics_page = requests.get(song_url)
            # Extract lyrics from the page (this is a simplified example)
            start = lyrics_page.text.find('<div class="lyrics">')
            end = lyrics_page.text.find('</div>', start)
            lyrics_html = lyrics_page.text[start:end]
            lyrics = lyrics_html.replace('<br/>', '\n').replace('<p>', '').replace('</p>', '')

            # Display lyrics in the text area
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, lyrics)

        except Exception as e:
            messagebox.showinfo("Error", f"Failed to fetch lyrics: {str(e)}")
    else:
        messagebox.showwarning("Input Error", "Please enter both song title and artist name.")

# Create GUI window
window = tk.Tk()
window.title("Lyrics Extractor")

# Song Title Label and Entry
title_label = tk.Label(window, text="Song Title:")
title_label.grid(row=0, column=0, padx=10, pady=10)
title_entry = tk.Entry(window, width=30)
title_entry.grid(row=0, column=1, padx=10, pady=10)

# Artist Name Label and Entry
artist_label = tk.Label(window, text="Artist Name:")
artist_label.grid(row=1, column=0, padx=10, pady=10)
artist_entry = tk.Entry(window, width=30)
artist_entry.grid(row=1, column=1, padx=10, pady=10)

# Fetch Lyrics Button
fetch_button = tk.Button(window, text="Fetch Lyrics", command=get_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Lyrics Display Text Area
lyrics_text = tk.Text(window, height=20, width=60)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI loop
window.mainloop()
