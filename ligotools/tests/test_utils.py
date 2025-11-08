import numpy as np
from scipy.signal import windows
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import h5py
import json
import os
from ligotools.utils import whiten, write_wavfile, reqshift

# --- Test whiten ---
def test_whiten():
    # Create dummies
    fs = 4096
    dt = 1.0 / fs
    t = np.linspace(0, 1, fs)
    strain = np.sin(2 * np.pi * 30 * t)   
    psd = np.ones_like(t[:fs//2+1])       
    interp_psd = interp1d(np.linspace(0, fs/2, len(psd)), psd, fill_value="extrapolate")

    white = whiten(strain, interp_psd, dt)

    # Check output
    assert not np.isnan(white).any()
    
# --- Test reqshift ---
def test_reqshift():
    fs = 4096
    t = np.linspace(0, 1, fs)
    signal = np.sin(2 * np.pi * 100 * t)
    shifted = reqshift(signal, fshift=100, sample_rate=fs)

    # Shape should be preserved
    assert shifted.shape == signal.shape
    # Output should be real-valued
    assert np.isrealobj(shifted)


# --- Test write_wavfile ---
def test_write_wavfile(tmp_path):
    # Create dummies
    data = np.random.randn(1000)
    fs = 4096
    filename = tmp_path / "test.wav"

    write_wavfile(filename, fs, data)