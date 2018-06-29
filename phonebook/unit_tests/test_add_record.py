import os
import sys
import unittest
import io
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from phonebook import Phonebook


class TestPhonebook(unittest.TestCase):

    def test_isinstance(self):
        """Check that phonebook is instance of class Phonebook"""
        phonebook = Phonebook()
        self.assertIsInstance(phonebook, Phonebook)

    def test_add_record(self):
        """Check record added in phonebook"""
        phonebook = Phonebook()
        phonebook.add_record("John Mayer", 12345)
        self.assertIn("John Mayer", Phonebook.phonebook.keys())
    
    def test_delete_record(self):
        """Check record deleted from phonebook"""
        phonebook = Phonebook()
        phonebook.add_record("John Mayer", 12345)
        phonebook.delete_record("John Mayer")
        self.assertNotIn("John Mayer", Phonebook.phonebook.keys())

    def test_phonebook_created(self):
        """Check that phonebook dictionary created"""
        self.assertIsNotNone(Phonebook.phonebook)

    def test_list_records(self):
        """Check for right output when record created and listed"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        phonebook = Phonebook()
        phonebook.add_record("John Mayer", 12345)
        phonebook.list_records()
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue(),
            "\nPhonebook has following entries:\n'John Mayer' => 12345\n")

    def test_raise_value_error(self):
        phonebook = Phonebook()
        self.assertRaises(TypeError, phonebook.add_record(123, 123))
