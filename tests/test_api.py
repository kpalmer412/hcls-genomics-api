from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_panels():
    response = client.get("/panels")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["panel_id"] == "P001"
    assert data[0]["sequence_type"] == "DNA"
