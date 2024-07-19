import pytest
import numpy as np
from parzenpy.parzen_smooth import parzenpy

@pytest.fixture
def sample_data():
    freq = np.linspace(0, 10, 1000)  # Sample frequency data
    fft = np.abs(np.fft.fft(np.sin(freq)))  # Sample FFT amplitude data
    return freq, fft

def test_parzen_smooth_windowed(sample_data):
    freq, fft = sample_data
    fc = np.linspace(1, 9, 5)  # Sample resampled frequencies
    b = 1.5
    windowed_flag = True
    
    smoothed_fas = parzenpy.parzen_smooth(freq, fft, fc, b=b, windowed_flag=windowed_flag)
    
    assert len(smoothed_fas) == len(fc)
    assert np.all(np.isfinite(smoothed_fas))

def test_parzen_smooth_non_windowed(sample_data):
    freq, fft = sample_data
    fc = np.linspace(1, 9, 5)  # Sample resampled frequencies
    b = 1.5
    windowed_flag = False
    
    smoothed_fas = parzenpy.parzen_smooth(freq, fft, fc, b=b, windowed_flag=windowed_flag)
    
    assert len(smoothed_fas) == len(fc)
    assert np.all(np.isfinite(smoothed_fas))

def test_apply_smooth(sample_data):
    freq, fft = sample_data
    fc = np.linspace(1, 9, 5)  # Sample resampled frequencies
    b = 1.5
    windowed_flag = True
    
    instance = parzenpy(freq, fft)
    smoothed_fas = instance.apply_smooth(fc, b=b, windowed_flag=windowed_flag)
    
    assert len(smoothed_fas) == len(fc)
    assert np.all(np.isfinite(smoothed_fas))

if __name__ == "__main__":
    pytest.main()

