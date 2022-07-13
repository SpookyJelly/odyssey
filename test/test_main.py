from config import URL,LOCAL_URL
import responses
from app.main import get_joke,app
import logging
from fastapi.testclient import TestClient
import requests
from app.models.dto import Joke


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

# 일부 프로퍼티 없는 jokes
disabled_json_list:list[Joke] = [{
    'id':'1',
}]

def test_read_main():
    response = client.get("/hello")
    assert response.json() == {"msg":"Hello World"}
    assert response.status_code == 200

@responses.activate
def test_joke_success():
    responses.add(responses.GET, f"{LOCAL_URL}/", status=200,
    json=clean_json_list[0]
    )

    req = requests.get(f'{LOCAL_URL}/')


    # check Joke class as a dict
    # p.s) vars() are amazing
    """
    vars([object])
    모듈, 클래스, 인스턴스 또는 __dict__ 어트리뷰트가 있는 다른 객체의 __dict__ 어트리뷰트를 돌려줍니다.

    """
    assert req.status_code == 200
    assert req.json() == vars(Joke(clean_json_list[0]))


def test_joke_disabled():
    # 하자 있는 json이 Joke instance화 되었을때도 각 key를 가지는지
    logger.debug(vars(Joke(disabled_json_list[0])))
    assert vars(Joke(disabled_json_list[0])) == {
        'id':'1',
        'value':None,
        'categories':None,
        'icon_url':None,
        'url':None,
        'updated_at':None,
        'created_at':None,
    }


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
