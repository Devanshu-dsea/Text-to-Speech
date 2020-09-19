import sys
import pyttsx3
from  PyQt5 import Qt
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QMessageBox,QLineEdit,QLabel
from PyQt5.QtGui import QIcon
class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.draw()
    def draw(self):

        self.lbl=QLabel(self)
        self.lbl.setText("Enter here:")
        self.lbl.move(100,125)

        self.line = QLineEdit(self)
        self.line.resize(250, 25)
        self.line.move(100, 150)
        self.line.returnPressed.connect(self.speak)

        btn=QPushButton('Speak',self)
        btn.resize(btn.sizeHint())
        btn.move(150,250)
        btn.clicked.connect(self.speak)

        qui=QPushButton('Quit',self)
        qui.clicked.connect(QApplication.instance().quit)
        qui.resize(qui.sizeHint())
        qui.move(250,250)

    #def keyPressEvent(self, event):
        #if event.key() == Qt.Key_Enter:
      #      self.speak

        self.setWindowTitle('Text to Speech')
        self.resize(500,500)
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def speak(self):

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        a = voices[1]
        engine.setProperty('voice', a.id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume',1.00)
        if self.line.text()=='':
            engine.say("Enter something first.")
            engine.runAndWait()
        else:
            engine.say(self.line.text())
            engine.runAndWait()

    def closeEvent(self, event):
        reply=QMessageBox.question(self,'Quit','Are you sure you want to Quit?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
def main():
    app=QApplication(sys.argv)
    win=GUI()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()