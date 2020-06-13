import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        0 - Administrative, an integer
        1 - Administrative_Duration, a floating point number
        2 - Informational, an integer
        3 - Informational_Duration, a floating point number
        4 - ProductRelated, an integer
        5 - ProductRelated_Duration, a floating point number
        6 - BounceRates, a floating point number
        7 - ExitRates, a floating point number
        8 - PageValues, a floating point number
        9 - SpecialDay, a floating point number
        10 - Month, an index from 0 (January) to 11 (December)
        11 - OperatingSystems, an integer
        12 - Browser, an integer
        13 - Region, an integer
        14 - TrafficType, an integer
        15- VisitorType, an integer 0 (not returning) or 1 (returning)
        16 - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
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
        


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)

    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    sensitivity = 0.0
    specificity = 0.0
    positive = 0.0
    negative = 0.0
    
    length = len(labels)
    for pos in range(length):
        if predictions[pos] == 1:
            positive += 1
            if labels[pos] == predictions[pos]:
                sensitivity += 1
        elif predictions[pos] == 0:
            negative += 1
            if labels[pos] == predictions[pos]:
                specificity += 1
    sensitivity /= positive
    specificity /= negative

    return sensitivity, specificity

if __name__ == "__main__":
    main()
