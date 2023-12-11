# from Bio import SeqIO
# from Bio.SeqUtils import GC


# def find_cpg_islands(dna_sequence, min_gc=0.5, min_length=200, min_obs_exp=60):
    
#     cpg_islands = []
#     for i in range(len(dna_sequence) - min_length):
#         window = dna_sequence[i:i+min_length]
#         gc_content = GC(window)
#         obs_exp_cpg = (window.count("CG") / len(window)) / ((window.count("C") + window.count("G")) / 2)
#         if gc_content >= min_gc and obs_exp_cpg >= min_obs_exp:
#             cpg_islands.append({
#                 "start": i+1,
#                 "end": i+min_length,
#                 "gc_content": gc_content,
#                 "obs_exp_cpg": obs_exp_cpg
#             })
#     return cpg_islands

# # Example usage
# dna_sequence = "GGCGGTATCGATCTCGTCTATCACGGCTAACGCGCGGCCGCAACCGGGGCGGCCAGGGCCGCAAGCGGCGGCCGCTCGATCTCGATCTCATCACGCGTATCGCGGCCGCGCGTATCACGGCT"

# cpg_islands = find_cpg_islands(dna_sequence)

# if cpg_islands:
#     print("Found CpG islands:")
#     for cpg_island in cpg_islands:
#         print(f"\tStart: {cpg_island['start']}, End: {cpg_island['end']}, GC content: {cpg_island['gc_content']:.2f}, Obs/Exp CpG: {cpg_island['obs_exp_cpg']:.2f}")
# else:
#     print("No CpG islands found.")
from Bio.Seq import Seq 
from Bio.SeqUtils import nt_search
dna_seq = Seq(input("Enter the DNA sequence: "))
dna_seq_str = str(dna_seq)

def find_cpg_islands(sequence) :
    cpg_positions = nt_search (sequence, "CG") [1:]
    islands = []
    current_island = []
    for pos in cpg_positions:
        if not current_island or pos == current_island[-1] + 1:
            current_island.append (pos)
        else:
            islands.append (current_island)
            current_island = [pos]
    islands.append (current_island)
    return islands
cpg_islands = find_cpg_islands(dna_seq_str)
print("CpG Islands found in:", cpg_islands)