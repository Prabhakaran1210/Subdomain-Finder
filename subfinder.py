import requests

domain = input("Enter target domain: ")

file = open("subdomains.txt","r")

found = []

print("\nScanning subdomains...\n")

for line in file:
    
    sub = line.strip()
    
    http_url = "http://" + sub + "." + domain
    https_url = "https://" + sub + "." + domain
    
    try:
        
        response = requests.get(http_url, timeout=3)
        
        print("FOUND:", http_url, "Status:", response.status_code)
        found.append(http_url)
        
    except:
        
        try:
            
            response = requests.get(https_url, timeout=3)
            
            print("FOUND:", https_url, "Status:", response.status_code)
            found.append(https_url)
            
        except:
            pass

print("\nScan Completed")

if len(found) > 0:
    
    file = open("results.txt","w")
    
    for subdomain in found:
        file.write(subdomain + "\n")
    
    file.close()
    
    print("Results saved in results.txt")

else:
    
    print("No subdomains found")
