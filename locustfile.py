from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def index(self):
        self.client.get("/")

    @task(2)
    def compute(self):
        self.client.get("/api/compute")

    @task(1)
    def health(self):
        self.client.get("/health")