import sys
import csv

DEFAULT_CARDS_STATUS_TO_EXCLUDE = 'tak'
ACCOUNT_STATUS_ACTIVE_VALUE = 'aktywne'

USER_COLUMN_NAME = 'Użytkownik'
ACCOUNT_STATUS_COLUMN_NAME = 'Status konta'
CARDS_PICKED_UP_COLUMN_NAME = 'odebrał karty?'


class DuplicatedSwitch(Exception):
    pass


def printHelpHint():
    print("See python3 cards_checker.py --help for expected csv structure")


def printInfo():
    print("cards_checker.py checks csv file for users who have colum 'Status konta' set to 'aktywne' (case insensitive)"
          " and column 'odebrał karty?' set to anything other than 'tak' by default.\n"
          "You can also define custom filter for filtering out column 'odebrał karty?' using"
          " --exclude=VALUE1,VALUE2 switch.")


def printCorrectUsage():
    print("cards_checker.py correct usage : python3 cards_checker.py csvFile")
    print("cards_checker.py correct usage : python3 cards_checker.py csvFile --exclude=tak,EMPTY,wpłacił")


def printCsvStructureHint():
    print("Expected CSV format:")
    print("Użytkownik,XXX,XXX,Status konta,XXX,XXX,XXX,odebrał karty?,XXX,XXX,XXX")
    print("Kowalski Jan,XXX,XXX,aktywne,XXX,XXX,XXX,tak,XXX,XXX,XXX")
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


def findUsersWhoHaveNotCollectedTheCards(csv_header_and_rows_list, excluded_card_statuses):
    if 'EMPTY' in excluded_card_statuses:
        excluded_card_statuses.remove('EMPTY')
        excluded_card_statuses.append('')

    rows_array = csv_header_and_rows_list[1]
    first_result = True
    result = []

    for row in rows_array:
        account_status = row[3].lower()
        card_status = row[7].lower()

        if account_status == ACCOUNT_STATUS_ACTIVE_VALUE and card_status not in excluded_card_statuses:
            if first_result:
                result.append(f"{USER_COLUMN_NAME}, {ACCOUNT_STATUS_COLUMN_NAME}, {CARDS_PICKED_UP_COLUMN_NAME}")
                first_result = False

            result.append(f"{row[0]}, {row[3]}, {row[7]}")

    return result


def printOutput(rows_to_print):
    for outputPiece in rows_to_print:
        print(outputPiece)


def getExcludedCardsStatusesSwitch(argv):
    result = ['tak']
    found_custom_switch = False

    for arg in argv:
        if arg.startswith('--exclude='):
            if found_custom_switch:
                raise DuplicatedSwitch('Incorrect usage: Two --exclude switches found')

            found_custom_switch = True
            comma_separated_card_statuses_to_exclude = arg.replace('--exclude=', '')
            result = comma_separated_card_statuses_to_exclude.split(',')

    return result


def getFileName(argv):
    for arg in argv:
        if not arg.startswith('--'):
            return arg


if __name__ == "__main__":
    numberOfArgs = len(sys.argv)
    if numberOfArgs < 2 or numberOfArgs > 3:
        printInfo()
        printCorrectUsage()
        printHelpHint()
    else:
        if '--help' in sys.argv:
            printInfo()
            printCorrectUsage()
            printCsvStructureHint()
        else:
            arguments = sys.argv.copy()
            arguments.pop(0) # removing script name from args array

            excluded_card_statuses = getExcludedCardsStatusesSwitch(arguments)
            file_name = getFileName(arguments)

            try:
                csvHeaderAndRowsList = readCsvFile(file_name)
                verifyCsvFile(csvHeaderAndRowsList)
                output = findUsersWhoHaveNotCollectedTheCards(csvHeaderAndRowsList, excluded_card_statuses)
                printOutput(output)
            except DuplicatedSwitch as error:
                print(f"ERROR: {error.args[0]}")
            except FileNotFoundError:
                print(f"ERROR: Provided file {file_name} does not exist")
            except:
                print(f"ERROR: Provided file {file_name} is not a valid csv file or has an invalid format.")
                printHelpHint()
