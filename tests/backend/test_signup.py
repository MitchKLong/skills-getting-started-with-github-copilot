from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_signup_adds_participant_to_activity():
    # Arrange
    activity_name = "Basketball Club"
    email = "new.student@example.com"

    if email in activities[activity_name]["participants"]:
        activities[activity_name]["participants"].remove(email)

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert email in activities[activity_name]["participants"]
