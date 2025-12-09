Configuration Guide
===================

This page explains how CPFA is configured in practice, including
environment settings, folder layout, and key file conventions.

Overview
--------

The current version of CPFA does **not** use a central configuration
file (such as YAML or JSON). Instead, configuration is defined by:

- The Python and library versions used in the Conda environment
- The folder structure in the project root
- The names and locations of input and output files
- The choice of ONNX model file

Environment Configuration
-------------------------

Recommended environment:

- Operating system: Windows
- Python: 3.9.2
- Package manager: Conda
- Required libraries:

  - ``numpy``
  - ``pandas``
  - ``matplotlib``
  - ``xarray``
  - ``cartopy``
  - ``onnx==1.13.1``
  - ``onnxruntime==1.14.0``

Create and activate the environment as described in
:doc:`getting_started`.

Folder Configuration
--------------------

Required folders:

- ``download_data``

  - Stores downloaded ERA5 data (NetCDF or similar).

- ``input_data``

  - Stores prepared input arrays such as ``input_surface.npy``.

- ``output_data``

  - Stores prediction outputs, visualization products, and evaluation
    results.

These folder names are assumed by the scripts and should be preserved
unless you adapt the code.

Input File Configuration
------------------------

CPFA expects an input file:

- Name: ``input_surface.npy``
- Location: ``input_data`` folder
- Shape: ``(4, 721, 1440)``
- Variable order: ``[MSLP, U10, V10, T2M]``

If you change the filename, shape, or order, you must update the
corresponding script sections that load and interpret this array.

Model Selection
---------------

Available Pangu-Weather ONNX models in the project root:

- ``pangu_weather_1.onnx``
- ``pangu_weather_3.onnx``
- ``pangu_weather_6.onnx``
- ``pangu_weather_24.onnx``

The prediction script chooses one of these models internally. To change
the model used:

- Locate the model-loading section in the prediction script and update
  the filename as needed.

Output Configuration
--------------------

Prediction, visualization, and evaluation outputs are written into
the ``output_data`` folder by default. Outputs may include:

- Numerical arrays
- Diagnostic logs
- Plot images

If you want to change the output location, modify the relevant paths
in the scripts.

Extending Configuration
-----------------------

Future versions of CPFA may introduce a more formal configuration file.
For now, the settings described above form the effective configuration
of the system.
