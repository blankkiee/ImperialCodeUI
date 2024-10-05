# ui.py
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QWidget, QTableWidget, QSpacerItem, QSizePolicy
from functionality import analyze_code_function, refresh_ui  # Import the new refresh_ui function
from PyQt5.QtGui import QIcon  # Import QIcon for setting the window icon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("ImperialCode Programming Language")
        self.setGeometry(100, 100, 1200, 800)
        
        # Set the window icon (logo)
        self.setWindowIcon(QIcon("./imgLogo/imperialCodeLogo.png"))  # Set the logo image as window icon


        # Main layout container widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create horizontal layout for top buttons (Lexical, Syntax, Semantic) and file buttons (New, Open, Save)
        top_layout = QHBoxLayout()

        # Top buttons (Lexical, Syntax, Semantic)
        lexical_btn = QPushButton("Lexical Analysis")
        lexical_btn.setStyleSheet("background-color: #0B6623; border-radius: 5px; padding: 10px; color: white; font-weight: bold; font-size: 13px; margin-bottom: 70px;")
        syntax_btn = QPushButton("Syntax Analysis")
        syntax_btn.setStyleSheet("border-radius: 5px; padding: 10px; font-weight: bold; font-size: 13px; color: #4a4a4a; border: 1px solid gray; margin-bottom: 70px;")
        semantic_btn = QPushButton("Semantic Analysis")
        semantic_btn.setStyleSheet("border-radius: 5px; padding: 10px; font-weight: bold; font-size: 13px; color: #4a4a4a; border: 1px solid gray; margin-bottom: 70px;")


        # Add buttons to the top layout (left-aligned)
        top_layout.addWidget(lexical_btn)
        top_layout.addWidget(syntax_btn)
        top_layout.addWidget(semantic_btn)

        # Spacer to push other buttons to the right
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        top_layout.addSpacerItem(spacer)

        # File buttons (right-aligned: New File, Open File, Save File)
        new_file_btn = QPushButton("New File")
        new_file_btn.setStyleSheet("border-radius: 5px; padding: 10px; font-weight: bold; font-size: 13px; color: #4a4a4a; border: 1px solid gray; margin-bottom: 70px;")
        open_file_btn = QPushButton("Open File")
        open_file_btn.setStyleSheet("border-radius: 5px; padding: 10px; font-weight: bold; font-size: 13px; color: #4a4a4a; border: 1px solid gray; margin-bottom: 70px;")
        save_file_btn = QPushButton("Save File")
        save_file_btn.setStyleSheet("border-radius: 5px; padding: 10px; font-weight: bold; font-size: 13px; color: #4a4a4a; border: 1px solid gray; margin-bottom: 70px;")

        # Add file buttons to the top layout (right-aligned)
        top_layout.addWidget(new_file_btn)
        top_layout.addWidget(open_file_btn)
        top_layout.addWidget(save_file_btn)

        # Create a layout for the code editor and buttons (Refresh, Analyze)
        editor_layout = QVBoxLayout()

        code_label = QLabel("Code Editor")
        code_label.setStyleSheet("padding: 10px; font-size: 14px; font-weight: bold;")
        self.code_edit = QTextEdit()
        self.code_edit.setPlaceholderText("01 Enter code here...")
        self.code_edit.setStyleSheet("background-color: #555; color: #eee; font-family: monospace; font-size: 14px; border-radius: 5px;")

        # Refresh and Analyze Code buttons
        button_layout = QHBoxLayout()
        refresh_btn = QPushButton("Refresh")
        analyze_btn = QPushButton("Analyze Code")
        refresh_btn.setStyleSheet("background-color: #ddd; padding: 10px;")
        analyze_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px;")

        # Add functionality to the analyze button
        analyze_btn.clicked.connect(lambda: analyze_code_function(self.code_edit.toPlainText(), self.result_table, self.console_edit))

        # Add functionality to the refresh button
        refresh_btn.clicked.connect(lambda: refresh_ui(self.code_edit, self.result_table, self.console_edit))

        # Add buttons to the layout
        button_layout.addWidget(refresh_btn)
        button_layout.addWidget(analyze_btn)

        editor_layout.addWidget(code_label)
        editor_layout.addWidget(self.code_edit)
        editor_layout.addLayout(button_layout)

        # Right-side table for displaying analysis results
        self.result_table = QTableWidget()
        self.result_table.setRowCount(0)
        self.result_table.setColumnCount(4)
        self.result_table.setHorizontalHeaderLabels(['Line', 'Lexeme', 'Token', 'Attribute'])
        self.result_table.setStyleSheet("background-color: #e5e7eb; color: black; border: 0px; font-weight: bold; color: #4a4a4a;")
        

        # Console area for messages
        console_label = QLabel("Console")
        self.console_edit = QTextEdit()
        self.console_edit.setReadOnly(True)
        self.console_edit.setPlaceholderText("Console output...")
        self.console_edit.setStyleSheet("background-color: #eee; padding: 10px;")

        # Layout for console and result table
        result_layout = QVBoxLayout()
        result_layout.addWidget(self.result_table)

        console_layout = QVBoxLayout()
        console_layout.addWidget(console_label)
        console_layout.addWidget(self.console_edit)

        # Create main horizontal layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(editor_layout, 2)  # Code editor on the left side
        main_layout.addLayout(result_layout, 1)  # Table on the right side

        # Add top buttons and the main layout to the central layout
        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addLayout(main_layout)
        layout.addLayout(console_layout)

        central_widget.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
