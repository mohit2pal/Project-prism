# Importing necessary libraries
import os
import kaggle

# Setting Kaggle API credentials
os.environ["KAGGLE_USERNAME"] = "sryytuuy"
os.environ["KAGGLE_KEY"] = "cb97a52ed6a41de27e450cd527611d23"

# Authenticating Kaggle API
kaggle.api.authenticate()

# Downloading dataset from Kaggle
kaggle.api.dataset_download_files('syedsaqlainhussain/sql-injection-dataset', path='data', unzip=True, force=True)