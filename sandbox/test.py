def branch(l: float, a: float) -> None:
    print("branch")
    print(f"a {a} - l {l}")
    if l < 4.0:
        ...
    else:
        branch(l * 0.5, a + 45.0)
        branch(l * 0.25, a - 45.0)
    print(f"a {a+180.0} - l{l}")


length: float = 8.0
angle: float = 90.0
branch(length, angle)

