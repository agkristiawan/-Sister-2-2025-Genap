from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 5)  # Random wait time between 1 and 5 seconds

    @task(1)
    def get_10kb(self):
        self.client.get("/html/10kb")

    @task(1)
    def get_100kb(self):
        self.client.get("/html/100kb")

    @task(1)
    def get_1mb(self):
        self.client.get("/html/1mb")

    @task(1)
    def get_5mb(self):
        self.client.get("/html/5mb")

    @task(1)
    def get_10mb(self):
        self.client.get("/html/10mb")