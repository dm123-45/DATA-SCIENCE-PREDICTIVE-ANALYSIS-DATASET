import pandas as pd
import pytest
from data_utils import filter_frame, numeric_columns, read_csv_bytes


def test_csv_load():
    frame = read_csv_bytes(b"name,score\nAda,5\nBob,8\n")
    assert frame.shape == (2, 2)
    assert numeric_columns(frame) == ["score"]


def test_empty_csv_rejected():
    with pytest.raises(ValueError, match="empty"):
        read_csv_bytes(b"")


def test_filter_and_missing_values():
    frame = pd.DataFrame({"group": ["A", "B", None], "score": [1, 2, 3]})
    assert len(filter_frame(frame, "group", ["A"])) == 1
    assert len(filter_frame(frame, None, [])) == 3


def test_categorical_only():
    frame = read_csv_bytes(b"name\nAda\nBob\n")
    assert numeric_columns(frame) == []
