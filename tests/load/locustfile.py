from locust import HttpUser, task, between

class UserBehavior1(HttpUser):
    wait_time = between(1, 2.5)
    host = "https://www.google.com"

    @task
    def load_homepage(self):
        self.client.get("/")

class UserBehavior2(HttpUser):
    wait_time = between(1, 2.5)
    host = "https://www.google.com"

    @task
    def perform_search(self):
        self.client.get("/search?q=openai")
