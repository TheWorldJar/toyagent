import unittest
from functions.get_files_content import get_file_content


class test_get_files_content(unittest.TestCase):
    def test_file(self):
        test_file = "main.py"
        test_work_dir = "calculator"
        test = get_file_content(test_work_dir, test_file)
        print(test)

    def test_nested_file(self):
        test_file = "pkg/calculator.py"
        test_work_dir = "calculator"
        test = get_file_content(test_work_dir, test_file)
        print(test)

    def test_error(self):
        test_file = "/bin/cat"
        test_work_dir = "calculator"
        test = get_file_content(test_work_dir, test_file)
        print(test)


if __name__ == "__main__":
    unittest.main()
