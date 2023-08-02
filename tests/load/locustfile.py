from locust import HttpUser, task
import uuid
import hashlib
import random
import string

class ApiUser(HttpUser):
    host = "https://wt-game-api.fb-games-stage.cc"

    @task
    def post_user_login(self):
        # 根據需要生成動態參數
        platform_id = "D3DFO"
        user_uuid = str(uuid.uuid4())
        username = "g6"
        credit = "1000"
        transaction_id = ''.join(random.choice(string.digits) for _ in range(6))  # 生成6位數字的亂數
        secret_key = "C76923E8E4F572C590FAE3C135A40838"  # 平台密鑰
        lang = ""  # 語言設定
        
        # 使用 hashlib 生成 MD5 值
        md5_value = hashlib.md5((username+credit+transaction_id+lang+secret_key).encode()).hexdigest()

        # 構建 JSON 載荷
        payload = {
            "platform-id": platform_id,
            "uuid": user_uuid,
            "username": username,
            "credit": credit,
            "transaction-id": transaction_id,
            "key": md5_value
        }

        # 發送 POST 請求
        self.client.post("/api/v1/user-login", json=payload)

    """ @task
    def post_trial_login(self):
        # 根据需要生成动态参数
        # 这些参数需要根据你的 API 的具体要求来设置
        # 下面是一些示例
        platform_id = "your-platform-id"
        trial_key = "your-trial-key"

        # 构建 JSON 载荷
        payload = {
            "platform-id": platform_id,
            "trial-key": trial_key
        }

        # POST 请求
        self.client.post("/api/v1/trial-login", json=payload) """
