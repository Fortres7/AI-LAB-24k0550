def calculate_average(marks):
    total = 0
    count = 0
    for m in marks:
        total += m
        count = count + 1
    return total / count
  
marks = [70, 80, 90]
print("Marks:", marks)
print("Average Marks:", calculate_average(marks))
