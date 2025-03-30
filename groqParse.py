import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

format = {
    'Goods_Name': {
        'allowed_in_cabin': 'boolean',
        'allowed_in_checked_bag': 'boolean',
    },
}


def parse_with_groq(dom_chunks, parse_description):
    parsed_results = {}


    for i, chunk in enumerate(dom_chunks, start=1):
        with open('prompt.txt', 'r') as f:
            prompt = f.read()
            prompt = prompt.format(
                dom_content=chunk,
                parse_description=parse_description,
                format=format,
            )
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                model="llama-3.3-70b-versatile",
                response_format={
                    "type": "json_object",
                },
            )
            print(f"Parsed batch: {i} of {len(dom_chunks)}")
            try:
                parsed_results.update(json.loads(response.choices[0].message.content))
            except json.JSONDecodeError:
                pass

    return parsed_results