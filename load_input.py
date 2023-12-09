import urllib.request
import functools

def get_token():
    with open("SESSION", "r") as f:
        return f.read().strip()

@functools.cache
def load_input(day):
    token = get_token()

    req = urllib.request.Request(f"http://adventofcode.com/2023/day/{day}/input")
    req.add_header("Cookie", f"session={token}")

    res = urllib.request.urlopen(req)

    return res.read().decode("utf-8")

