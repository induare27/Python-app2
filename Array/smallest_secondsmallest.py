def large_ele(arr, n):
    if n < 2:
        print("Array too small.")
        return
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

        
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    print("Largest:", largest)
    print("Second Largest:", second_largest if second_largest != float('-inf') else "Not Found")
    print("Smallest:", smallest)
    print("Second Smallest:", second_smallest if second_smallest != float('inf') else "Not Found")


arr = [3, 2, 1, 5, 4]
large_ele(arr, len(arr))
