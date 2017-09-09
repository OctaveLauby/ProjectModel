"""Skeleton for games.

Basically a game is:
    - A list of players playing one after the other
    - Each player perform an action
    - Each action change the state of the game
    - Each action has consequences on every players

Vocabulary:
    - environement: complete description of game (and players)
    - state:    descr of how the game looks like
                e.g. where are the pawns
    - status:   where the game is at
                e.g. who is playing, is it over
"""
from .gameobj import GameObject
from .players import Bot, Human


class InvalidAction(Exception):
    """Exception raised when an invalid action is tried."""
    pass


class Game(GameObject):
    """Game Skeleton

    Methods raising NotImplementedError must be implemented.
    If msg in raise says option, the method does not necessarily requires an
    implementation.
    """
    actions = None  # Possible actions
    bot = Bot       # Class used to build bots
    human = Human   # Class used to build humans
    players_n = 2   # Number of players in game

    # ----------------------------------------------------------------------- #
    # Initialisation and properties

    def __init__(self, bots=None, load_path=None, p_params=None, **params):
        """Init a game.

        Args:
            bots        (list): index of players to replace with bots
            load_path   (str):  path where game can be loaded from
            p_params    (dict): key arguments for players
            params      (dict): key arguments for game object

            @see .gameobj.GameObject.params
        """
        super().__init__(**params)

        # Players
        if p_params is None:
            p_params = {}
        if bots is None:
            bots = []
        self._players = [
            self.__class__.bot(**p_params)
            if player in bots
            else self.__class__.human(**p_params)

            for player in range(self.__class__.players_n)
        ]

        # Status
        self._player = 0    # Current player
        self._over = False

        if load_path:
            self.load(load_path)

    @property
    def players(self):
        """Return list of players."""
        return self._players

    @property
    def player(self):
        """Return current player."""
        return self.players[self._player]

    def status(self):
        """Return status of game."""
        return {
            'player': self._player,
            'over': self._over,
        }

    # ----------------------------------------------------------------------- #
    # Utils

    def av_actions(self):
        """Return available actions."""
        return self.actions

    def is_over(self):
        """Return whether game is over."""
        return self._over

    def raise_endflag(self):
        """Raise end flag."""
        self._over = True

    def refresh(self):
        """Refresh environement if necessary."""
        pass

    def state(self):
        """Return current game state."""
        return self.status

    # ----------------------------------------------------------------------- #
    # Gameplay

    def act(self, action):
        """Operate action (as current player).

        Returns:
            (list): consequences for each player
        """
        raise NotImplementedError

    def next(self):
        """Go to next player."""
        self._player += 1
        if self._player >= self.__class__.players_n:
            self._player = 0

    def play(self):
        """Play game until game is over."""
        self.log.debug("Game started")
        while not self.is_over():

            # Current Player
            cplayer = self.player
            self.log.debug("%s turn", cplayer)

            # Display game if player requires it
            if cplayer.requires_visual:
                self.display()

            # Catch and apply player action
            action = self.player.action(
                gstate=self.state(),
                actions=self.av_actions(),
            )
            try:
                consequences = self.act(action)
            except InvalidAction:
                self.log.warning(
                    "%s performed invalid action: %s",
                    cplayer, action
                )
                continue

            # Reverberate consequences on players
            self.log.debug("Apply consequences to players")
            assert len(consequences) == self.__class__.players_n
            for player, consequence in zip(self.players, consequences):
                player.take(consequence)

            # Refresh game and move on
            self.refresh()
            self.next()

    # ----------------------------------------------------------------------- #
    # Display

    def display(self):
        """Display game."""
        raise NotImplementedError

    # ----------------------------------------------------------------------- #
    # Save / Load

    def load(self, load_path):
        """Load game environement from file."""
        raise NotImplementedError("Option not implemented")

    def save(self, save_path):
        """Save game environement."""
        raise NotImplementedError("Option not implemented")
