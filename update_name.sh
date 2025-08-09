#!/bin/bash

# Script to remove 'key_' prefix from filenames in specified folders
# Usage: ./update_name.sh

# Function to rename files in a directory
rename_files() {
    local dir="$1"
    
    if [ ! -d "$dir" ]; then
        echo "Directory $dir does not exist, skipping..."
        return
    fi
    
    echo "Processing directory: $dir"
    
    # Change to the directory
    cd "$dir" || return
    
    # Find all files that start with 'key_' and rename them
    for file in key_*.mp3; do
        # Check if file exists (to avoid processing when no files match)
        if [ -f "$file" ]; then
            # Extract the number part after 'key_'
            new_name="${file#key_}"
            
            # Rename the file
            mv "$file" "$new_name"
            echo "Renamed: $file -> $new_name"
        fi
    done
    
    # Go back to original directory
    cd - > /dev/null
}

# Main script
echo "Starting file renaming process..."

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Define the base directory relative to the script location
BASE_DIR="$SCRIPT_DIR/../FluidR3_GM"

# List of directories to process
DIRECTORIES=(
    "orchestra_kit"
    "standard"
    "standard_1"
    "standard_2"
    "standard_3"
    "standard_4"
    "standard_5"
    "standard_6"
    "standard_7"
)

# Process each directory
for dir in "${DIRECTORIES[@]}"; do
    full_path="$BASE_DIR/$dir"
    rename_files "$full_path"
done

echo "File renaming process completed!"
