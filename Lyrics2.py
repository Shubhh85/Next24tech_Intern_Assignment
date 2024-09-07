import lyricsgenius
api_key ="qQzl6KdnVTmJ0hD_VcJzVmY1GdlRqLB8Rm2WpKOrFgm8Y-bgmXIM3fqr1ZmHdLzz"
genius = lyricsgenius.Genius(api_key)
name = input("Enter Artist name")
artist = genius.search_artist(name)
song = input("Type your song for lyrics")
song = artist.song(song)
print(song.lyrics)