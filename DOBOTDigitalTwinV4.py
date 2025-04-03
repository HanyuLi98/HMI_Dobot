from robolink import *    # RoboDK API
from robodk import *    # Robot toolbox
RDK = Robolink()
from dobot_apiV4 import *
import time
import tkinter as tk
import threading
import re
import numpy as np


current_actual = None
threadLock = False 

class DOBOTandRDK(object):
    enableRobot_Count = False
    def __init__(self,robottype):
        self.dobot29999 = None
        self.dobot30004 = None
        self.robotVisual = RDK.Item(f"DOBOT {robottype}(Visual)")
        self.robot = RDK.Item(f"DOBOT {robottype}")
        self.threadLock = threadLock
        self.thread = None
        self.diList = None
        self.doList = None
        self.RDKReset()


    def join(self,ip):
        self.dobot29999 = DobotApiDashboard(ip, 29999)
        self.dobot30004 = DobotApiFeedBack(ip,30004)
        self.dobot30004.socket_dobot.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1440)
        self.thread = threading.Thread(target=self.get_feed)
        self.thread.start()
        self.threadLock = True
        

    def quit(self):
        self.dobot30004.socket_dobot.close()
        self.dobot29999.socket_dobot.close()
        self.threadLock = False
        self.thread.join()


    def setDobotAngle(self):
        if not DOBOTandRDK.enableRobot_Count:
            self.dobot29999.EnableRobot()
            DOBOTandRDK.enableRobot_Count = True
        rdkAngle = self.getRDKAngle()
        if len(rdkAngle[0]) == 6:
            self.dobot29999.MovJ(rdkAngle[0][0],rdkAngle[0][1],rdkAngle[0][2],rdkAngle[0][3],rdkAngle[0][4],rdkAngle[0][5],1)
        else:
            print("数据错误...")
            return

    def getRDKAngle(self):
        return list(self.robot.Joints())
        
    def get_feed(self):
        global current_actual
        hasRead = 0
        while True:
            data = bytes()
            while hasRead < 1440:
                temp = self.dobot30004.socket_dobot.recv(1440 - hasRead)
                if len(temp) > 0:
                    hasRead += len(temp)
                    data += temp
            hasRead = 0
            a = np.frombuffer(data, dtype=MyType)
            if hex((a['test_value'][0])) == '0x123456789abcdef':
                current_actual = a["q_actual"][0]
                self.doList =  list(bin(a["digital_output_bits"][0])[2:].rjust(24, '0'))[::-1]
                self.diList =  list(bin(a["digital_input_bits"][0])[2:].rjust(24, '0'))[::-1]
                self.robotVisual.setJoints([current_actual[0],
                                            current_actual[1],
                                            current_actual[2],
                                            current_actual[3],
                                            current_actual[4],
                                            current_actual[5]
                                            ])
                self.setRobotIO(self.doList, self.diList)
            if self.threadLock == False:
                break
        


    def get_feed_one(self):
        global current_actual
        hasRead = 0
        data = bytes()
        while hasRead < 1440:
            temp = self.dobot30004.socket_dobot.recv(1440 - hasRead)
            if len(temp) > 0:
                hasRead += len(temp)
                data += temp
        hasRead = 0
        a = np.frombuffer(data, dtype=MyType)
        if hex((a['test_value'][0])) == '0x123456789abcdef':
            current_actual = a["q_actual"][0]
            self.robot.setJoints([current_actual[0],
                                        current_actual[1],
                                        current_actual[2],
                                        current_actual[3],
                                        current_actual[4],
                                        current_actual[5]
                                        ])



    def RDKReset(self):
        RDK.Render(False)
        RDK.Item("IO Base").setParentStatic(RDK.Item("DOBOT CR10(Visual) Base"))
        RDK.Item("IO Base").setPose(transl(0,0,0))
        for i in range(1,25):
            RDK.Item(f"DO {i}").setParentStatic(RDK.Item("IO Base"))
            RDK.Item(f"DO {i}").setPose(transl(500,110 * (i - 1),0) * roty(90 * pi / 180))
            RDK.Item(f"DO {i}").setColor([0.699999988079071, 0.699999988079071, 0.699999988079071, 1.0])

            RDK.Item(f"DI {i}").setParentStatic(RDK.Item("IO Base"))
            RDK.Item(f"DI {i}").setPose(transl(500,110 * (i - 1),110) * roty(90 * pi / 180))
            RDK.Item(f"DI {i}").setColor([0.699999988079071, 0.699999988079071, 0.699999988079071, 1.0])
        RDK.Render(True)  # 停止刷新工作站

    def setRobotIO(self,DIstate,DOstate):
        RDK.Render(False)  
        for index,value in enumerate(DIstate):
            if value == "0":
                RDK.Item(f"DI {index + 1}").setColor([0.699999988079071, 0.699999988079071, 0.699999988079071, 1.0])
            elif value == "1":
                RDK.Item(f"DI {index + 1}").setColor([0.0, 1.0, 0.0, 1.0])
        for index,value in enumerate(DOstate):
            if value == "0":
                RDK.Item(f"DO {index + 1}").setColor([0.699999988079071, 0.699999988079071, 0.699999988079071, 1.0])
            elif value == "1":
                RDK.Item(f"DO {index + 1}").setColor([0.0, 1.0, 0.0, 1.0])
        RDK.Render(True)  # 开始刷新工作站


class Gui(DOBOTandRDK):
    def __init__(self,robottype,master):
        DOBOTandRDK.__init__(self,robottype)
        self.connected = False
        self.master = master
        master.title("IP地址:")
        master.attributes('-topmost', 1)
        master.geometry("400x300+%d+%d" % ((master.winfo_screenwidth() - 400) / 2, (master.winfo_screenheight() - 300) / 2))
        
        self.ip_entry = tk.Entry(master,width=15,font=(10))
        self.ip_entry.insert(0, "127.0.0.1")
        self.ip_entry.place(relx=0.1,rely=0.1,width=150,height=50)

        self.connect_button = tk.Button(master, text="Connect", command=self.connect)
        self.connect_button.configure(bg="gray")
        self.connect_button.place(relx=0.6,rely=0.1,width=100,height=50)

        self.sync_button = tk.Button(master, text="同步", command=self.sync, width=8, height=2, font=("黑体", 20))
        self.sync_button.place(relx=0.1,rely=0.4)

        self.send_button = tk.Button(master, text="下发", command=self.send, width=8, height=2, font=("黑体", 20))
        self.send_button.place(relx=0.6,rely=0.4)

    def connect(self):
        ip_address = self.ip_entry.get()
        if self.connected:
            self.quit()  
            self.connect_button.configure(bg="gray")
            self.connect_button.configure(text="Connect")
            self.connected = False
        else:
            self.join(ip_address)
            self.connect_button.configure(bg="green")
            self.connect_button.configure(text="Disconnect")
            self.connected = True

    def sync(self):
        # 进行同步操作
        if self.connected:
            self.get_feed_one()
        else:
            messagebox.showwarning("", "未连接机器人，请先连接...")

    def send(self):
        if self.connected:
            self.setDobotAngle()
        else:
            messagebox.showwarning("", "未连接机器人，请先连接...")

if __name__ == "__main__":
    windows = tk.Tk()
    ui = Gui("CR10",windows)
    windows.mainloop()


# from DOBOTDigitalTwinV4 import *
# windows = tk.Tk()
# ui = Gui("CR10",windows)
# windows.mainloop()

    
