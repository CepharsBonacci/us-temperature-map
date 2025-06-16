import pandas as pd
import folium

# Define the get_color function first
def get_color(temp):
    # Use a conditional statement to set the marker color
    if temp < 50:
        return "green"
    elif temp < 60:
        return "orange"
    else:
        return "red"

def main():
    # Create a map using the us-states.json file
    us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    # Add a tile layer to the map
    folium.TileLayer('Mapbox Bright', attr='Mapbox Bright').add_to(us_map)

    # Read the Excel file into a DataFrame
    df = pd.read_excel("/Users/cephars/Downloads/states.xlsx")

    # Loop through the rows in the DataFrame
    for index, row in df.iterrows():
        # Get the data for each state
        lat = row["Latitude"]
        lon = row["Longitude"]
        temp = row["Temperature"]

        # Add a circle marker for each state
        folium.CircleMarker(
            location=[lat, lon],
            radius=10,
            popup=str(temp) + "°F",
            fill_color=get_color(temp),
            color="grey",
            fill_opacity=0.7
        ).add_to(us_map)

    # Save the map
    us_map.save("us_map.html")

if __name__ == "__main__":
    main()
