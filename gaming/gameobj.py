"""Class for major objects of a game (board, player, game itself, ...)"""
from utils.log import LogClass
from utils.params import read_params
from .parameters import LOGLVL


class GameObject(LogClass):
    """Major object of game."""

    counts = {
        'total': 0,
    }

    params = {
        "identity": None,
        "loglvl": None,
        "logpath": None,
    }

    def __new__(cls, *args, **kwargs):
        """Create a new game object."""

        # Update counts
        cls_name = cls.__name__
        GameObject.counts['total'] += 1
        if cls_name not in GameObject.counts:
            GameObject.counts[cls_name] = 1
        else:
            GameObject.counts[cls_name] += 1

        return super().__new__(cls)

    def __init__(self, **params):
        """Init new game object."""
        self.cls = self.__class__
        self.cls_name = self.cls.__name__

        params = read_params(params, self.cls.params)

        identity = params['identity']
        if identity is None:
            identity = GameObject.counts[self.cls_name]
        self._id = identity

        loglvl = params['loglvl']
        if loglvl is None:
            loglvl = LOGLVL

        super().__init__(
            name=self.name,
            loglvl=loglvl,
            logpath=params['logpath'],
        )

        self.log.debug("Created")

    @property
    def name(self):
        """Return name of instance"""
        return "%s_%s" % (self.cls_name, self._id)
