def func1(*args):
    print(sum(args))


# func1(10, 20, 30, 40)


def func2(**kwargs):
    print(kwargs)


students = ["amirali", "amirali", "parham", "shayan", "parsa", "farbod"]
func2(teacher="sadeghi", students=students, level="advanced")
