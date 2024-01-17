from abc import ABC, abstractmethod

# Интерфейс работника
class Employee(ABC):
    @abstractmethod
    def earned_amount(self) -> int:
        pass

# Реализация дизайнера
class Designer(Employee):
    def __init__(self, name: str, salary: int, bonus: int = 0):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def earned_amount(self) -> int:
        return self.salary + self.bonus

    def do_design(self):
        print("Do Design")

# Реализация разработчика
class Developer(Employee):
    def __init__(self, name: str, salary: int, bonus: int = 0):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def earned_amount(self) -> int:
        return self.salary + self.bonus

    def do_developer(self):
        print("Do Developer")

# Реализация менеджера
class Manager(Employee):
    def __init__(self, name: str, salary: int, bonus: int = 0):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def earned_amount(self) -> int:
        return self.salary

# Компоновщик для команды
class TeamComposite(Employee):
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, employee: Employee):
        self.employees.remove(employee)

    def earned_amount(self) -> int:
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.earned_amount()
        return total_salary

# Пример использования
if __name__ == "__main__":
    designer1 = Designer("Designer 1", 50000, 2000)
    developer1 = Developer("Developer 1", 60000, 3000)
    manager1 = Manager("Manager 1", 70000, 4000)

    team = TeamComposite()
    team.add_employee(designer1)
    team.add_employee(developer1)
    team.add_employee(manager1)

    print(f"Total earned amount for the team: ${team.earned_amount()}")
