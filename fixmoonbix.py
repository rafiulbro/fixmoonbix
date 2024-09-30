import os
import time

# Specify the file path you want to delete
file_path = "/data/data/com.termux/files/home/moonbix-bot/tokens.json"

while True:
    # Initial 5-second countdown before deleting the file
    for i in range(5, 0, -1):
        print(f"Deleting in {i} seconds...", end="\r")
        time.sleep(1)  # Wait 1 second for each step in the countdown

    # Check if the file exists before attempting to delete
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"\ndeleted")
    else:
        print(f"\nAlready Deleted")
    
    # Countdown for 28 minutes (28 * 60 seconds)
    total_seconds = 10 * 60
    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        print(f"Next deletion in {minutes:02d}:{seconds:02d} minutes", end="\r")
        time.sleep(1)  # Sleep for 1 second and update countdown
        total_seconds -= 1
