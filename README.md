# SAP BusinessObjects Launchpad SSRF & Timing Attack PoC

This Python script is a proof-of-concept (PoC) for executing SSRF (Server-Side Request Forgery) and Timing Attacks against SAP BusinessObjects Launchpad. It is designed to help security researchers and professionals identify open ports on a target IP by leveraging SAP BusinessObjects' authentication mechanisms.

## Features

- **SSRF Exploit:** Leverages SSRF to interact with internal services by targeting different ports on a specified IP address.
- **Timing Attack:** Measures the time taken by the SAP BusinessObjects server to respond to authentication attempts, allowing you to infer the status of targeted ports.
- **Customizable Ports:** Allows you to specify a list of ports to target, or you can use the default set of common ports.

## Requirements

- Python 3.x
- Internet access to reach the SAP BusinessObjects Launchpad instance.

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/MachadoOtto/sap_bo_launchpad-ssrf-timing_attack.git
cd sap_bo_launchpad-ssrf-timing_attack
```

## Usage

```bash
./sap_bo_launchpad-ssrf-timing_attack.py <affected_url> <targetIP> [targetPorts]
```

- `affected_url`: The URL of the SAP BusinessObjects Launchpad instance you want to test.
- `targetIP`: The IP address you want to probe for open ports.
- `targetPorts` (optional): A comma-separated list of ports to check (e.g., 22,80,443). If not specified, a default set of ports will be used.

##  Legal Disclaimer

This script is intended for educational purposes only and should only be used in environments where you have explicit permission to conduct security testing. Unauthorized use of this script against targets without consent is illegal and unethical.
