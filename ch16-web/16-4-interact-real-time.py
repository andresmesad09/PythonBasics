import mechanicalsoup
import time


def main():

    # ----
    # 1) Dice and current time
    # ----
    browser = mechanicalsoup.Browser()
    url = "http://olympus.realpython.org/dice"

    for i in range(4):
        page = browser.get(url)
        result = page.soup.select('#result')[0].text
        result_time = page.soup.select('#time')[0].text

        print(f"The dice result was {result} at {result_time}")

        # Wait 10 seconds for first 3 attempts
        if i < 3:
            time.sleep(5)


if __name__ == '__main__':
    main()
