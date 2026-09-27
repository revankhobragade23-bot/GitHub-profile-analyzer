import requests

username = input("Enter github username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\ngithub profile analyzer")
    print("------------------------")
    print("username:", data["login"])
    print("name:", data.get("name", "N/A"))
    print("followers:", data.get("followers", "N/A"))
    print("following:", data.get("following", "N/A"))
    print("public gists:", data.get("public_gists", "N/A"))
    print("profile:", data.get("html_url", "N/A"))
    print("account created:", data["created_at"][:10])

else:
    print("user not found")    