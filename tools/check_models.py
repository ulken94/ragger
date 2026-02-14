# check_models.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ API Key가 없습니다. .env 파일을 확인하세요.")
    exit()

genai.configure(api_key=api_key)

print("🔍 사용 가능한 임베딩 모델 목록:")
found = False
for m in genai.list_models():
    if 'embedContent' in m.supported_generation_methods:
        print(f"- {m.name}")
        found = True

if not found:
    print("❌ 사용 가능한 임베딩 모델이 없습니다. API Key 권한을 확인하세요.")
