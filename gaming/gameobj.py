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

    @classmethod
    def reboot(cls):
        """Reboot class counts.

        QUICKFIX: for tests, as counts are not reset between scripts
        """
        cls.counts = {
            'total': 0,
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
        params = read_params(params, self.__class__.params)

        identity = params['identity']
        if identity is None:
            identity = GameObject.counts[self.__class__.__name__]
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
        return "%s_%s" % (self.__class__.__name__, self._id)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
