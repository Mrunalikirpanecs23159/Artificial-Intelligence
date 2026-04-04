import networkx as nx

def create_resource_graph():
    G = nx.Graph()

    # Virtual Machines
    vms = [
        ("VM1", {"cpu": 4, "ram": 8}),
        ("VM2", {"cpu": 6, "ram": 16}),
        ("VM3", {"cpu": 8, "ram": 32})
    ]

    # Tasks
    tasks = [
        ("T1", {"cpu": 2, "ram": 4}),
        ("T2", {"cpu": 3, "ram": 6}),
        ("T3", {"cpu": 4, "ram": 8}),
        ("T4", {"cpu": 1, "ram": 2})
    ]

    for vm in vms:
        G.add_node(vm[0], type="vm", cpu=vm[1]["cpu"], ram=vm[1]["ram"])

    for task in tasks:
        G.add_node(task[0], type="task", cpu=task[1]["cpu"], ram=task[1]["ram"])

    return G