# ============================================================
# Name of Program  : Student Marks Calculator
# Purpose of Program: Allows the user to enter student marks,
#                    then calculates mean, median, mode,
#                    skewness, and supports file input.
# Author           : Galib
# Date Programmed  : May 2026
# ============================================================


# ---- Helper: Calculate Mean --------------------------------
def calculate_mean(numbers):
    # Add up all numbers in the list
    total = 0
    for num in numbers:
        total += num          # Running sum of all values

    # Divide total by the count to get the average (mean)
    return total / len(numbers)


# ---- Helper: Calculate Median ------------------------------
def calculate_median(numbers):
    # Sort a copy so the original list is not changed
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)      # Total count of numbers
    mid = n // 2              # Integer division gives middle index

    # If even count, average the two middle values
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        # Odd count: the middle element is the median
        return sorted_nums[mid]


# ---- Helper: Calculate Mode --------------------------------
def calculate_mode(numbers):
    # Build a frequency dictionary: {value: how many times it appears}
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1   # Increment existing key
        else:
            frequency[num] = 1    # Start count at 1 for new key

    # Find the highest frequency present
    max_freq = max(frequency.values())

    # Collect all values that share the highest frequency
    # (there can be more than one mode)
    modes = [k for k, v in frequency.items() if v == max_freq]

    return modes


# ---- Helper: Calculate Skewness ----------------------------
def calculate_skewness(numbers):
    # Skewness measures how asymmetric the distribution is.
    # Using the Fisher-Pearson standardised moment coefficient.
    n = len(numbers)

    # Need at least 3 values to compute skewness meaningfully
    if n < 3:
        return None

    mean = calculate_mean(numbers)

    # Step 1: calculate variance (average of squared deviations)
    variance = sum((x - mean) ** 2 for x in numbers) / n

    # Step 2: standard deviation is the square root of variance
    std_dev = variance ** 0.5

    # If all numbers are identical, std_dev is 0; skewness is 0
    if std_dev == 0:
        return 0

    # Step 3: apply the skewness formula
    # G1 = [n / ((n-1)(n-2))] * sum( ((x - mean) / std_dev)^3 )
    skewness = (n / ((n - 1) * (n - 2))) * sum(
        ((x - mean) / std_dev) ** 3 for x in numbers
    )

    return skewness


# ---- Helper: Read Numbers from a File ----------------------
def read_numbers_from_file(filename):
    # Open the file and parse every line for numeric values.
    # Each line may contain a single number or comma-separated numbers.
    numbers = []

    try:
        with open(filename, "r") as f:             # Open file in read mode
            for line in f:
                line = line.strip()                # Remove leading/trailing whitespace
                if not line:
                    continue                        # Skip blank lines

                # Split by comma to handle comma-separated values on one line
                parts = line.split(",")
                for part in parts:
                    part = part.strip()            # Remove spaces around each value
                    if part == "":
                        continue                   # Skip empty segments
                    try:
                        numbers.append(float(part))   # Convert to float and store
                    except ValueError:
                        # Warn the user but keep going with the rest of the file
                        print(f"  Warning: '{part}' is not a valid number — skipped.")

    except FileNotFoundError:
        # The file path the user typed does not exist
        print(f"  Error: File '{filename}' not found. Please check the path.")
    except PermissionError:
        # The OS blocked access to the file
        print(f"  Error: Permission denied when reading '{filename}'.")

    return numbers


# ---- Helper: Collect Numbers from the Keyboard -------------
def get_numbers_from_user(existing_numbers=None):
    # Start from an existing list (when adding more numbers) or a fresh list
    numbers = existing_numbers[:] if existing_numbers is not None else []

    print()
    print("Enter numbers one at a time OR as comma-separated values (e.g. 5, 8, 12).")
    print("Type 'done' and press Enter when you have finished entering numbers.")
    print("Type 'file' to load numbers from a text file instead.")
    print("-" * 60)

    while True:
        entry = input("Enter number(s): ").strip()

        # --- User signals they are done entering numbers ---
        if entry.lower() == "done":
            break

        # --- User wants to load from a file ---
        if entry.lower() == "file":
            filename = input("  Enter the full file path: ").strip()
            file_nums = read_numbers_from_file(filename)
            if file_nums:
                numbers.extend(file_nums)            # Add file values to our list
                print(f"  Loaded {len(file_nums)} number(s) from file.")
            else:
                print("  No valid numbers were loaded from the file.")
            continue

        # --- Handle comma-separated input on one line ---
        if "," in entry:
            parts = entry.split(",")    # Split the string at each comma
            temp_nums = []              # Temporary list for this batch
            valid = True               # Flag: stay True only if all parts parse

            for part in parts:
                part = part.strip()
                if part == "":
                    continue           # Skip extra commas (e.g. trailing comma)
                try:
                    temp_nums.append(float(part))    # Try to convert to number
                except ValueError:
                    # One part was not a number — reject the whole entry
                    print(f"  Error: '{part}' is not a valid number. Please try again.")
                    valid = False
                    break              # Stop processing this line

            if valid and temp_nums:
                numbers.extend(temp_nums)
                print(f"  Added {len(temp_nums)} number(s).")

        else:
            # --- Single number entry ---
            try:
                num = float(entry)     # Attempt conversion to float
                numbers.append(num)
                print(f"  Added {num}.")
            except ValueError:
                # The entry was not a number at all — ask again
                print(f"  Error: '{entry}' is not a valid number. Please try again.")

    return numbers


# ---- Display the Options Menu ------------------------------
def display_menu():
    print()
    print("=" * 40)
    print("           MENU")
    print("=" * 40)
    print("  1. Print the Mean")
    print("  2. Print the Median")
    print("  3. Print the Mode")
    print("  4. Print the Skewness")
    print("  5. Add more numbers to the current list")
    print("  6. Enter a NEW set of numbers")
    print("  7. Exit the application")
    print("=" * 40)


# ---- Main Application Loop ---------------------------------
def main():
    print("=" * 60)
    print("         STUDENT MARKS CALCULATOR")
    print("         Author: Galib")
    print("=" * 60)

    # Outer loop: allows the user to start over with a new set
    while True:

        # Step 1: collect marks from the user
        numbers = get_numbers_from_user()

        # Step 2: enforce minimum of two numbers before showing the menu
        while len(numbers) < 2:
            print()
            print(f"  You have entered only {len(numbers)} number(s).")
            print("  At least 2 numbers are required. Please enter more.")
            numbers = get_numbers_from_user(numbers)    # Pass existing list so entries are kept

        # Tell the user how many numbers are stored
        print()
        print(f"  You have entered {len(numbers)} number(s): {numbers}")

        # Step 3: inner menu loop — stays until user picks New Set or Exit
        while True:
            display_menu()
            choice = input("  Enter your choice (1-7): ").strip()

            # --- Option 1: Mean ---
            if choice == "1":
                mean = calculate_mean(numbers)
                print(f"\n  Mean = {mean:.4f}")

            # --- Option 2: Median ---
            elif choice == "2":
                median = calculate_median(numbers)
                print(f"\n  Median = {median:.4f}")

            # --- Option 3: Mode ---
            elif choice == "3":
                mode = calculate_mode(numbers)
                if len(mode) == len(numbers):
                    # Every value appears once — no single mode
                    print("\n  Mode = No mode (all values appear equally often)")
                else:
                    # Show all modes (could be one or several)
                    print(f"\n  Mode = {mode}")

            # --- Option 4: Skewness ---
            elif choice == "4":
                skew = calculate_skewness(numbers)
                if skew is None:
                    print("\n  Skewness requires at least 3 values.")
                else:
                    print(f"\n  Skewness = {skew:.4f}")
                    # Interpret the skewness value for the user
                    if skew > 0.5:
                        print("  Interpretation: Positively skewed (tail on the right).")
                    elif skew < -0.5:
                        print("  Interpretation: Negatively skewed (tail on the left).")
                    else:
                        print("  Interpretation: Approximately symmetric.")

            # --- Option 5: Add more numbers to the current list ---
            elif choice == "5":
                print("\n  Adding more numbers to the existing list...")
                numbers = get_numbers_from_user(numbers)   # Keep what we had
                print(f"\n  Updated list ({len(numbers)} numbers): {numbers}")

            # --- Option 6: Start over with a new set ---
            elif choice == "6":
                print("\n  Starting with a new set of numbers...")
                break    # Break inner loop → outer loop collects fresh numbers

            # --- Option 7: Exit ---
            elif choice == "7":
                print("\n  Thank you for using the Student Marks Calculator. Goodbye!")
                return   # Return from main() → program ends

            else:
                # User typed something that is not 1-7
                print("\n  Invalid choice. Please enter a number between 1 and 7.")


# Entry point: only run main() when this script is executed directly
if __name__ == "__main__":
    main()
