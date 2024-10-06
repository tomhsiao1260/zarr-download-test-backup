import os
import zarr
import numpy as np
import tifffile
import shutil

zdir = 'pi.zarr'

# data = zarr.open('../scroll2zarr-learn-forward/scroll.zarr/0/', mode="r")
data = zarr.open(f'{zdir}/0/', mode="r")
data = np.array(data)

if os.path.exists('stack'):
    shutil.rmtree('stack')

os.makedirs('stack', exist_ok=True)

print(data.shape)
print(np.min(data))
print(np.max(data))

for i in range(data.shape[0]):
    filename = os.path.join('stack', f'{i:03d}.tif')
    tifffile.imwrite(filename, data[i])
