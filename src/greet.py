"""Simple greeting demo pushed via SSH."""


def greet(name: str = "github") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
