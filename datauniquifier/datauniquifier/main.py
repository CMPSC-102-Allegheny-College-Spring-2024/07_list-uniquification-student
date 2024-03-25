"""Define the command-line interface for the datauniquifier program."""

from rich.console import Console

from pathlib import Path

import os
import psutil  # type: ignore

import typer

from datauniquifier import analyze
from datauniquifier import extract
from datauniquifier import uniquify

UNIQUE_FUNCTION_BASE = "unique"
UNDERSCORE = "_"

cli = typer.Typer()

console = Console()


@cli.command()
def main(
    approach: str = typer.Option(...),
    column: int = typer.Option(...),
    data_file: Path = typer.Option(...),
    display: bool = typer.Option(False, "--display"),
):
    """Create the list of data values in stored in the specified file and then uniquify the file contents."""
    # display the debugging output for the program's command-line arguments
    console.print("")
    console.print(f"The chosen approach to uniquify the file is: {approach}")
    console.print("")
    console.print(f"The data file that contains the input is: {data_file}")
    console.print("")
    # construct the full name of the function to call
    function = UNIQUE_FUNCTION_BASE + UNDERSCORE + approach
    # construct the requested function from the compute module
    # Reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    function_to_call = getattr(uniquify, function)
    # declare the variables that will store file content for a valid file
    data_text = ""
    data_column_text_list = []
    # --> the file was not specified so we cannot continue using program
    if data_file is None:
        console.print("No data file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if data_file.is_file():
        # TODO: read in the contents of the file and display welcome messages
        # TODO: read the example output in Discord to see what your program should
        # produce as output, ensuring that the program output matches exactly
        # display a final message and some extra spacing, asking a question
        # about the efficiency of the approach to computing the number sequence
        # TODO: use the extract_data_given_column function to get a data column text list
        data_column_text_list = extract.extract_data_given_column(data_text, column)
    # TODO: call the constructed function and capture the result
    # TODO: display debugging information with the function's output
    # TODO: make sure to only take this step if the --display is specified
    # display the estimated overall memory use as reported by the operating system
    # Reference:
    # https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
    # Note: you may need to adjust the implementation of the format_bytes function
    # in the analyze module depending on your operating system
    process = psutil.Process(os.getpid())
    console.print("Estimated overall memory according to the operating system:")
    console.print("   " + analyze.format_bytes(process.memory_info().vms))
    # TODO: display the reduction and percent reduction that is a result of the uniquification process
    # TODO: make sure that your program output is exactly like the
    # output provided in the project description on the Proactive Programmers web site
    # TODO: once you finish implementing the program make sure that you evaluate:
    # --> Time efficiency and memory consumption and percent reduction for column 0 and column 1
    #     when running at least three of the uniquification algorithms in the uniquify module
