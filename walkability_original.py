import osmnx as ox
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, box 

def calculate_walkability_score(location, radius): 
    
    # Download street network and amenities
    G = ox.graph_from_point(location, dist=radius, network_type='walk')

    # Get amenities from OSM
    amenities = ox.features_from_point(
        location, 
        tags={'amenity': True},
        dist=radius
    )

    # Calculate metrics
    area = radius * radius * 3.14159 / 1000000 # km²

    # Street density (km/km²)
    # Convert the graph's edges to a GeoDataFrame
    edges = ox.graph_to_gdfs(G, nodes=False)  # Get only edges, not nodes

    # Retrieve the 'length' attribute from the edges
    edge_lengths = edges['length'].tolist()

    street_density = sum(edge_lengths) / 1000 / area

    # Intersection density
    nodes, edges = ox.graph_to_gdfs(G)
    intersection_density = len(nodes[nodes.street_count > 1]) / area

    # Amenity score
    amenity_score = len(amenities) / area

    # Calculate final walkability score (weighted average)
    walkability_score = (
        0.4 * normalize(street_density) +
        0.4 * normalize(intersection_density) +
        0.2 * normalize(amenity_score)
    )

    
    return walkability_score, {
        'street_density': street_density,
        'intersection_density': intersection_density,
        'amenities_per_sqkm': amenity_score
    }

def normalize(value, min_val=0, max_val=100):
    """Normalize value to 0–100 scale"""
    return min(100, max(0, (value - min_val) / (max_val - min_val) * 100))

# Test location
location = (40.730610, -73.935242)  # New York City coordinates
radius = 1000  # 1km radius

score, details = calculate_walkability_score(location, radius)
print("Walkability Score:", score)
print("Details:", details)