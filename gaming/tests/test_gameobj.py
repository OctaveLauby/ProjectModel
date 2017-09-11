from gaming import gameobj


class MyGameObj(gameobj.GameObject):
    pass


def test_gameobject():

    gameobj.GameObject.reset_counter()

    instance = gameobj.GameObject()
    assert instance.name == "GameObject_1"
    assert instance.get_loglvl() == 20

    instance = gameobj.GameObject(
        identity="new",
        loglvl=10,
    )
    assert instance.name == "GameObject_new"
    assert instance.get_loglvl() == 10

    instance = gameobj.GameObject()
    assert instance.name == "GameObject_3"

    instance = MyGameObj(
        identity="first"
    )
    assert instance.name == "MyGameObj_first"

    instance = MyGameObj()
    assert instance.name == "MyGameObj_2"

    assert gameobj.GameObject.counter == {
        MyGameObj: 2,
        gameobj.GameObject: 5,
    }
