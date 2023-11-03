import threading
import os
import time

# Define constants
MAX_TIME_TO_GET_INFECTED = 600  # You can change this value as needed

# Define a function to get user input
def user_input():
    return input("Enter the path of folder to monitor:\n")

# Define the vssadmin_detector function
def vssadmin_detector(pData):
    while not pData['detected'][0]:
        # Simulate some logic to check for vssadmin.exe
        pass

# Define the Watcher function
def Watcher(pData):
    while not pData['detected'][0]:
        # Simulate some logic to monitor the file system
        pass

# Define the registry_monitor function
def registry_monitor(pData):
    while not pData['detected'][0]:
        # Simulate some logic to monitor the registry
        pass

def main():
    # Initialize data dictionaries
    pData_vssadmin_detector = {
        'path': "vssadmin.exe",
        'last_successful': int(time.time()) - MAX_TIME_TO_GET_INFECTED,
        'detected': [False]
    }

    pData_file_sytem_watcher = {
        'path': user_input(),
        'last_successful': int(time.time()) - 3 * MAX_TIME_TO_GET_INFECTED,
        'detected': [False]
    }

    pData_registry_monitor = {
        'path': "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
        'last_successful': int(time.time()) - 5 * MAX_TIME_TO_GET_INFECTED,
        'detected': [False]
    }

    # Create and start threads
    threads = []
    threads.append(threading.Thread(target=vssadmin_detector, args=(pData_vssadmin_detector,)))
    threads.append(threading.Thread(target=Watcher, args=(pData_file_sytem_watcher,)))
    threads.append(threading.Thread(target=registry_monitor, args=(pData_registry_monitor,)))

    for thread in threads:
        thread.start()

    print("\nRANSOMWARE DETECTION HAS STARTED:\n")

    # Monitor for ransomware detection
    while not any(pData['detected'][0] for pData in [pData_vssadmin_detector, pData_file_sytem_watcher, pData_registry_monitor]):
        pass

    # Signal threads to stop
    for pData in [pData_vssadmin_detector, pData_file_sytem_watcher, pData_registry_monitor]:
        pData['detected'][0] = True

    # Wait for threads to finish
    for thread in threads:
        thread.join()

    print("High possibility of a RANSOMWARE INFECTION!!!!")

if __name__ == "__main__":
    main()
