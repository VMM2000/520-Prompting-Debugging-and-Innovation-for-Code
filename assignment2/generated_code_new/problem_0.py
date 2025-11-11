def min_path(grid, k):

    N = len(grid)
    if N == 0:
        return []

    # --- Chain of Thought ---
    # 1. The problem asks for a lexicographically minimum path.
    # 2. This means we must prioritize making the first step as small as
    #    possible. Since we can start anywhere, we *must* start at the
    #    smallest value in the grid, which is 1.
    
    # Find the starting coordinates of the cell with value 1
    start_r, start_c = -1, -1
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1:
                start_r, start_c = r, c
                break
        if start_r != -1:
            break
            
    # 3. Initialize our path and current position.
    path_values = [1]
    current_r, current_c = start_r, start_c
    
    # 4. We need to take k-1 more steps.
    # 5. For each step, to maintain the lexicographical minimum,
    #    we *must* choose the neighbor with the smallest value.
    
    for _ in range(k - 1):
        min_neighbor_value = float('inf')
        best_neighbor_r, best_neighbor_c = -1, -1
        
        # Define the 4 possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            nr, nc = current_r + dr, current_c + dc
            
            # Check if the neighbor is within the grid boundaries
            if 0 <= nr < N and 0 <= nc < N:
                neighbor_value = grid[nr][nc]
                
                # If this neighbor is better, record it.
                # Since the answer is unique, we don't worry about ties.
                if neighbor_value < min_neighbor_value:
                    min_neighbor_value = neighbor_value
                    best_neighbor_r, best_neighbor_c = nr, nc
        
        # 6. After checking all 4 neighbors, we move to the best one
        #    and add its value to our path.
        path_values.append(min_neighbor_value)
        current_r, current_c = best_neighbor_r, best_neighbor_c
        
    # 7. After k-1 steps, our path is complete.
    return path_values