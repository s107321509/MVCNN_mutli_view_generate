# BlenderPhong
First, thanks for the work of weitang, this code is revised from https://github.com/WeiTang114/BlenderPhong.



This is an output from `airplane.off`:

<img src="https://github.com/s107321509/Use-blender-generate-multi-view-image-from-3D-model/blob/master/img/Allomyrina_12view.PNG">

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

### Single .off 
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
