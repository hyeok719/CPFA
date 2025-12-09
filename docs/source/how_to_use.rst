How to Use
==========

This page describes the typical usage flow of CPFA, from preparing
input data to running predictions, visualization, and evaluation.

Step 1: Prepare Input Data
--------------------------

CPFA expects a surface input file with the following structure:

- File name: ``input_surface.npy`` 
- Location: ``download_data`` folder
- Shape: ``(4, 721, 1440)``
- Order of variables:

  1. Mean sea level pressure (MSLP)
  2. 10m u-component of wind (U10)
  3. 10m v-component of wind (V10)
  4. 2m temperature (T2M)

- File name: ``input_upper.npy`` 
- Location: ``download_data`` folder
- Shape: ``(5, 13, 721, 1440)``
- Order of variables:

  1. z(Geopotential) 
  2. q(Specific humidity)
  3. t(Temperature) 
  4. u(Zonal wind) 
  5. v(Meridional wind)

ERA5 Download Guide
~~~~~~~~~~~~~~~~~~~

1. Visit the Copernicus Climate Data Store (CDS).
2. Sign up and log in.
3. Navigate to:
input_surface.npy → ERA5 monthly averaged data on single levels from 1940 to present  
input_upper.npy → ERA5 monthly averaged data on pressure levels from 1940 to present

4. Use the following settings:
**input_surface.npy**
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

**input_upper.npy**  
   - **Product type**: Monthly averaged reanalysis by hour of day  
   - **Variables** (in this order):  
     1. Geopotential  
     2. Specific humidity  
     3. Temperature   
     4. U-component of wind   
     5. V-component of wind  
   - **Pressure level**: 1000hPa, 925hPa, 850hPa, 700hPa, 600hPa, 500hPa, 400hPa, 300hPa, 250hPa, 200hPa, 150hPa, 100hPa and 50hPa in the exact order  
   - **Year / Month / Time**: select the desired range  
   - **Geographical area**: global coverage  
   - **Data format**: NetCDF4 (experimental)  
   - **Download format**: unarchived file  

5. Accept the terms of use, submit the form, and download the file.  
6. Place the downloaded ERA5 files in the ``download_data`` folder.  

Step 2: Transformate file
--------------------------
Run 
.. code-block:: bash

    python transform_nc_to_npy.py  

Check whether the newly generated data has been successfully created in the input_data folder.  

Step 3: Run the Prediction
--------------------------

With the virtual environment activated and input data prepared, move
to the project root in Anaconda Prompt and run:

.. code-block:: bash

    python prediction.py

This script performs the following tasks:

- Loads ``input_surface.npy`` from ``input_data``
- Loads the appropriate Pangu-Weather ONNX model (e.g. 1, 3, 6, or 24-hour)
- Executes the forward prediction
- Stores prediction results in the ``output_data`` folder


Step 4: Visualization
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

Step 5: Evaluation
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




