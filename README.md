# SOC-IOC-Enrichment 

This tool was built to demonstrate hands-on experience in automating IP reputation checks, a common SOC task. It reads a list of IP addresses, queries the [AbuseIPDB](https://www.abuseipdb.com/) threat intelligence feed, and returns enriched context useful for alert triage, investigation, and reporting.

---

## Use Case

In a Security Operations Center (SOC) or threat hunting environment, analysts often encounter suspicious IPs from alerts or logs. This tool speeds up manual research by automating enrichment with:

- **Abuse Confidence Score**
- **Country of origin**
- **ISP name**
- **Total number of abuse reports**

---

## Skills Demonstrated

- Python scripting for real-world security automation  
- API integration (AbuseIPDB)  
- Data parsing and validation (Regex, Pandas)  
- IOC triage and enrichment logic  
- Secure handling of secrets with `.env` files  
- Outputting usable results for report writing or evidence  

---

## File Structure

| File         | Purpose                                                   |
|--------------|-----------------------------------------------------------|
| `enrich.py`  | Main Python script that handles enrichment logic          |
| `input.csv`  | CSV list of IP addresses to check (one per line)          |
| `output.csv` | Auto-generated file with enriched results                 |
| `.env`       | Holds your API key (not uploaded for security reasons)    |

---

## How to Run

1. **Install dependencies**:
   ```bash
   pip install pandas requests python-dotenv

2. **Create .env file** (this keeps your API KEY secure)
   ```bash
   ABUSEIPDB_API_KEY=your_api_key_here

4. **Add IPs to input.csv like this:**
   ```bash
   8.8.8.8  1.1.1.1


6. **Run the script:**
   ```bash
   python enrich.py
