from constants import SEQUENCE_DIR_HARD, SEQUENCE_DIR_EASY
from editDistanceDP import editDistanceDP as dp
from editDistanceDAC import editDistanceDAC as dac
from genRecords import genRecords as gr

print('Generating records for the edit distance functions...')
print('DP')
gr(dp, 'dp', SEQUENCE_DIR_HARD)
print('DP EASY')
gr(dp, 'dp_easy', SEQUENCE_DIR_EASY)
print('DAC')
gr(dac, 'dac', SEQUENCE_DIR_EASY)
