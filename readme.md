# random-spotify-lyrics  
Grabs a random song from your recent streams on stats.fm and gets a random lyrics line of it

## Why  
You can integrate this in a flask server or wtv and put it on your website

## How to  
1. Login to stats.fm and get your username (you can do it in network tab and refresh page)  
2. Sign up for a free Musixmatch key  
3. Put both in config.json  

## Requirements  
```pip install requests```  

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