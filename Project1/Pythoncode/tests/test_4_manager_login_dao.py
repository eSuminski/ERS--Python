from dao_imp.manager_login_dao_imp import ManagerLoginDAOImp
from daos.manager_login_dao import ManagerLoginDAO
from entities.manager_login import ManagerLogin

manager_login_dao: ManagerLoginDAO = ManagerLoginDAOImp()

m_login1 = ManagerLogin(1, "Teddington", "P@333OrD")
m_login2 = ManagerLogin(2, "I Love Ted", "Passw0rd")
m_login3 = ManagerLogin(2, "Rufus", "Still the wrong show")


def test_create_manager_login():
    manager_login_dao.create_manager_login(m_login1)
    check_against = manager_login_dao.select_manager_login_by_id(1)
    assert check_against.user_id == m_login1.user_id


def test_select_manager_login_by_id():
    result = manager_login_dao.select_manager_login_by_id(1)
    assert result.user_id == 1


def test_select_all_manager_logins():
    manager_login_dao.create_manager_login(m_login2)
    m_login_list = manager_login_dao.select_all_manager_logins()
    assert len(m_login_list) == 2


def test_update_manager_login():
    manager_login_dao.update_manager_login(m_login3)
    result = manager_login_dao.select_manager_login_by_id(2)
    assert result.username == "Rufus"


def test_delete_manager_login():
    manager_login_dao.delete_manager_login(2)
    m_login_list = manager_login_dao.select_all_manager_logins()
    assert len(m_login_list) == 1
