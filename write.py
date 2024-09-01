import json

def getValue(title, text):
    title = title
    text = text

    send_data = {
        "title" : title,
        "text" : text
    }

    send_data = json.dumps(send_data)
    print(send_data)

    with open('./tasks/test_tasks.json', 'w') as writer:
        writer.write(send_data)