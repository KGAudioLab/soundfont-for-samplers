#!/usr/bin/env python3
"""
Package Size Reducer Script

This script filters the soundfont package to include only instruments specified
in a collection JSON file, helping reduce package size for CDN limitations.

Usage:
    python filter_package.py collection_core.json
"""

import json
import os
import sys
import shutil
from pathlib import Path

def load_collection(collection_file):
    """Load the collection JSON file."""
    try:
        with open(collection_file, 'r') as f:
            collection = json.load(f)
        print(f"✅ Loaded collection with {len(collection)} instruments")
        return collection
    except FileNotFoundError:
        print(f"❌ Collection file not found: {collection_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in collection file: {e}")
        sys.exit(1)

def update_names_json(collection, names_file="FluidR3_GM/names.json"):
    """Update the names.json file with filtered instruments."""
    try:
        # Backup original names.json
        if os.path.exists(names_file):
            shutil.copy2(names_file, f"{names_file}.backup")
            print(f"📋 Backed up original names.json")
        
        # Write filtered names
        with open(names_file, 'w') as f:
            json.dump(collection, f, indent=2)
        
        print(f"✅ Updated {names_file} with {len(collection)} instruments")
        
    except Exception as e:
        print(f"❌ Failed to update names.json: {e}")
        sys.exit(1)

def update_package_json(collection, package_file="package.json"):
    """Update package.json files list to include only filtered instruments."""
    try:
        # Read current package.json
        with open(package_file, 'r') as f:
            package_data = json.load(f)
        
        # Backup original package.json
        shutil.copy2(package_file, f"{package_file}.backup")
        print(f"📋 Backed up original package.json")
        
        # Create new files list with only filtered instruments
        new_files = [
            "index.js",
            "README.md", 
            "LICENSE"
        ]
        
        # Add each instrument directory
        for instrument in collection:
            new_files.append(f"FluidR3_GM/{instrument}-mp3/")
        
        # Add names.json
        new_files.append("FluidR3_GM/names.json")
        
        # Update package.json
        package_data["files"] = new_files
        
        # Write updated package.json
        with open(package_file, 'w') as f:
            json.dump(package_data, f, indent=2)
        
        print(f"✅ Updated {package_file} with {len(collection)} instrument directories")
        
    except Exception as e:
        print(f"❌ Failed to update package.json: {e}")
        sys.exit(1)

def remove_excluded_instruments(collection, instruments_dir="FluidR3_GM"):
    """Remove instrument directories not in the collection (optional)."""
    if not os.path.exists(instruments_dir):
        print(f"⚠️  Instruments directory not found: {instruments_dir}")
        return
    
    excluded_count = 0
    total_size_saved = 0
    
    # Get all existing instrument directories
    for item in os.listdir(instruments_dir):
        item_path = os.path.join(instruments_dir, item)
        
        # Skip if not a directory or doesn't end with -mp3
        if not os.path.isdir(item_path) or not item.endswith('-mp3'):
            continue
            
        # Extract instrument name (remove -mp3 suffix)
        instrument_name = item[:-4]  # Remove '-mp3'
        
        # If instrument not in collection, mark for removal
        if instrument_name not in collection:
            # Calculate directory size before removal
            dir_size = sum(
                os.path.getsize(os.path.join(dirpath, filename))
                for dirpath, dirnames, filenames in os.walk(item_path)
                for filename in filenames
            )
            total_size_saved += dir_size
            
            print(f"🗑️  Would remove: {item} ({dir_size / 1024 / 1024:.1f} MB)")
            excluded_count += 1
    
    if excluded_count > 0:
        total_mb = total_size_saved / 1024 / 1024
        print(f"\n📊 Summary:")
        print(f"   Instruments to remove: {excluded_count}")
        print(f"   Estimated size saved: {total_mb:.1f} MB")
        
        response = input(f"\nDo you want to actually delete these {excluded_count} directories? (y/N): ").strip().lower()
        
        if response == 'y':
            actual_removed = 0
            actual_size_saved = 0
            
            for item in os.listdir(instruments_dir):
                item_path = os.path.join(instruments_dir, item)
                
                if not os.path.isdir(item_path) or not item.endswith('-mp3'):
                    continue
                    
                instrument_name = item[:-4]
                
                if instrument_name not in collection:
                    # Calculate size before removal
                    dir_size = sum(
                        os.path.getsize(os.path.join(dirpath, filename))
                        for dirpath, dirnames, filenames in os.walk(item_path)
                        for filename in filenames
                    )
                    
                    # Remove directory
                    shutil.rmtree(item_path)
                    actual_removed += 1
                    actual_size_saved += dir_size
                    print(f"🗑️  Removed: {item}")
            
            print(f"\n✅ Successfully removed {actual_removed} directories")
            print(f"💾 Saved {actual_size_saved / 1024 / 1024:.1f} MB")
        else:
            print("ℹ️  No directories were deleted. Only package.json and names.json were updated.")
    else:
        print("✅ All existing instruments are already in the collection")

def main():
    if len(sys.argv) != 2:
        print("Usage: python filter_package.py <collection_file.json>")
        print("Example: python filter_package.py collection_core.json")
        sys.exit(1)
    
    collection_file = sys.argv[1]
    
    print("🎵 SoundFont Package Filter")
    print("=" * 40)
    
    # Load collection
    collection = load_collection(collection_file)
    
    # Update names.json
    update_names_json(collection)
    
    # Update package.json
    update_package_json(collection)
    
    # Ask about removing excluded instruments
    print("\n" + "=" * 40)
    remove_excluded_instruments(collection)
    
    print("\n🎉 Package filtering completed!")
    print("📝 Backups created: package.json.backup, names.json.backup")
    print("🚀 Your package is now ready for publishing with reduced size!")

if __name__ == "__main__":
    main()