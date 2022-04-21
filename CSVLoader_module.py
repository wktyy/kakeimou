import csv


def OpenCSV():
    csv_file = open("./data/kakeiho.csv", "r", encoding="ms932", errors="", newline="")

    return csv_file

def CloseCSV(f):
    f.close()