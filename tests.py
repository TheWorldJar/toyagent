import unittest
from functions.get_files_info import get_files_info


class test_get_files_info(unittest.TestCase):
    def test_local_outside_of_work(self):
        test_dir = "."
        test_work_dir = "calculator"
        expected = f'Error: Cannot list "{test_dir}" as it is outside the permitted working directory'
        self.assertEqual(get_files_info(test_work_dir, test_dir), expected)

    def test_work_is_dir(self):
        test_dir = "calculator"
        test_work_dir = "calculator"
        expected = "tests.py: file_size=1343 bytes, is_dir=False\nmain.py: file_size=576 bytes, is_dir=False\npkg: file_size=160 bytes, is_dir=True"
        self.assertEqual(get_files_info(test_work_dir, test_dir), expected)

    def test_sub_in_work(self):
        test_dir = "pkg"
        test_work_dir = "calculator"
        expected = "render.py: file_size=768 bytes, is_dir=False\n__pycache__: file_size=128 bytes, is_dir=True\ncalculator.py: file_size=1739 bytes, is_dir=False"
        self.assertEqual(get_files_info(test_work_dir, test_dir), expected)

    def test_root_outside_of_work(self):
        test_dir = "/bin"
        test_work_dir = "calculator"
        expected = f'Error: Cannot list "{test_dir}" as it is outside the permitted working directory'
        self.assertEqual(get_files_info(test_work_dir, test_dir), expected)

    def test_parent_outside_work(self):
        test_dir = "../"
        test_work_dir = "calculator"
        expected = f'Error: Cannot list "{test_dir}" as it is outside the permitted working directory'
        self.assertEqual(get_files_info(test_work_dir, test_dir), expected)

    def test_dir_is_file(self):
        test_dir = "tests.py"
        test_work_dir = "calculator"
        expected = f'Error: "{test_dir}" is not a directory'
        self.assertEqual(get_files_info(test_work_dir, test_dir), expected)

    def test_only_working(self):
        test_work_dir = "calculator"
        expected = "tests.py: file_size=1343 bytes, is_dir=False\nmain.py: file_size=576 bytes, is_dir=False\npkg: file_size=160 bytes, is_dir=True"
        self.assertEqual(get_files_info(test_work_dir), expected)


if __name__ == "__main__":
    unittest.main()
