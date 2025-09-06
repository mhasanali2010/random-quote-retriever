import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="logs.log",
    filemode="a"
)

base_url = "https://zenquotes.io/api/random"
response = requests.get(base_url)
data_retrieved = response.status_code == 200

if data_retrieved:
    logging.info(f"Data Retrieved Successfully {response.status_code}")
    data = response.json()
    quote = data[0]["q"]
    author = data[0]["a"]
    print(f"\"{quote}\"\n-{author}")

else:
    logging.error(f"Data Not Retrieved {response.status_code}")
    print("Data Not Retrieved")
