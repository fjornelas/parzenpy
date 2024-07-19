import pytest
import numpy as np
from parzenpy.parzen_smooth import parzenpy

@pytest.fixture
def sample_data():
    dt = 0.05
    Lwin = 300
    N = 778012
    h1 = np.random.rand(N) 
    Nwin = int(np.floor(N*dt/Lwin))
    N_per_window = int(np.floor(Lwin/dt))
    h1_win = np.reshape(h1[0:Nwin*N_per_window],(Nwin,N_per_window))
    freq = np.fft.rfftfreq(N,dt)
    f_sub = np.fft.rfftfreq(N_per_window,dt)
    fft = np.abs(np.fft.rfft(np.sin(h1)))
    fft_win = np.abs(np.fft.rfft(np.sin(h1_win)))
    return freq, fft, f_sub, fft_win

def test_parzen_smooth_windowed(sample_data):
    freq, fft, f_sub, fft_win = sample_data
    fc = np.logspace(-2, 2, 200)
    b = 1.5
    windowed_flag = True
    
    smoothed_fas = parzenpy.parzen_smooth(f_sub, fft_win, fc, b=b, windowed_flag=windowed_flag)
    
    assert len(smoothed_fas[0]) == len(fc)

def test_parzen_smooth_non_windowed(sample_data):
    freq, fft, f_sub, fft_win = sample_data
    fc = np.logspace(-2, 2, 200)
    b = 1.5
    windowed_flag = False
    
    smoothed_fas = parzenpy.parzen_smooth(freq, fft, fc, b=b, windowed_flag=windowed_flag)
    
    assert len(smoothed_fas) == len(fc)

def test_apply_smooth(sample_data):
    freq, fft, f_sub, fft_win = sample_data
    fc = np.logspace(-2, 2, 200)
    b = 1.5
    windowed_flag = True
    
    instance = parzenpy(f_sub, fft_win)
    smoothed_fas = instance.apply_smooth(fc, b=b, windowed_flag=windowed_flag)
    
    assert len(smoothed_fas[0]) == len(fc)

if __name__ == "__main__":
    pytest.main()
