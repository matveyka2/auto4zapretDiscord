import os
import subprocess
import time

def run_programs():
    bat_path = r"yourBypassPath"
    discord_path = r"yourDiscordPath"
    
    subprocess.Popen(bat_path, shell=True)
    time.sleep(2)
    os.startfile(discord_path)

if __name__ == "__main__":
    run_programs()