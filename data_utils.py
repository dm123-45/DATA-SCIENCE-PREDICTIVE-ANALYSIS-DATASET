"""Pure data helpers shared by the dashboard and automated tests."""
import io
import pandas as pd

MAX_UPLOAD_BYTES = 20 * 1024 * 1024


def read_csv_bytes(data: bytes) -> pd.DataFrame:
    if not data:
        raise ValueError("The uploaded file is empty.")
    if len(data) > MAX_UPLOAD_BYTES:
        raise ValueError("File exceeds the 20 MB upload limit.")
    try:
        frame = pd.read_csv(io.BytesIO(data), low_memory=False)
    except (UnicodeError, pd.errors.ParserError, pd.errors.EmptyDataError) as exc:
        raise ValueError(f"Unable to read CSV: {exc}") from exc
    if frame.columns.empty:
        raise ValueError("No columns detected.")
    frame.columns = [str(col) for col in frame.columns]
    return frame


def filter_frame(frame: pd.DataFrame, column: str | None, values: list[str]) -> pd.DataFrame:
    if not column or not values:
        return frame.copy()
    if column not in frame.columns:
        raise ValueError("Unknown filter column.")
    return frame.loc[frame[column].astype("string").isin(values)].copy()


def numeric_columns(frame: pd.DataFrame) -> list[str]:
    return frame.select_dtypes(include="number").columns.tolist()
