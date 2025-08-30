#!/usr/bin/env python3

import os
import re
import glob

def note_to_pitch(note_name, octave):
    """Convert note name and octave to MIDI pitch number."""
    note_names = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    
    if note_name not in note_names:
        raise ValueError(f"Invalid note name: {note_name}")
    
    note_index = note_names.index(note_name)
    pitch = (octave + 1) * 12 + note_index
    return pitch

def parse_note_filename(filename):
    """Parse filename like 'A0.mp3' to extract note name and octave."""
    # Remove the .mp3 extension
    basename = filename.replace('.mp3', '')
    
    # Handle flat notes (e.g., 'Ab', 'Bb', 'Db', 'Eb', 'Gb')
    if len(basename) >= 2 and basename[1] == 'b':
        note_name = basename[:2]  # e.g., 'Ab'
        octave_str = basename[2:]  # e.g., '4'
    else:
        note_name = basename[0]  # e.g., 'A'
        octave_str = basename[1:]  # e.g., '4'
    
    try:
        octave = int(octave_str)
        return note_name, octave
    except ValueError:
        return None, None

def get_pitch_range_for_instrument(instrument_name):
    """Get the min and max pitch for a given instrument."""
    instrument_folder = f"./FluidR3_GM/{instrument_name}-mp3"
    
    if not os.path.exists(instrument_folder):
        print(f"Warning: Instrument folder not found: {instrument_folder}")
        return None, None
    
    mp3_files = glob.glob(os.path.join(instrument_folder, "*.mp3"))
    
    if not mp3_files:
        print(f"Warning: No MP3 files found in {instrument_folder}")
        return None, None
    
    pitches = []
    
    for mp3_file in mp3_files:
        filename = os.path.basename(mp3_file)
        note_name, octave = parse_note_filename(filename)
        
        if note_name is not None and octave is not None:
            try:
                pitch = note_to_pitch(note_name, octave)
                pitches.append(pitch)
            except ValueError as e:
                print(f"Warning: Could not convert {filename}: {e}")
    
    if pitches:
        return min(pitches), max(pitches)
    else:
        return None, None

def process_mapping_file(input_file, output_file):
    """Process the mapping file and add pitch ranges."""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    processed_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # Skip empty lines and comments
        if not stripped or stripped.startswith('//'):
            processed_lines.append(line)
            continue
        
        # Parse instrument mapping lines
        # Pattern: instrument_name: { ... group: "...", ... },
        match = re.match(r'^(\w+):\s*{(.+)},?\s*$', stripped)
        
        if match:
            instrument_name = match.group(1)
            content = match.group(2)
            
            print(f"Processing instrument: {instrument_name}")
            
            # Get pitch range for this instrument
            min_pitch, max_pitch = get_pitch_range_for_instrument(instrument_name)
            
            if min_pitch is not None and max_pitch is not None:
                # Check if pitchRange already exists
                if 'pitchRange:' not in content:
                    # Add pitchRange after group
                    if 'group:' in content:
                        content = re.sub(
                            r'(group:\s*"[^"]+")(\s*)',
                            rf'\1, pitchRange: [{min_pitch}, {max_pitch}]\2',
                            content
                        )
                    else:
                        # If no group, add at the end
                        content = content.rstrip() + f', pitchRange: [{min_pitch}, {max_pitch}]'
                
                processed_lines.append(f"    {instrument_name}: {{ {content} }},\n")
                print(f"  -> Added pitch range: [{min_pitch}, {max_pitch}]")
            else:
                processed_lines.append(line)
                print(f"  -> Could not determine pitch range")
        else:
            # Non-matching lines (shouldn't happen with valid input)
            processed_lines.append(line)
    
    # Write the processed content to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)
    
    print(f"\nProcessing complete! Updated file saved as: {output_file}")

def main():
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 add_pitch_ranges.py <input_mapping_file>")
        print("Example: python3 add_pitch_ranges.py ./raw/v1_instrument_mapping.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Create output filename by adding suffix before extension
    if input_file.endswith('.txt'):
        output_file = input_file[:-4] + '_with_pitch_ranges.txt'
    else:
        output_file = input_file + '_with_pitch_ranges'
    
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)
    
    process_mapping_file(input_file, output_file)

if __name__ == "__main__":
    main()