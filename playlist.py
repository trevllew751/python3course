playlist = {"title": "Trevor",
            "author": "Trevor",
            "songs": [
                {"title": "song1", "artist": ["a"], "duration": 2.5},
                {"title": "songseki", "artist": ["a", "b"], "duration": 3.5},
                {"title": "bongseki", "artist": ["blackhoon", "nighoon"], "duration": 4}
            ]
            }
total_playtime = 0
for song in playlist["songs"]:
    total_playtime += song["duration"]
print(total_playtime)

