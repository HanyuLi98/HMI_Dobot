
# import sys
# import threading
# import time
# import numpy as np
# from PyQt6 import uic
# from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from PyQt6.QtGui import QPixmap, QPalette, QBrush
# from PyQt6.QtCore import QTimer, pyqtSlot
# from dobot_api import DobotApiDashboard, DobotApiFeedBack, MyType

# class MyHMI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("testHMI.ui", self)  # 加载 UI 文件
#         self.showMaximized()
        
#         # 设置背景图片
#         palette = self.palette()
#         pixmap = QPixmap(r"C:\Users\ciren\Desktop\二次开发\TCP-IP-Python-V4_HMI\HMI\backgroundikun.png")  # 绝对路径
#         palette.setBrush(self.backgroundRole(), QBrush(pixmap))
#         self.setPalette(palette)
        
#         # 设置默认 IP 和端口
#         self.get_IP.setText("192.168.5.1")
#         self.get_Dashbord_P.setText("29999")
#         self.get_Feedback_P.setText("30004")
#         #设置默认脚本名称
#         self.scriptNameInput.setText("blockly_HMItest") 
#         self.is_connected = False
#         self.is_enabled = False
#         self.client_dash = None
#         self.client_feed = None
        
#         # 用于存储实时关节数据
#         self.joint_data = [0, 0, 0, 0, 0, 0]
#         # 用于末端储存实时数据
#         self.tool_vector_data = [0, 0, 0, 0, 0, 0] 
        
#         # 绑定按钮点击事件
#         self.connect.clicked.connect(self.connect_or_disconnect)
#         self.Enable.clicked.connect(self.enable_or_disable_robot)
        
#         # 创建定时器，用于在主线程中更新UI（避免多线程更新UI的问题）
#         self.update_timer = QTimer(self)
#         self.update_timer.timeout.connect(self.update_joint_ui)
        
#         # 反馈数据线程
#         self.feedback_thread = None
#         self.is_feedback_running = False
        
#         #脚本启动暂停
#         self.runScriptBtn.clicked.connect(self.run_script)
#         self.stopBtn.clicked.connect(self.stop_script)
#         self.pauseBtn.clicked.connect(self.pause_script)
#         self.continueBtn.clicked.connect(self.continue_script)
        
        
#         #Jog点动
#         for joint_num in range(1, 7):  # Joints 1-6
#             getattr(self, f"J{joint_num}P").clicked.connect(lambda checked, jn=joint_num: self.adjust_joint(jn, 5.0))
#             getattr(self, f"J{joint_num}N").clicked.connect(lambda checked, jn=joint_num: self.adjust_joint(jn, -5.0))
#         #工具坐标系点动
#         for axis, letter in enumerate(['X', 'Y', 'Z', 'Rx', 'Ry', 'Rz']):
#             getattr(self, f"{letter}P").clicked.connect(lambda checked, ax=axis: self.adjust_cartesian(ax, 10.0 if ax < 3 else 5.0))
#             getattr(self, f"{letter}N").clicked.connect(lambda checked, ax=axis: self.adjust_cartesian(ax, -10.0 if ax < 3 else -5.0))
#         # Move相关
        
#         # MovJ
#         self.Move_J_btm.clicked.connect(self.movj)    
            
#     def connect_or_disconnect(self):
#         """连接/断开 Dobot 机械臂"""
#         if self.is_connected:
#             # 停止反馈数据线程
#             self.is_feedback_running = False
#             if self.feedback_thread and self.feedback_thread.is_alive():
#                 self.feedback_thread.join(timeout=1.0)  # 等待线程结束，最多等待1秒
            
#             # 停止UI更新定时器
#             self.update_timer.stop()
            
#             # 断开连接
#             print("断开成功")
#             if self.client_dash:
#                 self.client_dash.close()
#             if self.client_feed:
#                 self.client_feed.close()
            
#             self.client_dash = None
#             self.client_feed = None
#             self.conncet.setText("Connect")  # 按钮文字改回 "Connect"
#             self.Enable.setEnabled(False)  # 禁用 Enable 按钮
                                         
#         else:
#             try:
#                 # 获取 UI 输入框的值
#                 ip_address = self.get_IP.text()
#                 dashboard_port = int(self.get_Dashbord_P.text())
#                 feedback_port = int(self.get_Feedback_P.text())
                
#                 print(f"尝试连接到 Dobot：IP={ip_address}, Dashboard Port={dashboard_port}, Feedback Port={feedback_port}")

#                 # 连接到 Dobot
#                 self.client_dash = DobotApiDashboard(ip_address, dashboard_port)
#                 self.client_feed = DobotApiFeedBack(ip_address, feedback_port)
                
#                 print("连接成功！")
#                 self.connect.setText("Disconnect")  # 按钮文字改为 "Disconnect"
#                 self.Enable.setEnabled(True)  # 启用 Enable 按钮
                
#                 # 启动反馈数据线程
#                 self.is_feedback_running = True
#                 self.feedback_thread = threading.Thread(target=self.get_feedback_data)
#                 self.feedback_thread.daemon = True  # 设置为守护线程，随主线程退出
#                 self.feedback_thread.start()
                
#                 # 启动UI更新定时器，每100毫秒更新一次UI
#                 self.update_timer.start(100)
                
#             except Exception as e:
#                 QMessageBox.critical(self, "Attention!", f"Connection Error: {e}")
#                 return  # 连接失败，直接返回
        
#         # 反转连接状态
#         self.is_connected = not self.is_connected
    
#     def enable_or_disable_robot(self):
#         """启用/禁用机器人"""
#         if not self.is_connected:
#             QMessageBox.warning(self, "Warning", "请先连接到机器人！")
#             return
        
#         if self.is_enabled:
#             try:
#                 self.client_dash.DisableRobot()
#                 print("机器人已禁用")
#                 self.Enable.setText("Enable")  # 按钮显示 "Enable"
#             except Exception as e:
#                 QMessageBox.critical(self, "Error", f"Disable Error: {e}")
#                 return
#         else:
#             try:
#                 self.client_dash.EnableRobot()
#                 print("机器人已启用")
#                 self.Enable.setText("Disable")  # 按钮显示 "Disable"
#             except Exception as e:
#                 QMessageBox.critical(self, "Error", f"Enable Error: {e}")
#                 return
        
#         # 反转机器人状态
#         self.is_enabled = not self.is_enabled
    
#     def get_feedback_data(self):
#         """
#         持续获取机器人反馈数据的线程函数
#         在单独的线程中运行，避免阻塞主线程
#         """
#         print("反馈数据线程已启动")
        
#         while self.is_feedback_running:
#             try:
#                 # 设置为阻塞模式
#                 self.client_feed.socket_dobot.setblocking(True)
                
#                 # 接收数据
#                 data = bytes()
#                 temp = self.client_feed.socket_dobot.recv(144000)
#                 if len(temp) > 1440:
#                     temp = self.client_feed.socket_dobot.recv(144000)
#                 data = temp[0:1440]
                
#                 # 解析数据
#                 a = np.frombuffer(data, dtype=MyType)
#                 print(a)
#                 print(type(a))
#                 # 检查数据的有效性
#                 if hex((a['TestValue'][0])) == '0x123456789abcdef':
                    
#                     # 更新关节数据，这里保存到类变量中，避免多线程直接操作UI
#                     self.joint_data = a["QActual"][0]
#                     # 更新工具向量数据 (XYZ和RPY)
#                     self.tool_vector_data = a["ToolVectorActual"][0]
                    
#                     # digital
#                     # self.label_di_input["text"] = bin(a["DigitalInputs"][0])[
#                     # 2:].rjust(64, '0')
#                     # self.label_di_output["text"] = bin(a["DigitalOutputs"][0])[
#                     # 2:].rjust(64, '0')
                    
#             except Exception as e:
#                 print(f"获取反馈数据出错: {e}")
#                 time.sleep(0.5)  # 出错时等待一段时间再重试
#                 continue
            
#             # 控制循环速率，避免过度消耗CPU
#             time.sleep(0.05)
        
#         print("反馈数据线程已结束")
    
#     @pyqtSlot()
#     def update_joint_ui(self):
#         """
#         更新界面上关节角度显示
#         这个函数在主线程的定时器中运行，避免多线程更新UI的问题
#         """
#         try:
#             # 将获取到的关节角度数据显示到UI上
#             self.get_J1.setText(f"{self.joint_data[0]:.4f}")
#             self.get_J2.setText(f"{self.joint_data[1]:.4f}")
#             self.get_J3.setText(f"{self.joint_data[2]:.4f}")
#             self.get_J4.setText(f"{self.joint_data[3]:.4f}")
#             self.get_J5.setText(f"{self.joint_data[4]:.4f}")
#             self.get_J6.setText(f"{self.joint_data[5]:.4f}") 
            
            
#             self.get_X.setText(f"{self.tool_vector_data[0]:.4f}")
#             self.get_Y.setText(f"{self.tool_vector_data[1]:.4f}")
#             self.get_Z.setText(f"{self.tool_vector_data[2]:.4f}")
#             self.get_Rx.setText(f"{self.tool_vector_data[3]:.4f}")
#             self.get_Ry.setText(f"{self.tool_vector_data[4]:.4f}")
#             self.get_Rz.setText(f"{self.tool_vector_data[5]:.4f}")
#         except Exception as e:
#             print(f"更新UI出错: {e}")
    
#     def joint_movj(self):
#         """执行关节运动命令"""
#         try:
#             # 从输入框获取关节角度值
#             j1 = float(self.get_J1.text())
#             j2 = float(self.get_J2.text())
#             j3 = float(self.get_J3.text())
#             j4 = float(self.get_J4.text())
#             j5 = float(self.get_J5.text())
#             j6 = float(self.get_J6.text())
            
#             # 发送关节运动命令
#             self.client_dash.MovJ(j1, j2, j3, j4, j5, j6, 1)
#             print(f"执行关节运动: J1={j1}, J2={j2}, J3={j3}, J4={j4}, J5={j5}, J6={j6}")
#         except ValueError as e:
#             QMessageBox.warning(self, "输入错误", "请确保所有关节角度都是有效的数字")
#         except Exception as e:
#             QMessageBox.critical(self, "运动错误", f"执行关节运动时出错: {e}")
    
    
#     def cart_movl(self):
#         """执行笛卡尔直线运动命令"""
#         try:
#             # 从输入框获取笛卡尔坐标值
#             x = float(self.get_X.text())
#             y = float(self.get_Y.text())
#             z = float(self.get_Z.text())
#             rx = float(self.get_Rx.text())
#             ry = float(self.get_Ry.text())
#             rz = float(self.get_Rz.text())
            
#             # 发送笛卡尔直线运动命令
#             self.client_dash.MovL(x, y, z, rx, ry, rz, 0)
#             print(f"执行笛卡尔运动: X={x}, Y={y}, Z={z}, Rx={rx}, Ry={ry}, Rz={rz}")
#         except ValueError as e:
#             QMessageBox.warning(self, "输入错误", "请确保所有坐标值都是有效的数字")
#         except Exception as e:
#             QMessageBox.critical(self, "运动错误", f"执行笛卡尔运动时出错: {e}")
    
#     def adjust_joint(self, joint_num, delta):
#         """
#         Adjust a specific joint by delta degrees
        
#         Parameters:
#         joint_num (int): Joint number (1-6)
#         delta (float): Amount to change the joint angle
#         """
#         if not self.is_connected or not self.is_enabled:
#             QMessageBox.warning(self, "Warning", "请确保机器人已连接并启用!")
#             return
        
#         try:
#             # Get current joint values
#             joint_values = [0] * 6
#             for i in range(1, 7):
#                 # The 6th joint might have a different UI name based on your existing code
#                 ui_element = self.get_J6_2 if i == 6 and hasattr(self, "get_J6_2") else getattr(self, f"get_J{i}")
#                 joint_values[i-1] = float(ui_element.text())
            
#             # Apply the delta to the specified joint
#             joint_values[joint_num-1] += delta
            
#             # Send movement command
#             self.client_dash.MovJ(*joint_values, 1)
#             print(f"调整 J{joint_num} 旋转角度 {'+' if delta > 0 else ''}{delta}° 到 {joint_values[joint_num-1]}°")
        
#         except ValueError as e:
#             QMessageBox.warning(self, "输入错误", "获取当前关节角度失败")
#         except Exception as e:
#             QMessageBox.critical(self, "运动错误", f"执行关节运动时出错: {e}")
            
            
            
#     def adjust_cartesian(self, axis_num, delta):
#         """
#         Adjust a specific cartesian coordinate by delta
        
#         Parameters:
#         axis_num (int): Axis number (0-5 for X,Y,Z,Rx,Ry,Rz)
#         delta (float): Amount to change the coordinate
#         """
#         if not self.is_connected or not self.is_enabled:
#             QMessageBox.warning(self, "Warning", "请确保机器人已连接并启用!")
#             return
        
#         try:
#             # Get current cartesian values
#             cart_values = [0] * 6
#             axes_names = ["X", "Y", "Z", "Rx", "Ry", "Rz"]
#             for i, name in enumerate(axes_names):
#                 cart_values[i] = float(getattr(self, f"get_{name}").text())
            
#             # Apply the delta to the specified axis
#             cart_values[axis_num] += delta
            
#             # Send movement command in cartesian space (coordtype=0)
#             self.client_dash.MovL(*cart_values, 0)
#             print(f"调整 {axes_names[axis_num]} 值 {'+' if delta > 0 else ''}{delta} 到 {cart_values[axis_num]}")
        
#         except ValueError as e:
#             QMessageBox.warning(self, "输入错误", "获取当前坐标值失败")
#         except Exception as e:
#             QMessageBox.critical(self, "运动错误", f"执行笛卡尔运动时出错: {e}")
            
     
     
#     #用户定义Move
    
#     def movj(self):
#         """执行关节运动命令，使用自定义速度和加速度"""
#         if not self.is_connected or not self.is_enabled:
#             QMessageBox.warning(self, "Warning", "请确保机器人已连接并启用!")
#             return
            
#         try:
#             # 从输入框获取关节角度值
#             j1 = float(self.get_M_J1.text())
#             j2 = float(self.get_M_J2.text())
#             j3 = float(self.get_M_J3.text())
#             j4 = float(self.get_M_J4.text())
#             j5 = float(self.get_M_J5.text())
#             j6 = float(self.get_M_J6.text())
            
#             # 获取速度和加速度比例
#             velocity = int(float(self.get_M_Vel_Rate.text()))
#             acceleration = int(float(self.get_Acc_Rate.text()))
            
#             # 检查速度和加速度是否在有效范围内
#             if not (0 < velocity <= 100):
#                 QMessageBox.warning(self, "参数错误", "速度比例必须在(0,100]范围内")
#                 return
                
#             if not (0 < acceleration <= 100):
#                 QMessageBox.warning(self, "参数错误", "加速度比例必须在(0,100]范围内")
#                 return
            
#             # 发送关节运动命令，coordinateMode=1表示关节坐标模式
#             response = self.client_dash.MovJ(j1, j2, j3, j4, j5, j6, 1, a=acceleration, v=velocity)
#             print(f"执行关节运动: J1={j1}, J2={j2}, J3={j3}, J4={j4}, J5={j5}, J6={j6}, 速度={velocity}%, 加速度={acceleration}%")
#             print(f"响应: {response}")
            
#         except ValueError as e:
#             QMessageBox.warning(self, "输入错误", "请确保所有关节角度、速度和加速度都是有效的数字")
#         except Exception as e:
#             QMessageBox.critical(self, "运动错误", f"执行关节运动时出错: {e}")       
            
#     #脚本相关
    
#     def run_script(self):
#         """执行运行脚本命令"""
#         try:
#             project_name = self.scriptNameInput.text()  # 获取文本框输入的脚本名
#             if project_name.strip() == "":
#                 QMessageBox.warning(self, "输入错误", "脚本名称不能为空")
#                 return

#             response = self.client_dash.RunScript(project_name)  # 调用接口
#             print(f"运行脚本 {project_name}: {response}")
#         except Exception as e:
#             QMessageBox.critical(self, "错误", f"运行脚本时出错: {e}")
            
#     def stop_script(self):
#         """停止正在执行的运动或脚本"""
#         try:
#             response = self.client_dash.Stop()
#             print(f"停止脚本或运动: {response}")
#         except Exception as e:
#             QMessageBox.critical(self, "错误", f"停止脚本时出错: {e}")

#     def pause_script(self):
#         """暂停正在执行的运动或脚本"""
#         try:
#             response = self.client_dash.Pause()
#             print(f"暂停脚本或运动: {response}")
#         except Exception as e:
#             QMessageBox.critical(self, "错误", f"暂停脚本时出错: {e}")

#     def continue_script(self):
#         """继续暂停的脚本或运动"""
#         try:
#             response = self.client_dash.Continue()
#             print(f"继续脚本或运动: {response}")
#         except Exception as e:
#             QMessageBox.critical(self, "错误", f"继续脚本时出错: {e}")
            
            
                    
#     def closeEvent(self, event):
#         """
#         窗口关闭事件处理
#         确保在关闭窗口时正确清理资源
#         """
#         # 停止反馈线程
#         self.is_feedback_running = False
#         if self.feedback_thread and self.feedback_thread.is_alive():
#             self.feedback_thread.join(timeout=1.0)
        
#         # 停止更新定时器
#         self.update_timer.stop()
        
#         # 断开连接
#         if self.client_dash:
#             self.client_dash.close()
#         if self.client_feed:
#             self.client_feed.close()
        
#         # 接受关闭事件
#         event.accept()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyHMI()
#     window.show()
#     sys.exit(app.exec()
# 
# 
# 
# )

import sys
import threading
import time
import numpy as np
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap, QPalette, QBrush
from PyQt6.QtCore import QTimer, pyqtSlot
from dobot_api import DobotApiDashboard, DobotApiFeedBack, MyType

class MyHMI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("testHMI.ui", self)  # 加载 UI 文件
        self.showMaximized()
        
        # 设置背景图片
        palette = self.palette()
        pixmap = QPixmap(r"C:\Users\ciren\Desktop\二次开发\TCP-IP-Python-V4_HMI\HMI\backgroundikun.png")  # 绝对路径
        palette.setBrush(self.backgroundRole(), QBrush(pixmap))
        self.setPalette(palette)
        
        # 设置默认 IP 和端口
        self.get_IP.setText("192.168.5.1")
        self.get_Dashbord_P.setText("29999")
        self.get_Feedback_P.setText("30004")
        #设置默认脚本名称
        self.scriptNameInput.setText("blockly_HMItest") 
        self.is_connected = False
        self.is_enabled = False
        self.client_dash = None
        self.client_feed = None
        
        # 用于存储实时关节数据
        self.joint_data = [0, 0, 0, 0, 0, 0]
        # 用于末端储存实时数据
        self.tool_vector_data = [0, 0, 0, 0, 0, 0] 
        
        # 绑定按钮点击事件
        self._init_button_connections()
        
        # 创建定时器，用于在主线程中更新UI（避免多线程更新UI的问题）
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_joint_ui)
        
        # 反馈数据线程
        self.feedback_thread = None
        self.is_feedback_running = False
        
    def _init_button_connections(self):
        """初始化所有按钮连接"""
        # 连接和使能按钮
        self.connect.clicked.connect(self.connect_or_disconnect)
        self.Enable.clicked.connect(self.enable_or_disable_robot)
        
        # 运动控制按钮
        self.Move_J_btm.clicked.connect(self.movj)
        # 添加新按钮连接
        self.Move_J_C_btm.clicked.connect(self.cart_movj)
        self.Move_L_C_btm.clicked.connect(self.cart_movl)
        
        # Jog点动 - 关节坐标系
        for joint_num in range(1, 7):  # Joints 1-6
            getattr(self, f"J{joint_num}P").clicked.connect(lambda checked, jn=joint_num: self.adjust_joint(jn, 5.0))
            getattr(self, f"J{joint_num}N").clicked.connect(lambda checked, jn=joint_num: self.adjust_joint(jn, -5.0))
        
        # Jog点动 - 工具坐标系
        for axis, letter in enumerate(['X', 'Y', 'Z', 'Rx', 'Ry', 'Rz']):
            getattr(self, f"{letter}P").clicked.connect(lambda checked, ax=axis: self.adjust_cartesian(ax, 10.0 if ax < 3 else 5.0))
            getattr(self, f"{letter}N").clicked.connect(lambda checked, ax=axis: self.adjust_cartesian(ax, -10.0 if ax < 3 else -5.0))
            
        # 脚本控制按钮
        self.runScriptBtn.clicked.connect(self.run_script)
        self.stopBtn.clicked.connect(self.stop_script)
        self.pauseBtn.clicked.connect(self.pause_script)
        self.continueBtn.clicked.connect(self.continue_script)
        
    #--- 连接与状态相关函数 ---#
    
    def connect_or_disconnect(self):
        """连接/断开 Dobot 机械臂"""
        if self.is_connected:
            # 停止反馈数据线程
            self.is_feedback_running = False
            if self.feedback_thread and self.feedback_thread.is_alive():
                self.feedback_thread.join(timeout=1.0)  # 等待线程结束，最多等待1秒
            
            # 停止UI更新定时器
            self.update_timer.stop()
            
            # 断开连接
            print("断开成功")
            if self.client_dash:
                self.client_dash.close()
            if self.client_feed:
                self.client_feed.close()
            
            self.client_dash = None
            self.client_feed = None
            self.connect.setText("Connect")  # 按钮文字改回 "Connect"
            self.Enable.setEnabled(False)  # 禁用 Enable 按钮
                                         
        else:
            try:
                # 获取 UI 输入框的值
                ip_address = self.get_IP.text()
                dashboard_port = int(self.get_Dashbord_P.text())
                feedback_port = int(self.get_Feedback_P.text())
                
                print(f"尝试连接到 Dobot：IP={ip_address}, Dashboard Port={dashboard_port}, Feedback Port={feedback_port}")

                # 连接到 Dobot
                self.client_dash = DobotApiDashboard(ip_address, dashboard_port)
                self.client_feed = DobotApiFeedBack(ip_address, feedback_port)
                
                print("连接成功！")
                self.connect.setText("Disconnect")  # 按钮文字改为 "Disconnect"
                self.Enable.setEnabled(True)  # 启用 Enable 按钮
                
                # 启动反馈数据线程
                self.is_feedback_running = True
                self.feedback_thread = threading.Thread(target=self.get_feedback_data)
                self.feedback_thread.daemon = True  # 设置为守护线程，随主线程退出
                self.feedback_thread.start()
                
                # 启动UI更新定时器，每100毫秒更新一次UI
                self.update_timer.start(100)
                
            except Exception as e:
                QMessageBox.critical(self, "Attention!", f"Connection Error: {e}")
                return  # 连接失败，直接返回
        
        # 反转连接状态
        self.is_connected = not self.is_connected
    
    def enable_or_disable_robot(self):
        """启用/禁用机器人"""
        if not self.is_connected:
            QMessageBox.warning(self, "Warning", "请先连接到机器人！")
            return
        
        if self.is_enabled:
            try:
                self.client_dash.DisableRobot()
                print("机器人已禁用")
                self.Enable.setText("Enable")  # 按钮显示 "Enable"
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Disable Error: {e}")
                return
        else:
            try:
                self.client_dash.EnableRobot()
                print("机器人已启用")
                self.Enable.setText("Disable")  # 按钮显示 "Disable"
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Enable Error: {e}")
                return
        
        # 反转机器人状态
        self.is_enabled = not self.is_enabled
    
    def get_feedback_data(self):
        """
        持续获取机器人反馈数据的线程函数
        在单独的线程中运行，避免阻塞主线程
        """
        print("反馈数据线程已启动")
        
        while self.is_feedback_running:
            try:
                # 设置为阻塞模式
                self.client_feed.socket_dobot.setblocking(True)
                
                # 接收数据
                data = bytes()
                temp = self.client_feed.socket_dobot.recv(144000)
                if len(temp) > 1440:
                    temp = self.client_feed.socket_dobot.recv(144000)
                data = temp[0:1440]
                
                # 解析数据
                a = np.frombuffer(data, dtype=MyType)
                
                # 检查数据的有效性
                if hex((a['TestValue'][0])) == '0x123456789abcdef':
                    
                    # 更新关节数据，这里保存到类变量中，避免多线程直接操作UI
                    self.joint_data = a["QActual"][0]
                    # 更新工具向量数据 (XYZ和RPY)
                    self.tool_vector_data = a["ToolVectorActual"][0]
                    
            except Exception as e:
                print(f"获取反馈数据出错: {e}")
                time.sleep(0.5)  # 出错时等待一段时间再重试
                continue
            
            # 控制循环速率，避免过度消耗CPU
            time.sleep(0.05)
        
        print("反馈数据线程已结束")
    
    @pyqtSlot()
    def update_joint_ui(self):
        """
        更新界面上关节角度显示
        这个函数在主线程的定时器中运行，避免多线程更新UI的问题
        """
        try:
            # 将获取到的关节角度数据显示到UI上
            self.get_J1.setText(f"{self.joint_data[0]:.4f}")
            self.get_J2.setText(f"{self.joint_data[1]:.4f}")
            self.get_J3.setText(f"{self.joint_data[2]:.4f}")
            self.get_J4.setText(f"{self.joint_data[3]:.4f}")
            self.get_J5.setText(f"{self.joint_data[4]:.4f}")
            self.get_J6.setText(f"{self.joint_data[5]:.4f}") 
            
            # 更新笛卡尔坐标
            self.get_X.setText(f"{self.tool_vector_data[0]:.4f}")
            self.get_Y.setText(f"{self.tool_vector_data[1]:.4f}")
            self.get_Z.setText(f"{self.tool_vector_data[2]:.4f}")
            self.get_Rx.setText(f"{self.tool_vector_data[3]:.4f}")
            self.get_Ry.setText(f"{self.tool_vector_data[4]:.4f}")
            self.get_Rz.setText(f"{self.tool_vector_data[5]:.4f}")
        except Exception as e:
            print(f"更新UI出错: {e}")
            
    #--- 运动控制相关函数 ---#
    
    def _check_robot_status(self):
        """检查机器人连接和使能状态"""
        if not self.is_connected or not self.is_enabled:
            QMessageBox.warning(self, "Warning", "请确保机器人已连接并启用!")
            return False
        return True
    
    def _get_motion_params(self):
        """获取速度和加速度参数"""
        try:
            velocity = int(float(self.get_M_Vel_Rate.text()))
            acceleration = int(float(self.get_Acc_Rate.text()))
            
            # 检查参数范围
            if not (0 < velocity <= 100):
                QMessageBox.warning(self, "参数错误", "速度比例必须在(0,100]范围内")
                return None, None
                
            if not (0 < acceleration <= 100):
                QMessageBox.warning(self, "参数错误", "加速度比例必须在(0,100]范围内")
                return None, None
                
            return velocity, acceleration
        except ValueError:
            QMessageBox.warning(self, "输入错误", "速度或加速度不是有效的数字")
            return None, None
    
    def movj(self):
        """执行关节运动命令，使用自定义速度和加速度"""
        if not self._check_robot_status():
            return
            
        try:
            # 从输入框获取关节角度值
            j1 = float(self.get_M_J1.text())
            j2 = float(self.get_M_J2.text())
            j3 = float(self.get_M_J3.text())
            j4 = float(self.get_M_J4.text())
            j5 = float(self.get_M_J5.text())
            j6 = float(self.get_M_J6.text())
            
            # 获取速度和加速度比例
            velocity, acceleration = self._get_motion_params()
            if velocity is None:  # 如果返回None说明验证失败
                return
            
            # 发送关节运动命令，coordinateMode=1表示关节坐标模式
            response = self.client_dash.MovJ(j1, j2, j3, j4, j5, j6, 1, a=acceleration, v=velocity)
            print(f"执行关节运动: J1={j1}, J2={j2}, J3={j3}, J4={j4}, J5={j5}, J6={j6}, 速度={velocity}%, 加速度={acceleration}%")
            print(f"响应: {response}")
            
        except ValueError as e:
            QMessageBox.warning(self, "输入错误", "请确保所有关节角度都是有效的数字")
        except Exception as e:
            QMessageBox.critical(self, "运动错误", f"执行关节运动时出错: {e}")
    
    def cart_movj(self):
        """执行笛卡尔坐标系下的关节运动命令"""
        if not self._check_robot_status():
            return
            
        try:
            # 从输入框获取笛卡尔坐标值
            x = float(self.get_M_X.text())
            y = float(self.get_M_Y.text())
            z = float(self.get_M_Z.text())
            rx = float(self.get_M_Rx.text())
            ry = float(self.get_M_Ry.text())
            rz = float(self.get_M_Rz.text())
            
            # 获取速度和加速度比例
            velocity, acceleration = self._get_motion_params()
            if velocity is None:  # 如果返回None说明验证失败
                return
            
            # 发送笛卡尔关节运动命令，coordinateMode=0表示笛卡尔坐标模式
            response = self.client_dash.MovJ(x, y, z, rx, ry, rz, 0, a=acceleration, v=velocity)
            print(f"执行笛卡尔关节运动: X={x}, Y={y}, Z={z}, Rx={rx}, Ry={ry}, Rz={rz}, 速度={velocity}%, 加速度={acceleration}%")
            print(f"响应: {response}")
            
        except ValueError as e:
            QMessageBox.warning(self, "输入错误", "请确保所有坐标值都是有效的数字")
        except Exception as e:
            QMessageBox.critical(self, "运动错误", f"执行笛卡尔关节运动时出错: {e}")
    
    def cart_movl(self):
        """执行笛卡尔直线运动命令"""
        if not self._check_robot_status():
            return
            
        try:
            # 从输入框获取笛卡尔坐标值
            x = float(self.get_M_X.text())
            y = float(self.get_M_Y.text())
            z = float(self.get_M_Z.text())
            rx = float(self.get_M_Rx.text())
            ry = float(self.get_M_Ry.text())
            rz = float(self.get_M_Rz.text())
            
            # 获取速度和加速度比例
            velocity, acceleration = self._get_motion_params()
            if velocity is None:  # 如果返回None说明验证失败
                return
            
            # 发送笛卡尔直线运动命令，coordinateMode=0表示笛卡尔坐标模式
            response = self.client_dash.MovL(x, y, z, rx, ry, rz, 0, a=acceleration, v=velocity)
            print(f"执行笛卡尔直线运动: X={x}, Y={y}, Z={z}, Rx={rx}, Ry={ry}, Rz={rz}, 速度={velocity}%, 加速度={acceleration}%")
            print(f"响应: {response}")
            
        except ValueError as e:
            QMessageBox.warning(self, "输入错误", "请确保所有坐标值都是有效的数字")
        except Exception as e:
            QMessageBox.critical(self, "运动错误", f"执行笛卡尔直线运动时出错: {e}")
    
    def adjust_joint(self, joint_num, delta):
        """
        调整特定关节角度
        
        Parameters:
        joint_num (int): 关节编号 (1-6)
        delta (float): 角度变化量
        """
        if not self._check_robot_status():
            return
        
        try:
            # 获取当前关节值
            joint_values = [0] * 6
            for i in range(1, 7):
                ui_element = getattr(self, f"get_J{i}")
                joint_values[i-1] = float(ui_element.text())
            
            # 修改指定关节的角度
            joint_values[joint_num-1] += delta
            
            # 发送运动命令
            self.client_dash.MovJ(*joint_values, 1)
            print(f"调整 J{joint_num} 旋转角度 {'+' if delta > 0 else ''}{delta}° 到 {joint_values[joint_num-1]}°")
        
        except ValueError as e:
            QMessageBox.warning(self, "输入错误", "获取当前关节角度失败")
        except Exception as e:
            QMessageBox.critical(self, "运动错误", f"执行关节运动时出错: {e}")
            
    def adjust_cartesian(self, axis_num, delta):
        """
        调整特定笛卡尔坐标
        
        Parameters:
        axis_num (int): 轴编号 (0-5 对应 X,Y,Z,Rx,Ry,Rz)
        delta (float): 坐标变化量
        """
        if not self._check_robot_status():
            return
        
        try:
            # 获取当前笛卡尔坐标值
            cart_values = [0] * 6
            axes_names = ["X", "Y", "Z", "Rx", "Ry", "Rz"]
            for i, name in enumerate(axes_names):
                cart_values[i] = float(getattr(self, f"get_{name}").text())
            
            # 修改指定轴的坐标
            cart_values[axis_num] += delta
            
            # 发送运动命令 (coordinateMode=0 表示笛卡尔坐标模式)
            self.client_dash.MovL(*cart_values, 0)
            print(f"调整 {axes_names[axis_num]} 值 {'+' if delta > 0 else ''}{delta} 到 {cart_values[axis_num]}")
        
        except ValueError as e:
            QMessageBox.warning(self, "输入错误", "获取当前坐标值失败")
        except Exception as e:
            QMessageBox.critical(self, "运动错误", f"执行笛卡尔运动时出错: {e}")
            
    #--- 脚本控制相关函数 ---#
    
    def run_script(self):
        """执行运行脚本命令"""
        if not self._check_robot_status():
            return
            
        try:
            project_name = self.scriptNameInput.text()  # 获取文本框输入的脚本名
            if project_name.strip() == "":
                QMessageBox.warning(self, "输入错误", "脚本名称不能为空")
                return

            response = self.client_dash.RunScript(project_name)  # 调用接口
            print(f"运行脚本 {project_name}: {response}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"运行脚本时出错: {e}")
            
    def stop_script(self):
        """停止正在执行的运动或脚本"""
        if not self.is_connected:
            QMessageBox.warning(self, "Warning", "请先连接到机器人！")
            return
            
        try:
            response = self.client_dash.Stop()
            print(f"停止脚本或运动: {response}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"停止脚本时出错: {e}")

    def pause_script(self):
        """暂停正在执行的运动或脚本"""
        if not self.is_connected:
            QMessageBox.warning(self, "Warning", "请先连接到机器人！")
            return
            
        try:
            response = self.client_dash.Pause()
            print(f"暂停脚本或运动: {response}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"暂停脚本时出错: {e}")

    def continue_script(self):
        """继续暂停的脚本或运动"""
        if not self.is_connected:
            QMessageBox.warning(self, "Warning", "请先连接到机器人！")
            return
            
        try:
            response = self.client_dash.Continue()
            print(f"继续脚本或运动: {response}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"继续脚本时出错: {e}")
            
    def closeEvent(self, event):
        """
        窗口关闭事件处理
        确保在关闭窗口时正确清理资源
        """
        # 停止反馈线程
        self.is_feedback_running = False
        if self.feedback_thread and self.feedback_thread.is_alive():
            self.feedback_thread.join(timeout=1.0)
        
        # 停止更新定时器
        self.update_timer.stop()
        
        # 断开连接
        if self.client_dash:
            self.client_dash.close()
        if self.client_feed:
            self.client_feed.close()
        
        # 接受关闭事件
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyHMI()
    window.show()
    sys.exit(app.exec())