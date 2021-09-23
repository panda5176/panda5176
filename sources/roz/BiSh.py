"""http://rosalind.info/problems/list-view/"""


def _parse_fasta(fasta):
    """Parsing fasta file into dictionary. From gc"""
    strings = {}
    with open(fasta, "r") as fr:
        for string in fr.read().strip().split(">")[1:]:
            strings[string.split("\n")[0]] = "".join(string.split("\n")[1:])
    return strings


def _read_lbsv(lbsv):
    """Reading line-break-seperated values file"""
    values = []
    with open(lbsv, "r") as f:
        values = f.read().strip().split("\n")
    return values


def _write_lbsv(values, lbsv):
    """Writing line-break-seperated values file"""
    with open(lbsv, "w") as f:
        for value in values:
            if type(value) == str:
                f.write(value + "\n")
            elif type(value) == int:
                f.write(str(value) + "\n")
            elif type(value) == list:
                f.write(" ".join(list(map(str, value))) + "\n")
    return None


def dna(s):
    """Counting DNA Nucleotides"""
    return "%s %s %s %s" % (
        s.count("A"),
        s.count("C"),
        s.count("G"),
        s.count("T"),
    )


def rna(t):
    """Transcribing DNA into RNA"""
    return t.replace("T", "U")


def revc(s):
    """Complementing a Strand of DNA"""
    sc = ""
    for nt in s:
        if nt == "A":
            sc += "T"
        elif nt == "T":
            sc += "A"
        elif nt == "C":
            sc += "G"
        elif nt == "G":
            sc += "C"
    return sc[::-1]


def fib(n, k):
    """Rabbits and Recurrence Relations"""
    reproductive, mate, born = 0, 0, 1
    for _month in range(n - 1):
        reproductive += mate
        mate = born
        born = reproductive * k
        total = reproductive + mate + born
    return total


def gc(fasta):
    """Computing GC Content"""
    strings, gc_contents = _parse_fasta(fasta), {}
    for name in strings.keys():
        sequence = strings[name]
        gc_contents[name] = (sequence.count("G") + sequence.count("C")) / len(
            sequence
        )
    return max(gc_contents.keys(), key=lambda k: gc_contents[k]), round(
        max(gc_contents.values()) * 100, 6
    )


def hamm(s, t):
    """Counting Point Mutations"""
    hamming_distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hamming_distance += 1
    return hamming_distance


def iprb(k, m, n):
    """Mendel's First Law"""
    p = k + m + n
    return round(
        k / p
        + m
        / p
        * (k / (p - 1) + (m - 1) / (p - 1) * (3 / 4) + n / (p - 1) * (1 / 2))
        + n / p * (k / (p - 1) + m / (p - 1) * (1 / 2)),
        5,
    )


def prot(s):
    """Translating RNA into Protein"""
    codon_table = {
        "UUU": "F",
        "CUU": "L",
        "AUU": "I",
        "GUU": "V",
        "UUC": "F",
        "CUC": "L",
        "AUC": "I",
        "GUC": "V",
        "UUA": "L",
        "CUA": "L",
        "AUA": "I",
        "GUA": "V",
        "UUG": "L",
        "CUG": "L",
        "AUG": "M",
        "GUG": "V",
        "UCU": "S",
        "CCU": "P",
        "ACU": "T",
        "GCU": "A",
        "UCC": "S",
        "CCC": "P",
        "ACC": "T",
        "GCC": "A",
        "UCA": "S",
        "CCA": "P",
        "ACA": "T",
        "GCA": "A",
        "UCG": "S",
        "CCG": "P",
        "ACG": "T",
        "GCG": "A",
        "UAU": "Y",
        "CAU": "H",
        "AAU": "N",
        "GAU": "D",
        "UAC": "Y",
        "CAC": "H",
        "AAC": "N",
        "GAC": "D",
        "UAA": "*",
        "CAA": "Q",
        "AAA": "K",
        "GAA": "E",
        "UAG": "*",
        "CAG": "Q",
        "AAG": "K",
        "GAG": "E",
        "UGU": "C",
        "CGU": "R",
        "AGU": "S",
        "GGU": "G",
        "UGC": "C",
        "CGC": "R",
        "AGC": "S",
        "GGC": "G",
        "UGA": "*",
        "CGA": "R",
        "AGA": "R",
        "GGA": "G",
        "UGG": "W",
        "CGG": "R",
        "AGG": "R",
        "GGG": "G",
    }
    protein = ""
    for i in range(len(s))[::3]:
        frame = s[i : i + 3]
        if len(frame) == 3:
            aa = codon_table[s[i : i + 3]]
            # if aa != 'Stop':
            #     protein += aa
            protein += aa
    return protein


def subs(s, t):
    """Finding a Motif in DNA"""
    subs_loc = []
    for i in range(len(s) - len(t) + 1):
        if s[i : i + len(t)] == t:
            subs_loc.append(i + 1)
    return " ".join(map(str, subs_loc))


def cons(fasta):
    """Consensus and Profile"""
    sequences = list(_parse_fasta(fasta).values())
    seq_range = range(len(sequences[0]))
    profile_matrix = {
        "A": [0 for t in seq_range],
        "C": [0 for t in seq_range],
        "G": [0 for t in seq_range],
        "T": [0 for t in seq_range],
    }
    for i in seq_range:
        for sequence in sequences:
            profile_matrix[sequence[i]][i] += 1
    consensus_string = ""
    for nt_counts in zip(*list(profile_matrix.values())):
        consensus_string += ["A", "C", "G", "T"][
            nt_counts.index(max(nt_counts))
        ]
    return consensus_string, "A: %s C: %s G: %s T: %s" % (
        " ".join(map(str, profile_matrix["A"])),
        " ".join(map(str, profile_matrix["C"])),
        " ".join(map(str, profile_matrix["G"])),
        " ".join(map(str, profile_matrix["T"])),
    )


def fibd(n, m):
    """Mortal Fibonacci Rabbits"""
    rabbits = [0 for generation in range(m - 1)] + [1]
    for _month in range(n - 1):
        born = 0
        for generation in range(m):
            if generation == m - 1:
                rabbits[generation] = born
            else:
                born += rabbits[generation]
                rabbits[generation] = rabbits[generation + 1]
    return sum(rabbits)


def grph(fasta):
    """Overlap Graphs"""
    strings, overlap_graphs = _parse_fasta(fasta), []
    for key1, item1 in strings.items():
        for key2, item2 in strings.items():
            if key1 == key2:
                continue
            if item1[-3:] == item2[:3]:
                overlap_graphs.append((key1, key2))
    return overlap_graphs


def iev(c1, c2, c3, c4, c5, c6):
    """Calculating Expected Offspring"""
    return (c1 + c2 + c3 + c4 * (3 / 4) + c5 * (1 / 2) + c6 * 0) * 2


def lcsm(fasta):
    """Finding a Shared Motif"""
    sequences = list(_parse_fasta(fasta).values())
    seq0, lcs = sequences[0], ""
    for i in range(len(seq0) - 1):
        for j in range(i + 1, len(seq0)):
            substring = seq0[i : j + 1]
            all_passed = True
            for k in range(1, len(sequences)):
                seq_target = sequences[k]
                if substring not in seq_target:
                    all_passed = False
                    break
            if all_passed and len(substring) > len(lcs):
                lcs = substring
    return lcs


def lia(k, N):
    """Independent Alleles"""
    from math import factorial

    sigma, c = 0, 2 ** k
    for n in range(N):
        sigma += (
            (1 / 4) ** n
            * (3 / 4) ** (c - n)
            * (factorial(c) / factorial(n) / factorial(c - n))
        )
    return round(1 - sigma, 3)


def mprt(IDs):
    """Finding a Protein Motif"""
    import requests, re

    IDs_motif, N_Gly_motif = {}, "N[^P][ST][^P]"
    for ID in IDs:
        seq, locs = (
            "".join(
                requests.get("http://www.uniprot.org/uniprot/%s.fasta" % ID)
                .text.strip()
                .split("\n")[1:]
            ),
            [],
        )
        for i in range(len(seq) - 3):
            if re.fullmatch(N_Gly_motif, seq[i : i + 4]):
                locs.append(str(i + 1))
        if locs:
            IDs_motif[ID] = locs
    return IDs_motif


def mrna(string):
    """Inferring mRNA from Protein"""
    codon_counts, mrna_counts_million = {
        "*": 3,
        "F": 2,
        "L": 6,
        "S": 6,
        "Y": 2,
        "C": 2,
        "W": 1,
        "P": 4,
        "H": 2,
        "Q": 2,
        "R": 6,
        "I": 3,
        "M": 1,
        "T": 4,
        "N": 2,
        "K": 2,
        "V": 4,
        "A": 4,
        "D": 2,
        "E": 2,
        "G": 4,
    }, 1
    for aa in string + "*":
        mrna_counts_million *= codon_counts[aa]
        if mrna_counts_million >= 1e6:
            mrna_counts_million %= 1e6
    return int(mrna_counts_million)


def revc_rna(s):
    """Complementing a Strand of RNA"""
    sc = ""
    for nt in s:
        if nt == "A":
            sc += "U"
        elif nt == "U":
            sc += "A"
        elif nt == "C":
            sc += "G"
        elif nt == "G":
            sc += "C"
    return sc[::-1]


def orf(fasta):
    """Open Reading Frames"""
    rna_seq = rna(list(_parse_fasta(fasta).values())[0])
    rc_rna_seq, orfs = revc_rna(rna_seq), []
    for i in range(len(rna_seq) - 2):
        if rna_seq[i : i + 3] == "AUG":
            prt_seq = prot(rna_seq[i:])
            if "*" in prt_seq:
                orfs.append(prt_seq.split("*")[0])
    for j in range(len(rc_rna_seq) - 2):
        if rc_rna_seq[j : j + 3] == "AUG":
            prt_seq = prot(rc_rna_seq[j:])
            if "*" in prt_seq:
                orfs.append(prt_seq.split("*")[0])
    return set(orfs)


def perm(n):
    """Enumerating Gene Orders"""
    from itertools import permutations

    return list(permutations(range(1, n + 1), n))


def prtm(P):
    """Calculating Protein Mass"""
    monoisotopic_mass_table, weight = {
        "A": 71.03711,
        "C": 103.00919,
        "D": 115.02694,
        "E": 129.04259,
        "G": 57.02146,
        "F": 147.06841,
        "H": 137.05891,
        "I": 113.08406,
        "S": 87.03203,
        "K": 128.09496,
        "L": 113.08406,
        "M": 131.04049,
        "P": 97.05276,
        "Q": 128.05858,
        "R": 156.10111,
        "N": 114.04293,
        "V": 99.06841,
        "T": 101.04768,
        "W": 186.07931,
        "Y": 163.06333,
    }, 0
    for aa in P:
        weight += monoisotopic_mass_table[aa]
    return round(weight, 3)


def revp(fasta):
    """Locating Restriction Sites"""
    seq, palindromes = list(_parse_fasta(fasta).values())[0], {}
    for len_p in range(4, 13, 2):
        for i in range(len(seq) - len_p + 1):
            if seq[i : i + len_p] == revc(seq[i : i + len_p]):
                palindromes[i + 1] = len_p
    return palindromes


def splc(fasta):
    """RNA Splicing"""
    seqs = list(_parse_fasta(fasta).values())
    s = seqs[0]
    for intron in seqs[1:]:
        s = "".join(s.split(intron))
    return prot(rna(s))


def lexf(symbols, n):
    """Enumerating k-mers Lexicographically"""

    def recursive(symbols, k_mers, k):
        """Recursively append base to k-mers"""
        if k == 0:
            return k_mers
        k_mers_tmp = []
        for k_mer in k_mers:
            for base in symbols:
                k_mers_tmp.append(k_mer + base)
        return recursive(symbols, k_mers_tmp, k - 1)

    return recursive("".join(symbols.split()), symbols.split(), n - 1)


def lgis(lbsv):
    """Longest Increasing Subsequence"""
    values = _read_lbsv(lbsv)
    pi = list(map(int, values[1].split()))
    lis_tmp, lds_tmp, lis_is, lds_is = [pi[0]], [pi[0]], [1], [1]
    for i in range(1, len(pi)):
        p = pi[i]
        if p > lis_tmp[-1]:
            lis_tmp.append(p)
            lis_is.append(len(lis_tmp))
        else:
            for j in range(len(lis_tmp)):
                if p < lis_tmp[j]:
                    lis_tmp[j] = p
                    lis_is.append(j + 1)
                    break
        if p < lds_tmp[-1]:
            lds_tmp.append(p)
            lds_is.append(len(lds_tmp))
        else:
            for j in range(len(lds_tmp)):
                if p > lds_tmp[j]:
                    lds_tmp[j] = p
                    lds_is.append(j + 1)
                    break
    lis_count, lds_count, lis, lds = len(lis_tmp), len(lds_tmp), [], []
    for i in range(len(lis_is))[::-1]:
        if lis_is[i] == lis_count:
            lis.append(pi[i])
            lis_count -= 1
        if lis_count == 0:
            break
    for i in range(len(lds_is))[::-1]:
        if lds_is[i] == lds_count:
            lds.append(pi[i])
            lds_count -= 1
        if lds_count == 0:
            break
    return [lis[::-1], lds[::-1]]


def along(fasta):
    """Genome Assembly as Shortest Superstring"""
    strings = list(_parse_fasta(fasta).values())
    len_s, queue, sss = len(strings[0]), [strings.pop(0)], ""
    while queue:
        q = queue.pop(0)
        right_half_q = q[-len_s // 2 :]
        left_half_q = q[: -len_s // 2]
        i_list = {}
        for j in range(len(strings)):
            string = strings[j]
            try:
                i_list[string.index(right_half_q)] = (string, j)
            except ValueError:
                continue
        if i_list != {}:
            i_closest = sorted(i_list)[0]
            strings.append(left_half_q + i_list[i_closest][0][i_closest:])
            strings.pop(i_list[i_closest][1])
        else:
            strings.append(q)
        queue.append(strings.pop(0))
        if strings == []:
            sss = queue.pop(0)
            break

    return sss


def pmch(s):
    """Perfect Matchings and RNA Secondary Structures"""
    from math import factorial

    return factorial(s.count("A")) * factorial(s.count("G"))


def pper(n, k):
    """Partial Permutations"""
    p = 1
    for i in range(n - k + 1, n + 1):
        p *= i
        if p >= 1e6:
            p %= 1e6
    return int(p)


def prob(s, A):
    """Introduction to Random Strings"""
    from math import log10

    gc_s = s.count("G") + s.count("C")
    at_s, B = len(s) - gc_s, []
    for gc in A:
        B.append(round(log10(((gc / 2) ** gc_s) * (((1 - gc) / 2) ** at_s)), 3))
    return B


def sign(n):
    """Enumerating Oriented Gene Orderings"""
    from itertools import permutations, product

    signed_perm = []
    for perm in list(permutations(range(1, n + 1), n)):
        for cartesian in product([-1, 1], repeat=n):
            signed_perm.append(list(p * c for p, c in zip(perm, cartesian)))

    return [len(signed_perm)] + signed_perm


def sseq(fasta):
    """Finding a Spliced Motif"""
    values = list(_parse_fasta(fasta).values())
    s, t = values[0], values[1]
    i_t, indices, len_t = 0, [], len(t)
    for i_s in range(len(s)):
        if s[i_s] == t[i_t]:
            indices, i_t = indices + [i_s + 1], i_t + 1
            if i_t == len_t:
                break
    return indices


def tran(fasta):
    """Transitions and Transversions"""
    values = list(_parse_fasta(fasta).values())
    s1, s2 = values[0], values[1]
    transition, transversion = 0, 0
    for i in range(len(s1)):
        nt1, nt2 = s1[i], s2[i]
        if nt1 != nt2:
            if (
                (nt1, nt2) == ("A", "G")
                or (nt1, nt2) == ("G", "A")
                or (nt1, nt2) == ("C", "T")
                or (nt1, nt2) == ("T", "C")
            ):
                transition += 1
            else:
                transversion += 1
    return round(transition / transversion, 11)


def _read_simple_graph(lbsv):
    """Reading simple un-directed grapth in the edge list format"""
    edge_lists = _read_lbsv(lbsv)
    vertices_range = range(int(edge_lists[0].split()[0]))
    graph = [[] for vertex in vertices_range]
    for edge in edge_lists[1:]:
        u, v = list(map(int, edge.split()))
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    return graph, vertices_range


def tree(lbsv):
    """Completing a Tree"""
    graph, _vertices_range = _read_simple_graph(lbsv)
    queue = graph.pop(0)
    graph, connected_components = [True] + graph, 1
    for i, visited in enumerate(graph):
        if not queue:
            if visited == True:
                continue
            graph[i], queue = True, visited
            connected_components += 1
        while queue:
            node = queue.pop(0)
            if graph[node] != True:
                queue += graph[node]
                graph[node] = True

    return connected_components - 1


def cat(s):
    """Catalan Numbers and RNA Secondary Structures"""

    def recursive(seq, memo={}):
        if seq in memo:
            return memo[seq]
        if len(seq) <= 1:
            return 1
        c, nt0, cw, ccw = 0, seq[0], 1, 1
        for i in range(1, len(seq), 2):
            nt = seq[i]
            if (
                (nt0 == "A" and nt == "U")
                or (nt0 == "U" and nt == "A")
                or (nt0 == "C" and nt == "G")
                or (nt0 == "G" and nt == "C")
            ):
                cw = recursive(seq[1:i], memo)
                ccw = recursive(seq[i + 1 :], memo)
                c += cw * ccw % 1e6
        memo[seq] = c
        return c

    return recursive(s) % 1e6


def corr(fasta):
    """Error Correction in Reads"""
    strings = list(_parse_fasta(fasta).values())
    corrects, corrections = [], []
    for i, s in enumerate(strings):
        s_revc = revc(s)
        if (s in strings[i + 1 :] or s_revc in strings[i + 1 :]) and (
            s not in corrects or s_revc not in corrects
        ):
            corrects.append(s)
    for s in strings:
        if s in corrects or revc(s) in corrects:
            continue
        for c in corrects:
            hd = 0
            for i in range(len(s)):
                if s[i] != c[i]:
                    hd, i_wrong, right = hd + 1, i, c[i]
                if hd >= 2:
                    break
            if hd == 1:
                break
        if hd == 1:
            s_corrected = s[:i_wrong] + right + s[i_wrong + 1 :]
            corrections.append(s + "->" + s_corrected)
            continue
        for c in corrects:
            c_revc, hd = revc(c), 0
            for i in range(len(s)):
                if s[i] != c_revc[i]:
                    hd, i_wrong, right = hd + 1, i, c_revc[i]
                if hd >= 2:
                    break
            if hd == 1:
                break
        if hd == 1:
            s_corrected = s[:i_wrong] + right + s[i_wrong + 1 :]
            corrections.append(s + "->" + s_corrected)
            continue
    return corrections


def inod(n):
    """Counting Phylogenetic Ancestors"""
    return n - 2


def kmer(fasta):
    """k-Mer Composition"""
    s = list(_parse_fasta(fasta).values())[0]
    kmers = dict(zip(lexf("A C G T", 4), [0 for x in range(4 ** 4)]))
    for i in range(len(s) - 3):
        kmers[s[i : i + 4]] += 1
    return [x[1] for x in sorted(kmers.items())]


def kmp(fasta):
    """Speeding Up Motif Finding"""
    s, j, failures = list(_parse_fasta(fasta).values())[0], 0, [0]
    for k in range(1, len(s)):
        failed = False
        if s[: j + 1] == s[k - j : k + 1]:
            failures, j, failed = failures + [j + 1], j + 1, True
        else:
            for i in range(1, j + 1):
                if s[: j - i + 1] == s[k - j + i : k + 1]:
                    failures, j, failed = (
                        failures + [j - i + 1],
                        j - i + 1,
                        True,
                    )
                    break
        if not failed:
            failures, j = failures + [0], 0

    return failures


def lcsq(fasta):
    """Finding a Shared Spliced Motif"""
    strings = list(_parse_fasta(fasta).values())
    s, t = strings[0], strings[1]
    matrix = [[[0, 0] for x in range(len(t) + 1)] for y in range(len(s) + 1)]
    for i in range(len(s) + 1):
        if i == 0:
            continue
        for j in range(len(t) + 1):
            if j == 0:
                continue
            if s[i - 1] == t[j - 1]:
                matrix[i][j] = [matrix[i - 1][j - 1][0] + 1, 1]
            else:
                if matrix[i][j - 1][0] > matrix[i - 1][j][0]:
                    matrix[i][j] = [matrix[i][j - 1][0], 0]
                else:
                    matrix[i][j] = [matrix[i - 1][j][0], 2]
    lcs, i, j = "", 0, 0
    while -i - 1 >= -len(s) and -j - 1 >= -len(t):
        direction = matrix[-i - 1][-j - 1][1]
        if direction == 0:
            j += 1
        elif direction == 1:
            lcs += s[-i - 1]
            i, j = i + 1, j + 1
        elif direction == 2:
            i += 1

    return lcs[::-1]


def pdst(fasta):
    """Creating a Distance Matrix"""
    strings = list(_parse_fasta(fasta).values())
    matrix, len_s = [
        [format(0.0, "6.5f") for n in strings] for n in strings
    ], len(strings[0])
    for i in range(len(strings)):
        for j in range(len(strings)):
            if i == j:
                continue
            matrix[i][j] = format(hamm(strings[i], strings[j]) / len_s, "6.5f")
    return matrix


def rstr(N, x, s):
    """Matching Random Motifs"""
    p_s = 1
    for nt in s:
        if nt == "G" or nt == "C":
            p_s *= x / 2
        else:
            p_s *= (1 - x) / 2
    return round(1 - (1 - p_s) ** N, 3)


def sset(n):
    """Counting Subsets"""
    return int((2 ** n) % 1e6)


def eval(n, s, A):
    """Expected Number of Restriction Sites"""
    gc_s, len_s = s.count("G") + s.count("C"), len(s)
    at_s, B = len_s - gc_s, []
    for gc in A:
        p = ((gc / 2) ** gc_s) * (((1 - gc) / 2) ** at_s) * (n - len_s + 1)
        B.append(round(p, 3))
    return B


if __name__ == "__main__":
    print(sset(809))
