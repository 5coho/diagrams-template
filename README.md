# Diagram Template
Python application to generate diagrams using Mingrammer and Graphviz

## Requirements
 - Docker

## Running Locally
 - Build the docker image:

 `docker build -t diagrams .`
 
 - Run the image:

 `docker run --rm -v .:/app diagrams`

 - Generated diagram PNGs go into the `./diagrams` directory
