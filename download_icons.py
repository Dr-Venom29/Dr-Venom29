import os
import urllib.request

icons = {
    "mongodb": "mongodb/mongodb-original.svg",
    "express": "express/express-original.svg",
    "react": "react/react-original.svg",
    "nodejs": "nodejs/nodejs-original.svg",
    "python": "python/python-original.svg",
    "numpy": "numpy/numpy-original.svg",
    "pandas": "pandas/pandas-original.svg",
    "pytorch": "pytorch/pytorch-original.svg",
    "nextjs2": "nextjs/nextjs-original.svg",
    "typescript": "typescript/typescript-original.svg",
    "tailwindcss": "tailwindcss/tailwindcss-original.svg",
    "aws": "amazonwebservices/amazonwebservices-original-wordmark.svg",
    "docker": "docker/docker-original.svg",
    "kubernetes": "kubernetes/kubernetes-plain.svg",
    "githubactions": "github/github-original.svg",
    "postgresql": "postgresql/postgresql-original.svg"
}

os.makedirs("d:/Dr-Venom29/assets/icons", exist_ok=True)
base_url = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/"

for name, path in icons.items():
    url = base_url + path
    try:
        urllib.request.urlretrieve(url, f"d:/Dr-Venom29/assets/icons/{name}.svg")
        print(f"Downloaded {name}.svg")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
