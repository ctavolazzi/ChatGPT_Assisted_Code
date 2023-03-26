import os
import requests
import json

# Prompt the user to enter the search term they want to use
search_term = input('Enter the search term you want to use: ')

# Call the Wikipedia API to search for the specified term
url = f'https://en.wikipedia.org/w/api.php?action=opensearch&search={search_term}&limit=10&namespace=0&format=json'
response = requests.get(url)
data = response.json()

# Extract the search results from the API response
titles = data[1]
descriptions = data[2]
urls = data[3]

# Create a list to store the search results
results = []

# Iterate over the search results and extract the data you want to save
for title, description, url in zip(titles, descriptions, urls):
    result = {
        'title': title,
        'description': description,
        'url': url
    }
    results.append(result)

# Save the results to a text file in JSON format
folder_path = 'results'
os.makedirs(folder_path, exist_ok=True)
file_name = f'{search_term.lower()}_results.json'
file_path = os.path.join(folder_path, file_name)

# Check if a file with the same name already exists and add a sequential number if necessary
count = 1
while os.path.exists(file_path):
    file_name = f'{search_term.lower()}_results ({count}).json'
    file_path = os.path.join(folder_path, file_name)
    count += 1

with open(file_path, 'w') as f:
    json.dump(results, f)
