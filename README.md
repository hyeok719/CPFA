# **Please refer to the ReadTheDocs site for a more structured and detailed version of this README.**  
https://cpfa.readthedocs.io/en/main/index.html
---
# CPFA Project Overview

CPFA is an **open-source project designed to make climate prediction data easy to analyze and visualize using the Pangu-Weather model**.  
Traditional climate models often require **complex data preparation, difficult environment setup, and extensive expertise to interpret the results**.  
This project reduces such barriers and focuses on the following goals:

- Enable **fast and simple execution** of Pangu-Weather-based predictions  
- Provide **beginner-friendly data preparation steps**  
- Deliver a **complete analysis workflow**, from prediction to visualization and model performance evaluation  
- Offer detailed **Windows-based setup and execution instructions**

---

# Project Structure

This project follows a four-stage workflow:

1. **Data collection**  
2. **Future climate prediction** (using Pangu-Weather)  
3. **Visualization of predicted data**  
4. **Model performance evaluation** (comparison with ERA5 data)

---

# Installation Guide

## 1. Download the GitHub Repository
- Download the project folder from GitHub.
- Move the downloaded folder to the **C: drive**.

## 2. Install Anaconda
- Visit https://www.anaconda.com/  
- Install Anaconda (installation in the **C: drive** is recommended).

## 3. Install Python 3.9.2
- Visit https://www.python.org/  
- Download and install Python 3.9.2.

## 4. Download model  
Please download the four pre-trained models (~1.1GB each) from Google drive or Baidu netdisk:  
- The 1-hour model (pangu_weather_1.onnx): 'https://drive.google.com/file/d/1fg5jkiN_5dHzKb-5H9Aw4MOmfILmeY-S/view'
- The 3-hour model (pangu_weather_3.onnx): 'https://drive.google.com/file/d/1EdoLlAXqE9iZLt9Ej9i-JW9LTJ9Jtewt/view'
- The 6-hour model (pangu_weather_6.onnx):  'https://drive.google.com/file/d/1a4XTktkZa5GCtjQxDJb_fNaqTAUiEJu4/view'
- The 24-hour model (pangu_weather_24.onnx): 'https://drive.google.com/file/d/1lweQlxcn9fG0zKNW8ne1Khr9ehRTI6HP/view'


---

# How to Use the Project

## 1. Folder Structure
The downloaded files should be organized as follows:

root  
├── download_data  
│   └── ...  
├── input_data  
│   └── ...  
├── output_data  
│   └── ...  
├── pangu_weather_1.onnx  
├── pangu_weather_3.onnx  
├── pangu_weather_6.onnx  
├── pangu_weather_24.onnx  
├── prediction.py  
├── transform_nc_to_npy.py  
├── visualization.py  
└── evaluation.py  

## 2. Create a Virtual Environment

1. Search for **Anaconda Prompt** and run as Administrator.  
2. Navigate to the C: drive by entering `cd..` repeatedly until the path becomes `C:\>`.  
3. Move into the GitHub project folder: cd CPFA_Folder
4. Create a virtual environment: conda create -n <env_name> python=3.9.2 (Example: conda create -n myenv python=3.9.2)
5. Activate the environment: conda activate <env_name> (When activation is successful, the environment name appears to the left of the prompt.)

## 3. Install Required Libraries

- **Install dependencies:**
    - pip install numpy, pandas, matplotlib, xarray, cartopy,

    - pip install onnx==1.13.1

    - pip install onnxruntime==1.14.0


## 4. Input Data Preparation

### Structure of `input_surface.npy`
- Shape: **(4, 721, 1440)**
- Order: `[MSLP, U10, V10, T2M]`
### Structure of `input_upper.npy`
- Shape: **(5, 13, 721, 1440)**
- Order: `[z, q, t, u, v]`
### 4-1. ERA5 Download Guide
1. Visit https://cds.climate.copernicus.eu/  
2. Sign up and log in.  
3. Navigate to:  
   input_surface.npy → ERA5 hourly data on single levels from 1940 to present  
   input_upper.npy → ERA5 hourly data on pressure levels from 1940 to present
### 4-2 Download Settings
- **input_surface.npy**

  - **Product type**:  Reanalysis
  - **Variables** (in this order):  

     1. Mean sea level pressure  
     2. 10m u-component of wind  
     3. 10m v-component of wind  
     4. 2m temperature  

  - **Year / Month / Day / Time**: select the desired range
  - **Geographical area**: global coverage
  - **Data format**: NetCDF4 (experimental)
  - **Download format**: unarchived file  

- **input_upper.npy**
   - **Product type**: Reanalysis
   - **Variables** (in this order):  
     1. Geopotential  
     2. Specific humidity  
     3. Temperature   
     4. U-component of wind   
     5. V-component of wind  
   - **Pressure level**: 1000hPa, 925hPa, 850hPa, 700hPa, 600hPa, 500hPa, 400hPa, 300hPa, 250hPa, 200hPa, 150hPa, 100hPa and 50hPa in the exact order  
   - **Year / Month / Day / Time**: select the desired range  
   - **Geographical area**: global coverage  
   - **Data format**: NetCDF4 (experimental)  
   - **Download format**: unarchived file  


### 4-3. File Download
- Ensure *Terms of Use* is set to **Accepted**.  
- Click **Submit form**.  
- Download the generated file and place it inside the `download_data` folder.

---


# Running the Project 
*(VSCode recommended)*

1. Run the **transform_nc_to_npy.py**

2. Run the **prediction.py**

3. Run the **visualization.py**.  

4. Run the **evaluation.py**.


---

# Communication
- If you have questions, bug reports, or feature requests, please use **GitHub Issues**.  
      This helps us keep discussions transparent and accessible to all users.

- For urgent matters or private communication, you may contact the maintainers:
    - hyeok719 — jjh10197@gmail.com  
    - woobin723-cmd — woobin723@gmail.com  

---

#  License
- Apache License 2.0

---

# Bugs & Debugging
If you encounter unexpected behavior, broken functionality, or issues during installation or execution, please follow the steps below:

1. Check the Documentation
    Review the troubleshooting section in the official documentation to verify whether your issue is already addressed.

2. Verify Your Environment
    Ensure that your Python version, required libraries, and OS environment match the supported configurations described in the docs.

3. Reproduce the Issue
    Try to reproduce the bug in a clean environment (e.g., a new virtual environment) to confirm that the issue is project-related.

4. Submit a Bug Report
    If the problem persists, please open an issue in the GitHub repository with the following information:
    - Steps to reproduce
    - Error logs and stack traces
    - System details (OS, Python version, hardware)
    - Expected behavior vs. actual behavior  
**→ GitHub Issues: https://github.com/hyeok719/CPFA/issues**

---

# References
Below is a list of key resources and research materials referenced in the CPFA project:

- Pangu-Weather: Forecasting With Advanced Deep Learning Models  
    A foundational model used for climate prediction within this project.

- ERA5 Reanalysis Data (ECMWF)  
    The primary climate reanalysis dataset used for input and evaluation.

- Xarray Documentation  
    For handling multidimensional climate data structures.

- Cartopy Documentation  
    Used for geographic visualization and map projections.

- NumPy & SciPy Libraries  
    Essential for numerical computing and data preprocessing.

- Matplotlib  
    Used for generating climate maps, vector field plots, and statistical figures.
---
