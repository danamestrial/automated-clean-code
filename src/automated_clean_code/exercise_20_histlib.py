# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
from typing import Dict


def hist_filler(string: str) -> Dict[str, int]:
    """Fill up a histogram.

    Args:
      string (str): a string to be stuffed into hist

    Returns:
      (Dict[str, int]). The filled hist.
    """
    counter = {}
    for line in string:
        line = line.strip()
        if line in counter:
            counter[line] += 1
        else:
            counter[line] = 1
    return counter


def find_min_max_key(hist: Dict[str, int]) -> (int, int):
    """Find min max key.

    Args:
      hist (str): a dict

    Returns:
      (int, int). tuple containing min/max
    """
    max_key, min_key = None, None
    max_counter, min_counter = 0, 0

    for k, v in hist.items():
        if max_key is None or v > max_counter:
            max_key = k
            max_counter = v
        if min_key is None or v < min_counter:
            min_key = k
            min_counter = v

    return max_key, min_key


def hist_lib(args: str) -> None:
    """To run main function.

    Args:
      args (str): a argument.

    Returns:
      None.
    """
    hist = hist_filler(args)
    (max_key, min_key) = find_min_max_key(hist)

    print(f"Min Key = {min_key} with count = {hist[min_key]} \nMax Key = {max_key} with count = {hist[max_key]}")
