import math

# Исходные данные
movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# Этап 1. Разминка: переменные, числа, math


def average_rating(movies_list):
    """Возвращает среднюю оценку по каталогу, округленную до одного знака."""
    if not movies_list:
        return 0.0
    total_rating = sum(movie["rating"] for movie in movies_list)
    return round(total_rating / len(movies_list), 1)


def catalog_age_stats(movies_list, current_year=2026):
    """Возвращает кортеж: (старый, новый, средний возраст через ceil)."""
    if not movies_list:
        return (0, 0, 0)

    ages = [current_year - movie["year"] for movie in movies_list]
    oldest_age = max(ages)
    newest_age = min(ages)
    avg_age = math.ceil(sum(ages) / len(ages))

    return (oldest_age, newest_age, avg_age)


def duration_in_hours(minutes):
    """Переводит минуты в формат '2ч 35м' с помощью // и %."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

# Этап 2. Условия и match


def rating_tier(rating):
    if rating >= 7.0:
        return "шедевр" if rating >= 9.0 else "хорошо"
    elif rating >= 5.0:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"

# Этап 3. Циклы

for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(movies[i]["title"])
        break
    i += 1
else:
    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

# Этап 4. Строки


def normalize_title(title):
    words = title.split()
    capitalized_words = [
        word[0].upper() + word[1:] if word else "" for word in words
    ]
    return " ".join(capitalized_words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    hours, minutes = duration_in_hours(movie["duration_min"])
    genres_str = ", ".join(sorted(movie["genres"]))
    return (
        f'"{movie["title"]}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {hours}ч {minutes}м, жанры: {genres_str}'
    )