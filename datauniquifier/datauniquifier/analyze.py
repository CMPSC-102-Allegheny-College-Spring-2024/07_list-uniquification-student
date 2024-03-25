"""Analyze the results from the uniquification process."""


def format_bytes(size):
    """Format an output value in bytes in a human-readable fashion."""
    # TODO: Depending on your operating system, you may have to adjust
    # the computation performed in this function to ensure meaningful output
    # Reference:
    # https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb/37423778
    power = 2 ** 10
    n = 0
    power_labels = {0: "", 1: "kilo", 2: "mega", 3: "giga", 4: "tera"}
    while size > power:
        size /= power
        n += 1
    return str(size) + " " + power_labels[n] + "bytes"


def calculate_reduction(list_start, list_final):
    """Calculate the reduction in the size of the list."""
    # TODO: Calculate the reduction in the size of the list
    # You must subtract the size of the final list from the size of the starting list


def calculate_percent_reduction(list_start, list_final):
    """Calculate the percent reduction in the size of the list."""
    # TODO: Calculate the percent reduction in the size of the list
    # Step 1: Calculate the reduction using calculate_reduction
    # Step 2: Calculate the ratio between the reduction and the original size
    # Step 3: Convert the numerical value from step 2 into a percentage
