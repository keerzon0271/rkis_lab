class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

sessions = [
    FitnessCenter("C001", 2022, 1, 60),
    FitnessCenter("C002", 2022, 2, 45),
    FitnessCenter("C003", 2023, 1, 90),
    FitnessCenter("C004", 2023, 2, 30),
    FitnessCenter("C005", 2023, 3, 120),
    FitnessCenter("C006", 2023, 4, 60),
    FitnessCenter("C007", 2024, 1, 45),
    FitnessCenter("C008", 2024, 2, 90),
    FitnessCenter("C009", 2024, 3, 60),
    FitnessCenter("C010", 2024, 4, 30)
]

from collections import defaultdict

yearly_duration = defaultdict(int)
for session in sessions:
    yearly_duration[session.year] += session.duration

max_year = min(
    [year for year, duration in yearly_duration.items() if duration == max(yearly_duration.values())]
)

max_duration = yearly_duration[max_year]

print("Год с наибольшей суммарной продолжительностью:", max_year)
print("Суммарная продолжительность:", max_duration)