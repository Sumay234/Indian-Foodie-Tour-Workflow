
# Indian Foodie Tour Workflow

## Overview

This project builds a workflow that, for a list of cities, performs the following steps:

* Checks today's weather and suggests whether to dine indoors or outdoors.
* Picks 3 iconic local dishes for each city.
* Suggests top-rated restaurants serving these dishes.
* Creates a one-day foodie tour itinerary including breakfast, lunch, and dinner narratives that factor in weather conditions.

The workflow uses the Julep AI platform to generate all content without relying on external APIs.

## How It Works

1. Initializes a Julep Agent specialized in Indian food and travel recommendations.
2. Defines a Task template that describes the expected itinerary output.
3. For each city:

   * Starts a Task Execution providing the city name as input.
   * Waits for completion.
   * Prints the generated itinerary to the console.

## Requirements

* Python 3.7+
* Julep API key

## Installation

1. Install dependencies:

   ```
   pip install julep pyyaml
   ```

2. Create a `config.py` file with your API key:

   ```python
   JULEP_API_KEY = "your_actual_julep_api_key"
   ```

## Running the Workflow

Run the script:

```
python app.py
```

The script will process each city in the list and display the generated foodie tour.

## Customization

To change cities, edit the `cities` list in `app.py`.

To adjust the format or content of the itineraries, modify the prompt text in the task definition.

