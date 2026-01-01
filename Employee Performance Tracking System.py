
print("ابدأ البرنامج - نظام وسام (متابعة الأداء)")

import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

print("ابدأ البرنامج - نظام وسام (متابعة الأداء)")

# =========================
# كلاس النظام الرئيسي
# =========================
class PerformanceSystem:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

# =========================
# كلاس الموظف
# =========================
class Employee:
    def __init__(self, name, section):
        self.name = name
        self.section = section
        self.goal_list = []

    def add_goal(self, goal):
        self.goal_list.append(goal)

# =========================
# كلاس الهدف
# =========================
class Goal:
    def __init__(self, goal_name, start_date):
        self.goal_name = goal_name
        self.start_date = start_date
        self.tasks_list = []

    def add_task(self, task):
        self.tasks_list.append(task)

    def completion_percentage(self):
        total = len(self.tasks_list)
        completed = sum(1 for t in self.tasks_list if t.status == "complete")
        return (completed / total) * 100 if total > 0 else 0

# =========================
# كلاس المهمة
# =========================
class Task:
    def __init__(self, name_task):
        self.name_task = name_task
        self.status = "uncomplete"

    def finish_task(self):
        self.status = "complete"

# =========================
# كلاس التقرير
# =========================
class Report:
    def __init__(self, report_date):
        self.report_date = report_date

    def save_data(self, system):
        with open("employees.csv", "w", encoding="utf-8") as file:
            for emp in system.employee_list:
                file.write(f"{emp.name},{emp.section}\n")
                for goal in emp.goal_list:
                    file.write(f"  Goal: {goal.goal_name},{goal.start_date}\n")
                    for task in goal.tasks_list:
                        file.write(f"    Task: {task.name_task},{task.status}\n")

    def progress_chart(self, system):
        plt.figure(figsize=(12,6))
        for emp in system.employee_list:
            target_names = [goal.goal_name for goal in emp.goal_list]
            completion_rates = [goal.completion_percentage() for goal in emp.goal_list]

            reshaped_goals = [get_display(arabic_reshaper.reshape(g)) for g in target_names]
            plt.bar(reshaped_goals, completion_rates, label=emp.name)

        plt.ylim(0, 100)
        plt.xlabel(get_display(arabic_reshaper.reshape("الأهداف")))
        plt.ylabel(get_display(arabic_reshaper.reshape("نسبة الإنجاز")))
        plt.title(get_display(arabic_reshaper.reshape("تقدم الأهداف لكل الموظفين")))
        plt.xticks(rotation=25)
        plt.legend()
        plt.show()


# =========================
# تشغيل البرنامج
# =========================
system = PerformanceSystem()

# إنشاء موظفين
emp1 = Employee("وسام", "IT")
emp2 = Employee("ليلى", "HR")

system.add_employee(emp1)
system.add_employee(emp2)

# إنشاء أهداف لكل موظف
goal1 = Goal("تعلم بايثون", "2024-04-01")
goal2 = Goal("مشروع عملي", "2024-04-05")

goal3 = Goal("تطوير مهارات", "2024-04-02")
goal4 = Goal("تحديث قاعدة البيانات", "2024-04-07")

# إنشاء مهام للموظف 1
task1 = Task("OOP Basics")
task2 = Task("File Handling")
task1.finish_task()  # مكتملة
goal1.add_task(task1)
goal1.add_task(task2)
goal2.add_task(Task("عمل التقرير"))

emp1.add_goal(goal1)
emp1.add_goal(goal2)

# إنشاء مهام للموظف 2
t3 = Task("تدريب الموظفين")
t4 = Task("تحديث السياسات")
t3.finish_task()
t4.finish_task()
goal3.add_task(t3)
goal4.add_task(t4)

emp2.add_goal(goal3)
emp2.add_goal(goal4)

# إنشاء تقرير وحفظ البيانات
report = Report("2024-04-30")
report.save_data(system)

# رسم التقدم لجميع الموظفين
report.progress_chart(system)
