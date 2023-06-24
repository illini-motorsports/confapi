from confclient import ConfClient

cc = ConfClient("https://my.confluence.server.url.com", "myadminusername", "password")

# Get the first 100 users
users = cc.get_all_users(limit=100, start=0)

print(users)