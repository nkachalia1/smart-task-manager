def binary_search_tasks(tasks, target_date):
    left, right = 0, len(tasks) - 1
    while left <= right:
        mid = (left + right) // 2
        if tasks[mid].due_date == target_date:
            return tasks[mid]
        elif tasks[mid].due_date < target_date:
            left = mid + 1
        else:
            right = mid - 1
    return None

def max_completed_in_window(days, k):
    l = completed = max_completed = 0
    for r in range(len(days)):
        completed += days[r]
        while r - l + 1 > k:
            completed -= days[l]
            l += 1
        max_completed = max(max_completed, completed)
    return max_completed
