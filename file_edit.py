from random import choice


def get_id(in_line: str) -> str:
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
    return id_element


def run():
    """
    Main executable code
    :return:
    """
    id_list = []

    # This is first method, for lazy, but not good for education
    # and not good for reading
    with open("customer.txt") as fp:
        for line in fp:
            if line.strip() != "":
                id_list.append(line.split(",")[0].split(":")[0])

    id_list = []

    # This is more educational method

    with open("customer.txt") as fp:
        for line in fp:
            if line.strip() != "":
                id_list.append(get_id(line))

    print(f"Element list: {','.join(id_list)}")

    new_id = choice([i for i in range(1000, 9999) if i not in id_list])
    print(f"Random id number {new_id} not in {','.join(id_list)} -> {new_id not in id_list} ")


if __name__ == "__main__":
    run()
