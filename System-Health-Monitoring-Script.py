import psutil
import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
NUM_PROCESSES_THRESHOLD = 200

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"CPU usage is high - {cpu_usage}%")


def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"Memory usage is high - {memory_usage}%")

def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        print(f"Disk usage is high - {disk_usage}%")

def check_running_process():
    total_processes = psutil.process_iter()
    processes_list = list(total_processes)
    number_processes = len(processes_list)
    if number_processes > NUM_PROCESSES_THRESHOLD:
        print(f"Number of running process is high - {number_processes}")
    
def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp}:{message}"
    print(log_line)
    with open('system_health.log', 'a') as log_file:
        log_file.write(log_line + '\n')

def main():
    print("starting system health monitoring...")

    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_running_process()

if __name__ == "__main__":
    main()
