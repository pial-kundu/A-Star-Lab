import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    heap = [(0, 0, start, None)]
    g_cost = {start: 0}
    parents = {}
    
    while heap:
        f, g, node, parent = heapq.heappop(heap)
        
        if parent:
            parents[node] = parent
        
        if node == goal:
            path = []
            while node in parents:
                path.append(node)
                node = parents[node]
            path.append(start)
            return path[::-1], len(path) - 1
        
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            r, c = node[0] + dr, node[1] + dc
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0:
                neighbor = (r, c)
                new_g = g + 1
                if new_g < g_cost.get(neighbor, 9999):
                    g_cost[neighbor] = new_g
                    f_score = new_g + manhattan(neighbor, goal)
                    heapq.heappush(heap, (f_score, new_g, neighbor, node))
    
    return None, None

def main():
    print("A* Search Algorithm")
    print("Reading from input.txt...")
    
    try:
        with open("input.txt", "r") as f:
            lines = [line.strip() for line in f.readlines()]
            
            if not lines:
                print("Error: input.txt is empty!")
                return
            
            rows, cols = map(int, lines[0].split())
            
            maze = []
            for i in range(1, rows + 1):
                maze.append(list(map(int, lines[i].split())))
            
            sr, sc = map(int, lines[rows + 1].split())
            tr, tc = map(int, lines[rows + 2].split())
        
        print(f"\nMaze: {rows}x{cols}")
        print(f"Start: ({sr}, {sc})")
        print(f"Target: ({tr}, {tc})")
        
        path, cost = a_star(maze, (sr, sc), (tr, tc))
        
        with open("output.txt", "w") as f:
            if path:
                print(f"\n✓ Path found! Cost: {cost}")
                print(f"Path: {path}")
                f.write(f"Path found with cost {cost} using A*\n")
                f.write(f"Shortest Path: {path}\n")
            else:
                print("\n✗ No path found")
                f.write("Path not found using A*\n")
        
        print("\nResult saved to output.txt")
        
    except FileNotFoundError:
        print("Error: input.txt file not found!")
        print("\nCreate input.txt with this format:")
        print("Line 1: rows columns")
        print(f"Next {rows} lines: maze (0=empty, 1=wall)")
        print("Next line: start_row start_col")
        print("Last line: target_row target_col")
    except Exception as e:
        print(f"Error reading input.txt: {e}")

if __name__ == "__main__":
    main()
