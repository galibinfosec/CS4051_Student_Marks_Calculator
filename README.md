# Student Marks Calculator

A command-line Python application that helps users analyze student marks by calculating statistical measures including mean, median, mode, and skewness.

## Overview

The Student Marks Calculator is a straightforward, user-friendly tool designed for educators and students who need to quickly analyze test scores and grades. It supports both keyboard input and file-based data import, making it flexible for different use cases.

## Features

✅ Mean Calculation - Compute the average of all entered marks  
✅ Median Calculation - Find the middle value when marks are sorted  
✅ Mode Calculation - Identify the most frequently occurring mark(s)  
✅ Skewness Analysis - Measure the asymmetry of the distribution with interpretation  
✅ Flexible Input - Enter marks one at a time, comma-separated, or load from a file  
✅ Multiple Datasets - Work with multiple sets of marks in one session  
✅ Error Handling - Graceful handling of invalid input and file errors  

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/student-marks-calculator.git
cd student-marks-calculator


2. No installation required! Just run the script:
python student_marks_calculator.py


## Usage

### Running the Program

python student_marks_calculator.py


### Input Methods

The program supports three ways to input marks:

#### 1. Single Numbers
Enter number(s): 85
  Added 85.0.


#### 2. Comma-Separated Values
Enter number(s): 85, 92, 78, 88, 95
  Added 5 number(s).


#### 3. Load from File
Enter number(s): file
  Enter the full file path: marks.txt
  Loaded 20 number(s) from file.


### File Format

Your data file can contain numbers in any of these formats:
85
92
78
88
95


Or all on one line:
85, 92, 78, 88, 95


Or a mix:
85, 92, 78
88
95


### Menu Options

Once you've entered marks, the program presents this menu:

========================================
           MENU
========================================
  1. Print the Mean
  2. Print the Median
  3. Print the Mode
  4. Print the Skewness
  5. Add more numbers to the current list
  6. Enter a NEW set of numbers
  7. Exit the application
========================================


### Example Session

STUDENT MARKS CALCULATOR
  Author: Galib

Enter numbers one at a time OR as comma-separated values (e.g. 5, 8, 12).
Type 'done' and press Enter when you have finished entering numbers.
Type 'file' to load numbers from a text file instead.
------------------------------------------------------------
Enter number(s): 75, 82, 88, 92, 78, 85, 90
  Added 7 number(s).
Enter number(s): done

  You have entered 7 number(s): [75.0, 82.0, 88.0, 92.0, 78.0, 85.0, 90.0]

========================================
           MENU
========================================
  1. Print the Mean
  2. Print the Median
  3. Print the Mode
  4. Print the Skewness
  5. Add more numbers to the current list
  6. Enter a NEW set of numbers
  7. Exit the application
========================================
  Enter your choice (1-7): 1

  Mean = 85.7143


## Statistics Explained

### Mean
The average of all marks. Calculated by summing all values and dividing by the count.

### Median
The middle value when all marks are arranged in order. If there's an even number of marks, the median is the average of the two middle values.

### Mode
The mark(s) that appear most frequently. A dataset can have:
- One mode (unimodal)
- Multiple modes (bimodal or multimodal)
- No mode (all values appear with equal frequency)

### Skewness
Measures how asymmetrical the distribution of marks is:
- Skewness > 0.5: Positively skewed (tail extends to the right; some high outliers)
- Skewness < -0.5: Negatively skewed (tail extends to the left; some low outliers)
- -0.5 ≤ Skewness ≤ 0.5: Approximately symmetric

The calculator uses the Fisher-Pearson standardized moment coefficient for skewness calculation.

## Error Handling

The program gracefully handles various errors:

| Error | Message | Solut
