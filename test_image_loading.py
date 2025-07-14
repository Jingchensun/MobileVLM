#!/usr/bin/env python3
"""
测试图像加载异常处理的脚本
"""

import torch
import os
from PIL import Image
import sys

# 添加mobilevlm路径到sys.path
sys.path.insert(0, '.')

def test_image_loading():
    """Test image loading exception handling"""
    print("Testing image loading exception handling...")
    
    # Mock processor object
    class MockProcessor:
        def __init__(self):
            self.crop_size = {'height': 336, 'width': 336}
            self.image_mean = [0.485, 0.456, 0.406]
        
        def preprocess(self, image, return_tensors='pt'):
            # Mock preprocessing
            return {'pixel_values': [torch.zeros(3, 336, 336)]}
    
    # Mock data
    processor = MockProcessor()
    image_folder = "/nonexistent/path"
    image_file = "nonexistent_image.jpg"
    
    # Test exception handling
    try:
        image = Image.open(os.path.join(image_folder, image_file)).convert('RGB')
        print("Image loaded successfully")
    except (FileNotFoundError, OSError) as e:
        print(f"Caught exception: {type(e).__name__}")
        print(f"Exception message: {e}")
        
        # Create zero-filled image tensor
        crop_size = processor.crop_size
        image = torch.zeros(3, crop_size['height'], crop_size['width'])
        print(f"Created zero-filled tensor with shape: {image.shape}")
        
        print("Exception handling successful, training can continue")
    
    print("Test completed")

if __name__ == "__main__":
    test_image_loading() 