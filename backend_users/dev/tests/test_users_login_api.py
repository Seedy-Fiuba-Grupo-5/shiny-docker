import json
from prod.db_models.user_db_model import UserDBModel
from dev.aux_test import recreate_db


def test_dado_email_fdimaria_registrado_con_id_1_y_palabra_de_pase_tomate_cuando_POST_a_url_users_barra_login_el_email_y_la_palabra_de_pase_obtengo_el_email_y_el_id_anterior(test_app, test_database):
    """
    Dado una base de datos con un usuario registrado:
        nombre = "Franco Martin"
        apellido = "Di Maria"
        email = "fdimaria@fi.uba.ar"
        password = "tomate"
    Y una peticion:
        email = "fdimaria@fi.uba.ar"
        password = "tomate"
    Cuando POST "/users/login"
    Entonces obtengo status 200:
    Y obtengo cuerpo:
        email == "fdimaria@fi.uba.ar"
        id == 1
    """
    session = recreate_db(test_database)
    session.add(UserDBModel(name="Franco Martin",
                            lastname="Di Maria",
                            email="fdimaria@fi.uba.ar",
                            password="tomate"))
    session.commit()
    client = test_app.test_client()
    body = {
        "email": "fdimaria@fi.uba.ar",
        "password": "tomate"
    }
    response = client.post(
        "/users/login",
        data=json.dumps(body),
        content_type="application/json",
    )
    login_info = json.loads(response.data.decode())
    assert response.status_code == 200
    assert login_info["email"] == "fdimaria@fi.uba.ar"
    assert login_info["id"] == 1


def test_dado_email_fdimaria_registrado_y_password_tomate_cuando_POST_a_url_users_barra_login_el_email_y_la_palabra_de_pase_manzana_obtengo_un_error_401(
    test_app, 
    test_database):
    """
    Dado una base de datos con un usuario registrado:
        nombre = "Franco Martin"
        apellido = "Di Maria"
        email = "fdimaria@fi.uba.ar"
        password = "tomate"
    Y una peticion:
        email = "fdimaria@fi.uba.ar"
        password = "manzana"
    Cuando POST "/users/login"
    Entonces obtengo status 401
    Y obtengo cuerpo:
        'Email or password incorrect'
    """
    session = recreate_db(test_database)
    session.add(UserDBModel(name="Franco Martin",
                            lastname="Di Maria",
                            email="fdimaria@fi.uba.ar",
                            password="tomate"))
    session.commit()
    client = test_app.test_client()
    body = {
        "email": "fdimaria@fi.uba.ar",
        "password": "manzana"
    }
    response = client.post(
        "/users/login",
        data=json.dumps(body),
        content_type="application/json",
    )
    assert response.status_code == 401
    error = json.loads(response.data.decode())
    assert error == 'Email or password incorrect'


def test_dado_email_fdimaria_registrado_y_palabra_de_pase_tomate_cuando_POST_a_url_users_barra_login_email_fdimaria_obtengo_un_error(
    test_app, 
    test_database):
    """
    Dado una base de datos con un usuario registrado:
        nombre = "Franco Martin"
        apellido = "Di Maria"
        email = "fdimaria@fi.uba.ar"
        password = "tomate"
    Y una peticion:
        email = "fdimaria@fi.uba.ar"
    Cuando POST "/users/login"
    Entonces obtengo status 400
    Y obtengo cuerpo:
        'Missing arguments'
    """
    session = recreate_db(test_database)
    session.add(UserDBModel(name="Franco Martin",
                            lastname="Di Maria",
                            email="fdimaria@fi.uba.ar",
                            password="tomate"))
    session.commit()
    client = test_app.test_client()
    body = {"email": "fdimaria@fi.uba.ar"}
    response = client.post(
        "/users/login",
        data=json.dumps(body),
        content_type="application/json",
    )
    assert response.status_code == 400
    error = json.loads(response.data.decode())
    assert error == 'Missing arguments'
