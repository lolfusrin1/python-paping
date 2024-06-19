import socket
import time
import sys

def paping(ip, port, times):
    port = int(port)
    times = int(times)

    YELLOW = "\033[93m"
    GREEN = "\033[92m"   
    RED = "\033[91m"     
    RESET = "\033[0m"    

    print(f"\nConnecting to {YELLOW}{ip}{RESET} on TCP {YELLOW}{port}{RESET}:\n")
    
    successes = 0
    failures = 0
    total_time = 0

    for i in range(times):
        try:
            start_time = time.time()
            sock = socket.create_connection((ip, port), timeout=1)
            end_time = time.time()
            sock.close()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Connected to {GREEN}{ip}{RESET} time={GREEN}{elapsed_time:.2f}ms{RESET} protocol={GREEN}TCP{RESET} port={GREEN}{port}{RESET}")
            successes += 1
            total_time += elapsed_time
        except (socket.timeout, socket.error) as e:
            print(f"{RED}Connection timed out{RESET}")
            failures += 1
        
        time.sleep(1)

    if times > 0:
        print(f"\nConnection statistics: Attempted = {times}, Connected = {successes}, Failed = {failures} "
              f"({failures / times * 100:.2f}%)")
        if successes > 0:
            print(f"Approximate connection times: Minimum = {min(total_time / successes, 0):.2f}ms, Maximum = {max(total_time / successes, 0):.2f}ms, "
                  f"Average = {total_time / successes:.2f}ms")
    else:
        print("No connection attempts made.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python paping.py <ip> <port> <times>")
        sys.exit(1)

    ip = sys.argv[1]
    port = sys.argv[2]
    times = sys.argv[3]

    paping(ip, port, times)
