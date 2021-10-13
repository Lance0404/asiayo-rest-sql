import json

def test_round_down(test_app):
    data = {
        "from_currency": "TWD",
        "from_amount": 3.141,
        "to_currency": "TWD"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '3.14'

def test_round_up(test_app):
    data = {
        "from_currency": "TWD",
        "from_amount": 3.145,
        "to_currency": "TWD"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '3.15'

def test_TWD_to_TWD(test_app):
    data = {
        "from_currency": "TWD",
        "from_amount": 1,
        "to_currency": "TWD"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '1.00'

def test_TWD_to_USD(test_app):
    data = {
        "from_currency": "TWD",
        "from_amount": 1,
        "to_currency": "USD"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '0.03'

def test_TWD_to_JPY(test_app):
    data = {
        "from_currency": "TWD",
        "from_amount": 1,
        "to_currency": "JPY"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '3.67'        

def test_JPY_to_TWD(test_app):
    data = {
        "from_currency": "JPY",
        "from_amount": 1,
        "to_currency": "TWD"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '0.27'            

def test_JPY_to_TWD(test_app):
    data = {
        "from_currency": "JPY",
        "from_amount": 1,
        "to_currency": "TWD"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '0.27'                

def test_JPY_to_USD(test_app):
    data = {
        "from_currency": "JPY",
        "from_amount": 1,
        "to_currency": "USD"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '0.01'  


def test_USD_to_TWD(test_app):
    data = {
        "from_currency": "USD",
        "from_amount": 1,
        "to_currency": "TWD"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '30.44'


def test_USD_to_JPY(test_app):
    data = {
        "from_currency": "USD",
        "from_amount": 1,
        "to_currency": "JPY"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '111.80'  


def test_comma_format(test_app):
    data = {
        "from_currency": "JPY",
        "from_amount": 8888888.888,
        "to_currency": "JPY"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '8,888,888.89' 


def test_complex_1(test_app):
    data = {
        "from_currency": "TWD",
        "from_amount": 21398.3456,
        "to_currency": "USD"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '702.08'  

def test_complex_1(test_app):
    data = {
        "from_currency": "JPY",
        "from_amount": 21398.3456,
        "to_currency": "TWD"
    }
    response = test_app.post(
                "/currency",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json() == '5,768.14' 
