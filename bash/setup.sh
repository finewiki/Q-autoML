#!/bin/bash

# Setup script for AutoML project

# Create necessary directories
mkdir -p data/{raw,processed,external}
mkdir -p models
mkdir -p logs
mkdir -p configs

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install R packages
echo "Installing R packages..."
Rscript -e 'install.packages(c("tidyverse", "quantmod", "TTR", "ggplot2", "plotly"))'

# Setup Java environment
echo "Setting up Java environment..."
mvn clean install

# Set permissions
chmod +x bash/data_processing.sh

echo "Setup completed successfully!"