import math
from typing import List, Tuple, Union

from .mappings import DIGITS_WORDS_MAP, LARGE_NUMBERS, NUMBERS_WORDS_MAP, TENS_PLACE_MAP


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
        assert isinstance(value, int), "Invalid data type, expects int."

        if value > limit:
            raise ValueError(f"Value should not exceed {limit}")

        num_str = str(value)
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
        string = " ".join(string.split())
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
    def convert(value: Union[int, float, str]) -> str:
        supported_types = (int, float, str)
        assert isinstance(
            value, supported_types
        ), f"Invalid data type, expects one of {supported_types}"
        if isinstance(value, str):
            value = value.replace(",", "")
            if "." in value:
                value = float(value)
            else:
                value = int(value)

        if isinstance(value, float):
            return NumWords.convert_floats(value)
        else:
            return NumWords.convert_integers(value)
