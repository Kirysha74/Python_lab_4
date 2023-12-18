from datetime import date

import matplotlib.pyplot as plt
import pandas as pd


def delete_invalid(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    df = df.dropna()
    return df

def add_deviation(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    df["Deviation from the mean"]=df["Rate"]-df["Rate"].mean()
    df["Deviation from the median"]=df["Rate"]-df["Rate"].median()
    return df

def median_filter(df: pd.core.frame.DataFrame, median: float) -> pd.core.frame.DataFrame:
    return df[df["Deviation from the median"] > median]

def filter_by_dates(df: pd.core.frame.DataFrame, early_date: str | date, late_date: str | date) -> pd.core.frame.DataFrame:
    early_date, late_date = pd.to_datetime(early_date), pd.to_datetime(late_date)
    return df[(df["Date"] >= early_date) & (df["Date"] <= late_date)]

def course_per_month(df: pd.core.frame.DataFrame, date: date) -> None:
    p = df[(df["Date"].dt.year == date.year) & (df["Date"].dt.month == date.month)]
    p.plot(x = "Date", y = "Rate", marker='o')
    plt.show()

if __name__ == "__main__":

    filepath = r"C:\Users\user\Desktop\Python\Lab_1\Python_lab_1\dataset.csv"
    df = pd.read_csv(filepath, delimiter = ",", names = ["Date", "Rate"])

    print(df)
    df["Date"] = pd.to_datetime(df["Date"])
    df = delete_invalid(df)
    print(df)
    df = add_deviation(df)
    print(df)
    print(df[["Rate", "Deviation from the mean", "Deviation from the median"]].describe())
    df = median_filter(df, 1.0)
    print(df)
    print(filter_by_dates(df, date(2023, 7, 4), date(2023, 8, 4)))
    df_grouped = df.groupby([df['Date'].dt.year, df['Date'].dt.month])['Rate'].mean()
    df_grouped.plot(kind='line', marker='o', figsize=(300, 300))

    plt.title('Средний курс по годам и месяцам')
    plt.xlabel('Год и месяц')
    plt.ylabel('Средний курс')
    plt.grid()
    plt.show()

    course_per_month(df, date(2022, 2, 1))

    
    
