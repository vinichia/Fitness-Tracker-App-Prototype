import random

// Fitness Tracker App Prototype

print("=== Fitness Tracker App Prototype ===\n")

exercicios = []
weekly_goal = 0

motivational_phrases = [
    "You are stronger than you think!",
    "Every workout is a step closer to your goals.",
    "Don't stop until you're proud.",
    "Giving up is not an option.",
    "Discipline is the bridge between goals and achievements."
]

def register_exercise():
    name = input("Exercise name: ")
    duration = int(input("Duration (min): "))
    calories = int(input("Calories burned: "))
    day = input("Day of the week: ")
    exercise = {"name": name, "duration": duration, "calories": calories, "day": day}
    exercicios.append(exercise)
    print("Exercise saved.\n")

def daily_report():
    day = input("Which day do you want to view? ")
    total_time = 0
    total_calories = 0
    for e in exercicios:
        if e["day"].lower() == day.lower():
            total_time += e["duration"]
            total_calories += e["calories"]
    print("Total time:", total_time, "min")
    print("Calories burned:", total_calories, "\n")

def calculate_bmi():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    bmi = weight / (height * height)
    if bmi < 18.5:
        print("BMI:", round(bmi, 2), "- Underweight\n")
    elif bmi < 25:
        print("BMI:", round(bmi, 2), "- Normal\n")
    elif bmi < 30:
        print("BMI:", round(bmi, 2), "- Overweight\n")
    else:
        print("BMI:", round(bmi, 2), "- Obesity\n")

def set_weekly_goal():
    global weekly_goal
    weekly_goal = int(input("Set your weekly calorie goal: "))
    print("Goal set!\n")

def check_goal():
    total = 0
    for e in exercicios:
        total += e["calories"]
    if total >= weekly_goal:
        print("You did it! Burned", total, "calories.\n")
    else:
        print("Goal not reached yet. Burned", total, "calories.\n")

def show_motivational_phrase():
    phrase = random.choice(motivational_phrases)
    print(phrase, "\n")

def average_calories():
    if len(exercicios) == 0:
        print("No exercises registered.\n")
    else:
        total = sum(e["calories"] for e in exercicios)
        average = total / len(exercicios)
        print("Average calories per exercise:", round(average, 2), "\n")

def barcode():
    for e in exercicios:
        bars = "|" * (e["calories"] // 10)
        print(e["name"], "[" + bars + "]", e["calories"], "cal")
    print()

def menu():
    while True:
        print("""
--- Menu ---
1 - Register exercise
2 - View daily report
3 - Calculate BMI
4 - Set weekly goal
5 - Check goal
6 - Motivational phrase
7 - Average calories
8 - Bar code
9 - Exit
        """)
        option = input("Choose an option: ")

        if option == "1":
            register_exercise()
        elif option == "2":
            daily_report()
        elif option == "3":
            calculate_bmi()
        elif option == "4":
            set_weekly_goal()
        elif option == "5":
            check_goal()
        elif option == "6":
            show_motivational_phrase()
        elif option == "7":
            average_calories()
        elif option == "8":
            barcode()
        elif option == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid option.\n")

menu()
