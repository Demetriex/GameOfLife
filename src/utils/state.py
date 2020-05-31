class State(object):
    game = None

    def update(self):
        raise NotImplementedError("please implemented this method")

    def on_start(self):
        pass

    def on_stop(self):
        pass

    def on_resume(self):
        pass

    def handle_event(self):
        pass


class StateManager(object):
    game = None
    _stack = []

    def init(self, game):
        self.game = game
        self.game.manager = self

    def set_initial_state(self, initial_state):
        if not self._stack:
            initial_state.manager = self
            initial_state.game = self.game
            initial_state.on_start()
            self._stack.append(initial_state)

    def push(self, state):
        self._stack[0].on_stop()
        self._stack.insert(state)
        state.on_start()

    def pop(self):
        if len(self._stack) > 1:
            self._stack.pop(0)
            self._stack[0].on_resume()
        else:
            self._stack.pop(0)

    def update(self):
        if self._stack:
            self._stack[0].update()

    def handle_event(self):
        if self._stack:
            self._stack[0].handle_event()
