# List Uniquification

TODO: Please delete all of the TODO markers and prompts inside of this file. You
also need to ensure that this file does not have any mistakes in Markdown,
syntax, or technical content. This means that when you are finished with this
reflection it should contain polished responses that are suitable for
publication on your professional web site.

## Add Your Name Here

## Program Input and Output

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

`poetry run datauniquifier --approach dictionary --column 1 --data-file input/data.txt`

### What are the first five lines of the contents of the file that is input into the `datauniquifier`?

TODO: Use a fenced code block to provide the contents of the file.

### What is the output from running the test suite with the command `poetry run task test-silent`?

TODO: Use a fenced code block to provide the output from running the test suite.

## Source Code

### Describe in detail how your provided source code works

#### Please explain each line of source code from the `extract` module

TODO: Write at least one paragraph to explain the requested source code

```
for line in csv.reader(
    data.splitlines(),
    quotechar='"',
    delimiter=",",
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True,
):
```

#### Explain in detail the purpose of the following two Python functions

TODO: Write at least one paragraph to explain the requested source code

```
def calculate_reduction(list_start, list_final):
    """Calculate the reduction in the size of the list."""
    return len(list_start) - len(list_final)


def calculate_percent_reduction(list_start, list_final):
    """Calculate the percent reduction in the size of the list."""
    reduction = calculate_reduction(list_start, list_final)
    percent_reduction = (reduction / len(list_start)) * 100
    return percent_reduction
```

## Explain in detail the purpose of the following Python function

TODO: Your response to this question should explain every line of source code
in the provided function. If you do not initially understand one of the lines
of source code, then please consult online resources or ask a question on
Discord. If you are still not sure how a line of source code works, please use
explain everything that you do understand about that specific line.

```
def timing(function):
    """Define a profiling function for execution time."""
    @wraps(function)
    def wrap(*args, **kw):
        ts = time()
        result = function(*args, **kw)
        te = time()
        print("The function %r took: %2.4f sec" % (function.__name__, te - ts))
        return result

    return wrap
```

### Experimental Results

## Please use output from running the program to explain which Python function is the fastest. How did you know?

TODO: Your response to this question should use concrete numbers that resulted
from running the `datauniquifier` program.

## Please use output from running the program to explain how much list uniquification decreases the size of each column.

TODO: Your response to this question should use concrete numbers that resulted
from running the `datauniquifier` program.

## Professional Development

### What was the most confusing concept in this assignment? What did you do to ultimately understand it?

TODO: provide a one paragraph response to this question, using source code components and technical details.

### After completing this assignment, what do you think is the purpose of running experiments?

TODO: provide a one paragraph response to this question, using source code components and technical details.

### Explain how a technical concept in this assignment is connected to a topic in a different assignment

TODO: provide a one paragraph response to this question, using source code components and technical details.

### At your own option, do you have any other insights to share about this assignment?
