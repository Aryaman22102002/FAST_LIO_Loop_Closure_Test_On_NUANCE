# FAST_LIO_ON_NUANCE

This was our final project for the EECE 5554 (Robotics Sensing and Navigation) course at Northeastern University. <br>


### Data Collection
We collected data using the NUANCE autonomous car of Northeastern University. We utilized the Ouster 3D Lidar (OS1-64), the VectorNav IMU (VN-100), and the GPS sensors of the car. <br>

##### The uster 3D Lidar (OS1-64)
![OS1-Website](https://github.com/user-attachments/assets/a5c8f143-f684-43fb-bd8d-34f77c91f6be)

##### The VectorNav IMU (VN-100)
![vn-100-rugged](https://github.com/user-attachments/assets/3fca4701-d916-4213-abe7-6406af15cab0)

##### NUANCE autonomous car
 <br> <br>

We drove around Boston for about 10 minutes to collect the data. While collecting the data, we ensured that we had some loop closures in our path so that we could use them later. The exact path followed by us is provided below. <br>

![gps_utm](https://github.com/user-attachments/assets/7334b614-dba1-47e6-b06e-b0116fc04d0a)

This is the link to our dataset  - https://drive.google.com/drive/folders/1GNqsowswBNSMr-d3rEnTFEqyhZRcBWLL?usp=sharing <br>


### Aim of the project
The aim of our project was to compare the data we recorded on the FAST-LIO and LIO-SAM algorithms and compare those algorithms on the basis of loop-closure. <br>

We started off by running those algorithms on some existing datasets. After that, we tried to run them on our own dataset. We generated good results for FAST-LIO but couldn't run it on LIO-SAM due to some challenges that have been highlighted in detail in our project presentation. <br>

Although the results obtained from FAST-LIO were good, there was a small issue. There was a misalignment in our return trajectory and the trajectory when we commenced our journey. This was due to two reasons:
<li>
  The length of our path was huge.
</li>
<li>
  FAST-LIO didn't have loop-closure incorporated into it. 
</li>
<br>
Hence, we made use of FAST-LIO LC. It is an open-source repository that has loop-closure incorporated in it. The results we obtained using FAST-LIO LC, although not perfect, were much better as compared to FAST-LIO. 

### The Custom_Scripts Folder
Included in this repository is a Custom_Scripts folder used to plot the the gps data from NUANCE onto a satelite map image covering the area data was collected. We have provided a brief description of what each script's function purpose is: 

##### gps_to_csv.py
This script runs through the bag file and extracts the gps data into a csv file (output.csv) for further processing.

##### gps_kml.py
This script creates a kml file (gps_points.kml) file that can be uploaded to https://kmlviewer.nsspot.net that will automatically show all points onto Google Maps.

##### gps_plot.py
This script manually plots all of the gps points ontop of a satelite map image in longitude and latitude.

##### gps_plot_utm.py
This script manually plots all of the gps points ontop of a satelite map image in UTM coordinates, scaled local to the image.


### References

- [FAST-LIO GitHub Repository](https://github.com/hku-mars/FAST_LIO)
- [FAST-LIO Paper](https://ieeexplore.ieee.org/document/9372856)
- [LIO-SAM GitHub Repository](https://github.com/TixiaoShan/LIO-SAM)
- [LIO-SAM Paper](https://ieeexplore.ieee.org/document/9341176)
- [FAST-LIO LC GitHub Repository](https://github.com/yanliang-wang/FAST_LIO_LC)
- [Lidar_IMU_Init GitHub Repository](https://github.com/hku-mars/LiDAR_IMU_Init)


### Acknowledgements




### Contributors

- [Aryaman Shardul](https://github.com/Aryaman22102002)
- [Jaykumar Goswami]()
- [Jake Ross](https://github.com/JakeRoss12)
- [Rongxuan Zhou](https://github.com/Rongxuan-Zhou)


### Contact

- Aryaman Shardul - lnu.arya@northeastern.edu
- Jaykumar Goswami - goswami.j@northeastern.edu
- Jake Ross -
- Rongxuan Zhou - 













