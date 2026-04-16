import unittest

class TestViewStudents(unittest.TestCase):

    def setUp(self):
        self.students = []  # This will be the list to test against.

    def test_view_students_empty(self):
        # Test when there are no students
        result = view_students(self.students)
        self.assertEqual(result, [])  # expecting an empty list

    def test_view_students_non_empty(self):
        # Test when there are some students
        self.students = ["Alice", "Bob", "Charlie"]
        result = view_students(self.students)
        self.assertEqual(result, self.students)  # expecting the same list

if __name__ == '__main__':
    unittest.main()