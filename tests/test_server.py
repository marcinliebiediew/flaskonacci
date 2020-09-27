def test_algorithm(client):
    res = client.get('/fib/42')
    assert res.status_code == 200
    assert "[8, 13, 21]" in str(res.data)


def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
