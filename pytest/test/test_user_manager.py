from UserManager import UserManager
import pytest

@pytest.fixture
def user_manager(): #return a fresh user manager object for every test case
    yield UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("Ramit", "ramit.sharma@organisation.com") == True
    assert user_manager.get_user_email("Ramit") == "ramit.sharma@organisation.com"
    assert user_manager.get_user_email("Anu") == None

def test_add_duplicate_user_exception(user_manager):
    assert user_manager.add_user("Ramit", "ramit.sharma@organisation.com") == True
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.add_user("Ramit", "ramit.sharma@organisation.com") 

