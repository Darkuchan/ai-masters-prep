# Day 3 — Lists and Dictionaries

# --- LISTS ---

# A list is an ordered collection. Square brackets, commas between items.
agents = ["researcher", 
         "writer",
         "summarizer",
         "fact-checker"]

print(agents)
print(len(agents))
print(agents[0])
print(agents[-1])

# add an item to the end
agents.append("translator")
print(agents)

#remove a specific item by its value
agents.remove("writer")
print(agents)

#loop through the every item one at a time
for agent in agents:
    print("We have an agent called:", agent)

#slicing - grabbing a chunk of a list
print(agents[0:2])
print(agents[:2])
print(agents[2:])
print(agents[-2:])

# --- DICTIONARIES ---
# A dictionary is a collection of key-value pairs. Curly brackets, colons between key and value.

agent_info = {
    "name": "Researcher",
    "model" : "gemini-2.5-flash",
    "skill_level": 7,
    "active" : True
}

print(agent_info)
print(agent_info["name"])
print(agent_info["skill_level"])

# Add a new key-value pair (or update if it exists)
agent_info["language"] = "Python"
print(agent_info)

#update an existing value the same way
agent_info["skill_level"] = 9
print(agent_info)

#Remove a key
del agent_info["active"]
print(agent_info)

#check if a key exists
print("name" in agent_info)
print("salary" in agent_info)

#Loop through every key-value pair
for key, value in agent_info.items():
    print(key, "->", value)

# --- MINI EXERCISE: list of dicts ---

agents = [
    {"name": "Researcher", "model": "gemini-2.5-flash", "skill_level": 7},
    {"name": "Writer",     "model": "gemini-2.5-flash", "skill_level": 9},
    {"name": "Summarizer", "model": "gemini-2.5-pro",   "skill_level": 6},
    {"name": "FactChecker","model": "gemini-2.5-flash", "skill_level": 4},
    {"name": "Translator", "model": "gemini-2.5-pro",   "skill_level": 8},
]

for agent in agents:
    print(agent["name"])
    
for agent in agents:
    if (agent["skill_level"]) > 6:
        print (f"{agent['name']} (skill: {agent['skill_level']})")

agent_count = 0
skill_total = 0

for agent in agents:
    skill_total += agent["skill_level"]

print(skill_total/len(agents))