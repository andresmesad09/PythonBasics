from email.mime import image
from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    url = "http://olympus.realpython.org/profiles"
    page = urlopen(url)
    html = page.read().decode("UTF-8")
    soup = BeautifulSoup(html, "html.parser")

    # ----
    # 1) Get full HTML text
    # ----
    html_text = soup.get_text()
    print(html_text)
    
    # ----
    # 2) List of all the links
    # ----
    list_links = soup.find_all('a')
    for link in list_links:
        print(f"{link.getText()}: {link['href']}")

    # ----
    # 3) Get the html from each of the pages in the list
    # ----
    url = "http://olympus.realpython.org"
    for link in list_links:
        new_url = f"{url}{link['href']}"
        page = urlopen(new_url)
        html = page.read().decode("UTF-8")
        soup = BeautifulSoup(html, "html.parser")
        html_text = soup.get_text()
        print(html_text)


if __name__ == '__main__':
    main()