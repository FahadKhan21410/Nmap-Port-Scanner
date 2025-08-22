# Nmap-Port-Scanner
A Python-based port scanner that leverages the Nmap library to perform different types of scans on a given IP address. This tool is intended for ethical and educational purposes only.

## Features
* Interactive CLI: User chooses the scan type from multiple options.
* Scan Types Supported:
  * SYN Scan (-sS) – Detect open TCP ports.
  * UDP Scan (-sU) – Detect open UDP ports.
  * Comprehensive Scan (-sS -sV -sC -O) – Includes OS detection, version detection, and script scanning.
  * FIN Scan (-sF) – Test how target responds to FIN packets.
* Displays Results:
  * Scan information.
  * IP state (up/down).
  * Protocols detected.
  * Open TCP and UDP ports.

## Requirements
* Install dependencies: *pip install nmap*
* Clone repository (bash: git clone https://github.com/username/project.git) or Download as ZIP

## Demo
* https://youtu.be/QkYm9uigjaA (How The Code Works)

## Disclaimer
This project is created for educational and ethical purposes only.
The author does not condone or take responsibility for any misuse of this code.

You may use this project:

* To learn security concepts
* For testing in controlled environments with explicit permission
* As part of ethical hacking or cybersecurity research

You may not use this project:

* For unauthorized access to systems
* To harm, disrupt, or compromise any network, server, or individual

By using this code, you agree that any and all responsibility lies with you, the user.

## License
* This project is licensed under the MIT License - see the [([LICENSE](https://github.com/FahadKhan21410/Nmap-Port-Scanner/blob/main/LICENSE))] file for details.

