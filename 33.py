import csv


def write(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "field", "grade"])
        writer.writerows(data)

    print(f'{filename} has been created successfully.')


stds = [
    ["ali", "olom computer", 15],
    ["farzad", "mohandesi bargh", 18],
    ["mina", "mohandesi computer", 17],
]

write("students.csv", stds)
