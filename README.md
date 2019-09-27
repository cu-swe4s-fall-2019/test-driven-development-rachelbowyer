# test-driven-dev
Test Driven Development

## Installation
Clone this repository to your local machine.  You'll want to run
```
chmod +x gen_data.sh
```
to make the shell file executable

## Modules
math_lib.py - contains functions to calculate the mean and standard deviation of arrays
get_data.py - contains function that reads stdin and returns column of standard in that is specified
data_viz.py - contains functions to (1) create a histogram, (2) create a boxplot, (3) create both at the same time
viz.py - takes command line arguments to run functions in data_viz.py, user specifies plot type and output file name

## Unit Tests for Modules
The modules math_lib.py and data_viz.py have unit test scripts that go along with them.  get_data.py does not per Dr. Layer's instructions and viz.py also does not because it only calls functions in data_viz.py and does not have any novel code.  There is also no functional tests per Dr. Layer's instructions.

To run the unit tests for math_lib.py do 

```
python test_math_lib.py
```

To run the unit tests for data_viz.py do

```
bash gen_data.sh | python test_data_viz_hist.py
```
```
bash gen_data.sh | python test_data_viz_box.py
```
```
bash gen_data.sh | python test_data_viz_combo.py
```

## Running Examples
The program the user will be most interested in running is viz.py.  In order to run that script do

```
bash gen_data.sh | python viz.py out_name type
```
where out_name is the name of the output file you want and type is the type of plot you want
```
bas gen_data.sh | python viz.py myplot.png combo
```