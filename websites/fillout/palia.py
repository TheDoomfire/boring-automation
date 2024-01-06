from playwright.sync_api import sync_playwright
from mailtm import Email # temp mail
import time

#url = "https://accounts.palia.com/sign-up?referral=b27a6dd4-792f-4b3d-a562-7b77e4832d1b" # Albin
#url = "https://accounts.palia.com/sign-up?referral=693562f2-1a38-424b-82dc-cf27fe5d4c9b" # Emma
#url = "https://accounts.palia.com/sign-up?referral=e77ab715-345d-44a8-8f12-8d88242b15ce" # Bunny
#url = "https://accounts.palia.com/sign-up?referral=d2bf373f-f4e1-428b-aeb2-8c789f21fc49" # Pays
#url = "https://accounts.palia.com/sign-up?referral=abc65ea1-52f8-41b2-9e78-7779265ff1bf" # bunnies friend
url = "https://accounts.palia.com/sign-up?referral=5a57d16c-890c-492e-9e23-1f92a7e5b2cd" # Kaioni
#email = "email@email.com"
#username = "username"
#password = "password"

# Refer a Friend (RaF) Palia


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright, email, username, password) -> None:
    browser = playwright.chromium.launch(headless=False) # True if u wanna see everything
    context = browser.new_context()
    page = context.new_page()

    page.goto(url)
    page.get_by_placeholder("einar@palia.com").click()
    page.get_by_placeholder("einar@palia.com").fill(email)

    page.get_by_placeholder("EinarLovesPebbles11").click()
    page.get_by_placeholder("EinarLovesPebbles11").fill(username)

    page.get_by_placeholder("New Password").click()
    page.get_by_placeholder("New Password").fill(password)

    page.get_by_placeholder("Confirm Password").click()
    page.get_by_placeholder("Confirm Password").fill(password)

    page.get_by_placeholder("Month").click()
    page.get_by_role("option", name="January").click()
    page.get_by_placeholder("Day").click()
    page.get_by_role("option", name="1", exact=True).click()
    page.get_by_placeholder("Year").click()
    page.get_by_role("option", name="1990").click()
    page.locator("#vs1__combobox div").first.click()
    page.get_by_placeholder("Country / Region").fill("swe")
    page.get_by_role("option", name="Sweden").click()

    page.get_by_label("Check this box to get email").check()
    page.get_by_label("I agree to the Terms of").check()

    page.get_by_role("button", name="Submit").click()

    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])


def temp_mail():
    test = Email()
    # Make new email address
    test.register()
    email = str(test.address)

    # test.start(listener)
    # test.stop
    return email


with sync_playwright() as playwright:
    for i in range(5):
        email = temp_mail()
        username = "jkasdhj432" + str(i)
        password = '6n*"37Hnt3+q'
        print(email)
        run(playwright, email, username, password)