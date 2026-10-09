

def objective_function(x):
    return -(x**2) + 10

def hill_climbing(start, step_size, max_iteration):
    current = start
    current_value = objective_function(current)
    
    for i in range(max_iteration):
        left = current - step_size
        right = current + step_size
        
        left_value = objective_function(left)
        right_value = objective_function(right)
        
        if left_value > current_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:
            # If neither neighbor is better, stop moving
            break
            
    return current, current_value

# Input parameters
start = float(input("Enter the starting value: "))
step_size = float(input("Enter the step size: "))
max_iteration = int(input("Enter the maximum iterations: "))

# Execute algorithm
best_x, best_val = hill_climbing(start, step_size, max_iteration)
print(f"Optimal x: {best_x}, Maximum Value: {best_val}")
max_iterations = int(input("Enter maxm iterations: "))
best_position, best_value = hill_climbing(start, step_size, max_iterations)

print("\n Best-position = ", best_position)
print(" maxm value = ", best_value)