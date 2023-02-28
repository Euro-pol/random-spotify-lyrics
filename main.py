import requests, json, random

config = json.load(open("config.json"))

def fetch_streams(username):
    r = requests.get(f"https://beta-api.stats.fm/api/v1/users/{username}/streams/recent").json()
    return r["items"]

def fetch_lyrics(song, artist):
    api_key = config["musixmatch_key"]
    r = requests.get(f"https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_track={song}&q_artist={artist}&apikey={api_key}").json()
    if r["message"]["header"]["status_code"] == 404:
        return "No lyrics found"
    return r["message"]["body"]["lyrics"]["lyrics_body"].strip("\n******* This Lyrics is NOT for Commercial use *******")

def fetch_random_song_lyrics(username):
    songs = fetch_streams(username)
    song = random.choice(songs)
    name = song["track"]["name"]
    artist = song["track"]["artists"][0]["name"]
    print(f"Fetching lyrics for {name} by {artist}")
    lyrics = fetch_lyrics(name, artist)
    return lyrics

def fetch_random_lyrics(username):
    songs = fetch_streams(username)
    song = random.choice(songs)
    name = song["track"]["name"]
    artist = song["track"]["artists"][0]["name"]
    print(f"Fetching lyrics for {name} by {artist}")
    lyrics = fetch_lyrics(name, artist).split("\n")
    return random.choice(lyrics)



def main():
    lyrics = fetch_random_lyrics(config["username"])
    print(lyrics)

if __name__ == "__main__":
    main()