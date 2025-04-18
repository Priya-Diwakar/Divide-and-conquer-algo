import tkinter as tk
from tkinter import messagebox

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def sort_numbers():
    try:
        numbers = list(map(int, entry.get().split()))
        selected_algo = algo_var.get()

        if selected_algo == "Merge Sort":
            sorted_numbers = merge_sort(numbers)
        elif selected_algo == "Quick Sort":
            quick_sort(numbers, 0, len(numbers) - 1)
            sorted_numbers = numbers
        else:
            messagebox.showerror("Error", "Please select a sorting algorithm")
            return

        result_label.config(text=f"Sorted Array: {sorted_numbers}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers separated by spaces")

# GUI setup
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("500x400")
root.configure(bg="#2c3e50")

# Frame for content
frame = tk.Frame(root, bg="#34495e", padx=20, pady=20)
frame.pack(pady=30)

# Title Label
tk.Label(frame, text="Sorting Algorithm Visualizer", font=("Helvetica", 18, "bold"), fg="white", bg="#34495e").pack(pady=10)

# Entry
tk.Label(frame, text="Enter numbers (space-separated):", font=("Helvetica", 12), fg="white", bg="#34495e").pack(pady=5)
entry = tk.Entry(frame, width=40, font=("Helvetica", 12))
entry.pack(pady=5)

# Algorithm Selection
tk.Label(frame, text="Select Sorting Algorithm:", font=("Helvetica", 12), fg="white", bg="#34495e").pack(pady=5)
algo_var = tk.StringVar(value="Merge Sort")
tk.Radiobutton(frame, text="Merge Sort", variable=algo_var, value="Merge Sort", bg="#34495e", fg="white", font=("Helvetica", 11), selectcolor="#2c3e50").pack()
tk.Radiobutton(frame, text="Quick Sort", variable=algo_var, value="Quick Sort", bg="#34495e", fg="white", font=("Helvetica", 11), selectcolor="#2c3e50").pack()

# Sort Button
sort_button = tk.Button(frame, text="Sort", command=sort_numbers, bg="#1abc9c", fg="white", font=("Helvetica", 12, "bold"), width=15)
sort_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 13), bg="#2c3e50", fg="white")
result_label.pack()

root.mainloop()
