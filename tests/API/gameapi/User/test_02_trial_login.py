import requests
import uuid
import hashlib
import random
import string
import time
import json

host_url = "https://wt-game-api.fb-games-stage.cc"
api_path = "/api/v1/trial-login"
platform_id = "D3DFO"
user_uuid = str(uuid.uuid4())
username="g6"
transaction_id=''.join(random.choice(string.digits) for _ in range(6))  # 生成6位數字的亂數
secret_key = "C76923E8E4F572C590FAE3C135A40838"  # 平台密鑰
lang = ""  # 語言設定
timestamp = str(int(time.time()))
print("timestamp:",timestamp)

        
# 使用 hashlib 生成 MD5 值
md5_value = hashlib.md5((timestamp+lang+secret_key).encode()).hexdigest()
payload ={
    "key": md5_value,
    "uuid": user_uuid,
    "platform-id": platform_id,
    "timestamp": timestamp,
    "transaction-id": transaction_id,
    "lang":lang
    
    
}

def test_post_request():
    response = requests.post(f'{host_url+api_path}', data = payload)
    assert response.status_code == 200
    json_response = response.json()
    print(json_response)
    assert json_response['error']['msg'] == "Success"  # 驗證是否為成功


