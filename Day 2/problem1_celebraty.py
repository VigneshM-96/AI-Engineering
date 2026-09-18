#mark the celebraty

users = {
  "vignesh" : {
    "followers": 1200,
    "posts": 19
  },

  "dinesh" : {
    "followers":900,
    "posts": 8
  }
}

for key in users.keys():
  if users[key].get("followers", "N/A") >= 1000:
    users[key]["status"] = "celebraty"
print(users)