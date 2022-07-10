from config import URL,LOCAL_URL
import responses
from main import get_joke,app
import logging
from fastapi.testclient import TestClient
import requests

logger = logging.getLogger('test')
client = TestClient(app)

def test_read_main():
    response = client.get("/hello")
    assert response.json() == {"msg":"Hello World"}
    assert response.status_code == 200



@responses.activate
def test_api_joke_request():
    responses.add(
        responses.GET,
        URL,
        status=200,
        json={'id':'test','value':'test'}
    )
    assert get_joke().status_code == 200
    assert get_joke().json() == {'id':'test','value':'test'}

@responses.activate
def test_error():
    responses.add(responses.GET,f"{LOCAL_URL}/hello",status=200,json={'msg':"Hello World"})
    # 정상 응답
    res = requests.get(f"{LOCAL_URL}/hello")
    assert res.json() == {'msg':"Hello World"}
    
    # RequestMock을 이용한 의도적 오류
    #Responses as a context manager
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            f"{LOCAL_URL}/hello",
            json={"detail":"error occured"},
            status=400,
            content_type="application/json",
        )
        resp = requests.get(f"{LOCAL_URL}/hello")

        assert resp.status_code == 400
        assert resp.json() == {"detail":"error occured"}
