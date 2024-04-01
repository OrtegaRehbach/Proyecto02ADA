from tests import editDistanceTest
from editDistanceDP import editDistanceDP
from editDistanceDAC import editDistanceDAC

print('Running tests...')
print('DP')
editDistanceTest(editDistanceDP)
print('DAC')
editDistanceTest(editDistanceDAC)
