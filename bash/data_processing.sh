#!/bin/bash

# Data processing and cleanup script

# Configuration
DATA_DIR="/Users/usermail/Desktop/autoML/data"
RAW_DIR="$DATA_DIR/raw"
PROCESSED_DIR="$DATA_DIR/processed"
LOG_FILE="/Users/usermail/Desktop/autoML/logs/data_processing.log"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Clean raw data directory
clean_raw_data() {
    log "Cleaning raw data directory..."
    find "$RAW_DIR" -name "*.csv" -mtime +30 -exec rm {} \;
}

# Process new data files
process_data() {
    log "Processing new data files..."
    for file in "$RAW_DIR"/*.csv; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            # Remove duplicates and sort
            sort -u "$file" > "$PROCESSED_DIR/processed_$filename"
            log "Processed $filename"
        fi
    done
}

# Main execution
main() {
    log "Starting data processing script..."
    
    # Create directories if they don't exist
    mkdir -p "$RAW_DIR" "$PROCESSED_DIR"
    
    # Run processing steps
    clean_raw_data
    process_data
    
    log "Data processing completed"
}

main "$@"

# developer by wiki 