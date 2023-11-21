print("\nTask 1.1")
import requests

url = f"https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

if 400 <= response.status_code <= 599:
    print(f"Error: {response.status_code}")
else:
    print(response.json())

print("\nTask 1.2")
class ToDo:
    def __init__(self, user_id, id, title, completed):
        self.userId = user_id
        self.id = id
        self.title = title
        self.completed = completed
todo_item = ToDo(user_id=1, id=1, title="Sample ToDo", completed=False)

print("\nTask 1.3")
new_todo_item = ToDo(user_id=2, id=2, title="Another ToDo", completed=True)

print("\nTask 1.4")
new_todo = {
    "userId": new_todo_item.userId,
    "title": new_todo_item.title,
    "completed": new_todo_item.completed
}

response = requests.post("https://jsonplaceholder.typicode.com/todos", json=new_todo)

if 400 <= response.status_code <= 599:
    print(f"Error: {response.status_code}")
else:
    print(response.json())

print("\nTask 1.5")
new_todo_item.title = "Updated ToDo"
new_todo_item.completed = False

print("\nTask 1.6")
updated_todo = {
    "userId": new_todo_item.userId,
    "title": new_todo_item.title,
    "completed": new_todo_item.completed
}

response = requests.put(f"https://jsonplaceholder.typicode.com/todos/{new_todo_item.id}", json=updated_todo)

if 400 <= response.status_code <= 599:
    print(f"Error: {response.status_code}")
else:
    print(response.json())




print("\nTask 2.1")
import random

character_id = random.randint(1, 826)
character_data = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}").json()

print("\nTask 2.2")
print(character_data)
print(character_data.keys())

print("\nTask 2.3")
import json
with open(f"Characters\\info_character_{character_id}.json", "w") as file:
    json.dump(character_data, file)

print("\nTask 2.4")
episode_urls = character_data['episode']
episode_ids = []
for url in episode_urls:
    parts = url.split('/')
    episode_id = parts[-1]
    episode_ids.append(episode_id)

with open(f"Characters\\all_episodes_with_character_{character_id}", "a") as file:
    for url in episode_urls:
        file.write(url + "\n")

print("\nTask 2.5")
episode_response = requests.get("https://rickandmortyapi.com/api/episode/1").json()
print(episode_response.keys())

print("\nTask 2.6")

print("\nTask 2.7")
from episode import Episode

episodes = []

for eid in episode_ids:
    response = requests.get(f"https://rickandmortyapi.com/api/episode/{eid}").json()
    episode_obj = Episode(**response)
    episodes.append(episode_obj)

print("\nTask 2.8")

print("\nTask 2.9")
character_structure = requests.get("https://rickandmortyapi.com/api/character/1").json()
print(character_structure.keys())

print("\nTask 2.10")

print("\nTask 2.11")
from character import Character

random_character = Character(**character_data)
print("\nTask 2.12")

print("\nTask 2.13")
for episode in episodes:
    print(episode.display_info())

print(random_character.display_basic_info())

print(random_character.list_episodes())