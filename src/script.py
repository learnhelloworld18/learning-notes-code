import pandas as pd


def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def check_data(data):
    """Check statistics and quality of the data."""
    print("\n=== Data Statistics ===")
    print(f"Dataset shape: {data.shape}")
    print(f"\nColumn names and types:\n{data.dtypes}")
    print(f"\nMissing values before fill:\n{data.isnull().sum()}")

    # Coerce 'age' to numeric if present
    if "age" in data.columns:
        data["age"] = pd.to_numeric(data["age"], errors="coerce")

    # Fill missing values in all numeric columns with their mean
    numeric_cols = data.select_dtypes(include="number").columns
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

    print(f"\nMissing values after fill:\n{data.isnull().sum()}")
    print(f"\nBasic statistics:\n{data.describe()}")
    print("\n" + "=" * 30 + "\n")
    return data


def main():
    # Load the dataset
    data = load_data("data.csv")

    # Display the statistics and quality of the data
    if data is not None:
        check_data(data)


if __name__ == "__main__":
    main()
