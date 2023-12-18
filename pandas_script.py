import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

filepath = r"C:\Users\user\Desktop\Python\Practice\dataset.csv"

df = pd.read_csv(filepath, delimiter = ";", names = ["Дата", "Курс"])

def delete_invalid(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    df = df.dropna()
    return df

def add_deviation(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    df["Mean"]=df["Курс"]-df["Курс"].mean()
    df["Median"]=df["Курс"]-df["Курс"].median()
    return df

def median_filtr(df, median):
    return df[df["Median"] > median]

def dates(df, date1, date2):
    date1, date2 = pd.to_datetime(date1), pd.to_datetime(date2)
    return df[(df["Дата"] > date1) & (df["Дата"] < date2)]

def week_course(df, date):
    p = df[(df["Дата"].dt.year == date.year) & (df["Дата"].dt.month == date.month)]
    p.plot(x = "Дата", y = "Курс")
    plt.show()

if __name__ == "__main__":

    filepath = r"C:\Users\user\Desktop\Python\Practice\dataset.csv"
    df = pd.read_csv(filepath, delimiter = ";", names = ["Дата", "Курс"])
    print(df)
    df["Дата"] = pd.to_datetime(df["Дата"], format = "%Y.%m.%d")
    df = delete_invalid(df)
    print(df)
    df = add_deviation(df)
    print(df)
    print(df[["Курс", "Mean", "Median"]].describe())
    df = median_filtr(df, 1.0)
    print(df)
    print(dates(df, date(2023, 7, 4), date(2023, 8, 4)))
    df_grouped = df.groupby([df['Дата'].dt.year, df['Дата'].dt.month])['Курс'].mean()
    print(df_grouped.tail(15))
    df_grouped.plot(kind='line', marker='o', figsize=(300, 300))

    plt.title('Средний курс по годам и месяцам')
    plt.xlabel('Год и месяц')
    plt.ylabel('Средний курс')
    plt.grid()

# Показать график
    plt.show()

    week_course(df, date(2023, 7, 1))

    
    
