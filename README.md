🔍 Simple Python Port Scanner

A lightweight Python script to scan open ports on a target host.
Built for educational and learning purposes only.

⚠️ Disclaimer

This tool is intended strictly for educational, testing, and research purposes (e.g., CTFs, lab environments, personal network testing).
Do NOT use it on systems you don’t own or have explicit permission to test. Unauthorized scanning may be illegal.

📌 Features

Scans a range of ports (default: 50–85)

Identifies open ports on a target host

Error handling for invalid hostnames, connection issues, and keyboard interrupts

Simple and easy to extend

🚀 Usage
python3 scanner.py <target>

Example

python3 scanner.py 127.0.0.1

Output:

--------------------------------------------------
Scanning target 127.0.0.1
Time started 2025-08-16 14:30:00
--------------------------------------------------
port 80 is open
port 53 is open

🛠️ Requirements

    Python 3.x

No external dependencies required.
📂 File Structure

scanner.py   # main script
README.md    # documentation

🔧 Customization

You can change the port range by editing this line in scanner.py:

for port in range(50,85):

👉 Example: range(1,1025) for scanning common ports.
