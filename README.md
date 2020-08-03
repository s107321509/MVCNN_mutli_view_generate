# Use Blender to generate multi-view insect images from 3D insect model

You can download our open source 3d insect model from here　　
https://drive.google.com/drive/folders/1xJpZU-etuRomYk051nIgoM8YXlo1JYDy?usp=sharing　　

This is an output from `Allomyrina_01.`:

<img src="https://i.ibb.co/XDYRBZK/Allomyrina-12view.png" alt="Allomyrina-12view" border="0">  

If your model file is .off format , you must use [blender-off-addon](https://github.com/alextsui05/blender-off-addon) for .off importing.

## Requirements
 - [Blender](https://www.blender.org/)

## Usage
Because the blender install path is various with different OS,  you should assign the absolute install path for Blender in WIN10

### Run with Blender

```bash
<blender install path> phong.blend --background --python phong.py -- <model file> <output dir>
```
The followings are examples, you should change the absolute blender install path in win10.

### Single model
Win10:

```bash
"C:\Program Files\Blender Foundation\Blender\blender.exe" phong.blend --background --python phong.py -- .\\dataset_samples\\Allomyrina_01.stl .\\single_samples_MV
```

Ubuntu:

```bash
blender phong.blend --background --python phong.py -- ./dataset_samples/Allomyrina_01.stl ./single_samples_MV
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
