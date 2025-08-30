#!/bin/bash
# 
# SoundFont for Samplers - Instrument Copy Script for v0.0.3
# This script copies selected instruments from the raw FluidR3_GM collection
# to the main FluidR3_GM directory for distribution.
#

echo "Copying instruments for SoundFont for Samplers v0.0.3..."

# Source and destination directories
SRC_DIR="./raw/FluidR3_GM/full/FluidR3_GM"
DEST_DIR="./FluidR3_GM"

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Piano instruments
echo "Copying piano instruments..."
cp -r "$SRC_DIR/bright_acoustic_piano-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/electric_grand_piano-mp3" "$DEST_DIR/"

# Percussion instruments
echo "Copying percussion instruments..."
cp -r "$SRC_DIR/marimba-mp3" "$DEST_DIR/"

# Traditional instruments
echo "Copying traditional instruments..."
cp -r "$SRC_DIR/accordion-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/harmonica-mp3" "$DEST_DIR/"

# Bass instruments
echo "Copying bass instruments..."
cp -r "$SRC_DIR/acoustic_bass-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/synth_bass_1-mp3" "$DEST_DIR/"

# String instruments
echo "Copying string instruments..."
cp -r "$SRC_DIR/string_ensemble_2-mp3" "$DEST_DIR/"

# Brass instruments
echo "Copying brass instruments..."
cp -r "$SRC_DIR/tuba-mp3" "$DEST_DIR/"

# Saxophone instruments
echo "Copying saxophone instruments..."
cp -r "$SRC_DIR/soprano_sax-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/baritone_sax-mp3" "$DEST_DIR/"

# Woodwind instruments
echo "Copying woodwind instruments..."
cp -r "$SRC_DIR/oboe-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/english_horn-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/bassoon-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/piccolo-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/shakuhachi-mp3" "$DEST_DIR/"

# Pad instruments
echo "Copying pad instruments..."
cp -r "$SRC_DIR/pad_4_choir-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/pad_5_bowed-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/pad_6_metallic-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/pad_7_halo-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/pad_8_sweep-mp3" "$DEST_DIR/"

# FX instruments
echo "Copying FX instruments..."
cp -r "$SRC_DIR/fx_1_rain-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/fx_2_soundtrack-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/fx_3_crystal-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/fx_4_atmosphere-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/fx_5_brightness-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/fx_6_goblins-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/fx_7_echoes-mp3" "$DEST_DIR/"
cp -r "$SRC_DIR/fx_8_scifi-mp3" "$DEST_DIR/"

echo "All instruments copied successfully for v0.0.3!"
echo "Total instruments added: 29"