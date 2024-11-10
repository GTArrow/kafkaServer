from shapely.geometry import Polygon, Point
import random

# Print the forest boundary coordination and input new coordinations in a map
def generate_html_map(original_coordinates, new_coordinates, output_file='map.html'):
    """
    Generates an HTML file to visualize original and new coordinates on a map.

    Parameters:
    - original_coordinates (list of tuples): List of (longitude, latitude) tuples for the original boundary.
    - new_coordinates (list of tuples): List of (longitude, latitude) tuples for the new generated points.
    - output_file (str): Output file name for the generated HTML.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Forest Map with Original and Generated Coordinates</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
        <style>
            #map {{ height: 600px; width: 100%; }}
        </style>
    </head>
    <body>
        <h3>Forest Boundary with Original (Blue) and Generated (Red) Points</h3>
        <div id="map"></div>

        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
        <script>
            // Initialize the map centered around a midpoint of the forest boundary
            const map = L.map('map').setView([{original_coordinates[0][1]}, {original_coordinates[0][0]}], 14);

            // Add a tile layer to the map (OpenStreetMap)
            L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                maxZoom: 18,
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }}).addTo(map);

            // Original coordinates (boundary of the forest)
            const originalCoordinates = {original_coordinates};

            // Add the original boundary as a polygon in blue
            L.polygon(originalCoordinates.map(coord => [coord[1], coord[0]]), {{
                color: 'blue',
                weight: 2,
                opacity: 0.7
            }}).addTo(map);

            // Add markers for the original coordinates in blue
            originalCoordinates.forEach((coord, index) => {{
                L.marker([coord[1], coord[0]], {{
                    icon: L.divIcon({{
                        className: 'original-marker',
                        iconSize: [8, 8],
                        html: '<div style="background-color:blue;border-radius:50%;width:8px;height:8px;"></div>'
                    }})
                }})
                .bindPopup(`<b>Original Point ${{index + 1}}</b><br>Lat: ${{coord[1]}}<br>Lng: ${{coord[0]}}`)
                .addTo(map);
            }});

            // New coordinates (generated points within the boundary)
            const newCoordinates = {new_coordinates};

            // Add markers for the new generated coordinates with red points
            newCoordinates.forEach((coord, index) => {{
                L.marker([coord[1], coord[0]], {{
                    icon: L.divIcon({{
                        className: 'new-marker',
                        iconSize: [8, 8],
                        html: '<div style="background-color:red;border-radius:50%;width:8px;height:8px;"></div>'
                    }})
                }})
                .bindPopup(`<b>Generated Point ${{index + 1}}</b><br>Lat: ${{coord[1]}}<br>Lng: ${{coord[0]}}`)
                .addTo(map);
            }});
        </script>
    </body>
    </html>
    """
    
    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(html_content)
    print(f"Map has been generated and saved as {output_file}")
