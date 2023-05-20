class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time

    def execute(self, time_slice):
        if self.remaining_time <= time_slice:
            time_executed = self.remaining_time
            self.remaining_time = 0
        else:
            time_executed = time_slice
            self.remaining_time -= time_slice
        return time_executed

    def is_finished(self):
        return self.remaining_time == 0


class Scheduler:
    def __init__(self, processes, time_slice):
        self.processes = processes
        self.time_slice = time_slice
        self.current_time = 0
        self.ready_queue = []
        self.finished_queue = []

    def run(self):
        ret = ""
        while self.processes or self.ready_queue:
            # Add new processes to the ready queue
            while self.processes and self.processes[0].arrival_time <= self.current_time:
                process = self.processes.pop(0)
                self.ready_queue.append(process)
                self.ready_queue.sort(key=lambda x: x.priority)

            if not self.ready_queue:
                self.current_time += 1
                continue

            # Select the process with the highest priority and execute it
            process = self.ready_queue.pop(0)
            time_executed = process.execute(self.time_slice)
            if process.is_finished():
                process.finish_time = self.current_time + time_executed
                self.finished_queue.append(process)
            else:
                process.priority += 2
                self.ready_queue.append(process)
                self.ready_queue.sort(key=lambda x: x.priority)

            # Increment the current time
            # print(f"current time {self.current_time} : \npid\t arrival_time\t burst_time\t priority\t remaining_time\t")
            ret += f"current time {self.current_time} : \npid\t arrival_time\t burst_time\t priority\t remaining_time\t \n"

            for process in self.ready_queue:
                # print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.priority}\t\t{process.remaining_time}")
                ret += f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.priority}\t\t{process.remaining_time} \n"


            # print("\n")

            self.current_time += time_executed
        ret += "PID\tArrival Time\tBurst Time\tPriority\tFinish Time \n"

        for process in self.finished_queue:
            ret += f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.priority}\t\t{process.finish_time} \n"

        # print(ret)
        return ret


    def print_results(self):
        print("PID\tArrival Time\tBurst Time\tPriority\tFinish Time")
        for process in self.finished_queue:
            print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.priority}\t\t{process.finish_time}")


# if __name__=="__main__":
#
#     processes = [
#         Process(1, 0, 5, 10),
#         Process(2, 1, 3, 20),
#         Process(3, 2, 1, 30),
#         Process(4, 3, 7, 40),
#         Process(5, 4, 4, 50),
#     ]
#     scheduler = Scheduler(processes, time_slice=2)
#
#     scheduler.run()
    # scheduler.print_results()
