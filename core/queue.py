import lava_lyra


# Set CustomQueue
class CustomQueue(lava_lyra.Queue):
    def __init__(
        self,
        max_size: int | None = None,
        max_history: int = 0,
        *,
        overflow: bool = True,
    ):
        super().__init__(max_size, overflow=overflow)
        self._history: list = []
        self._max_history: int = max(0, max_history)

    @property
    def history_is_empty(self) -> bool:
        return not bool(self._history)

    @property
    def history_length(self) -> int:
        return len(self._history)

    def put_history(self, track: lava_lyra.Track) -> None:
        # Return if max set is 0
        if self._max_history == 0:
            return

        if len(self._history) >= self._max_history:
            if not self._overflow:
                raise lava_lyra.QueueFull("History is full.")

            if len(self._history) != 0:
                self._history.pop(0)

        self._history.append(track)

    def clear_history(self) -> list[lava_lyra.Track]:
        return self._history.clear()

    def get_history(self) -> list[lava_lyra.Track]:
        return self._history.copy()
