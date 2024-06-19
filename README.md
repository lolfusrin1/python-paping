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
```

## Usage
Run the script with Python, providing three command-line arguments:
```bash
python paping.py <ip> <port> <times>
```
- <ip>: IP address of the server to ping.
- <port>: Port number to connect to.
- <times>: Number of times to attempt the connection.

Example:
```bash
python paping.py 209.85.225.147 80 10
```
This will attempt to connect to 209.85.225.147 on port 80 ten times.

## Output
The script outputs:

- Connection attempts, showing success or failure.
- Connection statistics including total attempts, successful connections, failed connections, and percentages.
- Average, minimum, and maximum connection times for successful connections.
Example Output:
```bash
Connecting to 209.85.225.147 on TCP 80:

Connected to 209.85.225.147 time=24.00ms protocol=TCP port=80
Connected to 209.85.225.147 time=25.00ms protocol=TCP port=80
Connection timed out
Connected to 209.85.225.147 time=24.00ms protocol=TCP port=80

Connection statistics: Attempted = 4, Connected = 3, Failed = 1 (25.00%)
Approximate connection times: Minimum = 24.00ms, Maximum = 25.00ms, Average = 24.33ms
```

