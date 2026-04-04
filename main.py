from resources import create_resource_graph
from allocator import heuristic_allocate

def main():

    graph = create_resource_graph()

    allocations = heuristic_allocate(graph)

    print("\nTask Allocation Result\n")

    for task, vm in allocations.items():
        print(f"{task} -> {vm}")

if __name__ == "__main__":
    main()