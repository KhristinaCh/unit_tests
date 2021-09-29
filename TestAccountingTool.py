import unittest
from unittest.mock import patch
from AccountingTool import get_doc_owner_name, get_all_doc_owners_names, get_doc_shelf, delete_doc, add_new_doc, \
    add_new_shelf, move_doc_to_shelf


class TestAccountingTool1(unittest.TestCase):
# basic tests scenario

    @classmethod
    def setUpClass(cls):
        print('Cls method setup')

    def setUp(self):
        print('Method setup')

    def test_get_doc_owner_name(self):
        with unittest.mock.patch('builtins.input', return_value='p'):
            assert input() == 'p'
            self.assertEqual(get_doc_owner_name('11-2'), 'Геннадий Покемонов')

    def test_get_doc_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='s'):
            assert input() == 's'
            self.assertEqual(get_doc_shelf('10006'), '2')

    def test_get_all_doc_owners_names(self):
        with unittest.mock.patch('builtins.input', return_value='ap'):
            assert input() == 'ap'
            self.assertEqual(get_all_doc_owners_names(), {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'})

    def test_move_doc_to_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='m'):
            assert input() == 'm'
            self.assertEqual(move_doc_to_shelf('11-2', '2'), 'Документ номер 11-2 был перемещен на полку номер 2')

    def tearDown(self):
        print('Method teardown')

    @classmethod
    def tearDownClass(cls):
        print('Cls method teardown')


class TestAccountingTool2(unittest.TestCase):
# scenario with addition and deletion

    @classmethod
    def setUpClass(cls):
        print('Cls method setup')

    def setUp(self):
        print('Method setup')

    def test_add_new_doc(self):
        with unittest.mock.patch('builtins.input', return_value='a'):
            assert input() == 'a'
            self.assertEqual(add_new_doc('1111', 'SSN', 'Иван Иванов', '1'), '1')

    def test_delete_doc(self):
        with unittest.mock.patch('builtins.input', return_value='d'):
            assert input() == 'd'
            self.assertEqual(delete_doc('11-2'), ('11-2', True))

    def test_get_all_doc_owners_names(self):
        with unittest.mock.patch('builtins.input', return_value='ap'):
            assert input() == 'ap'
            self.assertEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Аристарх Павлов', 'Иван Иванов'})

    def test_get_doc_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='s'):
            assert input() == 's'
            self.assertEqual(get_doc_shelf('11-2'), 'No such document')

    def test_add_new_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='as'):
            assert input() == 'as'
            self.assertEqual(add_new_shelf('4'), ('4', True))

    def test_add_new_shelf_2(self):
        with unittest.mock.patch('builtins.input', return_value='as'):
            assert input() == 'as'
            self.assertEqual(add_new_shelf('3'), ('3', False))

    def tearDown(self):
        print('Method teardown')

    @classmethod
    def tearDownClass(cls):
        print('Cls method teardown')
