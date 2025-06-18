class Task:
    def __init__(self, date_start, date_finish, description):
        self.DateStart = date_start
        self.DateFinish = date_finish
        self.Description = description

    def __repr__(self):
        return f"Task(Description='{self.Description}', Start={self.DateStart}, Finish={self.DateFinish})"

tasks = [
    Task("2025-10-01 09:00", "2025-10-01 10:30", "Встреча с клиентом"),
    Task("2025-10-01 11:00", "2025-10-01 12:00", "Обед"),
    Task("2025-10-01 13:00", "2025-10-01 15:30", "Презентация"),
    Task("2025-10-01 16:00", "2025-10-01 18:00", "Совещание"),
    Task("2025-10-01 14:00", "2025-10-01 17:00", "Работа над проектом")
]

latest_task = max(tasks, key=lambda task: task.DateFinish)

print("Занятие, заканчивающееся позже всех:", latest_task)
