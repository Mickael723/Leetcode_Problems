from collections import deque
class Solution:
    def countStudents(self, students: list, sandwiches: list) -> int:

        student_q = deque(students)
        sandwich_stack = deque(sandwiches)
        num_iterations = 0

        while student_q and sandwich_stack and num_iterations <= len(sandwiches):

            front = student_q.popleft()
            curr_sand = sandwich_stack[0]

            if front != curr_sand:
                student_q.append(front)
                num_iterations += 1
            else:
                sandwich_stack.popleft()
                num_iterations = 0
        
        return len(student_q)

if __name__=="__main__":
    s = Solution()
    print(s.countStudents([1,1,0,0], [0,1,0,1]))
    print(s.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))