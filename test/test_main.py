from config import URL,LOCAL_URL
import responses
from app.main import get_joke,app,Joke
import logging
from fastapi.testclient import TestClient
import requests


logger = logging.getLogger('test')
client = TestClient(app)

clean_json_list:list[Joke] = [{
    'id':'1',
    'value':'value',
    'categories':[],
    'url':'url',
    'icon_url':'icon_url',
    'updated_at':'2022-01-01',
    'created_at':'2022-01-01'
    }]

def test_read_main():
    response = client.get("/hello")
    assert response.json() == {"msg":"Hello World"}
    assert response.status_code == 200

@responses.activate
def test_get_success():
    responses.add(responses.GET, f"{LOCAL_URL}/", status=200,
    json=clean_json_list[0]
    )

    req = requests.get(f'{LOCAL_URL}/')

    assert req.status_code == 200
    logger.debug(req.json())
    logger.debug(Joke(clean_json_list[0]))
    assert req.json() == Joke(clean_json_list[0]).broken_arrow()


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
