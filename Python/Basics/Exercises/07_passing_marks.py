# Task: Compare the average marks to a passing marks (say 40)
# Use comparison and logical operators to print if the student passed

math = 78
science = 89
english = 92

passing_marks = 40
# Print: Did student pass all subjects? True/False

passed_all = math >= passing_marks and science >= passing_marks and english >= passing_marks
print(f"Did the student pass all subjects? {passed_all}")


average_marks = (math + science + english) / 3
print(f"Average Marks: {average_marks:.2f}")
print(f"Passed based on average? {average_marks >= passing_marks}")
