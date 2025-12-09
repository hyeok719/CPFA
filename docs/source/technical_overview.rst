Technical Overview
==================

This page describes the technical structure of CPFA, including
the main components and overall workflow.

High-Level Architecture
-----------------------

CPFA (Climate Prediction For All) implements a four-stage workflow:

1. **Data collection**
2. **Future climate prediction (Pangu-Weather ONNX model)**
3. **Visualization of prediction results**
4. **Model performance evaluation (comparison with ERA5)**

Core Components
---------------

The repository is organized around the following elements:

- **ONNX model files**

  - ``pangu_weather_1.onnx``
  - ``pangu_weather_3.onnx``
  - ``pangu_weather_6.onnx``
  - ``pangu_weather_24.onnx``

- **Data folders**

  - ``download_data``: raw downloaded ERA5 data
  - ``input_data``: prepared input arrays (e.g. ``input_surface.npy``)
  - ``output_data``: prediction and evaluation outputs

- **Python scripts**

  - ``inference_cpu.py`` (or equivalent prediction script)
  - ``inference_iterative.py`` (optional multi-step prediction)
  - ``visualization.py``
  - ``evaluation.py``

Data Flow
---------

The typical data flow is as follows:

1. **ERA5 data download**

   ERA5 reanalysis data is downloaded from the Copernicus Climate Data
   Store and placed in ``download_data``.

2. **Input preparation**

   The ERA5 data is preprocessed into an ``input_surface.npy`` file,
   stored in ``input_data`` with the required shape and variable order.

3. **Model inference**

   The prediction script loads ``input_surface.npy`` and one of the
   Pangu-Weather ONNX models, runs inference, and writes outputs to
   ``output_data``.

4. **Visualization**

   The visualization script reads prediction outputs and generates
   plots for analysis.

5. **Evaluation**

   The evaluation script compares CPFA predictions with ERA5 reference
   data and computes metrics.

Technology Stack
----------------

CPFA uses the following main technologies:

- **Python 3.9.2**
- **NumPy, pandas, xarray** for data handling
- **matplotlib, cartopy** for visualization
- **ONNX** and **ONNX Runtime** for Pangu-Weather model inference
- **Anaconda** for environment management on Windows

Design Characteristics
----------------------

- Focused on clarity and reproducibility rather than performance tuning
- Designed for Windows-based classroom and self-study environments
- Emphasizes a linear, script-based workflow that is easy to follow
  for users new to climate prediction models
