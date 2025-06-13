





# Author : Angel Namaskodi
# Purpose : Developing a tool to scan open ports on devices
# Start date : 12-Jun-2025
# End date   : 13-Jun-2025
# Import necessary modules
import socket                         # For network connections and socket operations
#from datetime import datetime         # For tracking scan duration

try:
    # Prompt user for the IP address to scan and remove any leading/trailing spaces
    ip = input("Enter IP address to scan: ").strip()

    try:
        # Validate the entered IP address format
         ip = socket.gethostbyname(ip)
         socket.inet_aton(ip)         # Will raise an error if the IP is invalid
    except socket.error:
        print("Invalid IP address format or host name")
        exit()                       # Exit program if IP is invalid

    # Prompt user for port range (start and end)
    try:
        start_port = int(input("Enter starting port number (0-65535): "))   # Convert input to integer
        end_port = int(input("Enter ending port number (0-65535): "))
    except ValueError:
        print("Invalid input. Port numbers must be integers.")
        exit()                       # Exit program if ports are not valid integers

    # Check if ports are within valid range (0–65535)
    if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
        print("Port numbers must be between 0 and 65535.")
        exit()

    # Check if starting port is not greater than ending port
    if start_port > end_port:
        print("Starting port must be less than or equal to ending port.")
        exit()

    # Display scan details
    print(f"\nStarting scan on host: {ip}")
    print(f"Scanning ports from {start_port} to {end_port}")
    #start_time = datetime.now()     # Record the current time before scan starts
    opport =0 #Counter for opened ports
    # Loop through each port in the specified range
    for port in range(start_port, end_port + 1):
        try:
            
            # Create a new TCP socket using IPv4
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)    # Set timeout to half a second for each connection attempt

            # Try to connect to the IP and port
            result = sock.connect_ex((ip, port))   # Returns 0 if connection is successful

            if result == 0:
                
                print(f"Port {port} is OPEN", "and he Protocol is",socket.getservbyport(port,'TCP' ))     # Print open port
                opport+=1                          #Increment the counter if the port is opened
                
                #print(socket.getservbyport(port,'TCP'))      # Print the port name
                
            sock.close()                           # Close socket after check
           # print("the port",port,"is closed" )

        except socket.error as e:
            # Handle socket-related errors (e.g., network issues)
            print(f"Socket error on port {port}: {e}")

        except Exception as e:
            # Catch any unexpected errors
            print(f"Unexpected error on port {port}: {e}")
    if opport==0 :
      print("No open ports found.")
    # Record end time after scanning completes
    #end_time = datetime.now()
    
    # Calculate and display total scan duration
   # print(f"\nScan completed in: {end_time - start_time}")

# Handle user interruption with Ctrl+C
except KeyboardInterrupt:
    print("\nScan interrupted by user.")

# Catch any unexpected exceptions during the entire execution
except Exception as e:
    print(f"An unexpected error occurred: {e}")
