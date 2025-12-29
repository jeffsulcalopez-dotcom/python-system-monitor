import time
import psutil
import platform

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_hours = int(uptime_seconds // 3600)
    uptime_minutes = int((uptime_seconds % 3600) // 60)
    return f"{uptime_hours}h {uptime_minutes}m"

def monitor():
    print("=== System Resource Monitor ===")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
    print(f"Uptime: {get_uptime()}")

if __name__ == "__main__":
    monitor()
    input("\nPress Enter to exit...")
