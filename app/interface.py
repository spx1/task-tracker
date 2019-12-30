from mypy_extensions import TypedDict

class StateInterface(TypedDict, total=False):
    id: int
    name: str

class TaskInterface(TypedDict, total=False):
    id: int
    name: str
    state_id: int


