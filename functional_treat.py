values = []
Min = 0
Max = 0
Sum = 0
Average = 0

while True:
    print("Welcome to Data Analyzer and Tranform program ")
    print("main menu".title())
    print("1. Input data")
    print("2. Display data summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshhold")
    print("5. Sort data")
    print("6. Display Dataset Statistics")
    print("7. Exit")

    choice = input("Please Enter Your choice: ")

    def input_data():
        global values,Min, Max, Sum, Average,values

        values = input().strip().split(" ")
        if (
            type(values) is list
            and len(values) > 0
            and type(values[0]) is str
            and values[0].startswith("[")
        ):
            matrix = []
            for item in values:
                # Convert each string "[12,13,14]" into list
                row_str = item.strip("[]")
                row = [int(x.strip()) for x in row_str.split(",") if x.strip()]
                matrix.append(row)
            values = matrix

        else:
            values = [int(x) for x in values]
        
        if type(values) is list and len(values) > 0 and type(values[0]) is list:
            Sum = sum(sum(row) for row in values)
            Min = min(min(row) for row in values)
            Max = max(max(row) for row in values)
        else:
            Sum = sum(values)
            Max = max(values)
            Min = min(values)

        Average = Sum / len(values)

    def display_summary():
        global values,Min, Max, Sum, Average
        if values:

            if type(values) is list and len(values) > 0 and type(values[0]) is list:
                 Sum = sum(sum(row) for row in values)
                 Min = min(min(row) for row in values)
                 Max = max(max(row) for row in values)
            else:
                Sum = sum(values)
                Min = min(values)
                Max = max(values)

            Average = Sum / len(values)

            print("Data Summary:")
            print(f"- Total Elements: {len(values)}")
            print(f"- Minimun value: {Min}")
            print(f"- Maximum value: {Max}")
            print(f"- Sum of All value: {Sum}")
            print(f"- Average value: {Average}")
        else:
            print("Please Input the value first")

    def calculate_factorial(val):
        if val == 1 or val == 0:
            return 1
        else:
            return val * calculate_factorial(val - 1)

    def filter_data_by_threshold(threshold):
        global values
        if type(values) is list and len(values) > 0 and type(values[0]) is list:
            print("\nFiltering is only supported for 1D arrays. Please input a 1D array.\n")
        else:
            if values:
                filtered_values = list(filter(lambda x: x > threshold, values))
                print(f"\nValues greater than {threshold}: {filtered_values}\n")
            else:
                print("\nPlease Input the value first\n")

    def sort_array(arr):
        """
        Sorts a 1D or 2D list.

        - If the input is a 1D list, it sorts the list **in-place** using the .sort() method.
        - If the input is a 2D list, it returns a **new sorted** 2D list using the sorted() function.
        The 2D list is sorted by the first element of each inner list (row-wise sorting).
        
        """
        print("Chose how to sort the data:")
        print("1. Sort in Ascending Order")
        print("2. Sort in Descending Order")

        match input("Enter your choice: "):
            case "1":
                # Check if it's a 1D list
                if type(arr) is list and len(arr) > 0 and type(arr[0]) is not list:
                    arr.sort()
                    print(f"Sorted 1D Array: {arr}")  # In-place sorting for 1D using .sort()
                    return arr

                # Check if it's a 2D list
                elif type(arr) is list and len(arr) > 0 and type(arr[0]) is list:
                    # Sort 2D list using sorted() - sorts by first element of each row
                    print(
                        f"Sorted 2D Array: {sorted(arr, key=lambda x: x[0])}"
                    )  # New sorted list for 2D
                    return sorted(arr, key=lambda x: x[0])

                else:
                    print("Invalid input: Please provide a 1D or 2D list.")
            case "2":
                # Check if it's a 1D list
                if type(arr) is list and len(arr) > 0 and type(arr[0]) is not list:
                    arr.sort(reverse=True)
                    print(f"Sorted 1D Array: {arr}")  # In-place sorting for 1D using .sort()
                    return arr

                # Check if it's a 2D list
                elif type(arr) is list and len(arr) > 0 and type(arr[0]) is list:
                    # Sort 2D list using sorted() - sorts by first element of each row
                    print(
                        f"Sorted 2D Array: {sorted(arr, key=lambda x: x[0])}"
                    )  # New sorted list for 2D
                    return sorted(arr, key=lambda x: x[0],reverse=True)

                else:
                    print("Invalid input: Please provide a 1D or 2D list.")

    def display_dataset_statistics(**kwargs):
        global values
        if values:
            print("\nDataset Statistics:")
            for key, value in kwargs.items():
                print(f"{key}: {value}")
            if type(values) is list and len(values) > 0 and type(values[0]) is list:
                for i in range(len(values)):
                    print("-----------------\n")
                    for j in range(len(values[i])):
                        print(f"{j}",end="") 
                print("---------------------")  

    match choice:
        case "1":
            print("Enter Data for the 1D Array: (Separated by space)")
            input_data()
        case "2":
            display_summary()
        case "3":
            val = int(input("Enter the Number to calculate factorial: "))

            print(f"\n Answer: {calculate_factorial(val)}\n")
        case "4":
            threshold = int(input("Enter the threshold value: "))
            filter_data_by_threshold(threshold)
        case "5":
            sort_array(values)
        case "6":
            display_dataset_statistics(
                maximum=Max, minimum=Min, sum=Sum, average=Average
            )
        case "7":
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")
