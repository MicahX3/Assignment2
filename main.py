"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return (annual_cost / SEMESTERS_PER_YEAR) / CLASS_DAYS_PER_SEMESTER


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return (annual_cost / SEMESTERS_PER_YEAR) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return (cost_per_credit(annual_cost, credits) * CS1430_CREDITS) / CS1430_MEETINGS_PER_SEMESTER


def cost_per_minute(annual_cost, credits):
    return (cost_per_class(annual_cost, credits) / 50)


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    cost = float(input("Total cost for one year: "))
    credits = int(input("Credits this semester: "))
    while True:
        # Show your menu here.
        print("THE COST OF COLLEGE")
        print("1 Per semester")
        print("2 Per month")
        print("3 Per class day")
        print("4 Per credit")
        print("5 Per CS 1430 class")
        print("6 Per minute")
        print("Q Quit")
        choice = input("Choose an option: ")


        if choice == "Q":
            break

        if choice == "1":
            print("One semester costs", f"${cost_per_semester(cost):,.2f}")

        if choice == "2":
            print("One month costs", f"${cost_per_month(cost):,.2f}")

        if choice == "3":
            print("One day costs", f"${cost_per_day(cost):,.2f}")

        if choice == "4":
            print("One credit costs", f"${cost_per_credit(cost,credits):,.2f}")

        if choice == "5":
            print("One class costs", f"${cost_per_class(cost,credits):,.2f}")

        if choice == "6":
            print("One minute costs", f"${cost_per_minute(cost,credits):,.2f}")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
