from xml.etree import ElementTree as ET
import os
import dotenv
import json
import logging
import itertools
from generate import summaize_text
from concurrent.futures import ProcessPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO)
VERSION = 'v1'

# Load environment variables
dotenv.load_dotenv()
GEMINI_API_KEYs = os.getenv("GEMINI_API_KEY").strip().split(',')
GEMINI_API_KEYs = [key for key in GEMINI_API_KEYs if key]
keys = itertools.cycle(GEMINI_API_KEYs)


def generate_summary(args):
    try:
        data, key = args
        logging.info(key)
        response = summaize_text(data['text'], api_key=key)
        summary = response.text.strip()
        if summary:
            data['summary'] = summary
            with open(f'./useful_with_summary.jsonl', 'a', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False) + '\n')
    except Exception as e:
        logging.error(e)
        with open(f'./useful_without_summary_2.jsonl', 'a', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')

def main():
    with open(f'./useful (1).jsonl', 'r', encoding='utf-8') as f:
        dataset = f.readlines()
    dataset = [json.loads(data) for data in dataset]
    data_key_pairs = zip(dataset, itertools.cycle(GEMINI_API_KEYs))

    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(generate_summary, pair) for pair in data_key_pairs]
        for future in as_completed(futures):
            pass  # Here you could add logging for completed tasks or handle results

if __name__ == '__main__':
    main()
