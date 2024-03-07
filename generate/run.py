import itertools
import json
import dotenv
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from generate_gemini import process_word_to_text
dotenv.load_dotenv()
# google_api_key = os.getenv("GOOGLE_API_KEY")

def gen_qa_word_2_text(args):
    text_item , key = args
    result = process_word_to_text(text_item, key=key)
    with open("./generate/result_word2text.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False) + "\n")

gemini_api_key = os.getenv("GEMINI_API_KEY").split(",")

with open("./generate/Use.jsonl", "r", encoding="utf-8") as f:
    dataset = f.readlines()

dataset = [json.loads(data) for data in dataset]
data_key_pairs = zip(dataset, itertools.cycle(gemini_api_key))

with ProcessPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(gen_qa_word_2_text, pair) for pair in data_key_pairs]
    for future in as_completed(futures):
        pass  # Here you could add logging for completed tasks or handle results