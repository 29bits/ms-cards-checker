import unittest
import cards_checker

class TestSum(unittest.TestCase):
    def test_incorrect_file_throwing_exception(self):
        failed = False

        try:
            csv_header_and_rows_list = cards_checker.readCsvFile("./testData/incorrectFileFormat.csv")
            cards_checker.verifyCsvFile(csv_header_and_rows_list)
        except:
            failed = True

        self.assertTrue(failed, "cards_checker should have failed for an incorrect csv")

    def test_correct_file(self):
        csv_header_and_rows_list = cards_checker.readCsvFile("./testData/correctFile.csv")
        cards_checker.verifyCsvFile(csv_header_and_rows_list)
        output = cards_checker.findUsersWhoHaveNotCollectedTheCards(csv_header_and_rows_list)

        self.assertEqual(2, len(output))
        self.assertEqual("Użytkownik, Status konta, odebrał karty?", output[0])
        self.assertEqual("Nieodbierający Użytkownik, aktywne, nie", output[1])

if __name__ == '__main__':
    unittest.main()