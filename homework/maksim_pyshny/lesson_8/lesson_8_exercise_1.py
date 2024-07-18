import random


def calculate_salary_with_bonus(salary, bonus):
    if bonus:
        random_bonus = random.randrange(200, 2000)
        salary += random_bonus
    return salary


print('Какая у тебя зарплата?')

salary = int(input())
bonus = random.choice([True, False])

final_salary = calculate_salary_with_bonus(salary, bonus)

print(f'{salary}, {bonus} - ${final_salary}')
