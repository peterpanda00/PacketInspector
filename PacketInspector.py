import subprocess
import os
import time
import pandas as pd

def get_user_input():
    tshark_interface = input("Enter the capture interface (e.g., eth0 or Wi-Fi): ")
    tshark_filter = input("Enter the capture filter (e.g., tcp port 80): ")
    pcap_file = input("Enter the name of the pcap file to save (e.g., capture.pcap): ")
    capture_duration = int(input("Enter the capture duration in seconds (e.g., 60): "))
    
    networkminer_path = 'C:\\Users\\Jill\\Desktop\\PacketInspector\\networkminer-cli\\NetworkMinerCLI.exe' # Replace with your actual path to NetworkMinerCLI.exe
    
    return tshark_interface, tshark_filter, pcap_file, networkminer_path, capture_duration

def capture_packets(interface, capture_filter, pcap_output):
    tshark_path = r'C:\Program Files\Wireshark\tshark.exe'  # Replace with your actual path to tshark.exe
    tshark_command = [
        tshark_path,
        '-i', interface,
        '-f', capture_filter,
        '-w', pcap_output,
        '-F', 'pcap'
    ]
    print(f"Running tshark command: {' '.join(tshark_command)}")
    tshark_process = subprocess.Popen(tshark_command)

    return tshark_process

def analyze_pcap(networkminer_cli_path, pcap_input):
    networkminer_command = [
        networkminer_cli_path,
        pcap_input
    ]
    print(f"Running NetworkMinerCLI command: {' '.join(networkminer_command)}")
    subprocess.run(networkminer_command)


if __name__ == "__main__":
    # Get user input
    tshark_interface, tshark_filter, pcap_file, networkminer_path, capture_duration = get_user_input()
    
    # Start capturing packets
    tshark_process = capture_packets(tshark_interface, tshark_filter, pcap_file)
    
    # Capture packets for the specified duration
    print(f"Capturing packets for {capture_duration} seconds...")
    time.sleep(capture_duration)
    
    # Stop tshark
    tshark_process.terminate()
    tshark_process.wait()
    print("Packet capture completed.")
    
    # Analyze the captured pcap file with NetworkMinerCLI
    analyze_pcap(networkminer_path, pcap_file)
    print(f"Analysis completed. Output stored in networkminer-cli\AssembledFiles")
    