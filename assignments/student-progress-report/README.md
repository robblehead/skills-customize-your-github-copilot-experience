# 📘 Assignment: Student Progress Report Generator

## 🎯 Objective

Practice writing reusable Python functions and working with files by building a simple report generator that reads student scores and prints a progress summary.

## 📝 Tasks

### 🛠️ Load Student Scores from a File

#### Description
Read score data from a text file where each line is in the format `name,score`, then store the results in a list.

#### Requirements
Completed program should:

- Open `scores.txt` and read all lines.
- Split each line into `name` and `score` values.
- Convert `score` to an integer.
- Store data as a list of tuples like `(name, score)`.


### 🛠️ Build Report Functions

#### Description
Create helper functions that calculate summary information from the loaded scores.

#### Requirements
Completed program should:

- Create a function `calculate_average(scores)` that returns the class average.
- Create a function `count_passing(scores, passing_score=70)` that returns how many students passed.
- Create a function `highest_score(scores)` that returns the student name and highest score.


### 🛠️ Print a Student Progress Summary

#### Description
Use your functions to print a clear, friendly report for the class.

#### Requirements
Completed program should:

- Print total number of students.
- Print the average score.
- Print how many students passed using a passing score of 70.
- Print the name and score of the highest-scoring student.
