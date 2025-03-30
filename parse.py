from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import ast

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return null."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
    "5. **Format**: The extracted information should be in the given format: {format}."
    "6. **No Notes:** Do not include any notes or comments in your response."
)

model = OllamaLLM(model="llama3.1")

format = {
    'Goods_Name': {
        'allowed_in_cabin': 'boolean',
        'allowed_in_checked_bag': 'boolean',
    },
}


def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = {}

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description, "format": format }
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        try:
            parsed_results.update(ast.literal_eval(response))
        except:
            pass

    return parsed_results
