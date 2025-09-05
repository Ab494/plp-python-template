import os
import requests

# Prompt user for image URL
print("Welcome to the Ubuntu Image Fetcher")
print("A tool for  mindfully collecting images from the web")
url = input("Please enter the image URL: ")

# Create directory if it doesn't exists
folder_name = "Fetched_Images"
if not os.path.exists(folder_name):
 os.makedirs(folder_name)
 
 # Download Image
try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise the error for bad requests
     
     # Get file name
     
    filename = url.split("/")[-1] or "downloaded_image.jpg"
    file_path = os.path.join(folder_name, filename)
     
     # Save image
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print("Successfully fetched: {filename}")
    print("Image saved to {file_path}")
except requests.exceptions.RequestException as e:
    print("Error fetching the image:", e)
             
