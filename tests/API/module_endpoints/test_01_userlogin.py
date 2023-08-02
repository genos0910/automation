import requests
import uuid
import hashlib
import random
import string

host_url = "https://wt-game-api.fb-games-stage.cc"
api_path = "/api/v1/user-login"
platform_id = "D3DFO"
user_uuid = str(uuid.uuid4())
username="g6"
credit="1000"
transaction_id=''.join(random.choice(string.digits) for _ in range(6))  # 生成6位數字的亂數
secret_key = "C76923E8E4F572C590FAE3C135A40838"  # 平台密鑰
lang = ""  # 語言設定
        
# 使用 hashlib 生成 MD5 值
md5_value = hashlib.md5((username+credit+transaction_id+lang+secret_key).encode()).hexdigest()
payload ={
    "platform-id": platform_id,
    "uuid": user_uuid,
    "username": username,
    "credit": credit,
    "transaction-id": transaction_id,
    "key": secret_key
}

def test_post_request():
    response = requests.post(f'{host_url}+', data = payload)
    assert response.status_code == 200
    json_response = response.json()
    print(json_response)
