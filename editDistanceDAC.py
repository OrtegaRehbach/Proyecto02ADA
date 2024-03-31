def editDistanceDAC(str1: str, str2: str) -> int:
    '''
    Levenshtein distance or Edit distance using the Divide and Conquer approach
    '''
    # Base cases
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    # Divide
    if str1[-1] == str2[-1]:
        return editDistanceDAC(str1[:-1], str2[:-1])
    
    # Conquer and Combine
    return 1 + min(
        editDistanceDAC(str1[:-1], str2),     # Deletion
        editDistanceDAC(str1, str2[:-1]),     # Insertion
        editDistanceDAC(str1[:-1], str2[:-1]) # Substitution
    )
