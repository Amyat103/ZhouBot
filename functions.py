import requests
import json
import asyncpraw

def quote_of_the_day():
    r = requests.get("https://zenquotes.io/api/today")
    python_convert = json.loads(r.text)
    quote = python_convert[0]["q"] + " -" + python_convert[0]["a"]
    return quote

