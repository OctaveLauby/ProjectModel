import os
import pytest
import shutil

from gaming import game
from gaming.gameobj import GameObject
from gaming.players import Bot, Human


# --------------------------------------------------------------------------- #
# Parameters

TMP_DIR = "tmp"


# --------------------------------------------------------------------------- #
# Setup / Teardown

def setup_function(function):
    if os.path.exists(TMP_DIR):
        shutil.rmtree("tmp")


def teardown_function(function):
    if os.path.exists(TMP_DIR):
        shutil.rmtree("tmp")


# --------------------------------------------------------------------------- #
# Tests


def test_game_1():

    ginstance = game.Game(
        bots=[1],
        load_path=None,
        p_params={'loglvl': "INFO"},
        loglvl="DEBUG",
    )

    # ---- Players
    assert isinstance(ginstance, GameObject)
    assert ginstance.get_loglvl() == 10
    assert ginstance.players[0].get_loglvl() == 20
    assert ginstance.players[1].get_loglvl() == 20
    assert ginstance.player.name == "Human_1"

    assert isinstance(ginstance.players[0], Human)
    assert isinstance(ginstance.players[1], Bot)

    # ---- Environment
    assert ginstance.status() == {
        'over': False,
        'player': 0,
    }
    assert ginstance.state() == []
    assert ginstance.av_actions() is None
    assert ginstance.is_over() is False

    # ---- Actions on environment
    ginstance.next()
    assert ginstance.player.name == "Bot_1"
    ginstance.next()
    assert ginstance.player.name == "Human_1"

    ginstance.next()
    ginstance.raise_endflag()
    assert ginstance.is_over() is True
    assert ginstance.status() == {
        'over': True,
        'player': 1,
    }

    ginstance.next()
    assert ginstance.status() == {
        'over': True,
        'player': 0,
    }

    with pytest.raises(NotImplementedError):
        ginstance.act("action")

    with pytest.raises(NotImplementedError):
        ginstance.display()

    # ---- Save / Load
    save_dir = os.path.join(TMP_DIR, "test_1_game")

    ginstance.save(save_dir)
    assert os.path.exists(os.path.join(save_dir, game.STATE_FILE))
    assert os.path.exists(os.path.join(save_dir, game.STATUS_FILE))

    ninstance = game.Game(load_path=save_dir)
    assert ninstance.status() == ginstance.status()
