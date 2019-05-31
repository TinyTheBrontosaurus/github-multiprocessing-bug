#! /usr/bin/env python3

from loguru import logger
import multiprocessing


def do_something(my_id, print_function):
    string_to_print = "my_id: {:6}, my_process: {}".format(my_id, multiprocessing.current_process())

    print(string_to_print)
    print_function(string_to_print)


def main():

    # Working in single-process
    for my_id in range(5):
        do_something(my_id, logger.info)

    # Failing in multiprocess.
    # (Nominally a Pool would be bigger t han size 1, but it simplified
    # the output to limit to a single process)
    with multiprocessing.Pool(1) as pool:
        for my_id in range(5):
            pool.apply_async(do_something, (my_id, logger.info))
        pool.close()
        pool.join()



if __name__ == "__main__":
    main()
