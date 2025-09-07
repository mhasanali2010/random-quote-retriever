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


def main() -> None:
    try:
        base_url = "https://zenquotes.io/api/random"
        response = requests.get(base_url)
        data_retrieved = response.status_code == 200

        json_file = "quotes.json"

        if not save:
            if data_retrieved:
                logging.info(f"Data Retrieved Successfully {response.status_code}")
                data = response.json()
                raw_quote = data[0]["q"]
                author = data[0]["a"]
                quote = f"\"{raw_quote}\"\n-{author}"
                print(quote)

                quote_dict = {"author": author, "quote": raw_quote}
                with open("last_quote.json", "w") as f:
                    json.dump(quote_dict, f, indent=4)
            else:
                logging.error(f"Data Not Retrieved {response.status_code}")
                print("Data Not Retrieved")
        if save:
            if os.path.exists("last_quote.json") and os.path.getsize("last_quote.json") > 0:
                with open("last_quote.json", "r") as f:
                    file = json.load(f)
                if os.path.exists(json_file) and os.path.getsize(json_file) > 0:
                    with open(json_file, "r") as f:
                        data = json.load(f)
                else:
                    data = []
                data.append(file)
                with open(json_file, "w") as f:
                    json.dump(data, f, indent=4)

                logging.info("Quote saved successfully")
                print("Quote Saved")
            else:
                logging.error("Error while saving: last quote was not found")
                print("Could not save quote as no quote was found.")
    except Exception as e:
        logging.error(f"Error Occured: {e}")
        print("An error occured while retrieving, please try again later.")


if __name__ == "__main__":
    main()
