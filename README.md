# python-paping

A Python script to ping a server over TCP/IP and measure connection statistics.

## Description

This script (`paping.py`) connects to a specified IP address and port over TCP, attempts a number of connection pings, and measures various statistics including successful connections, failed connections, and average connection times.

The script utilizes ANSI escape sequences to colorize the output:
- Green for successful connections.
- Red for failed connections or timeouts.
- Yellow for connection information.

## Requirements

- Python 3.x
- `socket` library (standard library in Python)

## Installation

Clone the repository:

```bash
git clone https://github.com/lolfusrin1/python-paping.git
cd python-paping

Usage
Run the script with Python, providing three command-line arguments:
