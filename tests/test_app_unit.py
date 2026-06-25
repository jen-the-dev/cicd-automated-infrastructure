from app.main import get_health_payload


def test_get_health_payload_contains_expected_keys():
    payload = get_health_payload()
    assert payload["service"] == "portfolio-cicd-app"
    assert payload["status"] == "ok"
    assert payload["deployment"] == "kubernetes-ready"
