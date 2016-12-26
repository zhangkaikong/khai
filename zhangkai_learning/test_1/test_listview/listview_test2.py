#coding:utf-8
from PyQt4.QtGui import *
import sys
from PyQt4.QtCore import *
from PyQt4.Qt import *

class MyListView(QWidget):
    def __init__(self):
        super(MyListView,self).__init__()
        listdata = [1,2,3,4,5,6,7,8]
        self.lv = QListView()
        self.lv.setToolTip('My First ListView')
        lm = MyListMode(listdata,self)
        self.lv.setModel(lm)
        layot=QVBoxLayout()
        layot.addWidget(self.lv)
        self.setLayout(layot)



class MyListMode(QAbstractListModel):
    def __init__(self,datain,parnet=None):
        super(MyListMode,self).__init__(parnet)
        self.listdata = datain

    def rowCount(self, parent=QModelIndex()):
        return len(self.listdata)

    def data(self, QModelIndex, int_role=None):
        if QModelIndex.isValid() and int_role == Qt.DisplayRole:
            return QVariant(self.listdata[QModelIndex.row()])
        else:
            return QVariant()

app =QApplication(sys.argv)
listview = MyListView()
listview.show()
sys.exit(app.exec_())