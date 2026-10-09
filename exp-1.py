def bfs(graph , start_node):
    visited =[]
    queue =[start_node]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(f"exploring node:{current_node}")
            visited.append(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited and neighbor not in queue :
                    queue.append(neighbor)
                return visited
print("---build your graph---")
student_graph={}
num_edges = int(input("how many edges(connetion) does your graph have:"))
print("enter each separated by a space (eg A B):")
for i in range(num_edges):
    u,v=input(f"edge{i+1}:").split()
    if u not in student_graph:
        student_graph[u] =[]
    if v not in student_graph:
        student_graph[v] =[]
    student_graph[u].append(v)
    student_graph[v].append(u)
start = input("enter the starting node for bfs")
print(f"\nyour graph dictionary:{student_graph}")
print("starting bfs traversal...")
bfs(student_graph , start)
