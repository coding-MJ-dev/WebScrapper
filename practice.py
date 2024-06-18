from requests import get

websites = (
  "google.com",
  "airbnb.com",
  "x.com",
  "facebook.com",
  "https://tiktok.com",
)

results =  {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    results[website] = "Ok"
  else: 
    results[website] = "Fail"

print(results)
