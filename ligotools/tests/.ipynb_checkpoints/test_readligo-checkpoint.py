import numpy as np
from ligotools import readligo


def test_loaddata_missing_file_returns_none_triplet():

    strain, t_or_meta, dq = readligo.loaddata("this_file_does_not_exist.hdf5")
    assert strain is None and t_or_meta is None and dq is None


def test_dq_channel_to_seglist_basic():

    channel = np.array([0,1,1,0,1,1,1,0], dtype=int)
    slices = readligo.dq_channel_to_seglist(channel, fs=2)

    # Expect two slices
    assert isinstance(slices, list) and len(slices) == 2
    s1, s2 = slices
    assert isinstance(s1, slice) and isinstance(s2, slice)

    # start/stop are multiplied by fs inside the function
    assert (s1.start, s1.stop) == (2, 6)    # (1,3) * 2
    assert (s2.start, s2.stop) == (8, 14)   # (4,7) * 2


def test_dq2segs_basic():

    channel = np.array([0,1,1,0,1,1,1,0], dtype=int)
    segs = readligo.dq2segs(channel, gps_start=100)

    # SegmentList wraps a list of (start, stop) pairs
    assert hasattr(segs, "seglist")
    assert segs.seglist == [(101, 103), (104, 107)]
