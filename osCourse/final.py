import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

import source_code


class P_1(QWidget):

    def __init__(self):
        super().__init__()
        self.output = None
        self.input = None
        self.submit = None
        self.ui = None
        self.init_ui()
        # self.calculate()

    def init_ui(self):
        self.ui = uic.loadUi("./ui/P.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        self.submit = self.ui.pushButton
        self.input = self.ui.textEdit
        self.output = self.ui.textBrowser

        output_text = "输入进程数\n"
        output_text += "按如下格式输入进程信息(pid arrival_time burst_time priority)空格分开，一个一个程序输入，回车结束\n"
        self.output.setPlainText(output_text)

        self.submit.clicked.connect(self.st)

    def st(self):
        input_text = self.input.toPlainText()
        self.input.clear()
        self.output.append(input_text)

        print(input_text)

        result = input_text.split('\n')
        split_string = []
        for substr in result:
            split_string.extend(substr.split())

        split_string = list(map(int, split_string))

        n = split_string[0]
        split_string.pop(0)

        # print(n)
        # print(split_string)

        processes = []

        for i in range(n):
            i_pid = split_string[0]
            i_arrival_time = split_string[1]
            i_burst_time = split_string[2]
            i_priority = split_string[3]
            split_string.pop(0)
            split_string.pop(0)
            split_string.pop(0)
            split_string.pop(0)
            p = source_code.P_1.Process(pid=i_pid, arrival_time=i_arrival_time, burst_time=i_burst_time,
                                        priority=i_priority)
            # print(p)
            processes.append(p)
            # print(processes)

        scheduler = source_code.P_1.Scheduler(processes, time_slice=2)

        output_text = scheduler.run()
        self.output.append(output_text)

        self.output.moveCursor(self.output.textCursor().End)  # 移动光标到底部


class P_2(QWidget):

    def __init__(self):
        super().__init__()
        self.output = None
        self.input = None
        self.submit = None
        self.ui = None
        self.init_ui()
        # self.calculate()

    def init_ui(self):
        self.ui = uic.loadUi("./ui/P.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        self.submit = self.ui.pushButton
        self.input = self.ui.textEdit
        self.output = self.ui.textBrowser

        output_text = "输入进程数\n"
        output_text += "按如下格式输入进程信息（pid arrival_time burst_time）空格分开，一个一个程序输入，回车结束\n"
        output_text += "请输入(queue1_slice queue2_slice queue3_slice) 空格分开"
        self.output.setPlainText(output_text)

        self.submit.clicked.connect(self.st)

    def st(self):
        input_text = self.input.toPlainText()
        self.input.clear()
        self.output.append(input_text)

        result = input_text.split('\n')
        split_string = []
        for substr in result:
            split_string.extend(substr.split())

        split_string = list(map(int, split_string))

        n = split_string[0]
        split_string.pop(0)

        processes = []

        for i in range(n):
            i_pid = split_string[0]
            i_arrival_time = split_string[1]
            i_burst_time = split_string[2]
            split_string.pop(0)
            split_string.pop(0)
            split_string.pop(0)
            p = source_code.P_2.Process(pid=i_pid, arrival_time=i_arrival_time, burst_time=i_burst_time)
            # print(p)
            processes.append(p)

        queue1_slice = split_string[0]
        queue2_slice = split_string[1]
        queue3_slice = split_string[2]

        output_text = source_code.P_2.simulate(processes, queue1_slice, queue2_slice, queue3_slice)

        self.output.append(output_text)

        self.output.moveCursor(self.output.textCursor().End)  # 移动光标到底部


class J(QWidget):

    def __init__(self):
        super().__init__()
        self.output = None
        self.input = None
        self.submit = None
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./ui/J.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        self.submit = self.ui.pushButton
        self.input = self.ui.textEdit
        self.output = self.ui.textBrowser

        output_text = "输入作业数\n"
        output_text += "按如下格式输入进程信息(id submission_time running_time)空格分开，一个一个程序输入，回车结束\n"
        self.output.setPlainText(output_text)

        self.submit.clicked.connect(self.st)

    def st(self):
        input_text = self.input.toPlainText()
        self.input.clear()
        self.output.append(input_text)

        result = input_text.split('\n')
        split_string = []
        for substr in result:
            split_string.extend(substr.split())

        split_string = list(map(int, split_string))

        n = split_string[0]
        split_string.pop(0)

        jobs = []

        for i in range(n):
            i_id = split_string[0]
            i_submission_time = split_string[1]
            i_running_time = split_string[2]
            split_string.pop(0)
            split_string.pop(0)
            split_string.pop(0)
            job = source_code.J_1.Job(id=i_id, submission_time=i_submission_time, running_time=i_running_time)
            jobs.append(job)

        t_FCFS = source_code.J_1.simulate_FCFS(jobs)
        t_SJF = source_code.J_1.simulate_SJF(jobs)
        t_HRRN = source_code.J_1.simulate_HRRN(jobs)

        ret_str = t_FCFS[0] + t_SJF[0] + t_HRRN[0]

        ret_str += "\n"
        ret_str += "the least time Average Turnaround Time is "

        t_best = min(t_FCFS[1], min(t_SJF[1], t_HRRN[1]))

        ret_str += str(t_best)

        self.output.append(ret_str)


class MENU(QWidget):

    def __init__(self):
        super().__init__()
        self.btn_p_2 = None
        self.btn_p_1 = None
        self.p2 = None
        self.p1 = None
        self.j = None
        self.p = None
        self.btn_j = None
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./ui/menu.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        self.btn_p_1 = self.ui.pushButton
        self.btn_p_2 = self.ui.pushButton_3
        self.btn_j = self.ui.pushButton_2

        self.btn_p_1.clicked.connect(self.to_P_1)
        self.btn_p_2.clicked.connect(self.to_P_2)
        self.btn_j.clicked.connect(self.to_J)
        self.p1 = P_1()
        self.p2 = P_2()
        self.j = J()

    def to_P_1(self):
        self.hide()
        self.p1.ui.show()

    def to_P_2(self):
        self.hide()
        self.p2.ui.show()

    def to_J(self):
        self.hide()
        self.j.ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = MENU()
    menu.ui.show()
    app.exec()
