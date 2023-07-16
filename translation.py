import csv
import requests

translated_data = []

with open('translate.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        id = row['ID']
        language = row['language']
        source_text = row['source_text']
        context = row['context']
        
        response = requests.get(
            'https://api-free.deepl.com/v2/translate',
            {
                'text': source_text,
                'target_lang': language, 
                'auth_key': '63e6270f-ba81-5a04-f719-a015a5574ae3:fx'
            }
        )
        
        if response.status_code == 200:
            translated_text = response.json()['translations'][0]['text']
        else:
            translated_text = 'error'
            
        translated_data.append({'ID': id, 'language': language, 'source_text': source_text, 
                               'translated_text': translated_text, 'context': context})


fieldnames = ['ID', 'language', 'source_text', 'translated_text', 'context']

with open('translate2.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(translated_data)
