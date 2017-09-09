from gaming import gameobj


class MyGameObj(gameobj.GameObject):
    pass


def test_gameobject():

    instance = gameobj.GameObject()
    assert instance.name == "GameObject_1"
    assert instance.get_loglvl() == 10

    instance = gameobj.GameObject(
        identity="new",
        loglvl=20,
    )
    assert instance.name == "GameObject_new"
    assert instance.get_loglvl() == 20

    instance = gameobj.GameObject()
    assert instance.name == "GameObject_3"

    instance = MyGameObj()
    assert instance.name == "MyGameObj_1"

    assert gameobj.GameObject.counts == {
        "total": 4,
        "GameObject": 3,
        "MyGameObj": 1,
    }
