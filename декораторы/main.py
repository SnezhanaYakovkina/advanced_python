from app import file as f
from datetime import datetime
import os


def parametrized_logger(file_path):
    call_qty = 0

    def logger(func):
        def new_func(*args, **kwargs):
            nonlocal call_qty
            call_qty += 1
            result = func(*args, **kwargs)
            now = datetime.now()
            if os.path.exists(file_path):
                f_mode = 'a'
            else:
                f_mode = 'w'
            with open(file_path, f_mode, encoding='utf-8') as file:
                file.write(
                    f'{call_qty} | Дата и время:{now} | Имя: {func.__name__} | Аргументы: {args, kwargs} | '
                    f'Возвращаемое значение: {result} \n'
                )
            return result

        return new_func

    return logger


@parametrized_logger('logs.txt')
def calculate_salary(employees, months):
    return sum([e['salary'] * months for e in employees])


if __name__ == '__main__':
    calculate_salary(f.get_employees(), 4)
    calculate_salary(f.get_employees(), 1)
    calculate_salary(f.get_employees(), 7)
