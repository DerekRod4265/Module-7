# 3 Variables with different data types with descriptive variable names #
person_name = "Derek Rodriguez"
age = 18
dae_student = True


# Python application that performs repeated tasks and decisions # 
def check_sport_category(sport):
    if sport.lower() == "football" or sport.lower() == "soccer":
        return "Outdoor sport"
    elif sport.lower() == "basketball":
        return "Indoor and outdoor sport"
    elif sport.lower() == "tennis":
        return "Outdoor sport"
    else:
        return "Unknown sport"

def main():
    print("Welcome to the Sport Categorizer!")

    choice = input("Do you want to categorize a sport? (yes/no): ")

    if choice.lower() == "yes":
        sport_name = input("Enter the name of the sport: ")

        sport_category = check_sport_category(sport_name)
        print("{} is categorized as: {}".format(sport_name, sport_category))
    else:
        print("Okay, goodbye!")

if __name__ == "__main__":
    main()


# A Python application that has at least one iterated list that includes accessed and used elements #						
def print_sports(sports):
    for sport in sports:
        print(sport)

def main():
    print("Welcome to the Sports Catalog!")

    sports = ["Football", "Basketball", "Tennis", "Cricket", "Baseball"]

    print("Available sports:")
    print_sports(sports)

if __name__ == "__main__":
    main()
