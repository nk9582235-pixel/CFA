import json
import os

# Load a sample JSON file to see its structure
data_folder = os.path.join(os.path.dirname(__file__), 'data')
sample_file = os.path.join(data_folder, 'Module 1 Rates and Returns.json')

print("Current working directory:", os.getcwd())
print("Data folder exists:", os.path.exists(data_folder))
print("Sample file exists:", os.path.exists(sample_file))

if os.path.exists(sample_file):
    with open(sample_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Print the structure of the first question
    if 'items' in data and len(data['items']) > 0:
        first_item = data['items'][0]
        print("First item structure:")
        print(json.dumps(first_item, indent=2)[:500])  # Limit output to first 500 characters
        
        # Check if it has the entry structure
        if 'entry' in first_item:
            entry = first_item['entry']
            print("\nEntry structure:")
            print(json.dumps(entry, indent=2)[:500])  # Limit output to first 500 characters
            
            # Check for feedback and scoring data
            print("\nFeedback:", entry.get('feedback', 'Not found'))
            print("\nScoringData:", entry.get('scoringData', 'Not found'))
            print("\nAnswerFeedback:", entry.get('answerFeedback', 'Not found'))
else:
    print("Sample file not found")
    
    # List files in data folder
    if os.path.exists(data_folder):
        print("Files in data folder:")
        for file in os.listdir(data_folder)[:10]:  # Show first 10 files
            print(f"  {file}")