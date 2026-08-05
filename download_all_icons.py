import os
import urllib.request

slugs = {
    "html5": "html5", "css3": "css3", "javascript": "javascript", "react": "react", "bootstrap": "bootstrap",
    "python": "python", "java": "java", "nodejs": "nodedotjs", "express": "express", "jwt": "jsonwebtokens",
    "mongodb": "mongodb", "mysql": "mysql", "supabase": "supabase",
    "pytorch": "pytorch", "tensorflow": "tensorflow", "scikitlearn": "scikitlearn", "pandas": "pandas", "numpy": "numpy", "matplotlib": "matplotlib",
    "docker": "docker", "aws": "amazonwebservices", "googlecloud": "googlecloud", "vercel": "vercel", "render": "render", "jenkins": "jenkins", "nginx": "nginx",
    "c": "c", "git": "git", "github": "github", "postman": "postman"
}

os.makedirs("d:/Dr-Venom29/assets/icons", exist_ok=True)
base_url = "https://cdn.simpleicons.org/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

for name, slug in slugs.items():
    req = urllib.request.Request(base_url + slug, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            with open(f"d:/Dr-Venom29/assets/icons/{name}.svg", "wb") as out_file:
                out_file.write(response.read())
        print(f"Downloaded {name}.svg")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
