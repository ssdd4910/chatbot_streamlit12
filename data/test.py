from dotenv import load_dotenv
import os

load_dotenv()

# 자동으로 읽어서 알아서 api key 넘기도록 도와준다.
print(os.getenv('OPENAI_API_KEY'))

