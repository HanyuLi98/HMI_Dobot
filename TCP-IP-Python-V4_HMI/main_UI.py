# from ui import RobotUI

# robot_ui = RobotUI()

# robot_ui.pack()
# robot_ui.mainloop()


import sys
from PyQt6.QtWidgets import QApplication
from HMI import MyHMI  # 从你的 HMI.py 中导入窗口类

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyHMI()
    window.show()
    sys.exit(app.exec())