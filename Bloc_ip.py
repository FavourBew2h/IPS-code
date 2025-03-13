import ctypes

def block_ip_address(ip_address):
    # Load the Windows Firewall API library
    fw_api = ctypes.windll.iphlpapi
    
    # Define the IP address to block
    ip_address_bytes = ctypes.c_char_p(ip_address.encode())
    
    # Block the IP address
    fw_api.NetFwTypeLibBlockIP(ip_address_bytes, None)
    
    # Check if the IP address was blocked successfully
    if fw_api.GetLastError() == 0:
        print(f"IP address {ip_address} blocked successfully")
    else:
        print(f"Failed to block IP address {ip_address}")
