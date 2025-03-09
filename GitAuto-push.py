import os
import time
import subprocess
import hashlib
from pathlib import Path

# Path to monitor
DIRECTORY_TO_MONITOR = r"C:\xampp\htdocs\movie-booking-system"

def get_directory_hash(directory):
    """Calculate a hash of all files in the directory to detect changes"""
    hash_list = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Skip git directory
            if ".git" in root:
                continue
                
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                    hash_list.append(f"{file_path}:{file_hash}")
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    
    # Sort to ensure consistent ordering
    hash_list.sort()
    return hashlib.md5("".join(hash_list).encode()).hexdigest()

def git_operations():
    """Execute git operations: add, commit, and push"""
    try:
        # Change to the directory
        os.chdir(DIRECTORY_TO_MONITOR)
        
        # Git add
        print("Running git add...")
        add_process = subprocess.run(["git", "add", "."], 
                                    check=True, 
                                    capture_output=True, 
                                    text=True)
        print(f"git add output: {add_process.stdout}")
        
        # Check if there are changes to commit
        status_process = subprocess.run(["git", "status", "--porcelain"], 
                                       check=True, 
                                       capture_output=True, 
                                       text=True)
        
        if not status_process.stdout.strip():
            print("No changes to commit.")
            return False
        
        # Git commit
        print("Running git commit...")
        commit_process = subprocess.run(["git", "commit", "-m", "Auto-commit: Changes detected"], 
                                       check=True, 
                                       capture_output=True, 
                                       text=True)
        print(f"git commit output: {commit_process.stdout}")
        
        # Git push
        print("Running git push...")
        push_process = subprocess.run(["git", "push", "origin", "main"], 
                                     check=True, 
                                     capture_output=True, 
                                     text=True)
        print(f"git push output: {push_process.stdout}")
        
        print("Successfully pushed changes to repository!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error in git operations: {e}")
        print(f"Command output: {e.stdout}")
        print(f"Command error: {e.stderr}")
        return False

def main():
    print(f"Starting file monitor for {DIRECTORY_TO_MONITOR}")
    
    # Check if directory exists
    if not os.path.exists(DIRECTORY_TO_MONITOR):
        print(f"Error: Directory {DIRECTORY_TO_MONITOR} does not exist.")
        return
    
    # Check if it's a git repository
    if not os.path.exists(os.path.join(DIRECTORY_TO_MONITOR, ".git")):
        print(f"Error: {DIRECTORY_TO_MONITOR} is not a git repository.")
        return
    
    # Get initial directory hash
    previous_hash = get_directory_hash(DIRECTORY_TO_MONITOR)
    print("Initial directory hash calculated. Monitoring for changes...")
    
    try:
        while True:
            # Get current hash
            current_hash = get_directory_hash(DIRECTORY_TO_MONITOR)
            
            # Check if hash has changed
            if current_hash != previous_hash:
                print("Changes detected!")
                
                # Perform git operations
                success = git_operations()
                
                if success:
                    # Update hash after successful git operations
                    previous_hash = current_hash
                
            # Wait before checking again
            time.sleep(10)  # Check every 10 seconds
            
    except KeyboardInterrupt:
        print("\nStopping file monitor.")

if __name__ == "__main__":
    main()
