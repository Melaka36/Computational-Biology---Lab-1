import re 
 
def search_tfbs(sequence, tfbs_dict): 
    # Remove newlines and spaces from the sequence 
    sequence = "".join(sequence.split()) 
     
    positions = {} 
    for tf, consensus_sequence in tfbs_dict.items(): 
        # Convert ambiguity codes to regular expressions 
        consensus_sequence = consensus_sequence.replace('B', '[CGT]') 
        consensus_sequence = consensus_sequence.replace('D', '[AGT]') 
        consensus_sequence = consensus_sequence.replace('H', '[ACT]') 
        consensus_sequence = consensus_sequence.replace('K', '[GT]') 
        consensus_sequence = consensus_sequence.replace('M', '[AC]') 
        consensus_sequence = consensus_sequence.replace('N', '[ACGT]') 
        consensus_sequence = consensus_sequence.replace('R', '[AG]') 
        consensus_sequence = consensus_sequence.replace('S', '[CG]') 
        consensus_sequence = consensus_sequence.replace('V', '[ACG]') 
        consensus_sequence = consensus_sequence.replace('W', '[AT]') 
        consensus_sequence = consensus_sequence.replace('Y', '[CT]') 
         
        matches = [match.start() for match in 
re.finditer(f'(?={consensus_sequence})', sequence)] 
        if matches: 
            positions[tf] = matches 
    return positions 

if __name__ == "__main__": 
    search_seq = """ 
    GACACCTCAGTACTAGGATGNNNNNNTATCAGCCTGAACTAGCAGGCCTGGTTCCAAATT 
    TTTTTATCAACACTCGTAGGGGGATTATCCTAGAGGGGGTCTGGGATTTCTTTGACATCA 
    GAGTATTTTTGCCTTGCTCCTTCACAATTTGGGAACAAATAATTTAGTGGTTATTAACCC 
    TGGCTACGCACTGGAAACTTTAAAAATAATGCTGGTATGAAATTTACACAGAGTATCGTG 
    AAAATTTTCACTGAGTACCATGTGGTTATACATTGGATAAGGCTCCAGGAAGCAGCTACT 
    GGAAGACAGCCATGCCAAGAGTGGTTAGTGGTTGGAATTTTGGCAAGTCAGTTTTAGTCT 
    GCCTTATCAAATACATGGGCATACAGATAAATCCTTAGATGGCTCTCCTACTTACTGAAA 
    CATTTTCTATCTATCTATCTATCTATCTATCTATTTGGGAAGCTATCTATCTATCTATCA 
    TTTATTTAAGGTAGTCTCTATCTGCCTCTGTCTCTGTCTGTCTCTGTGTCTCTGTGTCTG 
    TCTGCTCTCTCTCTCTCTCTGTGGGAATCTCTCTCTGTGTGTGTGTGTGTATGTGTGTGT 
    GTGTGTGTGTGGTGTGCATGAACATGAGTAAAATCCATAAGGAAACTTTCAGAGTTGGTC 
    CCTCTCCTTATATCAAATGGATCCAGGAATTAAACTCAGGTTCAATTCTTGGTGCCTTTAC 
    TAGTTGAGCCATCTCACTGGCTCTTCATCATCTTTAGAATAAACTCACTTTATTACACAC 
    ACACACACACACACAACCTGGGAGTACACACACACACACAACCAAAGCCCCAACGGAAAA 
    CTACAATATTATAATGAATACACAGGTTCTCAACATAGTCTCTGCCACGCTTGCAGACAA 
    AGATGAGTAGAAGTAGAAAGAACCAGGGAAACGTGGAGCAAGTCAGAAGGAATAACAGTC 
    AGAAGGAATAACAGTCAGAAGGAATAACAGTCAGAAGGAGTAACAGTCAGAAGGAATAGC 
    AGTCAGAAGGAATAACAGTCAGAAGACAGCACAGTCAGAAGGAATAACAGTCAGAAGGAA 
    TAACAGTCAGAAGGAATAACAGTCAGAAGGAATAACAGTCAGAAGGAATAGCAGTCAGAA 
    GGAATAACAGTCAGAAGGAATAACAGTCAGAAGGAATAACAGTCAAAGAAATAGCAGTCA 
    GAAGGAATAGCAGTCAGAAGGAATAACAGTCAAAGGAGCAGTCAGAAGGAGTAACAGTCA 
    GAAGGAATAACAGTCAGAAGGAATAACAGTCAAAGGAATAGCAGTCAGAAGGAGTAACAG 
    TCAGAGCAAACACAGAGATGACAAAGGCAATGGGGTCAGAGACTTCACCACTCTCCAAGA 
    """ 
 
    tfbs_dict = { 
        "RUNX1": "BHTGTGGTYW", 
        "TGIF1": "WGACAGB", 
        "IKZF1": "BTGGGARD" 
    } 

    positions = search_tfbs(search_seq, tfbs_dict) 
 
    for tf, tf_positions in positions.items(): 
        print(f"{tf} found at positions: {tf_positions}") 
