import re
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

# Set headers for ABUSEIPDB API requests
headers = {
    'Key': API_KEY,
    'Accept': 'application/json'
}

# Read IPs from input.csv
df = pd.read_csv('input.csv')
results = []

# Function to defang IP to safely share in reports
def defang(ip):
    return ip.replace('.', '[.]')

# Check for valid IPv4 addresses to avoid crashing
def is_valid_ip(ip):
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip)

# For each IP, check ABUSEIPDB for reputation, reports, and abuse score
for ip in df['ip']:
    print(f"\nchecking IP: {ip}")
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        results.append({
            'Original_IP': ip,
            'Defanged_IP': defang(ip),
            'Abuse_Score': data['abuseConfidenceScore'],
            'Country': data['countryCode'],
            'ISP': data['isp'],
            'Total_Reports': data['totalReports']
        })
        print(f"  - Abuse Score: {data['abuseConfidenceScore']}")
        print(f"  - Country: {data['countryCode']}")
        print(f"  - ISP: {data['isp']}")
    else:
        results.append({
            'Original_IP': ip,
            'Defanged_IP': defang(ip),
            'Abuse_Score': 'Error',
            'Country': 'Error',
            'ISP': 'Error',
            'Total_Reports': 'Error'
        })
        print("  - Error: Could not retrieve data from ABUSEIPDB")

# Write the results to output.csv
output_df = pd.DataFrame(results)
output_df.to_csv('output.csv', index=False)

# Print summary
success_count = sum(1 for r in results if r['Abuse_Score'] != 'Error')
fail_count = len(results) - success_count

print(f"\n- Summary: {success_count} IPs proceed successfully, {fail_count} failed.")
print("\n- Done! Results saved to output.csv")

