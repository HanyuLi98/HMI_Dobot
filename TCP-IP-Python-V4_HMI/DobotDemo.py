
from dobot_api import DobotApiFeedBack,DobotApiDashboard
import threading
from time import sleep
import re
import sys
import struct

class DobotDemo:
    def __init__(self, ip):
        self.ip = ip
        self.dashboardPort = 29999
        self.feedPortFour = 30004
        self.dashboard = None
        self.feedInfo = []
        
        class item:
            def __init__(self):
                self.robotMode = 0     #
                self.robotCurrentCommandID = 0
                # 自定义添加所需反馈数据

        self.feedData = item()  # 定义结构对象

    def start(self):
        # 启动机器人并使能
        self.dashboard = DobotApiDashboard(self.ip, self.dashboardPort)
        self.feedFour = DobotApiFeedBack(self.ip, self.feedPortFour)
        if self.parseResultId(self.dashboard.EnableRobot())[0] != 0:
            print("使能失败: 检查29999端口是否被占用")
            return
        print("使能成功")

        # 启动状态反馈线程
        threading.Thread(target=self.GetFeed, daemon=True).start()

        # 定义两个目标点
        point_a = [-208, -15, 56, -44, -90, -85]
        point_b = [-208 + 5, -15, 56, -44, -90, -85]
        # 走点循环
        while True:
            self.RunPoint(point_a)
            self.RunPoint(point_b)
            sleep(3)
            
    # def GetFeed(self):
    # # 获取机器人状态
    #      while True:
    #         feedInfo = self.feedFour.feedBackData() #<class 'numpy.ndarray'> ,(1,)
    #         # self.feedData.robotMode = feedInfo['robot_mode'][0]
    #         print(hex((feedInfo['TestValue'][0])))
    #         if feedInfo is not None:
    #             try:
    #                 if feedInfo.shape == (1,):
    #                     # 获取第一个元素，这应该是包含所有数据的对象
    #                     data = feedInfo[0] #<class 'numpy.void'> 结构化数据类型
    #                     print(type(data))
    #                     # (1440, [0, 0, 0, 0, 0, 0], 544, 0, 7, 1742476422489, 251565, 81985529216486895, [0, 0, 0, 0, 0, 0, 0, 0], 64.0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 48.006316620607976, 1.36, 0.0, 0, 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [247.75296020507812, -15.0, 112.0, -13.0, -90.0, 176.0], [33.53458786010742, 0.0, -3.1805547778818166e-12, 3.975693472352271e-13, 0.0, 0.0], [162.10519409179688, 0.0, -1.5902773542464388e-09, 1.9878466928080485e-10, 0.0, 0.0], [0.7240774631500244, -0.753353476524353, -1.6042869091033936, -0.275678426027298, 0.008396773599088192, 0.002682802500203252], [10.238454818725586, -10.65241813659668, -16.307104110717773, -2.6967711448669434, 0.08213981986045837, 0.02624399960041046], [246.7303466796875, -14.999873161315918, 112.00001525878906, -13.000089645385742, -90.00016021728516, 176.00001525878906], [27.88860321044922, -0.0, 0.0, -0.0678507462143898, -0.0, -0.0], [1.3845, -0.7526, -1.9023, -0.2626, 0.0208, -0.013], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [-7.871181488037109, 311.48931884765625, 279.669921875, 174.03909301757812, 0.27270495891571045, 161.00125122070312], [-151.57362365722656, -3.730659008026123, 0.14967752993106842, 0.062446583062410355, -0.026535214856266975, 27.888427734375], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [-13.429533004760742, 311.2989501953125, 279.6704406738281, 174.03903198242188, 0.27255019545555115, 162.02389526367188], [-182.19984436035156, -7.860157489776611, 1.881288354266264e-11, 2.5809083602917893e-12, -1.0411119666028923e-12, 33.53458786010742], [58.0, 54.0, 66.0, 59.0, 62.0, 64.0], [8.0, 8.0, 8.0, 8.0, 8.0, 8.0], [48.0, 48.0, 48.0, 48.0, 47.0, 47.0], [1, 1, 1, 0], 0, 0, 1, 0, 100, 100, 0, 0, 0, 0, 0, [0, 0], 0, 1, 0, 1, 0, 0, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], -0.019039628243051453, 51, [19.57682991027832, -10.641763687133789, -19.336320877075195, -2.568834066390991, 0.20347200334072113, -0.12716999650001526], 0.19999999999999998, 0.0, 0.0, 0.0, [0.0, 0.0, 0.0, 0.0, -0.0, 0.0], [0.0, 0.0, 0.0, 0.0, -0.0, 0.0], [0, 0, 0, 0, 0, 0, 0, 0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.010469258762896061, 0.15589454770088196, 0.986401379108429, 0.05098607763648033], [0.010925091803073883, 0.1646910309791565, 0.9849709272384644, 0.05088987946510315], 0, 0, 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    #                     if hasattr(data, 'tobytes'):
    #                         byte_data = data.tobytes() #转换为原始二进制字节流
    #                         if len(byte_data) >= 1120:
    #                             self.feedData.robotMode = struct.unpack('<Q', byte_data[24:32])[0] #Q 代表 无符号 64 位整数 (uint64),< 代表 小端字节序（低字节在前）。
    #                             self.feedData.robotCurrentCommandID = struct.unpack('<Q', byte_data[1112:1120])[0]
                                
    #                             # print(f"通过 tobytes 获取 - RobotMode: {self.feedData.robotMode}, CommandID: {self.feedData.robotCurrentCommandID}")
    #             except Exception as e:
    #                 print(f"处理反馈数据时出错: {e}")
    def GetFeed(self):
        # 获取机器人状态
        while True:
            feedInfo = self.feedFour.feedBackData()
            if feedInfo is not None:   
                if hex((feedInfo['TestValue'][0])) == '0x123456789abcdef':
                    print(feedInfo)
                    self.feedData.robotMode = feedInfo['RobotMode'][0]
                    self.feedData.robotCurrentCommandID = feedInfo['CurrentCommandId'][0]
                    print("CurrentCommandId:" )
                    print(feedInfo['CurrentCommandId'][0])
                    # 自主添加所需机械臂反馈的数据
                    '''
                    self.feedData.robotErrorState = feedInfo['error_status'][0]
                    self.feedData.robotEnableStatus = feedInfo['enable_status'][0]
                    self.feedData.robotCurrentCommandID = feedInfo['currentcommandid'][0]
                    '''                    
                    
    def RunPoint(self, point_list):
        # 走点指令
        recvmovemess = self.dashboard.MovJ(*point_list, 1)
        print("MovJ:", recvmovemess)
        print(self.parseResultId(recvmovemess))
        currentCommandID = self.parseResultId(recvmovemess)[1]
        print("指令 ID:", currentCommandID)
        #sleep(0.02)
        while True:  #完成判断循环
            # print("========DEBUG INFORMATION=========")
            # print(self.feedData.robotMode)
            # print(self.feedData.robotCurrentCommandID)
            # print(currentCommandID)
            if self.feedData.robotMode == 5 and self.feedData.robotCurrentCommandID == currentCommandID:
                print("运动结束")
                break
            sleep(0.1)

    def parseResultId(self, valueRecv):
        # 解析返回值，确保机器人在 TCP 控制模式
        if "Not Tcp" in valueRecv:
            print("Control Mode Is Not Tcp")
            return [1]
        return [int(num) for num in re.findall(r'-?\d+', valueRecv)] or [2]

    def __del__(self):
        del self.dashboard
        del self.feedFour