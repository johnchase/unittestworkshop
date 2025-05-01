from unittest import mock

from utw.mocking import Emailer, EmailService, Tracker, greet_user


def test_greet_user_returns_mocked_name_context_manager():
    # typically better if there are multiple functions mocked
    with mock.patch("utw.mocking.get_current_user", return_value="Alice"):
        result = greet_user()
        assert result == "Hello, Alice!"


@mock.patch("utw.mocking.get_current_user", return_value="Alice")
def test_greet_user_returns_mocked_name_decorator(mock_user):
    result = greet_user()
    assert result == "Hello, Alice!"
    mock_user.assert_called_once()


def test_track_event_logs_correctly():
    mock_logger = mock.Mock()

    tracker = Tracker(logger=mock_logger)
    tracker.track_event("abc123", "login")

    mock_logger.log.assert_called_once_with("user=abc123 event=login")


def test_send_email_uses_mocked_sender_context_manager():
    emailer = Emailer()

    with mock.patch.object(emailer, "sender_email", "mocked@example.com"):
        result = emailer.send_email("user@example.com", "Welcome!")

    assert (
        result == "From: mocked@example.com -> To: user@example.com | Subject: Welcome!"
    )


def test_send_email_uses_mocked_sender_context_manager():
    emailer = Emailer()

    with mock.patch.object(emailer, "sender_email", "mocked@example.com"):
        result = emailer.send_email("user@example.com", "Welcome!")

    assert (
        result == "From: mocked@example.com -> To: user@example.com | Subject: Welcome!"
    )


@mock.patch("utw.mocking.requests.post")
def test_send_email_mocks_api_call(mock_post):
    mock_post.return_value.status_code = 200

    service = EmailService(sender_email="test@x.com", api_key="SECRET")

    # Optionally patch attribute values if needed
    with (
        mock.patch.object(service, "sender_email", "mocked@x.com"),
        mock.patch.object(service, "api_key", "mocked-api-key"),
    ):
        result = service.send_email("user@example.com", "Subject", "Body")

    assert result is True

    # ✅ Assert that the mocked post was called correctly
    mock_post.assert_called_once_with(
        "https://api.email-service.com/send",
        json={
            "from": "mocked@x.com",
            "to": "user@example.com",
            "subject": "Subject",
            "body": "Body",
        },
        headers={"Authorization": "Bearer mocked-api-key"},
    )
