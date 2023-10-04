from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task(1)
    def actions(self):
        self.client.post("api/users?page=2")

    def update(self):
        self.client.put("/api/users/2")

    def create(self):
        self.client.post("/api/users")

    def delete(self):
        self.client.delete("/api/users/2")

    def register(self):
        self.client.post("/api/register")

    def login(self):
        self.client.post("/api/login")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 0
    max_wait = 0