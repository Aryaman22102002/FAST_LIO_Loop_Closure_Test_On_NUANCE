import rosbag
import csv

def extract_gps_data(bag_file, output_csv, gps_topic):
    
    with rosbag.Bag(bag_file, 'r') as bag:
        with open(output_csv, mode='w', newline='') as csv_file:
            
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Timestamp', 'Latitude', 'Longitude', 'Altitude'])
            
            
            found_messages = 0
            for topic, msg, t in bag.read_messages(topics=[gps_topic]):
                try:
                   
                    latitude = msg.latitude
                    longitude = msg.longitude
                    altitude = msg.altitude
                    timestamp = t.to_sec()

                    
                    csv_writer.writerow([timestamp, latitude, longitude, altitude])
                    found_messages += 1
                except AttributeError as e:
                    print(f"Error accessing message fields: {e}")
                    continue
            
            
            if found_messages == 0:
                print(f"No messages found on topic '{gps_topic}'. Please check the bag file.")

if __name__ == "__main__":
    
    bag_file = "2024-11-26-13-44-09.bag"  
    output_csv = "output.csv"
    gps_topic = "/vehicle/gps/fix" 
    
    print(f"Extracting GPS data from {bag_file} on topic {gps_topic}...")
    extract_gps_data(bag_file, output_csv, gps_topic)
    print(f"GPS data saved to {output_csv}")
