Getting Started
===============

This page describes the prerequisites, installation steps,
and initial setup required to run CPFA on a Windows environment.

Prerequisites
-------------

To use CPFA, you need:

- **Windows** operating system
- **Anaconda** (Python distribution)
- **Python 3.9.2**
- An active internet connection to download ERA5 data

Download the Repository
-----------------------

1. Open your web browser and navigate to the CPFA GitHub repository.
2. Download the project folder (for example, as a ZIP file).
3. Extract or move the downloaded folder to the ``C:`` drive.

After extraction, the folder will be similar to::

    C:\CPFA\

Install Anaconda
----------------

1. Visit the Anaconda website.
2. Download the installer for Windows.
3. Install Anaconda (installation in the ``C:`` drive is recommended).

Install Python 3.9.2
--------------------

Although Anaconda provides its own Python distribution, CPFA is
documented and tested with **Python 3.9.2**.

1. Visit the official Python website.
2. Download the installer for Python 3.9.2.
3. Complete the installation.

Creating a Conda Environment
----------------------------

1. Open **Anaconda Prompt** as Administrator.
2. Move to the ``C:`` drive by entering ``cd..`` repeatedly until the
   prompt shows::

       C:\>

3. Navigate to the CPFA project folder, for example::

       cd CPFA

4. Create a new virtual environment with Python 3.9.2::

       conda create -n cpfa_env python=3.9.2

5. Activate the environment::

       conda activate cpfa_env

Installing Required Libraries
-----------------------------

With the environment activated, install the required packages:

.. code-block:: bash

    pip install numpy pandas matplotlib xarray cartopy
    pip install onnx==1.13.1
    pip install onnxruntime==1.14.0

After installation, the environment is ready to run CPFA.

Folder Structure
----------------

The project files should be organized as follows:

.. code-block:: text

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
    ├── inference_cpu.py          (or prediction script)
    ├── inference_iterative.py    (optional iterative prediction)
    ├── visualization.py
    └── evaluation.py

Make sure the ONNX model files and scripts are placed at the project
root as shown above.
