# with open("data.txt", "r+") as file:
#     file.write("\n")
#     file.write("ryusui gansai ken\n")
#     file.seek(0, 2)
#     file.write("senpu tetsuzan ken")

# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")

# from csv import DictReader
# with open("fighters.csv") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         print(row["Name"])

# from csv import writer
# with open("people.csv", "w", newline='') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Person", "Age"])
#     csv_writer.writerow(["Trevor", "19"])
#     csv_writer.writerow(["Gayseki", "69"])
#     csv_writer.writerow(["Joe Mama", "420"])

# from csv import reader, writer
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     with open("upper_fighters.csv", "w", newline='') as file:
#         csv_writer = writer(file)
#         for fighter in csv_reader:
#             csv_writer.writerow([s.upper() for s in fighter])

# from csv import DictWriter
# with open("people2.csv", "w", newline='') as file:
#     headers = ["Name", "Age"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({"Name": "Trevor", "Age": 19})
#     csv_writer.writerow({"Name": "Gayseki", "Age": 69})
#     csv_writer.writerow({"Name": "Joe Mama", "Age": 420})

from csv import DictReader, DictWriter


def cm_to_in(cm):
    return float(cm) * 0.393701


with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    with open("fighters_inches.csv", "w", newline='') as f:
        headers = ("Name", "Country", "Height")
        csv_writer = DictWriter(f, headers)
        csv_writer.writeheader()
        for f in list(csv_reader):
            csv_writer.writerow({"Name": f["Name"],
                                 "Country": f["Country"],
                                 "Height": cm_to_in(f["Height (in cm)"])})
