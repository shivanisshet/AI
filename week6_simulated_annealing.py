import math
import random

def cost_function(x):
    """
    Objective function to minimize.
    f(x) = x^2 + 10 * sin(x)
    """
    return x**2 + 10 * math.sin(x)

def simulated_annealing(cost_func, initial_solution, initial_temp=100.0, 
                        cooling_rate=0.95, stopping_temp=1e-3, 
                        iters_per_temp=100, step_size=0.5):
    """
    Executes the Simulated Annealing optimization algorithm.
    """
    # 1. Initialization
    current_sol = initial_solution
    current_cost = cost_func(current_sol)
    
    best_sol = current_sol
    best_cost = current_cost
    
    T = initial_temp
    
    # 3. Iterative process
    while T > stopping_temp:
        for _ in range(iters_per_temp):
            # Step 4: Generate a neighboring solution via random perturbation
            neighbor_sol = current_sol + random.uniform(-step_size, step_size)
            
            # Step 5: Evaluate neighboring solution
            neighbor_cost = cost_func(neighbor_sol)
            
            delta_cost = neighbor_cost - current_cost
            
            # Step 6: Acceptance criterion
            if delta_cost < 0:
                current_sol = neighbor_sol
                current_cost = neighbor_cost
            else:
                # Calculate acceptance probability exp(-delta / T)
                acceptance_prob = math.exp(-delta_cost / T)
                if random.random() < acceptance_prob:
                    current_sol = neighbor_sol
                    current_cost = neighbor_cost
            
            # Track best solution overall
            if current_cost < best_cost:
                best_sol = current_sol
                best_cost = current_cost
        
        # Step 7: Update temperature according to cooling schedule
        T *= cooling_rate
        
    # Step 10: Output best solution
    return best_sol, best_cost

if __name__ == "__main__":
    # Start at an arbitrary initial solution
    start_x = random.uniform(-10.0, 10.0)
    
    optimal_x, min_cost = simulated_annealing(
        cost_func=cost_function,
        initial_solution=start_x,
        initial_temp=100.0,
        cooling_rate=0.95,
        stopping_temp=1e-4,
        iters_per_temp=100
    )
    
    print(f"Initial Starting Point x : {start_x:.4f}")
    print(f"Optimal Solution x       : {optimal_x:.4f}")
    print(f"Minimum Cost f(x)        : {min_cost:.4f}")
