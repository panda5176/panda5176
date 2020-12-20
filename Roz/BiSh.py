"""http://rosalind.info/problems/list-view/"""


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


def parse_fasta(fasta):
    """Parsing fasta file into dictionary. From gc"""
    strings = {}
    with open(fasta, "r") as fr:
        for string in fr.read().strip().split(">")[1:]:
            strings[string.split("\n")[0]] = "".join(string.split("\n")[1:])
    return strings


def gc(fasta):
    """Computing GC Content"""
    strings, gc_contents = parse_fasta(fasta), {}
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
    sequences = list(parse_fasta(fasta).values())
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
    strings, overlap_graphs = parse_fasta(fasta), []
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
    sequences = list(parse_fasta(fasta).values())
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
    rna_seq = rna(list(parse_fasta(fasta).values())[0])
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
    seq, palindromes = list(parse_fasta(fasta).values())[0], {}
    for len_p in range(4, 13, 2):
        for i in range(len(seq) - len_p + 1):
            if seq[i : i + len_p] == revc(seq[i : i + len_p]):
                palindromes[i + 1] = len_p
    return palindromes


def splc(fasta):
    """RNA Splicing"""
    seqs = list(parse_fasta(fasta).values())
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


def lgis(file):
    """Longest Increasing Subsequence"""
    pass


def along(fasta):
    """Genome Assembly as Shortest Superstring"""
    pass


def pmch(s):
    """Perfect Matchings and RNA Secondary Structures"""
    pass


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
    pass


def sseq(fasta):
    """Finding a Spliced Motif"""
    s, t = list(parse_fasta(fasta).values())
    i_t, indices, len_t = 0, [], len(t)
    for i_s in range(len(s)):
        if s[i_s] == t[i_t]:
            indices, i_t = indices + [i_s + 1], i_t + 1
            if i_t == len_t:
                break
    return indices


def tran(fasta):
    """Transitions and Transversions"""
    s1, s2 = list(parse_fasta(fasta).values())
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


def lexv(A, n):
    """Ordering Strings of Varying Length Lexicographically"""
    pass


def rstr(N, x, s):
    """Matching Random Motifs"""
    p_s = 1
    for nt in s:
        if nt == "G" or nt == "C":
            p_s *= x / 2
        else:
            p_s *= (1 - x) / 2
    return round(1 - (1 - p_s) ** N, 3)


def eval(n, s, A):
    """Expected Number of Restriction Sites"""
    gc_s, len_s = s.count("G") + s.count("C"), len(s)
    at_s, B = len_s - gc_s, []
    for gc in A:
        p = ((gc / 2) ** gc_s) * (((1 - gc) / 2) ** at_s) * (n - len_s + 1)
        B.append(round(p, 3))
    return B
