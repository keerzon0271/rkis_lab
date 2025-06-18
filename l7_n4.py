class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

    def __repr__(self):
        return f"FitnessCenter(Client={self.client_code}, Year={self.year}, Month={self.month}, Duration={self.duration})"

sessions = [
    FitnessCenter("C001", 2023, 1, 45),
    FitnessCenter("C002", 2023, 2, 30),
    FitnessCenter("C003", 2023, 3, 60),
    FitnessCenter("C004", 2023, 4, 90),
    FitnessCenter("C005", 2023, 5, 20)
]

longest_session = max(sessions, key=lambda x: x.duration)
shortest_session = min(sessions, key=lambda x: x.duration)

print("Самое продолжительное занятие:", longest_session)
print("Самое короткое занятие:", shortest_session)