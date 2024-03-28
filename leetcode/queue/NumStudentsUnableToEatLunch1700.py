from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        iter_n = 0
        while True:
            length = len(students)
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                iter_n = 0

            else:
                student = students.pop(0)
                students.append(student)
                iter_n += 1

            if iter_n == len(students):
                return len(students)
            if len(sandwiches) == 0:
                break
        return 0
