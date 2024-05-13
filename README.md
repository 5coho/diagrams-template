# Diagram Template
Python application to generate diagrams using Mingrammer and Graphviz

## Requirements
 - Docker

## Running Locally
 - Build the Docker image:

 `docker build -t diagrams .`
 
 - Run the Docker image:

 `docker run --rm -v .:/app diagrams`

 - Generated diagram PNGs go into the `./diagrams` directory
 - Modify/create new diagram code in `./src`, example diagrams included
 - Be sure to call new diagrams in `main.py`
 - Mingrammer documentation can be found here: https://diagrams.mingrammer.com/docs/getting-started/installation
