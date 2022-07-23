from random import choice, randint
import time


def get_id(in_line: str) -> int:
    """
    This function return ID from given line
    :param in_line: input line
    :return: id
    """
    # Extract elements
    element_list = in_line.split(",")
    element_id = element_list[0]
    id_structure = element_id.split(":")
    id_element = id_structure[0]
    return int(id_element)


def print_result(elements: list) -> None:
    """
    This function returns new ID
    :param elements: input list of IDs
    :return: none
    """
    print(f"Element list: {','.join(str(x) for x in elements)}")

    new_id = choice([i for i in range(1000, 9999) if i not in elements])
    print(
        f"Random id number {new_id} not in {elements} -> {new_id not in elements} "
    )


def run_lazy() -> None:
    """
    Main executable code in lazy way
    :return:
    """
    id_list = []

    # This is first method, for lazy, but not good for education
    # and not good for reading
    with open("customer.txt") as fp:
        for line in fp:
            if line.strip() != "":
                id_list.append(int(line.split(",")[0].split(":")[0]))
    print_result(id_list)


def run_right() -> None:
    """
    Main executable code in academic way
    :return:
    """
    id_list = []

    # This is more educational method

    with open("customer.txt") as fp:
        for line in fp:
            if line.strip() != "":
                id_list.append(get_id(line))
    print_result(id_list)


if __name__ == "__main__":
    lazy_time = time.process_time()
    run_lazy()
    print(f">>>> Execution time of lazy {time.process_time() - lazy_time}\n")
    right_time = time.process_time()
    run_right()
    print(f">>>> Execution time of right {time.process_time() - right_time}\n")
