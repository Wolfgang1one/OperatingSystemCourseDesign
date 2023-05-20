from collections import deque

# Define process class
class Process:
    def __init__(self, pid, arrival_time, burst_time, queue_num=1):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.queue_num = queue_num
        self.remaining_time = burst_time

    def __repr__(self):
        return f'P{self.pid}'

# Define queue class
class Queue:
    def __init__(self, time_slice):
        self.time_slice = time_slice
        self.processes = deque()

    def enqueue(self, process):
        self.processes.append(process)

    def dequeue(self):
        return self.processes.popleft()

    def is_empty(self):
        return len(self.processes) == 0

# Define simulation function
def simulate(processes, queue1_slice, queue2_slice, queue3_slice):
    # Initialize queues
    queue1 = Queue(queue1_slice)
    queue2 = Queue(queue2_slice)
    queue3 = Queue(queue3_slice)

    # Enqueue processes in first queue
    for p in processes:
        queue1.enqueue(p)

    # Initialize time counter
    time = 0

    # Initialize list to store start and end times of processes
    start_end_times = []

    ret = ""

    # Main loop
    while True:
        # Check if all processes have completed
        if all(p.remaining_time == 0 for p in processes):
            break

        # Execute process in first queue
        if not queue1.is_empty():
            process = queue1.dequeue()
            start_time = max(process.arrival_time, time)
            end_time = min(start_time + queue1.time_slice, start_time + process.remaining_time)
            process.remaining_time -= (end_time - start_time)
            time = end_time

            print("queue1:")
            print(f"pid:{process.pid}  arrival_time:{process.arrival_time} remaining_time:{process.remaining_time} current_time:{time}")

            ret += "queue1:\n"
            ret += f"pid:{process.pid}  arrival_time:{process.arrival_time} remaining_time:{process.remaining_time} current_time:{time} \n"

            if process.remaining_time == 0:
                start_end_times.append((process.pid, start_time, end_time))
            else:
                process.queue_num += 1
                queue2.enqueue(process)

        # Execute process in second queue
        elif not queue2.is_empty():
            process = queue2.dequeue()
            start_time = max(process.arrival_time, time)
            end_time = min(start_time + queue2.time_slice, start_time + process.remaining_time)
            process.remaining_time -= (end_time - start_time)
            time = end_time
            print("queue2:")
            print(f"pid:{process.pid}  arrival_time:{process.arrival_time} remaining_time:{process.remaining_time} current_time:{time}")

            ret += "queue2:\n"
            ret += f"pid:{process.pid}  arrival_time:{process.arrival_time} remaining_time:{process.remaining_time} current_time:{time} \n"
            if process.remaining_time == 0:
                start_end_times.append((process.pid, start_time, end_time))
            else:
                process.queue_num += 1
                queue3.enqueue(process)

        # Execute process in third queue
        elif not queue3.is_empty():
            process = queue3.dequeue()
            start_time = max(process.arrival_time, time)
            end_time = start_time + process.remaining_time
            process.remaining_time = 0
            time = end_time
            print("queue3:")
            print(f"pid:{process.pid}  arrival_time:{process.arrival_time} remaining_time:{process.remaining_time} current_time:{time}")

            ret += "queue3:\n"
            ret += f"pid:{process.pid}  arrival_time:{process.arrival_time} remaining_time:{process.remaining_time} current_time:{time} \n"
            start_end_times.append((process.pid, start_time, end_time))

        # If all queues are empty, increment time counter
        else:
            time += 1

    print("\nthe conclusion : ")

    ret += "\nthe conclusion: \n"
    # Print start and end times of processes
    for pid, start_time, end_time in start_end_times:
        print(f'P{pid} started at time {start_time} and ended at time {end_time}')
        ret += f'P{pid} started at time {start_time} and ended at time {end_time} \n'

    return ret



# if __name__ == '__main__':
#     # Define processes
#     processes = [
#         Process(1, 0, 8),
#         Process(2, 1, 4),
#         Process(3, 2, 9),
#         Process(4, 3, 5),
#         Process(5, 4, 2),
#         Process(6, 5, 3),
#         Process(7, 6, 7),
#         Process(8, 7, 6),
#         Process(9, 8, 1),
#         Process(10, 9, 4)
#     ]
#
#     # Set time slice values for each queue
#     queue1_slice = 1
#     queue2_slice = 2
#     queue3_slice = 4
#
#     # Run simulation
#     simulate(processes, queue1_slice, queue2_slice, queue3_slice)

