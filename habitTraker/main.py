import pandas as  pd
from tabulate import tabulate
from datetime import datetime 
from habitTraker import traker_habit, Habit 


def main():
    habit: list[Habit] = [
        traker_habit("Coffe", datetime(2023, 3,3,3), cost=1, minutes_used=5)
    ]

    df = pd.DataFrame(habit)


    print(tabulate(df, headers="keys", tablefmt="psql"))



if __name__ == "__main__":
    main()
