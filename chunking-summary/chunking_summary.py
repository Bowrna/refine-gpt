import os
from pypdf import PdfReader
from openai import OpenAI
# creating a pdf reader object 
max_summary_token_len = 200
client = OpenAI(
    api_key= os.environ.get("OPEN_AI_API_KEY"),
)

def extract_text_from_pdf(book_path):
    reader = PdfReader('../books_for_summary/charlie_and_the_chocolate_factory.pdf') 
    start_page = 3
    end_page = len(reader.pages) 
    extracted_text = ""
    for page_num in range(start_page, end_page):
        extracted_text += reader.pages[page_num].extract_text()
    return extracted_text

def summarize_text(text):
    response = client.completions.create(
       model="gpt-3.5-turbo",
        prompt=f"Summarize the following text:\n\n{text}",
        max_tokens=max_summary_token_len,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

extracted_text = extract_text_from_pdf('../books_for_summary/charlie_and_the_chocolate_factory.pdf')
summarize_text(extracted_text)
