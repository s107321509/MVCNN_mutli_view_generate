# Use Blender to generate multi-view insect images from 3D models

This is an output from `Allomyrina_01.`:

<a href="https://ibb.co/vhXn5xT"><img src="https://i.ibb.co/m0NWsC2/Allomyrina-12view.png" alt="Allomyrina-12view" border="0" /></a>  

We use [blender-off-addon](https://github.com/alextsui05/blender-off-addon) for off importing support.

## Requirements
 - [Blender](https://www.blender.org/)

## Usage
Because the blender install path is various with different OS,  you should assign the absolute install path for Blender in WIN10

### Run with Blender

```bash
<blender install path> phong.blend --background --python phong.py -- <model file> <output dir>
```
The followings are examples, you should change the absolute blender install path in win10.

### Single.stl
Win10:

```bash
"C:\Program Files\Blender Foundation\Blender\blender.exe" phong.blend --background --python phong.py -- .\\single_off_samples\\airplane_0001.off .\\single_samples_MV
```

Ubuntu:

```bash
blender phong.blend --background --python phong.py -- ./single_off_samples/airplane_0001.off ./single_samples_MV
```



### Multiple models

Win10:

```bash
"C:\Program Files\Blender Foundation\Blender\blender.exe" phong.blend --background --python phong.py -- dataset.txt .\dataset_samples_MV
```

Ubuntu:

```bash
blender phong.blend --background --python phong.py -- dataset.txt ./dataset_samples_MV
```
