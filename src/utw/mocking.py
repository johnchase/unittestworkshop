import os

import requests


def greet_user() -> str:
    user = get_current_user()
    return f"Hello, {user}!"


def get_current_user() -> str:
    user = os.environ.get("TEST_USER")
    if user:
        return user
    else:
        raise ValueError("No user found in environment variables.")


class Tracker:
    def __init__(self, logger):
        self.logger = logger

    def track_event(self, user_id: str, event_name: str):
        self.logger.log(f"user={user_id} event={event_name}")


class Emailer:
    def __init__(self):
        self.sender_email = "noreply@example.com"

    def send_email(self, recipient: str, subject: str) -> str:
        return f"From: {self.sender_email} -> To: {recipient} | Subject: {subject}"


class EmailService:
    def __init__(self, sender_email: str, api_key: str):
        self.sender_email = sender_email
        self.api_key = api_key
        self.endpoint = "https://api.email-service.com/send"

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        payload = {
            "from": self.sender_email,
            "to": recipient,
            "subject": subject,
            "body": body,
        }

        headers = {"Authorization": f"Bearer {self.api_key}"}

        response = requests.post(self.endpoint, json=payload, headers=headers)
        return response.status_code == 200
