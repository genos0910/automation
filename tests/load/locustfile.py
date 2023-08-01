from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(2)
    def get_home(self):
        self.client.get("/")

    @task(1)
    def get_search(self):
        self.client.get("/search?q=locust")
