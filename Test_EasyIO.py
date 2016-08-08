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
        filename = 'testfile_io.dat'

        data = [2, 'c', ['a', 'different', 'list']]
        with open(filename, 'wb') as write_file:
            pickle.dump(data, filename)

        read_data = deserialize(filename, [None])
        self.assertEqual(read_data, data)

    def test_deserialize_existing(self):
        filename = 'no_file.dat'
        fallback = [None]

        read_data = deserialize(filename, fallback)
        self.assertEqual(read_data, fallback)


if __name__ == '__main__':
    unittest.main()
