import operator
from collections import deque


class Job:
    def __init__(self, id, submission_time, running_time):
        self.id = id
        self.submission_time = submission_time
        self.running_time = running_time
        self.response_ratio = 0


def simulate_FCFS(jobs):
    ret_str = "simulate_FCFS:\n"
    jobs.sort(key=operator.attrgetter('submission_time'))
    current_time = 0
    total_turnaround_time = 0

    for job in jobs:
        start_time = max(current_time, job.submission_time)
        end_time = start_time + job.running_time
        turnaround_time = end_time - job.submission_time
        total_turnaround_time += turnaround_time

        # print(f"Job ID: {job.id}, Start Time: {start_time}, End Time: {end_time}, Turnaround Time: {turnaround_time}")
        ret_str += f"Job ID: {job.id}, Start Time: {start_time}, End Time: {end_time}, Turnaround Time: {turnaround_time} \n"

        current_time = end_time

    avg_turnaround_time = total_turnaround_time / len(jobs)
    # print(f"\nAverage Turnaround Time for FCFS: {avg_turnaround_time}\n")
    ret_str += f"\nAverage Turnaround Time for FCFS: {avg_turnaround_time}\n"

    ret_tuple = (ret_str, avg_turnaround_time)
    # print(ret_tuple
    return ret_tuple


def simulate_SJF(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x.submission_time)

    queue = []
    current_time = 0
    total_jobs = len(sorted_jobs)
    turnaround_times = []

    ret_str = "simulate_SJF:\n"

    while len(queue) > 0 or len(sorted_jobs) > 0:
        # print(f"current_time:{current_time}")

        while len(sorted_jobs) > 0 and sorted_jobs[0].submission_time <= current_time:
            queue.append(sorted_jobs[0])
            sorted_jobs.pop(0)

        if len(queue) > 0:
            queue = sorted(queue, key=lambda x: x.running_time)
            current_job = queue.pop(0)
            start_time = max(current_time, current_job.submission_time)
            current_time = start_time + current_job.running_time
            end_time = current_time
            turnaround_time = end_time - current_job.submission_time
            turnaround_times.append(turnaround_time)

            # print(f"Job {current_job.id}: Start time: {start_time}, End time: {end_time}, Turnaround time: {turnaround_time}")
            ret_str += f"Job {current_job.id}: Start time: {start_time}, End time: {end_time}, Turnaround time: {turnaround_time} \n"
        else:
            current_time = current_time + 1

    avg_turnaround_time = sum(turnaround_times) / total_jobs

    # print(f"\nAverage Turnaround Time for SJF: {avg_turnaround_time}\n")
    ret_str += f"\nAverage Turnaround Time for SJF: {avg_turnaround_time}\n"

    ret_tuple = (ret_str, avg_turnaround_time)
    # print(ret_tuple)
    return ret_tuple


def simulate_HRRN(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x.submission_time)
    queue = []
    current_time = 0
    total_jobs = len(sorted_jobs)
    turnaround_times = []

    ret_str = "simulate_HRRN:\n"

    while len(queue) > 0 or len(sorted_jobs):

        while len(sorted_jobs) > 0 and sorted_jobs[0].submission_time <= current_time:
            queue.append(sorted_jobs[0])
            sorted_jobs.pop(0)

        if len(queue) > 0:
            for job in queue:
                waiting_time = current_time - job.submission_time
                response_ratio = (waiting_time + job.running_time) / job.running_time
                job.response_ratio = response_ratio
            queue = sorted(queue, key=lambda x: x.response_ratio)
            current_job = queue.pop(0)

            start_time = max(current_time, current_job.submission_time)
            current_time = start_time + current_job.running_time
            end_time = current_time
            turnaround_time = end_time - current_job.submission_time
            turnaround_times.append(turnaround_time)

            # print(f"Job {current_job.id}: Start time: {start_time}, End time: {end_time}, Turnaround time: {turnaround_time}")
            ret_str += f"Job {current_job.id}: Start time: {start_time}, End time: {end_time}, Turnaround time: {turnaround_time} \n"
        else:
            current_time = current_time + 1

    avg_turnaround_time = sum(turnaround_times) / total_jobs

    # print(f"\nAverage Turnaround Time for HRRN: {avg_turnaround_time}\n")
    ret_str += f"\nAverage Turnaround Time for HRRN: {avg_turnaround_time}\n"

    ret_tuple = (ret_str, avg_turnaround_time)
    return ret_tuple


# Define the jobs using the Job class
# jobs = [
#     Job(1, 0, 6),
#     Job(2, 1, 4),
#     Job(3, 2, 2),
#     Job(4, 3, 5),
#     Job(5, 4, 3),
# ]

# Simulate and display FCFS scheduling
# print("FCFS Scheduling:")
# simulate_FCFS(jobs)

# Simulate and display SJF scheduling
# print("SJF Scheduling:")
# simulate_SJF(jobs)

# Simulate and display HRRN scheduling
# print("HRRN Scheduling:")
# simulate_HRRN(jobs)
