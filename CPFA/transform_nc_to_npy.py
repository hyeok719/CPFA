import xarray as xr
import numpy as np
import os

# 1. NC 파일 경로 지정
nc_surface = 'download_data/input_surface.nc'
npy_surface = 'input_data/input_surface.npy'
nc_upper = 'download_data/input_upper.nc'
npy_upper = 'input_data/input_upper.npy'


sur_var_list=['msl','u10', 'v10', 't2m']
upper_var_list=['z', 'q', 't', 'u', 'v']
level_dim = 'pressure_level'
lat_dim   = 'latitude'
lon_dim   = 'longitude'

ds_surface = xr.open_dataset(nc_surface)
surface_list=[]
for var in sur_var_list:
    da_surface=ds_surface[var]
    da_surface=da_surface.squeeze('valid_time')
    da_surface=da_surface.transpose(lat_dim, lon_dim)
    arr=da_surface.values
    surface_list.append(arr)
upper_array = np.stack(surface_list, axis=0)
np.save(npy_surface, upper_array)

ds = xr.open_dataset(nc_upper)
stacked_list=[]
for var in upper_var_list:
    da=ds[var]
    da=da.squeeze('valid_time')
    da=da.transpose(level_dim, lat_dim, lon_dim)
    arr=da.values
    stacked_list.append(arr)
upper_array = np.stack(stacked_list, axis=0)
np.save(npy_upper, upper_array)

