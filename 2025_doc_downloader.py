'''


Let's look at the logic here:

For every day in 2025:
    We want to check to see if that date has a file on the website.
    If the file is unavailable,
        move on to the next date.
    But if the file is available,
        download the file
        Open the file,
        Extract the contents of the file to a dataframe
        add the date to the 'Date' column
        append it to the larger dataset
        move on to the next date

Save the dataset to an excel file

notes:
- date format is DD/MM/YYYY
- download link is https://opentreasury.gov.ng/images/2025/DAILYPAYMENTREPORTFGN/MONTH/YY-MM-DD.xlsx
- saved file format is YY-MM-DD.xlsx
    '''

import pandas as pd
import requests
from io import BytesIO
from datetime import date, timedelta

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

rows_to_skip = 14

start_date = date(2025, 12, 1)
end_date = date(2025, 12, 31)

delta = end_date - start_date

df_list = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for i in range (delta.days + 1):
    day = start_date + timedelta(days=i)
    file_date = day.strftime("%y-%m-%d")
    month = months[day.month - 1]

    url = f"https://opentreasury.gov.ng/images/2025/DAILYPAYMENTREPORTFGN/{month}/{file_date}.xlsx"


    try:
        response = requests.get(url, headers=headers, timeout=30, verify=False)

        if response.status_code !=200:
            raise ValueError("File not found")

        excel_data = BytesIO(response.content)

        teeny = pd.read_excel(excel_data, skiprows=rows_to_skip)
        teeny['Date'] = day.strftime("%m/%d/%Y")
        df_list.append(teeny)

    except Exception as e:
        print(f"No file found for {file_date}")


df = pd.concat(df_list, ignore_index=True)
df.to_excel('Dec 2025 Payments.xlsx', index=False)
