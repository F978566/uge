#Сколько существует программ, для которых при исходном числе 1 результатом является число 17 и при этом траектория вычислений содержит число 9

def task_23(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1

    return task_23(a+1, b) + task_23(a+3, b)

print(task_23(1, 9)*task_23(9, 17))