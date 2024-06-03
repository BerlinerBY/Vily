from playwright.sync_api import sync_playwright
import json

# playwright install firefox

def translate(file_name: str):
    with sync_playwright() as pw:
        browser = pw.firefox.launch(headless=True)
        page = browser.new_page()

        #go to url
        print("    Go to ulr")
        page.goto("https://translate.google.com/?sl=pl&tl=be&op=docs", timeout=0)

        f_button = "//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[1]/c-wiz/div[1]/c-wiz/div[2]/button"
        s_button = "//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[1]/c-wiz/div[1]/c-wiz/div[5]/button"

        print("    Choose Main Language")
        l_code = "en"
        page.wait_for_selector(f_button)
        page.locator(f_button).click()
        l_button = ""
        for i in range(1, page.locator("xpath=//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[1]/c-wiz/div[2]/c-wiz/div[1]/div/div[3]/div/div[3]/span").count()):
            if page.locator(f"xpath=//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[1]/c-wiz/div[2]/c-wiz/div[1]/div/div[3]/div/div[3]/span[{i}]/div[1]").get_attribute("data-language-code") == l_code:
                l_button = f"xpath=//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[1]/c-wiz/div[2]/c-wiz/div[1]/div/div[3]/div/div[3]/span[{i}]"
        page.locator(l_button).click()

        print("    Choose Belarus")
        b_code = "be"
        page.wait_for_timeout(70)
        page.locator(s_button).click()
        be_button = ""
        for i in range(1, page.locator("xpath=//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/span").count()):
            if page.locator(f"xpath=//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/span[{i}]/div[1]").get_attribute("data-language-code") == b_code:
                be_button = f"xpath=//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/span[{i}]"
        page.locator(be_button).click()

        print("    Upload xlsx file")
        with page.expect_file_chooser() as fc_info:
            page.locator("xpath=//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[2]/c-wiz/div/div[1]/div/div/div[1]/div[2]/div[2]/div/label").click()
        file_chooser = fc_info.value
        file_chooser.set_files(f"../../xlsx_files_temp/{file_name}.xlsx")

        page.locator("xpath=//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[2]/c-wiz/div/div[1]/div/div[2]/div/div/button").click()

        print("    Download xlsx file")
        dowload_button = "xpath=//html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[2]/c-wiz/div/div[1]/div/div[2]/div/button"
        page.wait_for_selector(dowload_button)
        page.wait_for_timeout(50)

        # Start waiting for the download
        with page.expect_download() as download_info:
            # Perform the action that initiates download
            page.locator(dowload_button).click()
        download = download_info.value

        print("    Save file")
        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as("../../xlsx_files/" + download.suggested_filename)

        return True
