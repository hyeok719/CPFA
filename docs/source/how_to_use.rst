How to Use
==========

This page describes the typical usage flow of CPFA, from preparing
input data to running predictions, visualization, and evaluation.

Step 1: Prepare Input Data
--------------------------

CPFA expects a surface input file with the following structure:

- File name: ``input_surface.npy``
- Location: ``input_data`` folder
- Shape: ``(4, 721, 1440)``
- Order of variables:

  1. Mean sea level pressure (MSLP)
  2. 10m u-component of wind (U10)
  3. 10m v-component of wind (V10)
  4. 2m temperature (T2M)

ERA5 Download Guide
~~~~~~~~~~~~~~~~~~~

1. Visit the Copernicus Climate Data Store (CDS).
2. Sign up and log in.
3. Navigate to:

   *Datasets → ERA5 monthly averaged data on single levels
   from 1940 to present*

4. Use the following settings:

   - **Product type**: Monthly averaged reanalysis by hour of day
   - **Variables** (in this order):

     1. Mean sea level pressure  
     2. 10m u-component of wind  
     3. 10m v-component of wind  
     4. 2m temperature  

   - **Year / Month / Time**: select the desired range
   - **Geographical area**: global coverage
   - **Data format**: NetCDF4 (experimental)
   - **Download format**: unarchived file

5. Accept the terms of use, submit the form, and download the file.
6. Place the downloaded ERA5 file in the ``download_data`` folder.
7. Convert the downloaded data into ``input_surface.npy`` according
   to the required shape and order, and place it in ``input_data``.

Step 2: Run the Prediction
--------------------------

With the virtual environment activated and input data prepared, move
to the project root in Anaconda Prompt and run:

.. code-block:: bash

    python inference_cpu.py

(or the designated prediction script for your repository.)

This script performs the following tasks:

- Loads ``input_surface.npy`` from ``input_data``
- Loads the appropriate Pangu-Weather ONNX model (e.g. 1, 3, 6, or 24-hour)
- Executes the forward prediction
- Stores prediction results in the ``output_data`` folder

If iterative prediction is supported in your setup, you can optionally
run:

.. code-block:: bash

    python inference_iterative.py

to generate predictions over multiple lead times.

Step 3: Visualization
---------------------

After predictions are generated, you can visualize the results using:

.. code-block:: bash

    python visualization.py

This script typically reads data from ``output_data`` and produces
figures such as:

- Global maps of temperature or pressure
- Spatial plots of wind components
- Time series at specific grid points (depending on implementation)

The plots are usually saved as image files (e.g. PNG) under the
``output_data`` or a dedicated visualization subfolder.

Step 4: Evaluation
------------------

To evaluate model performance against ERA5 data, run:

.. code-block:: bash

    python evaluation.py

This script:

- Loads CPFA prediction outputs
- Loads reference ERA5 data
- Computes basic verification metrics (for example, mean error or
  other statistics depending on the implementation)
- Optionally saves summary tables or plots

Recommended Editor
------------------

CPFA can be run entirely from Anaconda Prompt, but using **Visual
Studio Code (VS Code)** is recommended for easier script execution,
debugging, and inspection of outputs.
