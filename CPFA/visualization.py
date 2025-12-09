import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import cartopy.crs as ccrs


# npy 파일 불러오기
surface_data = np.load("input_data/input_surface.npy")  # (4, 721, 1440)

# 2m 온도 (T2M, index=3)
t2m = surface_data[3, :, :]

# 위도, 경도 좌표 생성
lat = np.linspace(90, -90, 721)
lon = np.linspace(0, 359.75, 1440)

# Dataset 생성 및 저장
ds = xr.Dataset(
    {"t2m": (("lat", "lon"), t2m)},
    coords={"lat": lat, "lon": lon}
)
ds.to_netcdf("surface_temperature.nc")

# --------------------
# 시각화 (예: 전지구 지도)
ds=ds.t2m -273.15 

fig=plt.figure(figsize=(12, 6))
ax2 = fig.add_subplot(1,1,1, projection=ccrs.PlateCarree())
ax2.coastlines()
plot1= ax2.contourf(lon, lat, ds, levels=np.arange(-40,40,2), cmap="coolwarm", extend='both', transform=ccrs.PlateCarree())
plt.pcolormesh(lon, lat, t2m, shading="auto", cmap="coolwarm")
plt.colorbar(label="2m Temperature (deg C)")
plt.title("ERA5 predict 2m Temperature")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
