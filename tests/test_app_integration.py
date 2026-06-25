from app.main import create_app


def test_health_endpoint_returns_expected_payload():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["service"] == "portfolio-cicd-app"
    assert payload["status"] == "ok"
