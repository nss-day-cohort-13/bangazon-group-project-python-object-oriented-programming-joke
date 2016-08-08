import pickle

def serialize(data, filename):
    """
    Write data to a file

    Arguments:
        data:       the data to be written
        filename:   the file to write to
    """

    with open(filename, 'wb') as write_file:
        pickle.dump(data, write_file)


def deserialize(filename, fallback):
    """
    Read data from a file

    Arguments:
        filename:   the file to read
        fallback:   the data to use if read failue
    """

    try:
        with open(filename, 'rb') as read_file:
            return pickle.load(read_file)
    except (FileNotFoundError, EOFError):
        return fallback
