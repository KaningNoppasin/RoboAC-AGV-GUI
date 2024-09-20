import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.buttons = [
            ['Set Up env', self.handleSetUpENV],
            ['RViz', self.handleRViz],
            ['Odometry', self.handleOdometry],
            ['Move to all position', self.handleMoveToAllPosition],
            ['Go to Home', self.handleGoToHome],
            ['New Row', self.handleDuplicateRow],
            ['Delete Row', self.handleDeleteRow],
        ]

        self.dataFromLayout2 = []
        self.buttonLayoutFromLayout2 = []
        self.process = ""
        # Set up the window
        self.setWindowTitle('RoboAC Controller')
        # self.setGeometry(1000, 1000, 300, 200)
        self.center_window()
        self.setStyleSheet("background-color: #f0f4f7;")

        # Create a label to display the event message
        self.label = QLabel('Click the button!', self)
        self.label.setStyleSheet("""
            QLabel {
                font-family: 'Tahoma';         /* Custom font */
                color: #333;                  /* Dark gray text */
                font-size: 16px;              /* Text size */
                padding: 10px 20px;           /* Padding inside the label */
                background-color: #ffffff;    /* White background */
                border: 1px solid #ccc;       /* Light gray border */
                border-radius: 5px;           /* Slightly rounded corners */
            }
        """)
        self.label.setAlignment(Qt.AlignCenter)

        # Set up the layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.createButton()
        self.addToWidget()

    def center_window(self):
        # Get the screen geometry
        screen = QApplication.primaryScreen()
        screen_size = screen.size()

        screen_width = screen_size.width()
        screen_height = screen_size.height()

        window_width = int(screen_width * 0.5)
        window_height = int(window_width * 9 / 16)

        # Calculate the position for the window to be centered
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window geometry
        self.setGeometry(x, y, window_width, window_height)

    def createButton(self):
        for (index, button) in enumerate(self.buttons):
            buttonWidget = QPushButton(button[0], self)
            buttonWidget.clicked.connect(button[1])
            buttonWidget.setStyleSheet("""
            QPushButton {
                font-family: 'Tahoma';         /* Custom font */
                background-color: #d0e8f2;  /* Light blue background */
                color: #333;                 /* Dark gray text */
                font-size: 14px;             /* Text size */
                padding: 8px 16px;           /* Minimal padding */
                margin: 10px;
                border: 1px solid #a6cbe3;   /* Light blue border */
                border-radius: 5px;          /* Slightly rounded corners */
            }
            QPushButton:hover {
                background-color: #b4d7eb;   /* Slightly darker blue on hover */
            }
        """)
            self.buttons[index].append(buttonWidget)

    def addToWidget(self):
        horizontal_layout1 = QHBoxLayout()
        horizontal_layout1.addWidget(self.buttons[0][2])
        horizontal_layout1.addWidget(self.buttons[1][2])
        horizontal_layout1.addWidget(self.buttons[2][2])
        self.layout.addLayout(horizontal_layout1)

        self.layout2 = QVBoxLayout()

        self.addNewRowLayout2(1)

        self.layout.addLayout(self.layout2)

        horizontal_layout3 = QHBoxLayout()
        horizontal_layout3.addWidget(self.buttons[3][2])
        horizontal_layout3.addWidget(self.buttons[4][2])
        self.layout.addLayout(horizontal_layout3)

        horizontal_layout4 = QHBoxLayout()
        horizontal_layout4.addWidget(self.buttons[5][2])
        horizontal_layout4.addWidget(self.buttons[6][2])
        self.layout.addLayout(horizontal_layout4)

    def addNewRowLayout2(self, index):
        xLabel = QLabel(f'x{index} :', self)
        xLabel.setStyleSheet("""
            QLabel {
                font-family: 'Tahoma';         /* Custom font */
                color: #333;                  /* Dark gray text */
                font-size: 16px;              /* Text size */
                padding: 5px 5px;           /* Padding inside the label */
            }
        """)

        xPosition = QLineEdit(self)
        xPosition.setPlaceholderText('xAxis')
        xPosition.setStyleSheet("""
            QLineEdit {
                background-color: #e0f4ff; /* Light blue background */
                border: 1px solid #b3e0ff; /* Light blue border */
                border-radius: 5px;        /* Slightly rounded corners */
                padding: 8px;              /* Padding inside the input box */
                color: #333;               /* Dark gray text */
                font-size: 14px;           /* Font size */
            }
            QLineEdit:focus {
                border: 1px solid #66b3ff; /* Darker blue border on focus */
                background-color: #cce6ff; /* Slightly darker background on focus */
            }
        """)

        yLabel = QLabel(f'y{index} :', self)
        yLabel.setStyleSheet("""
            QLabel {
                font-family: 'Tahoma';         /* Custom font */
                color: #333;                  /* Dark gray text */
                font-size: 16px;              /* Text size */
                padding: 5px 5px;           /* Padding inside the label */
            }
        """)

        yPosition = QLineEdit(self)
        yPosition.setPlaceholderText('yAxis')
        yPosition.setStyleSheet("""
            QLineEdit {
                background-color: #e0f4ff; /* Light blue background */
                border: 1px solid #b3e0ff; /* Light blue border */
                border-radius: 5px;        /* Slightly rounded corners */
                padding: 8px;              /* Padding inside the input box */
                color: #333;               /* Dark gray text */
                font-size: 14px;           /* Font size */
            }
            QLineEdit:focus {
                border: 1px solid #66b3ff; /* Darker blue border on focus */
                background-color: #cce6ff; /* Slightly darker background on focus */
            }
        """)

        thetaLabel = QLabel(f'theta{index} :', self)
        thetaLabel.setStyleSheet("""
            QLabel {
                font-family: 'Tahoma';         /* Custom font */
                color: #333;                  /* Dark gray text */
                font-size: 16px;              /* Text size */
                padding: 5px 5px;           /* Padding inside the label */
            }
        """)

        thetaDegree = QLineEdit(self)
        thetaDegree.setPlaceholderText('thetaDegree')
        thetaDegree.setStyleSheet("""
            QLineEdit {
                background-color: #e0f4ff; /* Light blue background */
                border: 1px solid #b3e0ff; /* Light blue border */
                border-radius: 5px;        /* Slightly rounded corners */
                padding: 8px;              /* Padding inside the input box */
                color: #333;               /* Dark gray text */
                font-size: 14px;           /* Font size */
            }
            QLineEdit:focus {
                border: 1px solid #66b3ff; /* Darker blue border on focus */
                background-color: #cce6ff; /* Slightly darker background on focus */
            }
        """)

        buttonMove = QPushButton(f"Move to Position {index}", self)
        buttonMove.clicked.connect(lambda : self.handleMoveToPositionByIndex(index))
        buttonMove.setStyleSheet("""
            QPushButton {
                font-family: 'Tahoma';         /* Custom font */
                background-color: #d0e8f2;  /* Light blue background */
                color: #333;                 /* Dark gray text */
                font-size: 14px;             /* Text size */
                padding: 8px 16px;           /* Minimal padding */
                margin: 10px;
                border: 1px solid #a6cbe3;   /* Light blue border */
                border-radius: 5px;          /* Slightly rounded corners */
            }
            QPushButton:hover {
                background-color: #b4d7eb;   /* Slightly darker blue on hover */
            }
        """)

        horizontal_layout2 = QHBoxLayout()
        horizontal_layout2.addWidget(xLabel)
        horizontal_layout2.addWidget(xPosition)
        horizontal_layout2.addWidget(yLabel)
        horizontal_layout2.addWidget(yPosition)
        horizontal_layout2.addWidget(thetaLabel)
        horizontal_layout2.addWidget(thetaDegree)
        horizontal_layout2.addWidget(buttonMove)
        self.layout2.addLayout(horizontal_layout2)
        self.dataFromLayout2.append([xPosition, yPosition, thetaDegree])
        self.buttonLayoutFromLayout2.append(horizontal_layout2)

    def getRawStringCommand(self, x, y, theta):
        position = "{ x: " + str(x) +", y : " + str(y) + ", theta : " + str(theta) + "}"
        command = f"ros2 topic pub --once /Ctrl_val geometry_msgs/msg/Pose2D '{position}'"
        return command

    # Event handler for button click
    def handleMoveToPositionByIndex(self, index):
        try:
            if self.process:
                self.process.terminate()
                self.process.wait()
            text = f"Move to Position{index}\t"
            (xPos, yPos, th) = self.dataFromLayout2[index - 1]
            text += f"x{index}: {xPos.text()} y{index}: {yPos.text()} theta{index}: {th.text()}\n"
            self.label.setText(text)
            self.process = subprocess.Popen(self.getRawStringCommand( float(xPos.text()), float(yPos.text()), float(th.text())), shell=True, executable='/bin/bash')
        except:
            self.label.setText(f'Input is required!')

    def handleDuplicateRow(self):
        if (len(self.dataFromLayout2) < 5):
            self.label.setText('New Row Success')
            self.addNewRowLayout2(len(self.dataFromLayout2) + 1)
        else:
            self.label.setText('Maximum Row')

    def handleDeleteRow(self):
        if len(self.dataFromLayout2) > 1:
            self.label.setText('Delete Success')
            self.dataFromLayout2.pop()
            layout_to_remove = self.buttonLayoutFromLayout2.pop()  # Get the last row
            for i in reversed(range(layout_to_remove.count())):
                widget = layout_to_remove.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()  # Remove the widget
            self.layout.removeItem(layout_to_remove)  # Remove the layout itself
        else:
            self.label.setText('Minimum 1 Row !!')

    def handleSetUpENV(self):
        self.label.setText('Set Up env')
        # result = subprocess.run('ls', shell=True, capture_output=True, text=True)
        # result = subprocess.run('source esphome/venv/bin/activate && python RoboAC-GUI.py', shell=True, capture_output=True, text=True)
        # result = subprocess.run('cd', shell=True, capture_output=True, text=True)
        # result = subprocess.run('echo ok', cwd='/', capture_output=True, text=True)
        # self.label.setText(f'{result.stdout} , {result.stderr}')
        # result = subprocess.run('source esphome/venv/bin/activate', shell=True, capture_output=True, text=True)
        # self.label.setText(f'{result.stdout} , {result.stderr}')

    def handleRViz(self):
        try:
            self.label.setText('RViz')
            # result = subprocess.run('rviz2', shell=True, capture_output=True, text=True)
            # result = subprocess.run('rviz2', shell=True, capture_output=False, text=True)
            # subprocess.run(['rviz2'])
            process = subprocess.Popen(['rviz2'])
            # self.label.setText(f'{result.stdout} , {result.stderr}')
        except:
            self.label.setText('RViz Eror')

    def handleOdometry(self):
        self.label.setText('Odometry')
        result = subprocess.run('ros2 topic echo /Odom_pub', shell=True, capture_output=True, text=True)
        self.label.setText(f'{result.stdout} , {result.stderr}')

    def handleMoveToAllPosition(self):
        try:
            text = "Move to All Position\n"
            for (index, (xPos, yPos, th)) in enumerate(self.dataFromLayout2,start=1):
                text += f"x{index}: {xPos.text()} y{index}: {yPos.text()} theta{index}: {th.text()}\n"
            self.label.setText(text)
        except:
            self.label.setText(f'Input is required!')

    def handleGoToHome(self):
        self.label.setText('Go to Home')


# Entry point for the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
