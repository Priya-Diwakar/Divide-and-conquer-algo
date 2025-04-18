from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
def home():
    sorted_array = None
    if request.method == "POST":
        numbers = request.form["numbers"]
        algorithm = request.form["algorithm"]
        arr = list(map(int, numbers.split()))

        if algorithm == "Merge Sort":
            sorted_array = merge_sort(arr)
        elif algorithm == "Quick Sort":
            quick_sort(arr, 0, len(arr) - 1)
            sorted_array = arr

    return render_template("index.html", sorted_array=sorted_array)

if __name__ == "__main__":
    app.run(debug=True)
