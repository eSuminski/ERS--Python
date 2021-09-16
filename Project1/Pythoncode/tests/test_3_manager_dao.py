from dao_imp.manger_dao_imp import ManagerDAOImp
from daos.manager_dao import ManagerDAO
from entities.manager import Manager

manager1 = Manager(0, "Ted", "Betteroff")
manager2 = Manager(0, "Linda", "I'm not actually sure")
manager3 = Manager(0, "Rufus", "wait wrong show")
manager_dao: ManagerDAO = ManagerDAOImp()


def test_create_manager():
    manager_dao.create_manager(manager1)
    assert manager1.manager_id == 1


def test_get_manager_by_id():
    target = manager1
    result = manager_dao.get_manager_by_id(1)
    assert target.manager_id == result.manager_id


def test_get_all_managers():
    manager_dao.create_manager(manager2)
    manager_dao.create_manager(manager3)
    list = manager_dao.get_all_managers()
    assert len(list) == 3


def test_update_manager():
    new_manager = Manager(2, "Veronica", "I'm the boss")
    manager_dao.update_manager(new_manager)
    result = manager_dao.get_manager_by_id(2)
    assert result.first_name == "Veronica"


def test_delete_manager():
    result = manager_dao.delete_manager(3)
    assert result
