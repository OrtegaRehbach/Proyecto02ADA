from constants import SEQUENCE_DIR


def getDirectoryFiles(directory: str) -> list:
    '''
    Get the files in a directory.
    '''
    from os import listdir
    from os.path import isfile, join

    return [f for f in listdir(directory) if isfile(join(directory, f))]


def genRecords(function: callable, saveAs: str, inputDir: str) -> None:
    '''
    Generate the times records for an edit distance function and save them to a file.

    Parameters:
        - function: callable, the function to test.
        - saveAs: str, the name of the file to save the records.
        - inputDir: str, the directory where the input files are.
    '''
    from time import perf_counter as time

    files = getDirectoryFiles(inputDir)
    records = []

    for file in files:
        with open(f'{SEQUENCE_DIR}/{file}', 'r') as f:
            lines = f.readlines()
            x, y = lines[0].strip(), lines[1].strip()
            x_len, y_len = len(x), len(y)

            start = time()
            function(x, y)
            end = time()

            records.append((file, x_len, y_len, end-start))

    with open(f'./times/{saveAs}.csv', 'w') as f:
        f.write('File,Length X,Length Y,Time\n')
        for record in records:
            f.write(f'{record[0]},{record[1]},{record[2]},{record[3]}\n')
