import csv
import sys
import gzip

def main():
    if len(sys.argv) < 9:
        print("Error : No result passed from Splunk")
        return
    
    results_file = sys.argv[8]

    try:
        with gzip.open(results_file, 'rt') as f:
            reader = csv.DictReader(f)
            for row in reader:
                attacker_ip = row.get('src_ip')

                if attacker_ip:
                    print(f"Action: blocking {attacker_ip} on Firewall...")
                    with open("D:/Sonuu/Documents/firewall_blocklist.txt", "a") as blocklist:
                        blocklist.write(f"{attacker_ip}\n")

    except Exception as e:
        print(f"Error processing allert results: {e}")

if __name__ == "__main__":
    main()                            