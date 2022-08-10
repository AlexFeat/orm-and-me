from locust import HttpUser, task, between
from faker import Faker
from json import JSONDecodeError


# RUN locust -f src/tests/load.py

fake = Faker()


class UserBehavior(HttpUser):
    wait_time = between(1, 3)

    @task
    def create(self):
        name: str = str(fake.user_name())
        body: dict = {'name': str(name), 'description': str(fake.email())}
        with self.client.post(f'/v1/stuff/', json=body, catch_response=True) as response:
            if response.status_code == 201:
                self.client.get(f'/v1/stuff/{name}')
                body['description'] = fake.email()
                self.client.patch(f'/v1/stuff/{name}', json=body)
                self.client.delete(f'/v1/stuff/{name}')
            else:
                try:
                    detail: str = response.json()["detail"]
                    response.failure({'d': detail, 'b': body})
                except JSONDecodeError:
                    response.failure("Response could not be decoded as JSON")
                except KeyError:
                    response.failure("Response did not contain expected key 'detail'")
