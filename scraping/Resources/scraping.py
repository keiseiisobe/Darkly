"""
A program to download all README files recursively from http://localhost/.hidden/
"""

if __name__ == "__main__":
    import os
    import requests
    from bs4 import BeautifulSoup

    base_url = "http://localhost/.hidden/"
    output_dir = "readmes/"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def download_readme(url, path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(path + "README", 'a', encoding='utf-8') as file:
                file.write(response.text)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url}")

    def scrape_directory(url, current_path):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href == 'README':
                readme_url = url + href
                download_readme(readme_url, current_path)
            elif href and href != '../':
                subdir_url = url + href
                scrape_directory(subdir_url, current_path)

    scrape_directory(base_url, output_dir)
