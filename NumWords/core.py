import math
from typing import List, Tuple, Union # Union is already here

from .mappings import (
    DIGITS_WORDS_MAP,
    LARGE_NUMBERS,
    NUMBERS_WORDS_MAP,
    TENS_PLACE_MAP,
    WORD_TO_NUM_MAP,
    WORD_TO_LARGE_NUM_MAP,
)


class NumWords:
    @staticmethod
    def __get_number_limit() -> int:
        return 10**66 - 1

    @staticmethod
    def __convert_decimal_digits(val: str) -> str:
        digits = list(val)
        digit_str_list = [DIGITS_WORDS_MAP[digit] for digit in digits]
        return " ".join(digit_str_list)

    @staticmethod
    def __batches_to_words(batch: str) -> Tuple[str, str]:
        string = ""
        if len(batch) == 3 and batch[2] != "0":
            string += f"{DIGITS_WORDS_MAP[batch[2]]} hundred"
        if len(batch) >= 2 and batch[1] != "0":
            if 9 < int(batch[1::-1]) < 20:
                string += f" {NUMBERS_WORDS_MAP[batch[1::-1]]}"
            else:
                string += f" {TENS_PLACE_MAP[batch[1]]}"
        if len(batch) >= 1 and batch[0] != "0":
            if 9 < int(batch[1::-1]) < 20:
                pass
            else:
                string += f" {DIGITS_WORDS_MAP[batch[0]]}"
        return (batch[::-1], string)

    @staticmethod
    def convert_integers(value: int) -> str:
        limit = NumWords.__get_number_limit()
        sign_prefix = ""
        assert isinstance(value, int), "Invalid data type, expects int."

        if value > limit:
            raise ValueError(f"Value should not exceed {limit}")

        num_str = str(value)

        # Check if number is negative
        if num_str[0] == "-":
            num_str = num_str[1:]
            sign_prefix = "minus"

        num_str_rev = num_str[::-1]  # Reversing the number

        batches: List[str] = []  # batches of utmost three
        n_div = math.ceil(len(num_str_rev) / 3)
        for idx in range(n_div):
            batches.append(num_str_rev[idx * 3 : (idx + 1) * 3 :])

        counter = -1

        for batch in batches:
            batch_num, batch_str = NumWords.__batches_to_words(batch)
            if counter == -1:
                string = batch_str
            elif batch_num == "000":
                pass
            else:
                string = f"{batch_str} {LARGE_NUMBERS[counter]} {string}"
            counter += 1
        string = f"{sign_prefix} {' '.join(string.split())}"
        return string.strip().title()

    @staticmethod
    def convert_floats(value: float) -> str:
        assert isinstance(value, float), "Invalid data type, expects float."
        num_str = str(value)
        integer, decimal_digits = num_str.split(".")
        integer_str = NumWords.convert_integers(int(integer))
        decimal_digits_str = NumWords.__convert_decimal_digits(decimal_digits)
        if decimal_digits_str:
            result = f"{integer_str} point {decimal_digits_str}"
        else:
            result = integer_str
        return result.strip().title()

    @staticmethod
    def convert(value: Union[int, float, str]) -> Union[str, int]: # Changed return type here
        supported_types = (int, float, str)
        assert isinstance(
            value, supported_types
        ), f"Invalid data type, expects one of {supported_types}"

        if isinstance(value, str):
            value_str = value.replace(",", "")
            try:
                float_val = float(value_str)
                if "." in value_str or float_val != int(float_val):
                    value = float_val
                else:
                    value = int(float_val)
            except ValueError:
                return NumWords.__text_to_int(value_str) # Removed # type: ignore

        if isinstance(value, float):
            return NumWords.convert_floats(value)
        elif isinstance(value, int):
            return NumWords.convert_integers(value)
        else:
            # Fallback, though current logic should ensure value is int/float if not returned early
            # This path should ideally not be hit given the initial assertion and string processing.
            # If value was a non-numerical string not parsable by __text_to_int (if it raised error),
            # or if initial type was not int, float, str.
            # However, __text_to_int currently returns 0 for unparseable, not raises error.
            # And initial types are asserted.
            # If somehow value is still not int here (e.g. float from string "123.0" became int(123.0)),
            # this ensures it's treated as an integer for word conversion.
            return NumWords.convert_integers(int(value))


    @staticmethod
    def __text_to_int(words: str) -> int:
        words_processed = words.lower().strip()
        if not words_processed:
            return 0

        parts = words_processed.split()

        sign = 1
        if parts[0] == "minus":
            sign = -1
            parts = parts[1:]

        if not parts:
            return 0

        if len(parts) == 1 and parts[0] == "zero":
            return 0

        total_number = 0
        current_number = 0

        for part in parts:
            if part in WORD_TO_NUM_MAP:
                current_number += WORD_TO_NUM_MAP[part]
            elif part == "hundred":
                current_number = (current_number if current_number != 0 else 1) * 100
            elif part in WORD_TO_LARGE_NUM_MAP:
                large_num_val = WORD_TO_LARGE_NUM_MAP[part]
                total_number += (current_number if current_number != 0 else 1) * large_num_val
                current_number = 0
            else:
                # Ignoring unknown words
                pass

        total_number += current_number
        return sign * total_number
