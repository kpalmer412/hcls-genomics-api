def check_dna(sequence: str) -> bool:
    """
    Validates if the incoming payload contains only valid DNA nucleotides (A, C, G, T).
    Returns True if valid, False if corrupted/invalid.
    """
    # 1. Handle case sensitivity by converting to uppercase
    clean_sequence = sequence.upper()
    
    # 2. Define the strict whitelist allowed in the pipeline
    allowed_nucleotides = {"A", "C", "G", "T"}
    
    # 3. If the input is empty or contains any character outside the whitelist
    if not clean_sequence or not set(clean_sequence).issubset(allowed_nucleotides):
        return False # Fail fast: Pipeline should reject this payload
        
    return True # Schema is valid
    