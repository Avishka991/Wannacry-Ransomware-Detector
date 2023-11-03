import time

def get_current_time():
    # Get the current time in milliseconds since the epoch
    return int(time.time() * 1000)

# Example usage
current_time = get_current_time()
print("Current time in milliseconds since the epoch:", current_time)
