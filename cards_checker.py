import sys
import csv

CARDS_PICKED_UP_TRUE_VALUE = 'tak'
ACCOUNT_STATUS_ACTIVE_VALUE = 'aktywne'

USER_COLUMN_NAME = 'Użytkownik'
ACCOUNT_STATUS_COLUMN_NAME = 'Status konta'
CARDS_PICKED_UP_COLUMN_NAME = 'odebrał karty?'


def printHelpHint():
    print("See python3 cards_checker.py --help for expected csv structure")


def printInfo():
    print("cards_checker.py checks csv file for users who have colum 'Status konta' set to 'aktywne' (case insensitive)"
          " and column 'odebrał karty?' set to anything other than 'tak'")


def printCorrectUsage():
    print("cards_checker.py correct usage: python3 cards_checker.py csvFile")


def printCsvStructureHint():
    print("Expected CSV format:")
    print("Użytkownik,XXX,XXX,Status konta,XXX,XXX,XXX,odebrał karty?,XXX,XXX,XXX")
    print("Kowalski Jan,XXX,XXX,aktywne,XXX,XXX,XXX,odebrał karty?,XXX,XXX,XXX")
    print("\nCSV headers names are being validated")


def readCsvFile(filename):
    file = open(filename)
    csv_reader = csv.reader(file)
    header_row_array = next(csv_reader)
    rows_array = []
    for row in csv_reader:
        rows_array.append(row)

    file.close()
    return [header_row_array, rows_array]


# Here's the spot where you change column checks if you change the CSV
def verifyCsvFile(csv_header_and_rows_list):
    header = csv_header_and_rows_list[0]

    user_column = header[0]
    activity_column = header[3]
    were_cards_picked_up_column = header[7]

    assert user_column == USER_COLUMN_NAME
    assert activity_column == ACCOUNT_STATUS_COLUMN_NAME
    assert were_cards_picked_up_column == CARDS_PICKED_UP_COLUMN_NAME


def findUsersWhoHaveNotCollectedTheCards(csv_header_and_rows_list):
    rows_array = csv_header_and_rows_list[1]
    first_result = True
    result = []

    for row in rows_array:
        if row[3].lower() == ACCOUNT_STATUS_ACTIVE_VALUE and row[7].lower() != CARDS_PICKED_UP_TRUE_VALUE:
            if first_result:
                result.append(f"{USER_COLUMN_NAME}, {ACCOUNT_STATUS_COLUMN_NAME}, {CARDS_PICKED_UP_COLUMN_NAME}")
                first_result = False

            result.append(f"{row[0]}, {row[3]}, {row[7]}")

    return result


def printOutput(rows_to_print):
    for outputPiece in rows_to_print:
        print(outputPiece)


if __name__ == "__main__":
    numberOfArgs = len(sys.argv)
    if numberOfArgs < 2 or numberOfArgs > 2:
        printInfo()
        printCorrectUsage()
        printHelpHint()
    else:
        argument = sys.argv[1]
        if argument == '--help':
            printInfo()
            printCorrectUsage()
            printCsvStructureHint()
        else:
            try:
                csvHeaderAndRowsList = readCsvFile(argument)
                verifyCsvFile(csvHeaderAndRowsList)
                output = findUsersWhoHaveNotCollectedTheCards(csvHeaderAndRowsList)
                printOutput(output)
            except:
                print(f"ERROR: Provided file {argument} is not a valid csv file or has an invalid format.")
                printHelpHint()
