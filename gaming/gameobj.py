"""Class for major objects of a game (board, player, game itself, ...)"""
from collections import defaultdict

from utils.log import LogClass
from utils.params import read_params
from .parameters import LOGLVL


class GameObjMeta(type):
    """Meta class to track ineheritance within GameObject."""

    __inheritors__ = defaultdict(list)

    def __new__(mcs, clsname, superclasses, attributedict):
        """Create a new game class."""
        klass = type.__new__(mcs, clsname, superclasses, attributedict)
        for base in klass.mro()[1:-1]:
            mcs.__inheritors__[base].append(klass)
        return klass


class GameObject(LogClass, metaclass=GameObjMeta):
    """Major object of game."""

    # ----------------------------------------------------------------------- #
    # Class attributes / methods

    # ---- Log

    dft_log_kwargs = {
        'name': None,
        'loglvl': LOGLVL,
        'logpath': None,
    }

    # ---- Object counter

    counter = defaultdict(int)  # (class, number of instances) dict

    @classmethod
    def count(cls):
        """Return number of instances."""
        return GameObject.counter[cls]

    @staticmethod
    def reset_counter():
        """Reset counter of game objects.

        QUICKFIX: for tests, as counts are not reset between scripts
        """
        GameObject.counter = defaultdict(int)

    # ----------------------------------------------------------------------- #
    # Instances methods

    def __new__(cls, *args, **kwargs):
        """Create a new game object."""

        # Update counter of all mother classes within GameObject
        GameObject.counter[GameObject] += 1
        for gameobj_cls in GameObjMeta.__inheritors__[GameObject]:
            if issubclass(cls, gameobj_cls):
                GameObject.counter[gameobj_cls] += 1
        return super().__new__(cls)

    def __init__(self, identity=None, **log_kwargs):
        """Init new game object."""
        if identity is None:
            identity = self.__class__.count()
        self._id = identity

        log_kwargs = read_params(log_kwargs, self.__class__.dft_log_kwargs)
        if log_kwargs['name'] is None:
            log_kwargs['name'] = self.name
        super().__init__(**log_kwargs)

        self.log.debug("Created")

    @property
    def name(self):
        """Return name of instance"""
        return "%s_%s" % (self.__class__.__name__, self._id)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
