import json

def return_info():
    print("retrieve!")

    data = {}
    
    with open('./tasks/test_tasks.json', 'r') as file:
        data = json.load(file) 
        file.close()
    
    title = data.get('title', '')
    text = data.get('text', '')

    return title, text