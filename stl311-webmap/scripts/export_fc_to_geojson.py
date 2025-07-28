import arcpy
import os

# Set your workspace and feature class name
arcpy.env.workspace = r"C:\Users\mills\geo_dev\stlouis311\StLouis311.gdb"
input_fc = 'SERVICE_REQUESTS'
output_geojson = r"C:\Users\mills\geo_dev\stlouis311-webmap\data\service_requests.geojson"

# Ensure output directory exists
os.makedirs(os.path.dirname(output_geojson), exist_ok=True)

# Export to GeoJSON (ArcGIS Pro 2.6+)
arcpy.FeaturesToJSON_conversion(
    in_features=input_fc,
    out_json_file=output_geojson,
    format_json='FORMATTED',
    geoJSON='GEOJSON'  # This ensures output is GeoJSON, not Esri JSON
)
print("Exported to GeoJSON:", output_geojson) 