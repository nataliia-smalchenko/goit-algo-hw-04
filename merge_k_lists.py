def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def merge_k_lists(lists):
    n = len(lists)
    if n == 0:
        return lists
    if n == 1:
        return lists[0]
    
    while n > 1:
        merged = []
        for i in range(0, n // 2):
            merged.append(merge(lists[i*2], lists[i*2+1]))
        if n % 2 == 1:
            merged.append(lists[-1])
        lists = merged
        n = len(lists)
    
    return merged[0]
        
    

lists = [[1, 4, 5], [1, 3, 4], [2, 6], [1, 4, 7, 9], [2, 3, 4], [2, 5, 8, 9], [1, 3, 5]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
# Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
