from llama_index.core import SimpleDirectoryReader
from llama_parse import LlamaParse
import nest_asyncio
import os
nest_asyncio.apply()
from dotenv import load_dotenv

load_dotenv()
first_api = os.getenv("LLAMA_CLOUD_API_KEY")

parser = LlamaParse(api_key = first_api
                    ,result_type="markdown", user_prompt="Make sure the structure of all info is preserved",
                    extract_charts=True,auto_mode_trigger_on_table_in_page=True,  auto_mode_trigger_on_image_in_page=True,
)

documents = SimpleDirectoryReader(
    input_dir="./docs", 
    file_extractor={"pdf": parser}
).load_data()
print("docs ingested")
print(documents[0].text[:100])

import pickle

with open("mds", 'wb') as f: #changed to .pkl later
    pickle.dump(documents, f)