#!/bin/bash

# Script to convert pitch numbers to MIDI key names
# Usage: ./convert_pitch_to_midi_key.sh

# Function to convert pitch number to note name and octave
pitch_to_note() {
    local pitch=$1
    
    # Note names array (0-11 corresponding to C through B) - using flats instead of sharps
    local note_names=("C" "Db" "D" "Eb" "E" "F" "Gb" "G" "Ab" "A" "Bb" "B")
    
    # Calculate note and octave
    local note_index=$((pitch % 12))
    local octave=$((pitch / 12 - 1))
    
    # Get note name
    local note_name="${note_names[$note_index]}"
    
    echo "${note_name}${octave}"
}

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
    
    # Find all .mp3 files and rename them
    for file in *.mp3; do
        # Check if file exists (to avoid processing when no files match)
        if [ -f "$file" ]; then
            # Extract the number from the filename (remove .mp3 extension)
            local pitch_number="${file%.mp3}"
            
            # Check if the filename is a number
            if [[ "$pitch_number" =~ ^[0-9]+$ ]]; then
                # Convert pitch to note name
                local new_name=$(pitch_to_note "$pitch_number")
                
                # Rename the file
                mv "$file" "${new_name}.mp3"
                echo "Renamed: $file -> ${new_name}.mp3"
            else
                echo "Skipping $file (not a number)"
            fi
        fi
    done
    
    # Go back to original directory
    cd - > /dev/null
}

# Main script
echo "Starting pitch to MIDI key conversion..."

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

echo "Pitch to MIDI key conversion completed!"
