import csv
from simplekml import Kml

def csv_to_kml(input_csv, output_kml):
    kml = Kml()
    
    
    with open(input_csv, mode='r') as file:
        reader = csv.DictReader(file)
        
        
        for row in reader:
            latitude = float(row['Latitude'])
            longitude = float(row['Longitude'])
            kml.newpoint(name="GPS Point", coords=[(longitude, latitude)]) 
    
    
    kml.save(output_kml)
    print(f"KML file saved as {output_kml}")

if __name__ == "__main__":
    input_csv = "output.csv"  
    output_kml = "gps_points.kml"
    csv_to_kml(input_csv, output_kml)
