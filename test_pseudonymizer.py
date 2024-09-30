
import unittest
from pseudonymizer import CustomAnonymizer

class TestTravelSpecificPIIPseudonymization(unittest.TestCase):
    
    def setUp(self):
        # Initialize the CustomPseudonymizer before each test
        self.pseudonymizer   = CustomAnonymizer(add_default_faker_operators=False)
    
    # Add custom recognizers and fake data generators
        self.pseudonymizer.add_custom_recognizers()
        self.pseudonymizer.add_custom_fake_data_generators()
        
        
    def test_pseudonymize_pnr(self):
        document_content = "My PNR is LHKQK9."
        anonymized_content = self.pseudonymizer.anonymize_document(document_content)
        self.assertNotIn("LHKQK9", anonymized_content)
    
    def test_pseudonymize_pnr_(self):
        document_content = "My PNR is 9PROWK."
        anonymized_content = self.pseudonymizer.anonymize_document(document_content)
        self.assertNotIn("9PROWK", anonymized_content)

    def test_pseudonymize_e_ticket(self):
        document_content = "My e-ticket number is 123-4567890123."
        anonymized_content = self.pseudonymizer.anonymize_document(document_content)
        self.assertNotIn("123-4567890123", anonymized_content)
        
    def test_pseudonymize_e_ticket_(self):
        document_content = "My e-ticket number is 123-3049203039."
        anonymized_content = self.pseudonymizer.anonymize_document(document_content)
        self.assertNotIn("123-3049203039", anonymized_content)


    def test_pseudonymize_registration(self):
        document_content = "My registration number is N390HA."
        anonymized_content = self.pseudonymizer.anonymize_document(document_content)
        self.assertNotIn("N390HA", anonymized_content)



    def test_pseudonymize_flight_numbers(self):
        document_content = "The disruption of flight DL1234 "
        anonymized_content = self.pseudonymizer.anonymize_document(document_content)

        self.assertNotIn("DL1234", anonymized_content)



    def test_pseudonymize_contact_information(self):
        document_content = "My phone number is 999-888-7777 and email is johndoe@example.com."
        anonymized_content = self.pseudonymizer.anonymize_document(document_content)

        self.assertNotIn("999-888-7777", anonymized_content)
        self.assertNotIn("johndoe@example.com", anonymized_content)



if __name__ == '__main__':
    unittest.main()
