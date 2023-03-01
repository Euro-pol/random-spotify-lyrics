import json
import random
import typing
import requests

# Load config
config = json.load(open(file="config.json", mode="r", encoding="utf-8"))


def fetch_streams(username: str) -> typing.List[typing.Dict[str, typing.Any]]:
    """Fetches the last 50 songs played by the user.
    Args:
        `username` (str): The username of the user on stats.fm.
    Returns:
        `typing.List[typing.Dict[str, typing.Any]]`: A list of dictionaries containing the songs.
    """
    res = requests.get(
        f"https://beta-api.stats.fm/api/v1/users/{username}/streams/recent", timeout=10
    ).json()
    return res["items"]


def fetch_lyrics(song: str, artist: str) -> str:
    """Fetches lyrics from musixmatch.
    Args:
        `song` (str): The name of the song.
        `artist` (str): The name of the artist.
    Returns:
        str: The lyrics of the song.
    """
    api_key = config["musixmatch_key"]
    res = requests.get(
        f"https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_track={song}&q_artist={artist}&apikey={api_key}",
        timeout=10,
    ).json()
    if res["message"]["header"]["status_code"] == 404:
        return "No lyrics found"
    return res["message"]["body"]["lyrics"]["lyrics_body"].strip(
        "\n******* This Lyrics is NOT for Commercial use *******"
    )


def fetch_random_song_lyrics(username: str) -> str:
    """Fetches random lyrics from the last 50 songs played by the user.
    This is different from `fetch_random_lyrics()` in that it fetches the
    lyrics of a random song, instead of a random line from a random song.
    Args:
        `username` (str): The username of the user on stats.fm.
    Returns:
        `str`: The lyrics of a random song.
    """
    songs = fetch_streams(username)
    song = random.choice(songs)
    name = song["track"]["name"]
    artist = song["track"]["artists"][0]["name"]
    print(f"Fetching lyrics for {name} by {artist}")
    return fetch_lyrics(name, artist)


def fetch_random_lyrics(username: str) -> str:
    """Fetches random lyrics from the last 50 songs played by the user.
    This is different from `fetch_random_song_lyrics()` in that it fetches
    a random line from a random song, instead of the lyrics of a random song.
    Args:
        `username` (str): The username of the user on stats.fm.
    Returns:
        `str`: The lyrics of a random song.
    """
    songs = fetch_streams(username)
    song = random.choice(songs)
    name = song["track"]["name"]
    artist = song["track"]["artists"][0]["name"]
    print(f"Fetching lyrics for {name} by {artist}")
    lyrics = fetch_lyrics(name, artist).split("\n")
    return random.choice(lyrics)


def main() -> None:
    """
    Main function.
    Examples you can try:
        >>> songs = fetch_streams(config["username"])
        >>> print(songs)
        >>> randSongLyrics = fetch_random_song_lyrics(config["username"])
        >>> print(randSongLyrics)
        >>> randLyrics = fetch_random_lyrics(config["username"])
        >>> print(randLyrics)
        `[{'endTime': '2023-02-28T23:15:26.829Z', 'track': {'name': 'Beatbox - Remix', 'explicit': True, 'durationMs': 109740, 'spotifyPopularity': 13, 'albums': [{'id': 2331872, 'image': 'https://i.scdn.co/image/ab67616d0000b27397d9bf2ea7af680486eca463', 'name': 'Beatbox (Remix)'}], 'artists': [{'id': 2102939, 'name': 'Gangsta Goofy'}], 'id': 14354078, 'externalIds': {'spotify': ['0MRAf09t8SuHltL01gXhAT']}}} ...`\n
        `Fetching lyrics for Type monëy by Yeat`\n
        `.556, big bullets to the head (woo, woo)`\n
        `...`\n
        `Fetching lyrics for No morë talk by Yeat`\n
        `Ain't adding up, yeah (yeah-ah)`\n
    """
    lyrics = fetch_random_lyrics(config["username"])
    print(lyrics)


# Driver code
if __name__ == "__main__":
    main()
