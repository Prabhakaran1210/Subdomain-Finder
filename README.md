\# Python Subdomain Finder



A simple cybersecurity tool written in Python to discover subdomains using a wordlist.



\## Features



\- Wordlist based subdomain enumeration

\- HTTP and HTTPS detection

\- Status code checking

\- Saves results to file



\## Installation



Clone the repository



git clone https://github.com/yourusername/subdomain-finder.git



Install dependencies



pip install -r requirements.txt



\## Usage



python subfinder.py



Enter the target domain when prompted.



\## Example



Enter target domain: google.com

Scanning subdomains...

FOUND: http://www.google.com Status: 429
FOUND: http://mail.google.com Status: 200
FOUND: http://admin.google.com Status: 200
FOUND: http://blog.google.com Status: 200
FOUND: http://api.google.com Status: 404
FOUND: http://shop.google.com Status: 200
FOUND: http://support.google.com Status: 200
FOUND: http://docs.google.com Status: 200
FOUND: http://news.google.com Status: 200
FOUND: http://download.google.com Status: 404
FOUND: http://upload.google.com Status: 404
FOUND: http://store.google.com Status: 200
FOUND: http://cloud.google.com Status: 200
FOUND: http://video.google.com Status: 429
FOUND: http://images.google.com Status: 200
FOUND: http://files.google.com Status: 200
FOUND: http://services.google.com Status: 429
FOUND: http://apps.google.com Status: 200
FOUND: http://mobile.google.com Status: 200
FOUND: http://billing.google.com Status: 404
FOUND: http://tools.google.com Status: 200
FOUND: http://sandbox.google.com Status: 404
FOUND: http://help.google.com Status: 200
FOUND: http://partners.google.com Status: 200
FOUND: http://search.google.com Status: 429
FOUND: http://analytics.google.com Status: 200
FOUND: http://security.google.com Status: 200
FOUND: http://account.google.com Status: 200
FOUND: http://accounts.google.com Status: 200

Scan Completed
Results saved in results.txt
