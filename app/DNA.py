import pandas as pd
import numpy as np
import zlib, sys

DNA_CLASS = np.array(["C","T","A"])
# Tweet: A, Retweet: C, Reply: T

def get_dna(x,id=None):
	if id is None:
		id = x['user'].values[0]['name']
		
	x = x[['in_reply_to_status_id','retweeted']].copy()
	x['reply'] = x['in_reply_to_status_id'].notnull()
	
	x.drop(columns=['in_reply_to_status_id'],inplace=True)
	
	x['tweet'] = ~(x['retweeted'] | x['reply'])
	x = x.astype(int)
	
	dna = ''.join(DNA_CLASS[x.values.argmax(axis = 1)]).encode('ascii')
	# dna = bytes(dna,'ascii')
	compressed_dna = zlib.compress(dna)
	return {'name':id,
	        'DNA':dna,
	        'compressed_size':sys.getsizeof(compressed_dna),          
	        'size':sys.getsizeof(dna),
	        'compression_ratio':sys.getsizeof(dna)/sys.getsizeof(compressed_dna)}

if __name__ == "__main__":
	logging.info("This is DNA compressor method that returns dict values containg name, DNA string, compressed size, size and compression ratio")


