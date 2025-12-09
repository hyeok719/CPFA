Maintenance and Troubleshooting
===============================

This page provides guidance on keeping CPFA up to date and resolving
typical issues.

Maintenance
-----------

Updating the Repository
~~~~~~~~~~~~~~~~~~~~~~~

To update CPFA to the latest version:

1. Open Anaconda Prompt.
2. Navigate to the CPFA project folder.
3. Pull the latest changes from GitHub (if using git directly)::

       git pull origin main

Reinstalling Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~

If dependencies become inconsistent, you can reinstall them:

.. code-block:: bash

    conda activate cpfa_env
    pip install --upgrade --force-reinstall \
        numpy pandas matplotlib xarray cartopy \
        onnx==1.13.1 onnxruntime==1.14.0

Managing Output Size
~~~~~~~~~~~~~~~~~~~~

Prediction and visualization steps can generate a large number of
files. Periodically clean the ``output_data`` folder by removing
old experiments that are no longer needed.

Troubleshooting
---------------

Environment Not Found
~~~~~~~~~~~~~~~~~~~~~

**Symptom:** Conda reports that the environment cannot be found.

- Ensure the environment name is correct (for example, ``cpfa_env``).
- Run ``conda env list`` to see all available environments.

Import Errors
~~~~~~~~~~~~~

**Symptom:** ``ModuleNotFoundError`` or similar import issues.

- Confirm that the correct environment is activated.
- Reinstall the required packages.
- Verify that the Python version is 3.9.2 as documented.

ONNX Runtime Errors
~~~~~~~~~~~~~~~~~~~

**Symptom:** Errors mentioning ONNX or ONNX Runtime when running
the prediction script.

- Check that ONNX and ONNX Runtime versions match the documented
  versions:

  - ``onnx==1.13.1``
  - ``onnxruntime==1.14.0``

- Reinstall both packages to ensure consistency.

Incorrect or Missing Input Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Symptom:** The prediction script fails because it cannot find
``input_surface.npy`` or because the file has an unexpected shape.

- Verify that ``input_surface.npy`` exists in the ``input_data``
  folder.
- Confirm that the array shape is ``(4, 721, 1440)`` and that
  the variable order is correct.

Unexpected Prediction Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Symptom:** Predictions look unrealistic or inconsistent.

- Check that the ERA5 data used to generate ``input_surface.npy``
  matches the documented variable order and units.
- Confirm that the correct ONNX model file is being used.

Getting Additional Help
-----------------------

If an issue persists:

- Open a GitHub issue with:

  - A clear problem description
  - Steps to reproduce
  - Error messages or logs
  - Environment details (OS, Python, package versions)

- Alternatively, contact the maintainers via the e-mail addresses
  listed on the project communication channels.
