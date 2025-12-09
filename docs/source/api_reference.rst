API Reference
=============

This page documents the main script-level interfaces exposed by CPFA.
Each script can be treated as an entry point (API) in the workflow.

Prediction Script
-----------------

Name
~~~~

- ``inference_cpu.py`` (or equivalent prediction script)

Inputs
~~~~~~

- Environment:

  - Python 3.9.2
  - Required libraries installed in the active Conda environment

- Files:

  - ``input_data/input_surface.npy``

    - Shape: ``(4, 721, 1440)``
    - Order: ``[MSLP, U10, V10, T2M]``

  - One of the ONNX model files located in the project root:

    - ``pangu_weather_1.onnx``
    - ``pangu_weather_3.onnx``
    - ``pangu_weather_6.onnx``
    - ``pangu_weather_24.onnx``

Behavior
~~~~~~~~

- Loads the input array from ``input_surface.npy``
- Performs forward inference using the selected Pangu-Weather ONNX model
- Writes prediction results to ``output_data``

Outputs
~~~~~~~

- Numerical prediction files stored in ``output_data``.
  The specific format (e.g. NumPy arrays, NetCDF, or others) depends on
  the implementation of the script.

Iterative Prediction Script
---------------------------

Name
~~~~

- ``inference_iterative.py`` (optional component)

Purpose
~~~~~~~

- Provides multi-step or iterative predictions across longer lead times
  by chaining shorter forecasts.

Visualization Script
--------------------

Name
~~~~

- ``visualization.py``

Inputs
~~~~~~

- Prediction outputs from ``output_data``
- Optional reference data, depending on implementation

Behavior
~~~~~~~~

- Reads prediction results
- Generates figures (for example, global maps of surface variables)

Outputs
~~~~~~~

- Image files (e.g. PNG) saved under ``output_data`` or a related folder

Evaluation Script
-----------------

Name
~~~~

- ``evaluation.py``

Inputs
~~~~~~

- Prediction results from ``output_data``
- Reference ERA5 data (typically stored in ``download_data`` or
  a dedicated folder)

Behavior
~~~~~~~~

- Reads both prediction and reference data
- Computes basic comparison metrics such as differences or error
  statistics

Outputs
~~~~~~~

- Numeric metrics (e.g. printed to console or written to file)
- Optional plots summarizing model performance

Notes
-----

- The exact internal function signatures are implementation-specific
  and may evolve over time.
- Users are encouraged to inspect the script source code for additional
  details when extending or modifying CPFA.
