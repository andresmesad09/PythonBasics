from nis import match
from urllib.request import urlopen
import re


def main():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    # ----
    # 1) Grab full HTML from the web page
    # ----
    html = page.read().decode('UTF-8')
    print(html)

    # ----
    # 2) Use .find() to display Name and Favorite Color
    # ----
    for tag in ["Name: ", "Favorite Color: "]:
        tag_start = html.find(tag) + len(tag)
        tag_end = html[tag_start:].find('<')
        print(html[tag_start: tag_start + tag_end].strip())

    # ----
    # 3) Same exercise as above but with re module
    # ----
    for pattern in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
        match_results = re.search(pattern, html)
        result = match_results.group()
        result = re.sub(".*: ", "", result).strip(' \n<')
        print(result)


if __name__ == '__main__':
    main()
