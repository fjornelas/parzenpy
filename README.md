# parzenpy

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11273315.svg)](https://doi.org/10.5281/zenodo.11273315)
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/fjornelas/parzenpy/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/fjornelas/parzenpy/tree/main)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/54d26dbfd8fb4a9d902081a8c7f74807)](https://app.codacy.com/gh/fjornelas/parzenpy/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![codecov](https://codecov.io/github/fjornelas/parzenpy/graph/badge.svg?token=7QATD07693)](https://codecov.io/github/fjornelas/parzenpy)
![pypi - version](https://img.shields.io/pypi/v/parzenpy)
![PyPI - License](https://img.shields.io/pypi/l/parzenpy)
[![Report Issues!](https://img.shields.io/badge/Report%20Issues-Here-1abc9c.svg)](https://github.com/fjornelas/parzenpy/issues)
[![Open Source?
Yes!](https://img.shields.io/badge/Open%20Source-Yes-green.svg)](https://github.com/fjornelas/parzenpy)

A python library that perform Parzen spectral smoothing using numpy vectorized operations very efficiently.

# Background

A Parzen window also known as a Kernel Density Estimation function which was developed by Emanuel Parzen (see reference)

> E. Parzen, “Mathematical Considerations in the Estimation of Spectra”, Technometrics, Vol. 3, No. 2 (May, 1961), pp. 167-    190.

is a non-parametric estimation method that can apply smoothing by fitting a 4th order spline window to frequency spectra. In this case we apply the function to smooth Fourier Amptlitude Spectra (FAS).

# Installation
parzenpy is available using pip and can be installed with:

`pip install parzenpy`

# Usage

A user can smooth a seismic signal using a the function apply_smoothing using a bandwidth of 1.5. Larger values will return greater smoothing

`from parzenpy.parzen_smooth import parzenpy
smooth_fas = parzenpy.apply_smooth(freq, fft, fc, b=1.5, windowed_flag=True)`

# Citation

>Ornelas,F.J.. (2024). fjornelas/parzenpy: parzenpy (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.11273315

