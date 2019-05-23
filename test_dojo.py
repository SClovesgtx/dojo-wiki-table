import pytest
from dojo import app
import json


@pytest.fixture
def client():
    with app.test_client() as tc:
        yield tc


def test_filmes(client):
	wiki_url = 'https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria'
	resp = client.get("/count-wiki-table", query_string={"url": wiki_url})
	print(resp.data)
	json_resp = json.loads(resp.data)
	          # resp.json
	assert isinstance(json_resp["line"], int)
	assert json_resp["line"] == 101
	assert resp.headers['content-type'] == "application/json"



