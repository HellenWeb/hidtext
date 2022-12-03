"""
  name: hidtext
  date: 3.12.22
  creator: HellenWeb
  github: https://github.com/HellenWeb/hidtext

"""

# Modules

import os
import sys

try:
    import requests
    import argparse
except ModuleNotFoundError:
    os.system("pip install -r requirements.txt")

# Logic

def main(url):
    req = requests.get(url).text
    with open("hidtext/site.txt", "w") as f:
        f.write(req)
        f.write("<style>a,p,bid,h1,h2,h3,h4,h5,span,li,strong{color:whitesmoke;background-color:whitesmoke;border-radius:10px;padding:0}</style>")
    with open("hidtext/site.txt", "r+") as f:
        l = f.readlines()
        for line in l:
            if "color" in line:
                line.replace("color", "")
    os.system("python3 manage.py runserver")

# Polling

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Your site for app", type=str, dest="url")
    args = parser.parse_args()
    main(args.url)
