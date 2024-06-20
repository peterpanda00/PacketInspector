# PacketInspector

PacketInspector is a tool designed to automate the process of capturing and extracting files from network traffic. By integrating `tshark` and a scripted version of NetworkMiner CLI, PacketInspector provides a streamlined interface for real-time packet capture and efficient file extraction from the captured packets.

## Features

- **Automated Packet Capture**: Uses `tshark` to capture network packets based on user-specified interfaces and filters.
- **File Extraction**: Utilizes a scripted version of NetworkMiner CLI to extract files from captured packets.
- **User-Friendly Workflow**: Combines the functionalities of `tshark` and NetworkMiner CLI into a single, easy-to-use command-line interface.

## Requirements

- Python 3.x
- `tshark` (part of Wireshark) installed and accessible in your system's PATH
- NetworkMiner CLI executable

## Installation

1. **Install Python 3**
   - Download and install Python 3 from the official website: https://www.python.org/downloads/

2. **Install Wireshark**
   - Download and install Wireshark, which includes `tshark`: https://www.wireshark.org/download.html

3. **Set Up NetworkMiner CLI**
   - Ensure you have NetworkMiner CLI executable and note its path. Download from here: https://github.com/mammo0/networkminer-cli

4. **Clone or Download PacketInspector**
   - Clone the repository or download the source code to your local machine.

## Usage

1. **Navigate to the PacketInspector Directory**
   ```sh
   cd path/to/PacketInspector
   ```

2. **Run PacketInspector**
   ```sh
   python PacketInspector.py
   ```

3. **Follow the Prompts**
   - Enter the capture interface (e.g., eth0 or Wi-Fi).
   - Enter the capture filter (e.g., tcp port 80).
   - Enter the name of the pcap file to save (e.g., capture.pcap).
   - Enter the capture duration in seconds (e.g., 60).

## Example

### Input

```
Enter the capture interface (e.g., eth0 or Wi-Fi): Wi-Fi
Enter the capture filter (e.g., tcp port 80): tcp port 80
Enter the name of the pcap file to save (e.g., capture.pcap): capture.pcap
Enter the capture duration in seconds (e.g., 60): 60
```

### Output

```
Running tshark command: "C:\Program Files\Wireshark\tshark.exe" -i Wi-Fi -f tcp port 80 -w capture.pcap -F pcap
Capturing packets for 60 seconds...
Packet capture completed.
Running NetworkMinerCLI command: "C:\Users\YourUsername\Desktop\PacketInspector\networkminer-cli\NetworkMinerCLI.exe" capture.pcap
Analysis completed. Output stored in C:\Users\YourUsername\Desktop\PacketInspector\
```

### Extracted Files

The extracted files from the analysis will be stored in the networkminer-cli\AssembledFiles.


