def editDistanceTest(function: callable) -> None:
    '''
    Some test cases for the editDistance function.
    '''
    assert function("kitten", "sitting") == 3
    assert function("kitten", "kitten") == 0
    assert function("kitten", "kittens") == 1
    assert function("kitten", "kitt") == 2
    assert function("kitten", "kit") == 3
    assert function('sit', 'kiit') == 2
    assert function('saturday', 'sunday') == 3
    assert function('sunday', 'saturday') == 3
