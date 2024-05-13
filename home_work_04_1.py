import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def timsort_sort(arr):
    arr.sort()

def measure_time(algorithm, dataset):
    setup_code = f"from __main__ import {algorithm}, {dataset}"
    stmt = f"{algorithm}({dataset})"
    time = timeit.timeit(stmt=stmt, setup=setup_code, number=1)
    return time

dataset1 = [i for i in range(1000)]
dataset2 = [i for i in range(10000)]
dataset3 = [i for i in range(100000)]

merge_sort_time_1 = measure_time("merge_sort", "dataset1")
insertion_sort_time_1 = measure_time("insertion_sort", "dataset1")
timsort_time_1 = measure_time("timsort_sort", "dataset1")

merge_sort_time_2 = measure_time("merge_sort", "dataset2")
insertion_sort_time_2 = measure_time("insertion_sort", "dataset2")
timsort_time_2 = measure_time("timsort_sort", "dataset2")

merge_sort_time_3 = measure_time("merge_sort", "dataset3")
insertion_sort_time_3 = measure_time("insertion_sort", "dataset3")
timsort_time_3 = measure_time("timsort_sort", "dataset3")

print("Час сортування (у секундах) для набору даних з 1000 елементів:")
print(f"Сортування злиттям: {round(merge_sort_time_1, 5)}")
print(f"Сортування вставками: {round(insertion_sort_time_1, 5)}")
print(f"Timsort: {round(timsort_time_1, 5)}\n")

print("Час сортування (у секундах) для набору даних з 10000 елементів:")
print(f"Сортування злиттям: {round(merge_sort_time_2, 5)}")
print(f"Сортування вставками: {round(insertion_sort_time_2, 5)}")
print(f"Timsort: {round(timsort_time_2, 5)}\n")

print("Час сортування (у секундах) для набору даних з 100000 елементів:")
print(f"Сортування злиттям: {round(merge_sort_time_3, 5)}")
print(f"Сортування вставками: {round(insertion_sort_time_3, 5)}")
print(f"Timsort: {round(timsort_time_3, 5)}")