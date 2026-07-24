import requests
import pandas as pd
import os

# Folder to save CSV files
output_folder = "Data/Raw"

# Create folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# AMFI Scheme Codes
scheme_codes = [
    125497,
    119551,
    120503,
    118632,
    119092,
    120841
]

for code in scheme_codes:
    print(f"\nFetching data for Scheme Code: {code}")

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            # Check if NAV data exists
            if "data" in data:
                df = pd.DataFrame(data["data"])

                file_name = f"{code}_nav.csv"
                file_path = os.path.join(output_folder, file_name)

                df.to_csv(file_path, index=False)

                print(f"Saved: {file_name}")

            else:
                print("No NAV data found.")

        else:
            print("Failed to fetch data.")

    except Exception as e:
        print("Error:", e)

print("\nAll done!")