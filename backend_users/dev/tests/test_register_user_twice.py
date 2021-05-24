from prod.db_models.user_db_model import UserDBModel


def test_get_minus_one_when_register_user_twice(
        test_app,
        test_database
):
    session = test_database.session
    session.remove()
    test_database.drop_all()
    test_database.create_all()
    assert 1 == UserDBModel.add_user(name="Franco", lastname="Di Maria",
                                     email="fdimaria@fi.uba.ar",
                                     password="hola")
    assert -1 == UserDBModel.add_user(name="Franco", lastname="Di Maria",
                                      email="fdimaria@fi.uba.ar",
                                      password="hola")