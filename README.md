# List Uniquification

## Assigned: Monday, 25th March 2024

## Due: Monday, 1st April 2024

## Expiration Date: 8th April 2024

## Project Goals

This engineering effort invites you to investigate how to use various discrete
structures, such as the dictionary and the set, to extract the unique values
contained inside of a list of strings. In addition to implementing and testing
the functions that perform list uniquification, you will produce the majority of
the functions for the program's command-line interface and input processing. You
will also implement functions that calculate the reduction in size and the
percent reduction in size for a list of strings with an unknown amount of
redundancy. To experimentally assess the efficiency of the `datauniquifier`
program that you implement, this project also invites you to conduct an
experiment to study, for instance, which uniquification process is best at
reducing a list's size.

## Project Access

You can access this assignment by clicking the link provided to you in lab.
Once you click this link it will create a GitHub repository that you can clone
to your computer. Specifically, you
will need to use the `git clone` command to download the project from GitHub to
your computer. Now you are ready to add source code and documentation to the
project!

## Expected Output

To get started on this engineering effort, please make sure that you read the
blog post entitled [Fastest Way to Uniquify a List in
Python](https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6).
As part of this assignment, you are going to implement at least three ways to
remove the duplicate values from one of the columns in a large input file that
contains automatically generated data. Here is a sample of the data that you
input into the program that you will implement as part of this assignment:

```
dana74@mahoney-perez.com,"Administrator, charities/voluntary organisations"
nathanjohnson@davila.net,Software engineer
pbush@gmail.com,"Journalist, newspaper"
timothy75@chang.com,Osteopath
gsparks@yahoo.com,"Psychologist, clinical"
daniel39@gmail.com,Logistics and distribution manager
jason85@ward.com,Logistics and distribution manager
jacobwalton@hotmail.com,Television camera operator
markmcgee@hernandez-roberts.com,IT sales professional
shannon35@allen.com,Ecologist
```

When the program accepts this type of input it will also accept a specific
column for which it should eliminate duplicates through the process of
uniquification. For instance, when the program is run with the command `poetry
run datauniquifier --approach listcomprehension --column 1 --data-file
input/data.txt` then it will remove all of the duplicates from column `1` in
the data file that stores the job descriptions of specific individuals.
Alternatively, if the program was run with the command `poetry run
datauniquifier --approach listcomprehension --column 0 --data-file
input/data.txt` then it will remove all of the duplicates from column `0` in
the data file that stores the email addresses of specific individuals. If we run
the first of these commands two previous commands then the program will produce
output like this:

```
The chosen approach to uniquify the file is: listcomprehension

The data file that contains the input is: input/data.txt

The data file contains 50000 data values in it!

🚀 Let's do some uniquification!

🔍 So, was this an efficient approach to uniquifying the data?

The function 'unique_listcomprehension' took: 0.0063 sec

Estimated overall memory according to the operating system:
   37.921875 megabytes

🔍 So, did this remove a lot of duplicate data?

The number of values removed from the data: 1155
The percent reduction due to uniquification: 2.31%
```

    Don't forget that if you want to run the `datauniqifier` you must use your
    terminal to first go into the GitHub repository containing this project and
    then go into the `datauniqifier` directory that contains the project's code.
    Finally, remember that before running the program you must run `poetry
    install` to add the dependencies.

## Adding Functionality

One of your tasks for this project is to address all of the `TODO` markers in
the `analyze`, `extract`, and `main` modules of the `datauniqifier` program.
After you have completed all of the `TODO` markers inside of the provided Python
source code, you should execute the program in a variety of configurations so as
to determine the influence that the size of the input data set, the procedure
chosen for performing uniquification, and the type of data that is input into
the uniquification procedure has on the memory and time efficiency of the
process and the amount of reduction achieved by a specific configuration.

To automatically generate data sets of different sizes, you can use the [CSV
Faker](https://github.com/pereorga/csvfaker) tool that relies on the [Faker
Package](https://github.com/joke2k/faker) package with a command like `csvfaker
--rows 50000 email job > data.txt`. Note that this command will create a data
file called `data.txt` that contains two columns, the first for an `email` and
the second for a `job`. It is also important to note that this command will
generate a data set that contains a total of 50,000 individual records of data.
Please bear in mind that running the `csvfaker` program in this fashion may,
depending on the performance characteristics of your laptop, require a long time
to run. Using the aforementioned approach for running the `csvfaker` program you
should generate different data files and then use them as the input to the
`datauniquifier` program. While everyone
is encouraged to use the `csvfaker` tool to generate their own data sets, you
can complete this project's required tasks by using the provided `data.txt` file
in the `input` directory.

Along with varying the size of the data, your experiments should also consider
how the removal of redundant data values varies depending on the type of the
data input into your tool. You can do this by running the program with both
`--column 0` and `--column 1`. Finally, you should notice that the `uniquify.py`
file contains a total of three different procedures for performing
uniquification, with more approaches outlined in the blog post called [Fastest
Way to Uniquify a List in
Python](https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6).
You should make sure to run the `datauniquifier` with at least the three
required ways to remove duplication, checking to see if different approaches
vary in terms of their memory consumption and execution time. Along with
noticing the trends in the data sets that you collect, you should also aim to
explain why these trends are evident, leveraging your knowledge of how the
Python programming languages uses discrete structures such as the set.

The evaluation metrics for the efficiency of the `datauniquifier` program are as
follows: (i) execution time of the approach, (ii) estimated memory overhead of
the entire Python program, (iii) reduction in the size of the column of data,
and (iv) percent reduction in the size of the column of data. As you are working
to understand each of these evaluation metrics, make sure that you review the
following Python functions that respectively calculate the reduction and percent
reduction in the size of the data. In the `calculate_reduction` function, line
`3` calculates and returns the difference in size between the length of the
`list_final` and the `list_start`, with larger values suggesting that there was
a greater reduction in the size of the list. Finally, lines `3` through `5` in
`calculate_percent_reduction` use the output of the `calculate_reduction`
function to compute the percent reduction when the size of `list_start` is
compared to that of `list_final`, with higher values indicating a greater
overall reduction in size.

```python linenums="1"
def calculate_reduction(list_start, list_final):
    """Calculate the reduction in the size of the list."""
    return len(list_start) - len(list_final)
```

```python linenums="1"
def calculate_percent_reduction(list_start, list_final):
    """Calculate the percent reduction in the size of the list."""
    reduction = calculate_reduction(list_start, list_final)
    percent_reduction = (reduction / len(list_start)) * 100
    return percent_reduction
```

As you conduct the experiment using the `datauniqifier` program, you should ask
yourself what type of values would suggest that the tool worked well. For
instance, if you want to reduce the overall size of a data set through the
process of uniquification, is it better to have a large or a small value for
these two evaluation metrics calculated by `calculate_reduction` and
`calculate_percent_reduction`? Remember, part of your goal for this assignment
is to evaluate how the different configurations of the `datauniquifier` program
influence these four evaluation metrics! To accomplish this task you will need
to run the `datauniqifier` with different command-line arguments and record
the time and memory overhead data that it reports.

One noteworthy aspect of this program is that it uses the `getattr` function to
"construct" an executable version of a Python function when provided with the
name of the function, as described in this [StackOverflow
reference](https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string).
After reading the discussion on StackOverflow, make sure that you understand the
source code line `unique_result_list = function_to_call(data_column_text_list)`.
You should also notice that, instead of accepting as input the full name of a
function, this program accepts the name of the approach and then builds up the
name of the function. Can you find and understand the source code that completes
this task? Finally, this approach adopts a different approach to recording the
execution time of the three functions that perform uniquification, leveraging
the timing "decorator" described in the following function. Make sure that you
review the following [StackOverflow
discussion](https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator)
to understand how this approach works!

```python
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

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section section of tasks that use
[taskipy](https://github.com/illBeRoy/taskipy):

```toml
[tool.taskipy.tasks]
black = { cmd = "black datauniqifier tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 datauniqifier tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy datauniqifier", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle datauniqifier tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint datauniqifier tests", help = "Run the pylint checks for source code documentation" }
test = { cmd = "pytest -x -s", help = "Run the pytest test suite" }
test-silent = { cmd = "pytest -x --show-capture=no", help = "Run the pytest test suite without showing output" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy && task test"
lint = "task black && task flake8 && task pydocstyle && task pylint"
```

This section makes it easy to run commands like `poetry run task lint` to
automatically run all of the linters designed to check the Python source code in
your program and its test suite. You can also use the command `poetry run task
black` to confirm that your source code adheres to the industry-standard format
defined by the `black` tool. If it does not adhere to the standard then you can
run the command `poetry run black datauniqifier tests` and it will automatically
reformat the source code.

If your program has
all of the anticipated functionality, you can run the command `poetry run task
test-silent` and see that the test suite produces output like the following. It
is important to note that `datauniqifier` comes with three test suites, each of
which should pass so as to establish a confidence in its correctness.

```
tests/test_analyze.py ......                                         [ 54%]
tests/test_extract.py ..                                             [ 72%]
tests/test_uniquify.py ...                                           [100%]
```

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the Python source code segments that you
implemented, and answer all of the other questions about your experiences in
completing this project. The finished version of your reflection should fully
describe the influence that the size of the input data set, the procedure chosen
for performing uniquification, and the type of data that is input into the
uniquification procedure has on the memory and time efficiency of the process
and the amount of size reduction achieved by a specific configuration.

## GatorGrade Checking

You can also use `gatorgrade` to check the baseline requirements of this assignment by running the following command in your terminal:

`gatorgrade --config config/gatorgrade.yml`

If `gatorgrade` shows that all checks pass, you will know that you have met baseline requirements of this project.

## Submission

As you are working on your lab, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 50%]:**: For the lab01 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is only checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

## Seeking Assistance

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.
