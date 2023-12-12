"""

Одиночка (Singleton) - это паттерн проектирования, который гарантирует, что у класса есть только один экземпляр, 
и предоставляет глобальную точку доступа к этому экземпляру.
"""


"""
Functional Singleton
"""

from typing import Callable


def functional_singleton(
    create_object: Callable[[], object],
) -> Callable[[], object]:
    """Ensure a single instance is returned from a factory function."""
    instance = None

    def get_instance():
        nonlocal instance
        # print(f"instance={instance}")
        if instance is None:
            instance = create_object()
        return instance

    return get_instance


def create_logger():
    return {"logs": []}


get_logger = functional_singleton(create_logger)


def log(message):
    logger = get_logger()
    logger["logs"].append(message)


def show_logs():
    print("Show logs!")
    logger = get_logger()
    logs = "\n---\n".join(logger["logs"])
    print(logs)


logger1 = get_logger()
logger2 = get_logger()

print(logger1 is logger2)  # True
log("log1")
log("log2")
print(logger1["logs"])
print(logger2["logs"])
show_logs()