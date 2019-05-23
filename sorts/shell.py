"""A implemention of shell sort."""


def shellsort(arr, h=None):
    lenght = len(arr)
    gap = h if h else lenght // 2

    while gap > 0:
        for i in range(gap, lenght):
            temp = arr[i]

            j = i

            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr
