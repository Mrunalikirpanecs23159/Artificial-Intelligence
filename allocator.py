def heuristic_allocate(graph):

    allocations = {}

    vms = [n for n,d in graph.nodes(data=True) if d['type']=="vm"]
    tasks = [n for n,d in graph.nodes(data=True) if d['type']=="task"]

    vm_resources = {}

    for vm in vms:
        vm_resources[vm] = {
            "cpu": graph.nodes[vm]["cpu"],
            "ram": graph.nodes[vm]["ram"]
        }

    for task in tasks:

        cpu_req = graph.nodes[task]["cpu"]
        ram_req = graph.nodes[task]["ram"]

        for vm in vms:

            if vm_resources[vm]["cpu"] >= cpu_req and vm_resources[vm]["ram"] >= ram_req:

                allocations[task] = vm

                vm_resources[vm]["cpu"] -= cpu_req
                vm_resources[vm]["ram"] -= ram_req

                break

    return allocations