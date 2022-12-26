import numpy as np
import pandas as pd

# Methods for analyzing pupil-size data
"""
Metrics:
- Peak pupil-size in specified time window
- Peak latency: time between critical point in task (such as stimulus onset) and peak dilation
- Mean dilation in specified time window
- Dilation slope: steepness of increase in pupil-size in specified time window
- Intra-trial change in pupil-size
- Inter-trial change in pupil-size
"""

'''
# Get peak pupil size in time window
Params:
- arr:
- start:
- end: 

Returns: 
-
'''
def peak_pupil_size(arr, start=None, end=None):
    arr = reshape_ndarr(arr)
    
    if start is not None and end is not None:
        return np.nanmax(arr[:, start:end], axis=1)
    else:
        return np.nanmax(arr, axis=1)

    return False

'''
# Get minimum pupil size in time window
Params:
- arr:
- start:
- end: 

Returns: 
-
'''
def min_pupil_size(arr, start=None, end=None):
    arr = reshape_ndarr(arr)
    
    if start is not None and end is not None:
        return np.nanmin(arr[:, start:end], axis=1)
    else:
        return np.nanmin(arr, axis=1)

    return False

# Get peak latency in time window
def peak_latency(arr, start, end):
    arr = reshape_ndarr(arr)
    
    return np.argmax(arr[:, start:end], axis=1) - start

# Get mean pupil size in time window
def mean_pupil_size(arr, start=None, end=None):
    arr = reshape_ndarr(arr)

    if start is not None and end is not None:
        return np.mean(arr[:, start:end], axis=1)
    else:
        return np.mean(arr, axis=1)

# Get variance of pupil size in time window
def var_pupil_size(arr, start=None, end=None):
    arr = reshape_ndarr(arr)

    if start is not None and end is not None:
        return np.var(arr[:, start:end], axis=1)
    else:
        return np.var(arr, axis=1)

# Get standard deviation of pupil size in time window
def std_pupil_size(arr, start=None, end=None):
    arr = reshape_ndarr(arr)

    if start is not None and end is not None:
        return np.std(arr[:, start:end], axis=1)
    else:
        return np.std(arr, axis=1)

# Get difference in pupil size at two different times t1 and t2
def diff_pupil_size(arr, t1, t2):
    return arr[:, t2] - arr[:, t1]

# Get dilation slope in specified time window
def dilation_slope():
    pass

# Average pupil-size changes across series (intra/inter-trial changes in pupil-size) 
# Krejitz et al., 2018
def avg_pupil_size_change():
    pass


"""
Ajasse et al., 2018:

- The mean pupil size and pupil size variance computed for each fixation period (i.e., in-between two positioning saccades).
- The latency of the start of a constriction: the time between the end of a positioning saccade to the first inflection point computed on pupil signal (see aforementioned and Figure 2).
- The postsaccadic dilation amplitude: the difference of pupil size at saccade end and the beginning of constriction.
- The constriction amplitude, computed as the difference of pupil size at the beginning and the end of a constriction, defined by the inflection points computed on the pupil signal.
- The latency of the end of the pupil constriction: the time between the positioning saccade and the second inflection point.
- The constriction velocity, defined in percentage of baseline per second: the constriction amplitude divided by the time between the first and the second inflection points of the pupil signal.
- The quality of fixation: the percentage of the time during which the gaze position was inside a spatial window of 1° centered on the target disks.
"""

def reshape_ndarr(arr):
    assert isinstance(arr, np.ndarray)

    if arr.ndim == 1:
        arr = arr.reshape(-1, arr.shape[0])
    
    return arr
