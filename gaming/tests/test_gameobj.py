from gaming import gameobj


class MyGameObj(gameobj.GameObject):
    pass


class MySubGameObj(MyGameObj):
    pass


class MyOtherGameObj(gameobj.GameObject):
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

    instance = MySubGameObj()
    assert instance.name == "MySubGameObj_1"

    instance = MyOtherGameObj()
    assert instance.name == "MyOtherGameObj_1"

    assert gameobj.GameObject.counter == {
        gameobj.GameObject: 7,
        MyGameObj: 3,
        MyOtherGameObj: 1,
        MySubGameObj: 1,
    }
