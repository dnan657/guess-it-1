import sys
import math

def calculate_mean(numbers):
    """Calculates the arithmetic mean of a list of numbers."""
    n = len(numbers)
    if n == 0:
        return 0
    return sum(numbers) / n

def main():
    """
    Main function to read numbers from stdin, predict a range for the next number,
    and print the prediction to stdout.
    """
    numbers = []
    # This percentage is used to calculate the prediction range.
    # A percentage-based range (e.g., mean +/- 15%) was chosen over a 
    # standard-deviation-based range because it adapts better to datasets with
    # different scales and volatility, providing more consistent scores.
    # 0.15 was found to be a good balance between accuracy and range size
    # across the provided test datasets.
    percentage = 0.15

    # The loop now reads first, then predicts.
    for line in sys.stdin:
        try:
            number = float(line.strip())
            if number > 0: # Only consider positive numbers as valid data points
                numbers.append(number)
        except (ValueError, IndexError):
            # Stop if input is not a valid number.
            continue

        if not numbers:
            # If we have no valid numbers yet, predict a wide default range
            print("1 200")
            sys.stdout.flush()
            continue

        # Now, based on the history including the new number, predict the *next* one.
        mean = calculate_mean(numbers)
        
        range_size = mean * percentage
        
        lower_bound = int(mean - range_size)
        upper_bound = int(mean + range_size)
    
        if lower_bound < 1:
            lower_bound = 1

        # Print the prediction for the next number.
        print(f"{lower_bound} {upper_bound}")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
