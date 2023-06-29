def find_third_largest_smallest(numbers):
    unique_numbers = list(set(numbers))  
    sorted_numbers = sorted(unique_numbers)   

    if len(sorted_numbers) >= 3:
        third_smallest = sorted_numbers[2]
        third_largest = sorted_numbers[-3]
        return third_smallest, third_largest
    else:
        return None


input_list = input("Enter a list of numbers (space-separated): ").split()
numbers = [int(num) for num in input_list]

result = find_third_largest_smallest(numbers)

if result:
    third_smallest, third_largest = result
    print("Third Smallest Number:", third_smallest)
    print("Third Largest Number:", third_largest)
else:
    print("Insufficient numbers in the list.")
