import subprocess
import sys

def check_ip_availability(ip_list, output_file):
    with open(output_file, 'w') as f:
        for ip in ip_list:
            result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE)
            if result.returncode == 0:
                f.write(f"{ip} is reachable\n")
            else:
                f.write(f"{ip} is not reachable\n")

if __name__ == "__main__":
    ip_list = sys.argv[1:]
    output_file = "ip_availability.txt"
    check_ip_availability(ip_list, output_file)
