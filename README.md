# functional_Treat

## Overview

This Python script provides a command-line interface for basic data analysis and manipulation operations. It supports both 1D arrays and 2D matrices, allowing users to input data, compute statistics, perform transformations, and more through an interactive menu system.

## Features

- **Data Input**: Accept 1D arrays or 2D matrices as input
- **Data Summary**: Display minimum, maximum, sum, and average values
- **Factorial Calculation**: Compute factorial of a given number
- **Data Filtering**: Filter values above a specified threshold
- **Data Sorting**: Sort 1D arrays or 2D matrices
- **Dataset Statistics**: Display comprehensive statistics

## Requirements

- Python 3.x

## Installation

1. Ensure Python 3.x is installed on your system.
2. Download or clone the repository containing `functional_treat.py`.
3. Navigate to the project directory.

## Usage

Run the script using Python:

```bash
python functional_treat.py
```

### Menu Options

1. **Input Data**: Enter data as space-separated values for 1D arrays or bracketed rows for 2D matrices (e.g., `[1,2,3] [4,5,6]`).
2. **Display Data Summary**: Shows total elements, min, max, sum, and average.
3. **Calculate Factorial**: Enter a number to compute its factorial.
4. **Filter Data by Threshold**: Enter a threshold to filter values greater than it.
5. **Sort Data**: Sorts the input data (1D in-place, 2D by first element).
6. **Display Dataset Statistics**: Shows max, min, sum, and average.
7. **Exit**: Quit the program.

## Examples

### Inputting 1D Data
```
Enter Data for the 1D Array: (Separated by space)
10 20 30 40 50
```

### Inputting 2D Data
```
Enter Data for the 1D Array: (Separated by space)
[1,2,3] [4,5,6] [7,8,9]
```

### Calculating Factorial
```
Enter the Number to calculate factorial: 5
Answer: 120
```

## Notes

- The program uses global variables for data storage.
- Filtering and some operations are optimized for 1D arrays.
- Ensure input is properly formatted to avoid errors.

## Contributing

Feel free to submit issues or pull requests for improvements.

## License

This project is open-source. Please check for any applicable licenses.
