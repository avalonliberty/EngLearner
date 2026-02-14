import pytest
from datetime import date, timedelta

from englearner.core.fibonacci import (
    FIBONACCI_SEQUENCE,
    get_fibonacci_interval,
    calculate_next_review_date,
    advance_progress,
    reset_progress,
    is_completed,
)


class TestFibonacciSequence:
    def test_fibonacci_sequence_values(self):
        assert FIBONACCI_SEQUENCE == [1, 2, 3, 5, 8, 13, 21]

    def test_get_fibonacci_interval_day_1(self):
        assert get_fibonacci_interval(0) == 1

    def test_get_fibonacci_interval_day_2(self):
        assert get_fibonacci_interval(1) == 2

    def test_get_fibonacci_interval_day_3(self):
        assert get_fibonacci_interval(2) == 3

    def test_get_fibonacci_interval_day_5(self):
        assert get_fibonacci_interval(3) == 5

    def test_get_fibonacci_interval_day_8(self):
        assert get_fibonacci_interval(4) == 8

    def test_get_fibonacci_interval_day_13(self):
        assert get_fibonacci_interval(5) == 13

    def test_get_fibonacci_interval_day_21(self):
        assert get_fibonacci_interval(6) == 21

    def test_get_fibonacci_interval_invalid_negative(self):
        with pytest.raises(ValueError):
            get_fibonacci_interval(-1)

    def test_get_fibonacci_interval_invalid_too_high(self):
        with pytest.raises(ValueError):
            get_fibonacci_interval(7)


class TestCalculateNextReviewDate:
    def test_calculate_next_review_date_day_1(self):
        base_date = date(2026, 2, 15)
        result = calculate_next_review_date(0, base_date)
        assert result == date(2026, 2, 16)

    def test_calculate_next_review_date_day_2(self):
        base_date = date(2026, 2, 15)
        result = calculate_next_review_date(1, base_date)
        assert result == date(2026, 2, 17)

    def test_calculate_next_review_date_day_3(self):
        base_date = date(2026, 2, 15)
        result = calculate_next_review_date(2, base_date)
        assert result == date(2026, 2, 18)

    def test_calculate_next_review_date_default_today(self):
        result = calculate_next_review_date(0)
        expected = date.today() + timedelta(days=1)
        assert result == expected


class TestAdvanceProgress:
    def test_advance_from_day_1_to_day_2(self):
        assert advance_progress(0) == 1

    def test_advance_from_day_2_to_day_3(self):
        assert advance_progress(1) == 2

    def test_advance_from_day_3_to_day_5(self):
        assert advance_progress(2) == 3

    def test_advance_from_day_21_completes(self):
        assert advance_progress(6) == -1


class TestResetProgress:
    def test_reset_returns_zero(self):
        assert reset_progress() == 0


class TestIsCompleted:
    def test_not_completed_at_day_1(self):
        assert is_completed(0) is False

    def test_not_completed_at_day_13(self):
        assert is_completed(5) is False

    def test_completed_at_day_21(self):
        assert is_completed(6) is True
