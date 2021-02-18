"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730342554"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    target_two: str = str(target)
    # TODO 2: Call days_to_target and store result in a variable.
    """Our target date"""
    remain: int = str(days_to_target(population, doses, doses_per_day, target))
    # TODO 4: Call future_date and store result in a variable.
    future: int = int(remain)
    date_future: int = str(future_date(future))
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + target_two + "% vaccination in " + remain + " days, which falls on " + date_future + ".")


# TODO 1: Define days_to_target function
"""how many days until we reach the targeted percent of the population"""
def days_to_target(population, doses, doses_per_day, target):
    VACC_CURRENT_DATE: int = int(doses_per_day/ 2)
    POP_PERCENT_DECI: float = float(target / 100)
    VACC_NEEDED: float = float(population * POP_PERCENT_DECI)
    REMAINDER_VACC: float = float(VACC_NEEDED - VACC_CURRENT_DATE)
    DAYS_GOAL_REACHED: float = float(( 2 * REMAINDER_VACC) / doses_per_day)
    ROUND_DAYS: int = int(round(DAYS_GOAL_REACHED))
    DAY_REACHED: str = int(ROUND_DAYS)
    return(DAY_REACHED)


# TODO 3: Define future_date function
"""the day our goal is met"""
def future_date(future):
    today: datetime = datetime.today()
    day: timedelta = today + timedelta(future)
    date: datetime = day.strftime("%B %d, %Y")
    return(date)


if __name__ == "__main__":
    main()

