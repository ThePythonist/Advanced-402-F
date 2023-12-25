import random


def irancell():
    pn = ""
    code = random.choice(["0930", "0939", "0933", "0902"])

    for i in range(7):
        pn += str(random.randint(0, 9))

    pn = f"{code}{pn}"
    return pn


def hamrahaval():
    pn = ""
    code = random.choice(["0912", "0910", "0919", "0993"])

    for i in range(7):
        pn += str(random.randint(0, 9))

    pn = f"{code}{pn}"
    return pn


def rightell():
    pn = ""
    code = random.choice(["0921", "0922", "0923"])

    for i in range(7):
        pn += str(random.randint(0, 9))

    pn = f"{code}{pn}"
    return pn


if __name__ == "__main__":  # Run as a script
    print(irancell())
    print(hamrahaval())
    print(rightell())
