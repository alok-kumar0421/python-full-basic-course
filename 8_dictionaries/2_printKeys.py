info={
    "name":"Alok",
    "subject":"science",
    "score":30,
    8:"eight"
}

print(info.keys())
print(info.values())
print(info.items())

# ------------get values----------
print(info["name"])
print(info.get("name"))

# ---------update--------
info.update({       # add in dict
    "roll":78
})

print(info)