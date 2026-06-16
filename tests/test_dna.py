from dna_check import check_dna

def test_valid_dna():
    assert check_dna("ACTG") == True

def test_invalid_dna():
    assert check_dna("ACTGZ") == False
