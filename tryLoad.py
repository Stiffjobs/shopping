import csv
import sys


def main():

    evidence, labels = load_data(sys.argv[1])
    print(evidence[0])
    print(labels[0])

def load_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader) # skip the first row

        evidences = []
        labels = []
        for row in reader:
            if row[-1] == "TRUE":
                labels.append(1)
            else:
                labels.append(0)
            evidence = []
            for pos in range(len(row) - 1):
                if pos == 0:
                    num_to_add = int(row[pos])
                elif pos == 1:
                    num_to_add = float(row[pos])
                elif pos == 2:
                    num_to_add = int(row[pos])
                elif pos == 3:
                    num_to_add = float(row[pos])
                elif pos == 4:
                    num_to_add = int(row[pos])
                elif pos == 5:
                    num_to_add = float(row[pos])
                elif pos == 6:
                    num_to_add = float(row[pos])
                elif pos == 7:
                    num_to_add = float(row[pos])
                elif pos == 8:
                    num_to_add = float(row[pos])
                elif pos == 9:
                    num_to_add = float(row[pos])
                elif pos == 10:
                    if row[pos] == "Jan":
                        num_to_add = 0
                    elif row[pos] == "Feb":
                        num_to_add = 1
                    elif row[pos] == "Mar":
                        num_to_add = 2
                    elif row[pos] == "Apr":
                        num_to_add = 3
                    elif row[pos] == "May":
                        num_to_add = 4
                    elif row[pos] == "June":
                        num_to_add = 5
                    elif row[pos] == "Jul":
                        num_to_add = 6
                    elif row[pos] == "Aug":
                        num_to_add = 7
                    elif row[pos] == "Sep":
                        num_to_add = 8
                    elif row[pos] == "Oct":
                        num_to_add = 9
                    elif row[pos] == "Nov":
                        num_to_add = 10
                    elif row[pos] == "Dec":
                        num_to_add = 11
                elif pos == 11:
                    num_to_add = int(row[pos])
                elif pos == 12:
                    num_to_add = int(row[pos])
                elif pos == 13:
                    num_to_add = int(row[pos])
                elif pos == 14:
                    num_to_add = int(row[pos])
                elif pos == 15:
                    if row[pos] == "Returning_Visitor":
                        num_to_add = 1
                    else:
                        num_to_add = 0
                elif pos == 16:
                    if row[pos] == "FALSE":
                        num_to_add = 0
                    else:
                        num_to_add = 1
                evidence.append(num_to_add)
            evidences.append(evidence)
        
        return evidences, labels


if __name__ == "__main__":
    main()