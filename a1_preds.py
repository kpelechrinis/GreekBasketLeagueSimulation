from scipy.stats import norm
import sys
import pandas as pd
import numpy as np
from scipy import optimize

def predictions(f,rtgs):
	games = pd.read_csv(f)
	pts_diff = [np.random.normal(rtgs['Home']+rtgs[games['home'][i]]-rtgs[games['away'][i]],12) for i in range(len(games))]		
	games['ptsDiff'] = pts_diff

	return games
