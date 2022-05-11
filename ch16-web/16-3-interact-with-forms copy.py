import mechanicalsoup


def main():

    # ----
    # 1) login
    # ----
    browser = mechanicalsoup.Browser()
    url = "http://olympus.realpython.org/login"
    login_page = browser.get(url)
    login_html = login_page.soup

    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"

    # Submit the form
    profile_pages = browser.submit(form, login_page.url)

    # ----
    # 2) Display the title of the current page
    # ----
    print(profile_pages.url)

    # ----
    # 3)
    # ----
    browser = mechanicalsoup.Browser()
    login_page = browser.get(url)
    print(login_page.soup.title)

    # ----
    # 4)
    # ----
    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "wrong"

    # Submit the form with wrong credentials
    profile_pages = browser.submit(form, login_page.url)

    print(profile_pages.url)


if __name__ == '__main__':
    main()
