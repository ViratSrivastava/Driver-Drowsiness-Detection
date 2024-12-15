import os
import shutil
import random

# Define the specific path for Close-Eyes
source_dir = 'data/Close-Eyes'
train_dir = 'data/Close-Eyes/train'
test_dir = 'data/Close-Eyes/test'
split_ratio = 0.9

def split_data(source_dir, train_dir, test_dir, split_ratio):
    """Split .png files into training and testing sets."""
    try:
        # Get list of all .png files
        files = [f for f in os.listdir(source_dir) if f.lower().endswith('.png') and os.path.isfile(os.path.join(source_dir, f))]
        
        # Check if there are files to split
        if not files:
            print(f"No .png files found in {source_dir}.")
            return

        # Randomly shuffle files
        random.shuffle(files)
        
        # Calculate split point
        split_point = int(len(files) * split_ratio)
        
        # Split and copy files
        train_files = files[:split_point]
        test_files = files[split_point:]
        
        # Create train and test directories if they don't exist
        os.makedirs(train_dir, exist_ok=True)
        os.makedirs(test_dir, exist_ok=True)

        # Copy files to train directory and print their components
        for file in train_files:
            src = os.path.join(source_dir, file)
            dst = os.path.join(train_dir, file)
            shutil.copy2(src, dst)
            # Extract components from filename
            components = file[:-4].split('_')  # Remove '.png' and split by '_'
            print(f"Train File: {file}, Components: {components}")
        
        # Copy files to test directory and print their components
        for file in test_files:
            src = os.path.join(source_dir, file)
            dst = os.path.join(test_dir, file)
            shutil.copy2(src, dst)
            # Extract components from filename
            components = file[:-4].split('_')  # Remove '.png' and split by '_'
            print(f"Test File: {file}, Components: {components}")

    except Exception as e:
        print(f"An error occurred while processing {source_dir}: {e}")

def main():
    """Main function to execute the data splitting for Close-Eyes."""
    split_data(source_dir, train_dir, test_dir, split_ratio)
    print("Data split completed for Close-Eyes!")

if __name__ == "__main__":
    main()