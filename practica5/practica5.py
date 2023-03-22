import pandas as pd


def first_fit(mb, p):
    allocated_memory = [-1] * len(p)
    for i in range(len(p)):
        for j in range(len(mb)):
            if mb[j]["size"] >= p[i]["process_size"]:
                allocated_memory[i] = mb[j]["id"]
                mb[j]["size"] -= p[i]["process_size"]
                break
    for i in range(len(p)):
        if allocated_memory[i] != -1:
            print("Process {0} allocated to memory block {1}".format(p[i]["process"],allocated_memory[i]))
        else:
            print("Process {0} cannot be allocated to any memory block".format(p[i]["process"]))


def best_fit(mb, p):
    allocated_memory = [-1] * len(p)
    for i in range(len(p)):
        best_block_index = -1
        for j in range(len(mb)):
            if mb[j]["size"] >= p[i]["process_size"]:
                if best_block_index == -1 or mb[j]["size"] < mb[best_block_index]["size"]:
                    best_block_index = j
        if best_block_index != -1:
            allocated_memory[i] = mb[best_block_index]["id"]
            mb[best_block_index]["size"] -= p[i]["process_size"]
    for i in range(len(p)):
        if allocated_memory[i] != -1:
            print("Process {0} allocated to memory block {1}".format(p[i]["process"],allocated_memory[i]))
        else:
            print("Process {0} cannot be allocated to any memory block".format(p[i]["process"]))



def worst_fit(p, mb):
    memory = {}
    for block in mb:
        memory[block['id']] = [None] * block['size']
    for process in p:
        size = process.get('process_size')
        allocated = False
        max_size = -1
        max_block_id = None
        for block_id, block_memory in memory.items():
            for i in range(len(block_memory) - size + 1):
                if all(memory[block_id][i:i+size] is None for i in range(i, i+size)):
                    if len(block_memory[i:i+size]) > max_size:
                        max_size = len(block_memory[i:i+size])
                        max_block_id = block_id
                        max_index = i
        if max_block_id is not None:
            for i in range(max_index, max_index+size):
                memory[max_block_id][i] = process
            allocated = True
        if not allocated:
            print(f"Process {process.get('id')} cannot be allocated.")
    for block_id, block_memory in memory.items():
        for i in range(len(block_memory)):
            if block_memory[i] is not None:
                print(f"Memory at block {block_id}, index {i}: {block_memory[i]}")


def next_fit(processes, memory_blocks):
    memory = {}
    for block in memory_blocks:
        memory[block['id']] = [None] * block['size']
    current_block_id = None
    current_index = 0
    for process in processes:
        size = process.get('process_size')
        allocated = False
        for i in range(len(memory)):
            block_id = list(memory.keys())[i]
            block_memory = memory[block_id]
            if current_block_id is not None and block_id == current_block_id:
                for j in range(current_index, len(block_memory) - size + 1):
                    if all(memory[current_block_id][j:j+size] is None for j in range(j, j+size)):
                        for k in range(j, j+size):
                            memory[current_block_id][k] = process
                        allocated = True
                        current_index = j+size
                        break
            else:
                for j in range(len(block_memory) - size + 1):
                    if all(memory[block_id][j:j+size] is None for j in range(j, j+size)):
                        for k in range(j, j+size):
                            memory[block_id][k] = process
                        allocated = True
                        current_block_id = block_id
                        current_index = j+size
                        break
            if allocated:
                break
        if not allocated:
            print(f"Process {process.get('id')} cannot be allocated.")
    for block_id, block_memory in memory.items():
        for i in range(len(block_memory)):
            if block_memory[i] is not None:
                print(f"Memory at block {block_id}, index {i}: {block_memory[i]}")


def main():
    col_names = ["process", "process_size"]
    processes = pd.read_csv("practica5/archivos.txt", names=col_names).to_dict('records')
    for process in processes:
        process['process_size'] = int(process['process_size'][:-2])
    print(pd.DataFrame(processes))
    memory_blocks = [{'id': 0, 'size': 1000},
                     {'id': 1, 'size': 400},
                     {'id': 2, 'size': 1800},
                     {'id': 3, 'size': 700},
                     {'id': 4, 'size': 900},
                     {'id': 5, 'size': 1200},
                     {'id': 6, 'size': 1500}]

    while True:
        print("Select an algorithm:")
        print("1. First fit")
        print("2. Best fit")
        print("3. Worst fit")
        print("4. Next fit")
        print("5. Exit")
        algo = input("Enter your choice: ")
        if algo == '1':
            first_fit(memory_blocks, processes)
        elif algo == '2':
            best_fit(memory_blocks, processes)
        elif algo == '3':
            worst_fit(processes, memory_blocks)
        elif algo == '4':
            next_fit(processes, memory_blocks)
        elif algo == '5':
            print("Good bye!")
            return False
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")

if __name__ == '__main__':
    main()