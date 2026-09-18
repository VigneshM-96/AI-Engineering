#Counting free users

users = {
  "praveen":{
    "coins":100,
    "streak":20,
    "plan": "Free"
  },
  "rohan":{
    "coins":50,
    "streak":12,
    "plan": "Free"
  },"david":{
    "coins":150,
    "streak":15,
    "plan": "Starter"
  },
}
count = 0
for user in users.keys():
  if users[user].get("plan") == "Free":
    count += 1
print(count)
    