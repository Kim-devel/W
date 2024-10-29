grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Упорядочиваем множество студентов в алфавитном порядке
students_list = sorted(students)

# Создаем словарь, где ключ — имя студента, а значение — его средний балл
average_grades = {
    student: sum(grades[i]) / len(grades[i])  # Вычисляем средний балл для каждого студента
    for i, student in enumerate(students_list)  # Используем enumerate для получения индексов и имен студентов
}

print(average_grades)
