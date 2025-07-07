
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Data Loading and Cleaning


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None


def clean_data(df):
    df_clean = df.dropna(subset=["age"])
    return df_clean

# Sorting and Saving


def sort_data(df, column):
    if column in df.columns:
        sorted_df = df.sort_values(by=column)
        sorted_df.to_csv("Lung Cancer.csv", index=False)
        print(
            f" Data sorted by '{column}' and saved as 'Lung Cancer.csv'.")
        return sorted_df
    else:
        print("Column not found.")
        return df

 # Summary Stats


def show_basic_stats(df):
    print("\n Summary Statistics:")
    print(df.describe())


def show_age_stats(df):
    if "age" in df.columns:
        print("\n Age Insights:")
        print("Average Age:", round(df["age"].mean(), 2))
        print("Min Age:", df["age"].min())
        print("Max Age:", df["age"].max())

# Visualizations


def plot_age_distribution(df):
    if "age" in df.columns:
        plt.hist(df["age"], bins=10, color='red', edgecolor='black')
        plt.title("Age Distribution of Cancer Patients")
        plt.xlabel("Age")
        plt.ylabel("Number of Patients")
        plt.show()


def plot_column_distribution(df, column):
    if column in df.columns:
        sns.countplot(data=df, x=column, palette="Set2")
        plt.title(f"{column} Distribution")
        plt.xticks(rotation=45)
        plt.show()

# Search and filter data


def filter_patients_by_age(df, age_limit):
    filtered = df[df["age"] > age_limit]
    print(f"\nFound {len(filtered)} patients older than {age_limit} years.")
    filtered.to_csv("patients_over_" + str(age_limit) + ".csv", index=False)
    print(" Filtered data saved.")


def search_by_keyword(df, column, keyword):
    if column in df.columns:
        results = df[df[column].astype(str).str.contains(
            keyword, case=False, na=False)]
        print(results)
    else:
        print("Column not found.")

# Main function


def main():
    file_path = input("Enter the CSV file name: ")
    df = load_data(file_path)
    if df is None:
        return

    df = clean_data(df)
    show_basic_stats(df)
    show_age_stats(df)

    # Sort Data
    column_to_sort = input(
        f"\nWhich column would you like to sort by? Options: {list(df.columns)}\n")
    df = sort_data(df, column_to_sort)

    # Visualize
    if input("\nDo you want to see an age distribution chart? (yes/no): ").lower() == "yes":
        plot_age_distribution(df)

    col_to_plot = input(
        "\nWhich column would you like to plot? (or type 'skip'): ")
    if col_to_plot.lower() != "skip":
        plot_column_distribution(df, col_to_plot)

    # Filter
    if input("\nDo you want to filter patients above a certain age? (yes/no): ").lower() == "yes":
        try:
            age_limit = int(input("Enter the age limit: "))
            filter_patients_by_age(df, age_limit)
        except ValueError:
            print("Invalid number.")

    # Search
    if input("\nDo you want to search for patients by keyword? (yes/no): ").lower() == "yes":
        col = input("Enter the column to search in (e.g., Name, Diagnosis): ")
        keyword = input("Enter keyword to search: ")
        search_by_keyword(df, col, keyword)

    print("\n Analysis complete. Goodbye!")


# entry point
if __name__ == "__main__":
    main()
