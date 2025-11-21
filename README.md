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

---

# How to Use the Project

## 1. Folder Structure
The downloaded files should be organized as follows:

root
├── input_data
│ ├── input_surface.npy
│ └── ...
├── output_data
├── pangu_weather_1.onnx
├── pangu_weather_3.onnx
├── pangu_weather_6.onnx
├── pangu_weather_24.onnx
├── inference_cpu.py
├── inference_iterative.py
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

### 4-1. ERA5 Download Guide
1. Visit https://cds.climate.copernicus.eu/  
2. Sign up and log in.  
3. Navigate to:  
   **Datasets → ERA5 monthly averaged data on single levels from 1940 to present**

### 4-2 Download Settings
- **Product type:** Monthly averaged reanalysis by hour of day  
- **Variables (must be selected in this order):**  
  1. Mean sea level pressure  
  2. 10m u-component of wind  
  3. 10m v-component of wind  
  4. 2m temperature  
- **Year / Month / Time:** Select desired range  
- **Geographical area:** Whole available region  
- **Data format:** NetCDF4 (Experimental)  
- **Download format:** Unarchived  


### 4-3. File Download
- Ensure *Terms of Use* is set to **Accepted**.  
- Click **Submit form**.  
- Download the generated file and place it inside the `input_data` folder.

---


# Running the Project 
*(VS Code recommended)*

1. Run the **prediction.py**

2. Run the **visualization.py**.  

3. Run the **evaluation.py**.


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
*(To be updated as the project evolves.)*

---

# References
*(To be added as needed.)*

---

# Version & Update History
*(To be updated.)*
