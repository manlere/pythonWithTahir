food = "supergetti and beans"
print(food.upper())
print(food.split())
print(food.strip())
print(food.count("e"))
print(list(food))
print(food.capitalize())
print(food.casefold())
print(food.endswith("w"))
print(food.isalpha())
print(food.isalnum())

team = "Atletico Madrid"
coach = "######Deigo Simone######"
players = "Oblack, Savic, Morata, Saul, Koke"
print(players.replace("Morata","Abuluhameed"))
print(coach.strip("#"))
print(team.join(coach))
print(team.title())
print(coach.translate(coach))
print(players.zfill(0))
print(team.startswith("A"))
print(team.endswith("i"))
print(team.splitlines(5))
print(players.isprintable())

school = "Dahir Muhammad Dahir University, Zaria"
course = "python"
year = "2019"
print(school.isupper())
print(course.islower())
print(year.isnumeric())
print(year.isdigit())
print(year.isdecimal())
print("{}".format(school,course))