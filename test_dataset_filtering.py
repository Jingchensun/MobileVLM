#!/usr/bin/env python3
"""
Test script for dataset filtering mechanism
"""

import json
import os
import tempfile
import shutil

def test_dataset_filtering():
    """Test the dataset filtering mechanism"""
    print("Testing dataset filtering mechanism...")
    
    # Create temporary directory and files for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test image folder
        image_folder = os.path.join(temp_dir, "images")
        os.makedirs(image_folder)
        
        # Create one existing image file
        existing_image = os.path.join(image_folder, "existing.jpg")
        with open(existing_image, "w") as f:
            f.write("fake image content")
        
        # Create test data json
        test_data = [
            {"image": "existing.jpg", "conversations": [{"from": "human", "value": "What's in this image?"}]},
            {"image": "missing1.jpg", "conversations": [{"from": "human", "value": "What's in this image?"}]},
            {"image": "missing2.jpg", "conversations": [{"from": "human", "value": "What's in this image?"}]},
            {"conversations": [{"from": "human", "value": "Text only conversation"}]}  # No image
        ]
        
        data_path = os.path.join(temp_dir, "test_data.json")
        with open(data_path, "w") as f:
            json.dump(test_data, f)
        
        # Mock data_args
        class MockDataArgs:
            def __init__(self):
                self.image_folder = image_folder
        
        data_args = MockDataArgs()
        
        # Test the filtering logic
        list_data_dict = json.load(open(data_path, "r"))
        original_count = len(list_data_dict)
        print(f"Original dataset size: {original_count}")
        
        valid_data = []
        missing_files = []
        
        for item in list_data_dict:
            if 'image' in item:
                image_path = os.path.join(data_args.image_folder, item['image'])
                if os.path.exists(image_path):
                    valid_data.append(item)
                else:
                    missing_files.append(image_path)
            else:
                # Keep text-only samples
                valid_data.append(item)
        
        print(f"Valid samples: {len(valid_data)}")
        print(f"Missing files: {len(missing_files)}")
        
        if missing_files:
            print("Missing files:")
            for missing_file in missing_files:
                print(f"  {missing_file}")
        
        # Expected results
        expected_valid = 2  # 1 existing image + 1 text-only
        expected_missing = 2  # 2 missing images
        
        if len(valid_data) == expected_valid and len(missing_files) == expected_missing:
            print("✅ Dataset filtering test passed!")
        else:
            print("❌ Dataset filtering test failed!")
            print(f"Expected {expected_valid} valid samples, got {len(valid_data)}")
            print(f"Expected {expected_missing} missing files, got {len(missing_files)}")
    
    print("Test completed")

if __name__ == "__main__":
    test_dataset_filtering() 