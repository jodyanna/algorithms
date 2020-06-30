
import maker
import sort
import logging


def main():
    numbers = maker.Maker.create_array_random_int(1000, 0, 100)

    print(numbers, "\n")
    leet = sort.Sort()
    numbers = leet.merge_sort_top_down(numbers)
    print(numbers)


def setup_logger(method_name):
    logger = logging.getLogger(method_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

    file_handler = logging.FileHandler('sorter.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


main()
