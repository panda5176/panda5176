"""http://rosalind.info/problems/list-view/?location=algorithmic-heights"""


def fibo(n):
    """Fibonacci Numbers"""
    if n == 0:
        return 0
    elif n == 1:
        return 1

    def recurrence(n, Fn_2=0, Fn_1=1, Fn=0):
        """Recurrence relation of for the Fibonacci sequence"""
        if n == 0:
            return Fn_1
        Fn = Fn_2 + Fn_1
        return recurrence(n - 1, Fn_1, Fn)

    return recurrence(n - 1)


def read_lbsv(lbsv):
    """Reading line-break-seperated values file"""
    values = []
    with open(lbsv, "r") as f:
        values = f.read().strip().split("\n")
    return values


def write_lbsv(values, lbsv):
    """Writing line-break-seperated values file"""
    with open(lbsv, "w") as f:
        for value in values:
            if type(value) == int:
                f.write(str(value) + "\n")
            elif type(value) == list:
                f.write(" ".join(list(map(str, value))) + "\n")
    return None


def bind(lbsv):
    """Binary Search"""
    values = read_lbsv(lbsv)
    n, _m, A, B = (
        int(values[0]),
        int(values[1]),
        list(map(int, values[2].split())),
        list(map(int, values[3].split())),
    )
    idxes = []

    def binary_search(b, A, n, origin=0):
        if n == origin or n == origin + 1:
            if b == A[origin]:
                return origin + 1
            elif b == A[n]:
                return n + 1
            else:
                return -1
        idx = (origin + n) // 2
        median = A[idx]
        if b < median:
            idx = binary_search(b, A, idx, origin)
        elif b > median:
            idx = binary_search(b, A, n, idx)
        else:
            return idx + 1
        return idx

    for b in B:
        idxes.append(binary_search(b, A, n))
    return idxes


def read_simple_graph(lbsv):
    """Reading simple un-directed grapth in the edge list format"""
    edge_lists = read_lbsv(lbsv)
    vertices_range = range(int(edge_lists[0].split()[0]))
    graph = [[] for vertex in vertices_range]
    for edge in edge_lists[1:]:
        u, v = list(map(int, edge.split()))
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    return graph, vertices_range


def deg(lbsv):
    """Degree Array"""
    graph, _vertices_range = read_simple_graph(lbsv)
    D = []
    for vertex in graph:
        D.append(len(vertex))
    return D


def ins(lbsv):
    """Insertion Sort"""
    values = read_lbsv(lbsv)
    n, A = int(values[0]), list(map(int, values[1].split()))
    disorder, swaps = True, 0
    while disorder:
        disorder = False
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                disorder, swaps = True, swaps + 1
    return swaps


def ddeg(lbsv):
    """Double-Degree Array"""
    graph, vertices_range = read_simple_graph(lbsv)
    D = [0 for vertex in vertices_range]
    for i in vertices_range:
        for neighbor in graph[i]:
            D[i] += len(graph[neighbor])
    return D


def maj(lbsv):
    """Majority Element"""
    """Boyer–Moore majority vote algorithm"""
    values = read_lbsv(lbsv)
    _k, n = list(map(int, values[0].split()))
    A = []
    for array in values[1:]:
        array = list(map(int, array.split()))
        mode, count = array[0], 1
        for m in array[1:]:
            if mode == m:
                count += 1
            else:
                count -= 1
            if count == 0:
                mode, count = m, 1
        count = 0
        for m in array:
            if mode == m:
                count += 1
        if count * 2 > n:
            A.append(mode)
        else:
            A.append(-1)
    return A


def mer(lbsv):
    """Merge Two Sorted Arrays"""
    values = read_lbsv(lbsv)
    _n, A, _m, B, C, i_A, i_B = (
        int(values[0]),
        list(map(int, values[1].split())),
        int(values[2]),
        list(map(int, values[3].split())),
        [],
        0,
        0,
    )
    while A and B:
        if A[i_A] < B[i_B]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
    return C + A + B


def a2sum(lbsv):
    """2SUM"""
    values = read_lbsv(lbsv)
    _k, n = list(map(int, values[0].split()))
    hash_table, A = {}, []
    for array in values[1:]:
        array, A, hash_table = list(map(int, array.split())), A + [-1], {}
        for i in range(n):
            p = array[i]
            if p in hash_table:
                A[-1] = sorted([i + 1, hash_table[p] + 1])
                break
            else:
                hash_table[-p] = i
    return A


def bfs(lbsv):
    """Breadth-First Search"""
    graph, vertices_range = read_simple_graph(lbsv)
    D, queue = [0] + [-1 for vertex in vertices_range][1:], [(0, 1)]
    while queue:
        vertex, depth = queue.pop(0)
        for vertex_next in graph[vertex]:
            if D[vertex_next] == -1:
                queue.append((vertex_next, depth + 1))
                D[vertex_next] += depth + 1
    return D


def cc(lbsv):
    """Connected Components"""
    """Depth-first search"""
    graph, _vertices_range = read_simple_graph(lbsv)
    queue = graph.pop(0)
    graph, connected_components = [True] + graph, 1
    for i, visited in enumerate(graph):
        if not queue:
            if visited == True:
                continue
            graph[i], queue = True, queue + visited
            connected_components += 1
        while queue:
            node = queue.pop(0)
            if graph[node] != True:
                queue += graph[node]
                graph[node] = True
    return connected_components


def hea(lbsv):
    """Building a Heap"""
    """Max heap"""
    import heapq

    values = read_lbsv(lbsv)
    _n, A, heap = int(values[0]), list(map(int, values[1].split())), []
    for integer in A:
        heapq.heappush(heap, -integer)
    return list(map(lambda x: -x, heap))


def ms(lbsv):
    """Merge Sort"""
    values = read_lbsv(lbsv)
    _n, A = int(values[0]), list(map(int, values[1].split()))
    A = list(map(lambda x: [x], A))
    while len(A) > 1:
        A_merged = []
        for i in range(len(A))[::2]:
            if len(A) == i + 1:
                A_merged.append(A[i])
                break
            left, right, merged = A[i], A[i + 1], []
            while left and right:
                if left[0] < right[0]:
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))
            A_merged.append(merged + left + right)
        A = A_merged
    return A


def par(lbsv):
    """2-Way Partition"""
    values = read_lbsv(lbsv)
    _n, A = int(values[0]), list(map(int, values[1].split()))
    element1, small_list, large_list = A.pop(0), [], []
    for a in A:
        if element1 > a:
            small_list.append(a)
        else:
            large_list.append(a)
    return small_list + [element1] + large_list


def a3sum(lbsv):
    """3SUM"""
    values = read_lbsv(lbsv)
    _k, n = list(map(int, values[0].split()))
    A = []

    def calc_a3sum(array, A):
        hash_table = {}
        for i in range(n):
            r = array[i]
            hash_table[-r] = i
        for i in range(n - 1):
            p = array[i]
            for j in range(i + 1, n):
                q = array[j]
                if p + q in hash_table:
                    if hash_table[p + q] != i and hash_table[p + q] != j:
                        A[-1] = sorted([hash_table[p + q] + 1, i + 1, j + 1])
                        return A
        return A

    for array in values[1:]:
        array, A = list(map(int, array.split())), A + [[-1]]
        A = calc_a3sum(array, A)

    return A


if __name__ == "__main__":
    # print(a3sum("Roz/f.txt"))
    write_lbsv(a3sum("Roz/f.txt"), "Roz/o.txt")
