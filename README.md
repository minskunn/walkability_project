# Walkability Score Tool 

### Walkability Project (Practice Version)

This project is a practice implementation of an open-source tool (source https://medium.com/@animagun/5-open-source-gis-projects-for-urban-planning-you-can-build-this-weekend-2c820cb10f3c) I found online for calculating walkability scores using OSMnx. 

I used this as a learning opportunity to better understand geospatial analysis and the use of OSMnx library.


## Overview 

This tool calculates a walkability score on a scale 1 to 100 for a given location based on three key metrics derived from OpenStreetMap (OSM) data:

1. **Street Density**: Total street length within a defined radius.
2. **Intersection Density**: Number of street intersections within the radius.
3. **Amenity Density**: Number of amenities within the radius.

The final walkability score is calculated as a weighted combination of these metrics:

- **40% Street Density**
- **40% Intersection Density**
- **20% Amenity Density**

---

## How It Works

1. **Input**: The user specifies a geographic location (latitude and longitude) and a radius (default: 1000 meters).
2. **Data Retrieval**: The tool retrieves street network and amenity data from OpenStreetMap using the OSMnx library.
3. **Metrics Calculation**:
   - **Street Density**: Calculated as the total street length per square kilometer.
   - **Intersection Density**: Calculated as the number of intersections per square kilometer.
   - **Amenity Density**: Calculated as the number of amenities per square kilometer.
4. **Normalization**: The metrics are normalized on a scale of 0–100 for comparability.
5. **Walkability Score**: The final score is computed as a weighted sum of the three metrics.

---

## Limitations identified

Note: The following limitations are my observations and improvement ideas for the purpose of enhancing this tool, based on my understanding of walkability and urban planning concepts.

### 1. **Distance Measurement**

- The radius is measured as a straight-line (Euclidean) distance, not actual walking paths along the street network.

### 2. **Metric Weighting**

- The weighting scheme is subjective, and not based on real-world studies.

### 3. **Simplified Assumptions**

- Factors such as safety, infrastructure quality (e.g., sidewalks), and accessibility are not considered.

### 4. **Amenity Classification**

- The tool does not differentiate between types of amenities. For example, a hospital and a café are both treated equally, even though their contribution to walkability might differ depending on the context.

### 5. **Public Transportation**

- Walkability often depends on access to public transit. This tool does not consider proximity to bus stops, train stations, or other transit options that promote sustainable mobility.

### 6. **Noise and Air Pollution**

- The tool ignores urban factors like noise pollution or air quality, which are essential to creating sustainable and walkable environments.

### 7. **Climate and Weather**

- The tool does not factor in weather conditions or urban climate influences (e.g., shaded areas, heat islands) that can affect pedestrian comfort and walkability.

### 8. **Quality of Green Spaces**

- While amenities are counted in the analysis, the tool does not assess the quality or accessibility of parks, green spaces, and recreational areas, which are critical for walkable and sustainable urban environments.
