from locust import HttpUser, task, between


class BackendUser(HttpUser):
    wait_time = between(2, 10)
    
    @task # tags=["root"] # Problem with tags
    def load_root_page(self):
        self.client.get("/")
    
    @task # tags=["random"] # Problem with tags
    def load_random_page(self):
        self.client.get("/random")
        
    @task # tags=["db"] # Problem with tags
    def load_db_page(self):
        self.client.post(
            "/db",
            json={
                "title": "yep"
            }
        )
