from datetime import date, timedelta
from typing import List


FIBONACCI_SEQUENCE: List[int] = [1, 2, 3, 5, 8, 13, 21]


def get_fibonacci_interval(day_index: int) -> int:
    """Get the interval in days for the given Fibonacci index."""
    if day_index < 0 or day_index >= len(FIBONACCI_SEQUENCE):
        raise ValueError(
            f"Invalid day_index: {day_index}. Must be between 0 and {len(FIBONACCI_SEQUENCE) - 1}"
        )
    return FIBONACCI_SEQUENCE[day_index]


def calculate_next_review_date(current_day_index: int, base_date: date = None) -> date:
    """Calculate the next review date based on current Fibonacci index."""
    if base_date is None:
        base_date = date.today()

    interval = get_fibonacci_interval(current_day_index)
    return base_date + timedelta(days=interval)


def advance_progress(current_day_index: int) -> int:
    """Advance to the next Fibonacci interval. Returns new index or -1 if completed."""
    if current_day_index >= len(FIBONACCI_SEQUENCE) - 1:
        return -1
    return current_day_index + 1


def reset_progress() -> int:
    """Reset progress to day 1 (index 0)."""
    return 0


def is_completed(current_day_index: int) -> bool:
    """Check if the vocabulary has completed all review levels."""
    return current_day_index >= len(FIBONACCI_SEQUENCE) - 1
