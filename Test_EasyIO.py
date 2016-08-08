import unittest
import pickle

from easy_io import *

class TestEasyIO(unittest.TestCase):

    def test_serialize(self):
        filename = 'testfile_io.dat'

        data = [1, 'b', ['a', 'list']]
        serialize(data, filename)

        with open(filename, 'rb') as read_file:
            test_read = pickle.load(read_file)
            self.assertEqual(test_read, data)

    def test_deserialize_no_file(self):
        pass

    def test_deserialize_existing(self):
        pass


if __name__ == '__main__':
    unittest.main()
