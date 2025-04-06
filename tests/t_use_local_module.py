import pytest
from practice import use_local_module
# from classes_methods import class_samp

@pytest.mark.unit
def test_use_local_module(capsys):
    use_local_module.people = [{'firstname': 'JOSE', 'lastname': 'Diaz'}, {'firstname': 'julie', 'lastname': 'ONG'}]
    use_local_module.heroes = [{'firstname': 'steve', 'lastname': 'rogers', 'codename': 'captain america'}, {'firstname': 'tony', 'lastname': 'stark', 'codename': 'ironman'}]

    assert use_local_module.gen_info(use_local_module.people[0]) == "Person's name is Diaz, Jose and the email address is jose.diaz@xcompany.com.au"
    assert use_local_module.gen_info(use_local_module.heroes[0]) == "Person's name is Rogers, Steve and the email address is steve.rogers@xcompany.com.au... and also known as CAPTAIN AMERICA"

@pytest.mark.unit
def test_square():
    assert use_local_module.square(2) == 4
    assert use_local_module.square(3) == 9
    assert use_local_module.square(4) == 16
    assert use_local_module.square(5) == 25
