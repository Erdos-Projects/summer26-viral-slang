import os
from dotenv import load_dotenv

# 1. Load the credentials from .env BEFORE importing kaggle
load_dotenv()

# 2. Now we can safely import the kaggle API
import kaggle

def main():
    # Define the dataset and destination
    dataset_name = "pavellexyr/the-reddit-dataset-dataset"
    raw_dir = os.path.join('data', 'raw')
    
    # Ensure the target directory exists
    os.makedirs(raw_dir, exist_ok=True)
    
    print(f"Authenticating with Kaggle...")
    # Initialize the API client (it automatically reads the KAGGLE_USERNAME and KAGGLE_KEY from the environment)
    api = kaggle.api
    api.authenticate()
    
    print(f"Downloading '{dataset_name}'...")
    print(f"Destination: {raw_dir}/")
    
    # 3. Download and unzip the dataset directly into data/raw/
    try:
        api.dataset_download_files(
            dataset_name, 
            path=raw_dir, 
            unzip=True  # Automatically extracts the CSV so you don't have to deal with zip files
        )
        print("\n[SUCCESS] Download and extraction complete!")
        print("Your baseline modelers can now start working with the CSV in data/raw/")
        
    except Exception as e:
        print(f"\n[ERROR] Failed to download dataset: {e}")

if __name__ == "__main__":
    main()