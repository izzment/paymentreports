import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random

def classify_registration(s:str) -> str:
    prefix = s[:4].upper()

    match prefix:
        case "DATE":
            return "date"
        case "NATU":
            return "nature"
        case "STAT":
            return "status"

driver = webdriver.Chrome()


driver.get("https://icrp.cac.gov.ng/public-search")
time.sleep(5)


df = pd.read_excel('Contractors_UNTAGGED_ONLY.xlsx')
df["Contractors_Cleaned"] = (df["Beneficiary Name"]
                             .str.replace(r"\bLIMITED\b|\bLTD\b|\bMESSRS\b|\bM/S\b", "", case=False, regex=True)
                             .str.replace(r"\([^)]*\)", "", regex=True)
                             .str.replace(".", ""))
df["RC"] = df["RC"].astype("string")

contractor = ""

for row in df.itertuples(index=True):
    contractor = row.Contractors_Cleaned
    idx = row.Index
    print(f"made it to row {idx + 1}")
    if idx % 200 == 0:
        df.to_excel('Contractors.xlsx', index=False)
    try:
        text_area = driver.find_element(By.XPATH, "/html/body/app-root/main/app-public-search/div/div/form/div/input")
        search_btn = driver.find_element(By.XPATH, "/html/body/app-root/main/app-public-search/div/div/form/div/button")
        text_area.send_keys(contractor)
        search_btn.click()
        time.sleep(random.uniform(2, 5))

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/main/app-public-search/div/div[2]/div[2]/span")))

        registration_type = driver.find_element(By.XPATH, "/html/body/app-root/main/app-public-search/div/div[2]/div[2]/span").text
        df.at[idx, "Type of Registration"] = registration_type

        registered_name = driver.find_element(By.XPATH, "/html/body/app-root/main/app-public-search/div/div[2]/div[2]/h3").text
        df.at[idx, "Registered Name"] = registered_name

        registration_number = driver.find_element(By.XPATH, "/html/body/app-root/main/app-public-search/div/div[2]/div[2]/p").text[5::]
        df.at[idx, "RC"] = registration_number


        tester = driver.find_elements(By.CSS_SELECTOR, "span.text-secondary")
        for i in tester:
            if classify_registration(i.text) == "date":
                registration_date = i.text.split("-")[-1].strip()
                df.at[idx, "Date of Registration"] = registration_date

            elif classify_registration(i.text) == "nature":
                purpose = i.text.split("-")[-1].strip()
                df.at[idx, "Nature of Business"] = purpose

            else:
                status = i.text.strip()[9::]
                df.at[idx, "Status"] = status

        print(registration_type)
        print(registered_name)
        print(registration_number)
        print(registration_date)
        print(status)
        print(purpose)

        purpose =  ""


        text_area = driver.find_element(By.XPATH, "/html/body/app-root/main/app-public-search/div/div/form/div/input")
        text_area.send_keys(Keys.CONTROL + "a")
        text_area.send_keys(Keys.DELETE)

    except Exception as e:
        print(f"Error at row {idx + 1}: {e}")
        purpose = ""
        text_area = driver.find_element(By.XPATH, "/html/body/app-root/main/app-public-search/div/div/form/div/input")
        text_area.send_keys(Keys.CONTROL + "a")
        text_area.send_keys(Keys.DELETE)

df.to_excel('Contractors.xlsx', index=False)


driver.quit()

