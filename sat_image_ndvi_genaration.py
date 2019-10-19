# NDVI_Genration of sat image

# loading required libraries


from osgeo import gdal
from matplotlib import pyplot as plt
import sys
import numpy as np


# loading sat daa
b=gdal.Open("\sa_image_path")


# extracting the each red and nir bands


b3=b.GetRasterBand(3)
b4=b.GetRasterBand(4)


# read each band as array 


img_b3=b3.ReadAsArray()
img_b4=b4.ReadAsArray()


# Generating NDVI Indices


ndvi = (img_b4 - img_b3) / (img_b4 + img_b3)
#ndvi = (img_b4-img_b3) / (img_b4+img_b3)


# vusualizing the generated image 


fig = plt.figure(figsize=(10, 10))
fig.set_facecolor('white')
plt.imshow(ndvi, cmap='RdYlGn') # Typically the color map for NDVI maps are the Red to Yellow to Green
plt.title('NDVI')
plt.show()


# zooming the image


fig = plt.figure(figsize=(10,10))
fig.set_facecolor('white')
plt.imshow(ndvi[8000:10000, 0:3000], cmap='RdYlGn')
plt.title('NDVI - Zoomed')
plt.show()


# saving the output file in our directory


[cols, rows] = img_b3.shape
format = "GTiff"
driver = gdal.GetDriverByName(format)
geo = b.GetGeoTransform()  
proj = b.GetProjection() 

outDataRaster = driver.Create("D:\\2016\\ndvi16_new1.tif", rows, cols, 1, gdal.GDT_Float32)
outDataRaster.SetGeoTransform(geo)##sets same geotransform as input
outDataRaster.SetProjection(proj)##sets same projection as input


outDataRaster.GetRasterBand(1).WriteArray(ndvi)

outDataRaster.FlushCache() ## remove from memory
del outDataRaster ## delete the data (not the actual geotiff)


# open output image


n= gdal.Open("D:\\2016\\ndvi16_new1.tif")

n1 = b.GetRasterBand(1)
n2=n1.ReadAsArray(1)
fig = plt.figure(figsize=(10, 10))
fig.set_facecolor('white')
plt.imshow(n, cmap='RdYlGn') # Typically the color map for NDVI maps are the Red to Yellow to Green
plt.title('ndvi')
plt.show()


