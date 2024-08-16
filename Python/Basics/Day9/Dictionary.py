# dict = {
#     "adobe photoshop" : "Photo editing",
#     "Adobe primer": "video editing",
#     "Adobe xd": "uiux"
# }
# for key in dict:
#     print(key)
#     print(dict[key])

# print(dict["Adobe xd"])


# student_scores = {
#     "Azan": 93,
#     "Ali": 83,
#     "Azam": 72,
#     "Azani": 63,
#     "Azlan": 50
# }

# student_grades = {}
# def grade():
#     if scores > 85:
#      student_grades[student] = "A"
#     elif scores > 80:
#      student_grades[student] = "A-" 
#     elif scores > 75:
#       student_grades[student] = "B+"
#     elif scores > 70:
#       student_grades[student] = "B"
#     elif scores >65 :
#      student_grades[student] = "B-"
#     elif scores > 60:
#      student_grades[student] = "C+" 
#     elif scores > 55:
#       student_grades[student] = "C"
#     elif scores >= 50:
#        student_grades[student] = "D"
#     else:
#        print("Fail")


# for student in student_scores:
#    scores = student_scores[student]
#    grade()
# for i in student_grades:
#     print(i, end= " ")
#     print(student_grades[i])


# #nesting
travel_log =[
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "lilli", "Djlon"]
},
{
    "country": "Pakistan",
    "visits": 15,
    "cities": ["lahore", "karachi", "islambad"]
}
]

def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

add_new_country("India", 2, ["Delhi", "Mumbai", "Kolkata"])
for i in travel_log:
   print(i)