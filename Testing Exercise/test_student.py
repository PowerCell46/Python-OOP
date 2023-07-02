import unittest
from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.my_student = Student("Peter")

    def test_init_with_empty_courses(self):
        self.assertEqual(self.my_student.name, "Peter")
        self.assertEqual(self.my_student.courses, {})

    def test_init_with_courses(self):
        self.other_student = Student("Ivan", {"Python OOP": ["some note"], "C# Advanced": ["some note"]})
        self.assertEqual(self.other_student.name, "Ivan")
        self.assertEqual(self.other_student.courses, {"Python OOP": ["some note"], "C# Advanced": ["some note"]})

    def testing_enroll_method_with_new_course_and_empty_course_notes(self):
        self.assertEqual(self.my_student.enroll("Python OOP", ["Some notes"]), "Course and course notes have been added.")
        self.assertTrue("Some notes" in self.my_student.courses["Python OOP"])

    def testing_enroll_method_with_new_course_and_Y_course_notes(self):
        self.assertEqual(self.my_student.enroll("Python OOP", ["Some notes"], "Y"), "Course and course notes have been added.")
        self.assertTrue("Some notes" in self.my_student.courses["Python OOP"])

    def testing_enroll_method_with_already_added_course(self):
        self.my_student.enroll("Python OOP", ["Some notes"], "Y")
        self.assertEqual(self.my_student.enroll("Python OOP", ["Some new Notes", "Another new Note"],), "Course already added. Notes have been updated.")
        self.assertEqual("Some new Notes" in self.my_student.courses["Python OOP"], True)

    def testing_enroll_method_with_new_course_and_some_course_notes(self):
        self.assertEqual(self.my_student.enroll("JS Applications", ["Note"], "No"), "Course has been added.")
        self.assertEqual(len(self.my_student.courses["JS Applications"]), 0)

    def testing_add_notes_method_with_invalid_course(self):
        with self.assertRaises(Exception) as ex:
            self.my_student.add_notes("JS Applications", "Some random note")
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def testing_add_notes_method_with_valid_course(self):
        self.my_student.enroll("Python OOP", ["Some notes"], "Y")
        self.assertEqual(self.my_student.add_notes("Python OOP", "New Added Note"), "Notes have been updated")
        self.assertEqual("New Added Note" in self.my_student.courses["Python OOP"], True)

    def testing_leave_course_method_with_invalid_course(self):
        with self.assertRaises(Exception) as ex:
            self.my_student.leave_course("JS Applications")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")

    def testing_leave_course_with_valid_course(self):
        self.my_student.enroll("Python OOP", ["Some notes"], "Y")
        self.assertEqual(self.my_student.leave_course("Python OOP"), "Course has been removed")
        self.assertEqual(self.my_student.courses, {})

if __name__ == "__main__":
    unittest.main()