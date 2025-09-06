import requests
import logging
import argparse
import json
import os

parser = argparse.ArgumentParser(description='finds a random quote')
parser.add_argument("--save", action="store_true", help="save the quote to file")
args = parser.parse_args()

save = args.save

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="logs.log",
    filemode="a"
)

base_url = "https://zenquotes.io/api/random"
response = requests.get(base_url)
data_retrieved = response.status_code == 200

json_file = "quotes.json"

if data_retrieved:
    logging.info(f"Data Retrieved Successfully {response.status_code}")
    data = response.json()
    quote = data[0]["q"]
    author = data[0]["a"]
    quote = f"\"{quote}\"\n-{author}"
    print(quote)

    if save:
        quote_dict = {"author": author, "quote": quote}

        if os.path.exists(json_file) and os.path.getsize(json_file) > 0:
            with open(json_file, "r") as f:
                quotes = json.load(f)
        else:
            quotes = []

        quotes.append(quote_dict)

        with open(json_file, "w") as f:
            json.dump(quotes, f, indent=4)

        logging.info("Saved Quote Successfully")
else:
    logging.error(f"Data Not Retrieved {response.status_code}")
    print("Data Not Retrieved")
