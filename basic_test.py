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

    def test_correct_file_default_exclusion(self):
        csv_header_and_rows_list = cards_checker.readCsvFile("./testData/correctFile.csv")
        cards_checker.verifyCsvFile(csv_header_and_rows_list)
        card_statuses_to_exclude = cards_checker.getExcludedCardsStatusesSwitch([]) # get default exclusion
        output = cards_checker.findUsersWhoHaveNotCollectedTheCards(csv_header_and_rows_list, card_statuses_to_exclude)

        self.assertEqual(5, len(output))
        self.assertEqual("Użytkownik, Status konta, odebrał karty?", output[0]) # header
        self.assertEqual("Nieodbierający Użytkownik, aktywne, nie", output[1])
        self.assertEqual("Płacący Użytkownik, aktywne, wpłacił", output[2])
        self.assertEqual("Niewiadomy Użytkownik, aktywne, ", output[3])
        self.assertEqual("Inny Użytkownik, aktywne, inny", output[4])


    def test_correct_file_excluding_cards_statuses(self):
        csv_header_and_rows_list = cards_checker.readCsvFile("./testData/correctFile.csv")
        cards_checker.verifyCsvFile(csv_header_and_rows_list)

        output = cards_checker.findUsersWhoHaveNotCollectedTheCards(csv_header_and_rows_list, ['tak','EMPTY'])
        self.assertEqual(4, len(output), output)
        self.assertEqual("Użytkownik, Status konta, odebrał karty?", output[0], output) # header
        self.assertEqual("Nieodbierający Użytkownik, aktywne, nie", output[1], output)
        self.assertEqual("Płacący Użytkownik, aktywne, wpłacił", output[2], output)
        self.assertEqual("Inny Użytkownik, aktywne, inny", output[3], output)

        output = cards_checker.findUsersWhoHaveNotCollectedTheCards(csv_header_and_rows_list, ['tak','inny'])
        self.assertEqual(4, len(output), output)
        self.assertEqual("Użytkownik, Status konta, odebrał karty?", output[0], output) # header
        self.assertEqual("Nieodbierający Użytkownik, aktywne, nie", output[1], output)
        self.assertEqual("Płacący Użytkownik, aktywne, wpłacił", output[2], output)
        self.assertEqual("Niewiadomy Użytkownik, aktywne, ", output[3], output)

        output = cards_checker.findUsersWhoHaveNotCollectedTheCards(csv_header_and_rows_list, ['inny', 'wpłacił'])
        self.assertEqual(4, len(output), output)
        self.assertEqual("Użytkownik, Status konta, odebrał karty?", output[0], output) # header
        self.assertEqual("Nieodbierający Użytkownik, aktywne, nie", output[1], output)
        self.assertEqual("Odbierający Użytkownik, aktywne, tak", output[2], output)
        self.assertEqual("Niewiadomy Użytkownik, aktywne, ", output[3], output)

        output = cards_checker.findUsersWhoHaveNotCollectedTheCards(csv_header_and_rows_list, ['tak','EMPTY', 'wpłacił'])
        self.assertEqual(3, len(output), output)
        self.assertEqual("Użytkownik, Status konta, odebrał karty?", output[0], output) # header
        self.assertEqual("Nieodbierający Użytkownik, aktywne, nie", output[1], output)
        self.assertEqual("Inny Użytkownik, aktywne, inny", output[2], output)

        output = cards_checker.findUsersWhoHaveNotCollectedTheCards(csv_header_and_rows_list, ['tak','EMPTY', 'wpłacił', 'inny'])
        self.assertEqual(2, len(output), output)
        self.assertEqual("Użytkownik, Status konta, odebrał karty?", output[0], output) # header
        self.assertEqual("Nieodbierający Użytkownik, aktywne, nie", output[1], output)



if __name__ == '__main__':
    unittest.main()