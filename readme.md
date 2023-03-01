# random-spotify-lyrics
Grabs a random song from your recent streams on stats.fm and gets a random lyrics line of it.
Stats.fm is a website that shows your recent streams on spotify, it's not affiliated with spotify in any way.

## Why?
You can integrate this in a flask server and make a website that shows random lyrics from your recent streams, or you can just run it in a cronjob and get a random lyrics line every 5 minutes.

Or you can just run it once and get a random lyrics line.

## How to use
1. Login to [stats.fm](https://stats.fm/) and get your username.
2. Sign up for a free [Musixmatch key](https://developer.musixmatch.com/) and get your key.
3. Put both in `config.json`.

## Requirements
- Python 3.6+
```bash
pip install -r requirements.txt
```

## Example
```
[user@archlinux lyrics]$ python main.py
Fetching lyrics for Hate Me! by MASN
Tell me all that brings you grace
[user@archlinux lyrics]$ python main.py
Fetching lyrics for Sunset by LUCKI
Can't sip Sprite with the Hi-Tech, ayy
```

###### please dont sue me for the use of undocumented stats.fm api