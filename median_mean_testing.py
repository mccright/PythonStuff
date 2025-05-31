import datetime
from zoneinfo import ZoneInfo
import statistics

def are_list_elements_numbers(list):
    """
    DESCRIPTION: Check if list contains only numbers.
    INPUT:
    OUTPUT:
    """
    for item in list:
        return_value: bool = ""
        if isinstance(item, int):
            return_value = True
        elif isinstance(item, float):
            return_value = True
        else:
            return False
    if return_value == True:
        return True
    
def get_median_with_statistics(list):
    return statistics.median(list)

def get_median_with_code(list):
    """
    DESCRIPTION: 
    Calculate the median as described in https://en.wikipedia.org/wiki/Median
    Model from: https://www.codingem.com/python-calculate-median/
    Function steps:
    1. Accept a list as input.
    2. Sorts the list.
    3. If the list length is odd.
        a. Get the mid-value, then return it.
    4. If the list length is even.
        b. Get the two middle values, calculate their average, then return that.
	INPUT: list
	RETURN: value
	"""
    sorted_list = sorted(list)
    list_length = len(sorted_list)
    middle = (list_length - 1) // 2
    if middle % 2:
        return sorted_list[middle]
    else:
        return (sorted_list[middle] + sorted_list[middle + 1]) / 2.0

def get_average_with_code(list):
    return sum(list) / len(list)

def get_average_with_statistics(list):
    return statistics.mean(list)


if __name__ == '__main__':
# Example usage:
    # numbers = [1, 2, 3, 4, 5, 6, 7]
    # numbers = ["a", 1, 2.2, 3.14, 4, 5, 6, 7]
    # numbers = [1, 4, 3, 2, 1, 3, 7, 1, 4, 1]
    # numbers = [1, 1024, 4, 3, 2, 1, 3, 7, 1, 4, 1]
    numbers = [1, 61, 2, 127, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1024]
    # numbers = [55251, 59, 18, 63, 34, 17, 17, 48, 26, 16, 38, 21, 22, 50, 45, 12, 10, 8, 58, 15, 3, 56, 33, 4, 47, 36, 26, 51, 65, 8, 33, 70, 39, 34, 35, 2, 44, 1, 55, 31, 61, 3, 19, 45, 39, 28, 35, 23, 18, 6, 61, 5, 4, 14, 26, 57, 41, 22, 4, 18, 24, 28, 58, 52, 61, 6, 49, 57, 51, 10, 19, 6, 34, 40, 19, 55, 32, 14, 67, 47, 6, 25, 32, 21, 419, 228, 47, 186, 245, 284, 583, 522, 611, 60, 499, 578, 517, 106, 195, 64, 343, 402, 191, 155, 332]
    # numbers = ["a", "b", "c", "d", "e", "f"]
    if (are_list_elements_numbers(numbers)) == True:
        us_central_dt = datetime.datetime.now(tz=ZoneInfo("America/Chicago")).strftime('%Y-%m-%d %I:%M:%S%P %Z')
        print(f"Test run at: {us_central_dt}")
        # print(f"{datetime.datetime.today().strftime('%Y-%m-%d %I:%M:%S%P %Z')}")
        average = get_average_with_code(numbers)
        print(f"list = {numbers}")
        print(f"The list contains {len(numbers)} elements")
    
        median = get_median_with_code(numbers)
        print(f"median value using code =       {median:.2f}")
        median = get_median_with_statistics(numbers)
        print(f"median value using statistics = {median:.2f}")

        average = get_average_with_code(numbers)
        print(f"average value using code =       {average:.2f}")
        average = get_average_with_statistics(numbers)
        print(f"average value using statistics = {average:.2f}")
    else:
        print(f"Something went wrong.  Your list must contain only int and/or float elements.\r\nThe list = {numbers}")
