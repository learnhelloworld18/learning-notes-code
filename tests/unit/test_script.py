import pytest
import pandas as pd
from src.script import load_data, check_data

# Test load_data


@pytest.fixture
def dummy_csv(tmp_path):
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
    csv_path = tmp_path / "dummy.csv"
    df.to_csv(csv_path, index=False)
    return csv_path, df


def test_load_data_success(dummy_csv):
    csv_path, df = dummy_csv
    loaded = load_data(str(csv_path))
    assert isinstance(loaded, pd.DataFrame)
    assert loaded.equals(df)


def test_load_data_failure():
    # File does not exist
    df = load_data("nonexistent.csv")
    assert df is None


# Test check_data


def test_check_data_stats(dummy_csv, capsys):
    csv_path, df = dummy_csv
    result = check_data(df)
    out = capsys.readouterr().out
    assert "Data Statistics" in out
    assert "Dataset shape" in out
    assert "Missing values" in out
    assert isinstance(result, pd.DataFrame)


def test_check_data_fills_missing(dummy_csv, capsys):
    csv_path, df = dummy_csv
    df_missing = df.copy()
    df_missing.loc[0, "age"] = None
    result = check_data(df_missing)
    out = capsys.readouterr().out
    assert "Data Statistics" in out
    assert result.isnull().sum()["age"] > 0  # Should fill missing values
