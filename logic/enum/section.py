from enum import Enum


class Section(Enum):
    """
    Defines the possible sections for tasks on the board.

    The sections include:
    - WORKING_ON_IT: Tasks that are currently being worked on.
    - DONE: Tasks that have been completed.
    - STUCK: Tasks that are blocked or facing issues.
    - NOT_STARTED: Tasks that have not been started yet.
    """
    WORKING_ON_IT = "Working On It"
    DONE = "Done"
    STUCK = "Stuck"
    NOT_STARTED = "Not Started"
