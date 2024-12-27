import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
import utm  

def plot_gps_on_map_with_image_utm(map_image_path, gps_csv, map_bounds_utm):

    
    img = mpimg.imread(map_image_path)

   
    min_easting, max_easting = map_bounds_utm['min_easting'], map_bounds_utm['max_easting']
    min_northing, max_northing = map_bounds_utm['min_northing'], map_bounds_utm['max_northing']

    
    normalized_eastings = []
    normalized_northings = []

   
    with open(gps_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            latitude = float(row['Latitude'])
            longitude = float(row['Longitude'])
            easting, northing, _, _ = utm.from_latlon(latitude, longitude)  
            normalized_eastings.append(easting - min_easting)  
            normalized_northings.append(northing - min_northing)  

    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(img, extent=[0, max_easting - min_easting, 0, max_northing - min_northing], aspect='auto')

    
    ax.plot(normalized_eastings, normalized_northings, marker='o', color='red', markersize=3, linestyle='-', label="GPS Path (UTM)")

   
    ax.set_xlabel('Easting (m)')
    ax.set_ylabel('Northing (m)')
    ax.set_title('GPS Path Overlay on Map')
    ax.legend()

   
    plt.show()

if __name__ == "__main__":
    
    map_image_path = "map_image.png"  
    
    gps_csv = "output.csv"  
    

    min_easting, min_northing, _, _ = utm.from_latlon(42.33473, -71.08936)
    max_easting, max_northing, _, _ = utm.from_latlon(42.34106, -71.07930)

    map_bounds_utm = {
        'min_easting': min_easting,   
        'max_easting': max_easting,   
        'min_northing': min_northing, 
        'max_northing': max_northing  
    }

   
    plot_gps_on_map_with_image_utm(map_image_path, gps_csv, map_bounds_utm)
