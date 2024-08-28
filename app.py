import os
import sys
from datetime import datetime



path = os.getenv('ANALYSIS_PATH', '/')

def analyze_filesystem(path):
    files = []
    total_files = 0

    for root, dirs, filenames in os.walk(path):
        for f in filenames:
            try:
                full_path = os.path.join(root, f)
                size = os.path.getsize(full_path)
                files.append((full_path, size))
                total_files += 1
            except OSError:
                pass

   
    files.sort(key=lambda x: x[1], reverse=True)
    top_10_files = files[:10]

    print(f"\nTotal number of files: {total_files}")
    print("\nTop 10 largest files:")
    for file, size in top_10_files:
        print(f"{file}: {size/1024:.2f} KB")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_name = sys.argv[1]
    else:
        user_name = "User"

   
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello, {user_name}! Current date and time: {current_time}")

    
    analyze_filesystem(path)
