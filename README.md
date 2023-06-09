# OperatingSystemCourseDesign
A university student use python to write a course design with GUI.

# question description
The Chinese(simplied) version is original,and the English version is from Google translate.

Chinese version:
According to the rule, the writer can't show others.

English version:
- Simulate the realization of priority-based time slice round-robin scheduling algorithm and multi-level feedback queue round-robin scheduling algorithm in process scheduling. The priority-based time slice round-robin scheduling algorithm can arbitrarily select the number of processes, the arrival time, running time and time slice size of each process, where the time slice size, process arrival time (starting from 0) and running time are all integers. The initial value of the process priority number is an integer between 1 and 100, and the smaller the priority number, the higher the priority. The priority of the process decreases every time a time slice is executed (such as the priority number + 2 or 3). The round-robin scheduling algorithm of multi-level feedback queues sets the number of queues to 3, and the time slice size of each level of queues is selected according to the sequential increase of the queue number. The time slice size, number of processes, process arrival time, and running time requirements are the same as those of the priority-based time slice round-robin scheduling algorithm. It is required to design a corresponding algorithm, simulate the execution process of each process in the algorithm and display it dynamically, that is, each time a process is switched, the execution status of each process (how much time has been executed, how much time is left to be executed, the state of the process is ready It is still executed, the process queuing in each queue), and finally lists the start execution time and end time of each process.

- Simulate the implementation of first-come-first-serve, short-job priority and highest response ratio scheduling algorithms in job scheduling. The number of jobs, the submission time (clock time) and running time (hours) of each job can be selected arbitrarily. It is required to design a corresponding algorithm, simulate the job scheduling process and display, that is, each job scheduling, the execution status of each job (start execution time, end time, turnaround time), and finally calculate and list the average turnaround time, and the same In this case, the performance analysis and comparison of different scheduling algorithms are carried out.

- The simulation implementation process requires the use of a visual graphical interface for operation and display.
