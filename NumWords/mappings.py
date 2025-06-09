from typing import Dict, List

DIGITS_WORDS_MAP: Dict[str, str] = {
    "0": "zero", # Added zero for completeness, common in number parsing
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

NUMBERS_WORDS_MAP: Dict[str, str] = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}

TENS_PLACE_MAP: Dict[str, str] = {
    "2": "twenty", # tens map usually maps to the tens value, e.g. 20, 30
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}

LARGE_NUMBERS: List[str] = [
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
    "undecillion",
    "duodecillion",
    "tredecillion",
    "quattuordecillion",
    "quindecillion",
    "sexdecillion",
    "septendecillion",
    "octodecillion",
    "novemdecillion",
    "vigintillion",
]

# --- Inverse Mappings for text-to-number conversion ---

WORD_TO_NUM_MAP: Dict[str, int] = {
    "zero": 0, # from DIGITS_WORDS_MAP
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10, # from NUMBERS_WORDS_MAP
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20, # from TENS_PLACE_MAP
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}

WORD_TO_LARGE_NUM_MAP: Dict[str, int] = {
    "thousand": 1000,
    "million": 1_000_000,
    "billion": 1_000_000_000,
    "trillion": 1_000_000_000_000,
    "quadrillion": 1_000_000_000_000_000,
    "quintillion": 1_000_000_000_000_000_000,
    "sextillion": 1_000_000_000_000_000_000_000,
    "septillion": 1_000_000_000_000_000_000_000_000,
    "octillion": 1_000_000_000_000_000_000_000_000_000,
    "nonillion": 1_000_000_000_000_000_000_000_000_000_000,
    "decillion": 1_000_000_000_000_000_000_000_000_000_000_000,
    "undecillion": 1_000_000_000_000_000_000_000_000_000_000_000_000,
    "duodecillion": 1_000_000_000_000_000_000_000_000_000_000_000_000_000,
    "tredecillion": 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
    "quattuordecillion": 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
    "quindecillion": 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
    "sexdecillion": 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
    "septendecillion": 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
    "octodecillion": 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
    "novemdecillion": 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
    "vigintillion": 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
}