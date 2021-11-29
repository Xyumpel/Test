from app import get_doc_owner_name,delete_doc,add_new_doc
import unittest


class TestApp(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name("2207 876234"), "Василий Гупкин")

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('1-1', 'passport RF', 'Dmitriy Polyakov', 2), 2)

    def test_delete_doc(self):
        self.assertTrue(delete_doc('2207 876234'))