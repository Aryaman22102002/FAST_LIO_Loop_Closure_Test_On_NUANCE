import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv

def plot_gps_on_map_with_image(map_image_path, gps_csv, map_bounds):

    
    img = mpimg.imread(map_image_path)

    
    min_lat, max_lat = map_bounds['min_lat'], map_bounds['max_lat']
    min_lon, max_lon = map_bounds['min_lon'], map_bounds['max_lon']

    
    latitudes = []
    longitudes = []

    
    with open(gps_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            latitudes.append(float(row['Latitude']))
            longitudes.append(float(row['Longitude']))

    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(img, extent=[min_lon, max_lon, min_lat, max_lat], aspect='auto')

    
    ax.plot(longitudes, latitudes, marker='o', color='red', markersize=3, linestyle='-', label="GPS Path")

    
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('GPS Path Overlay on Map')
    ax.legend()

    
    ax.ticklabel_format(useOffset=False, style='plain', axis='x')

    
    plt.show()

if __name__ == "__main__":
    
    map_image_path = "map_image.png"  
    
    gps_csv = "output.csv"  
    
    map_bounds = {
        'min_lat': 42.33473,  
        'max_lat': 42.34106,  
        'min_lon': -71.08936, 
        'max_lon': -71.07930  
    }

    
    plot_gps_on_map_with_image(map_image_path, gps_csv, map_bounds)
