import os
import sys
import webbrowser
import subprocess
import data
from PySide6 import QtWidgets as qtw

import main.app
from prefs.UI.prefs import Ui_PrefsWindow

class PrefsView(qtw.QWidget, Ui_PrefsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        def openlists():
            listfile = data.getModulePath('lists')
            # print(listfile)
            try:
                if data.getsysname() == 'Windows':
                    os.startfile(listfile)
                elif data.getsysname() == 'Darwin':
                    subprocess.call(['open', listfile])
                self.restart_label.setText('changes will apply after app restart')
            except:
                self.restart_label.setText('could not locate file')

        def opengenlog():
            logfile = data.getModulePath('sval')
            # print(logfile)
            try:
                if data.getsysname() == 'Windows':
                    os.startfile(logfile)
                elif data.getsysname() == 'Darwin':
                    subprocess.call(['open', logfile])
            except:
                self.restart_label.setText('could not locate file')

        def openrepo():
            repo = "https://github.com/willowyx/RandomizeMe/releases"
            webbrowser.open(repo, new=0, autoraise=True)

        def openrepo_info():
            repo = "https://github.com/willowyx/RandomizeMe#randomize-me"
            webbrowser.open(repo, new=0, autoraise=True)

        def locunins():
            ufile_path = ''
            if data.getsysname() == 'Windows':
                ufile_path = os.environ["ProgramW6432"]
                ufile_path += '\\RandomizeMe'
                try:
                    os.startfile(ufile_path)
                    self.restart_label.setText('You must quit the app before uninstalling')
                except:
                    self.restart_label.setText('could not locate directory')
            elif data.getsysname() == 'Darwin':
                # return os.path.join(os.path.expanduser('~/Library/Application Support'), 'RandomizeMe/unins.app')
                self.restart_label.setText('uninstaller does not exist')

        self.quit_btn.clicked.connect(self.close)

        self.open_lists_btn.clicked.connect(openlists)

        self.open_genlog_btn.clicked.connect(opengenlog)

        self.unins_btn.clicked.connect(locunins)

        self.about_btn.clicked.connect(self.showabout)

        self.update_btn.clicked.connect(openrepo)
        self.repo_btn.clicked.connect(openrepo_info)

        self.uwuify_btn.stateChanged.connect(self.state_changed)

    def uwuify_prefs(self):
        self.label.setText('p-pwefewences')
        self.label_2.setText('edit wists')
        self.label_3.setText('u-updates')
        self.label_4.setText('u-uninstall')
        self.label_5.setText('g-genewation wog')
        self.restart_label.setText('some c-changes may wequire a-app westawt')
        self.quit_btn.setText('cwose')
        self.repo_btn.setText('open wepositowy')
        self.about_btn.setText('about this pwoject')
        self.update_btn.setText('view weweases')
        self.unins_btn.setText('w-wocate uninstawwew')
        self.setWindowTitle('pwefewences | wandomize me')

    def state_changed(self):
        if self.uwuify_btn.isChecked():
            with open(data.getModulePath('prefs'), 'w') as f:
                f.write('PREFS_UWU=1\n')
                f.close()
        # elif not self.uwuify_btn.isChecked():
        else:
            with open(data.getModulePath('prefs'), 'w') as f:
                f.write('PREFS_UWU=0\n')
                f.close()
        self.restart_label.setText('restart the app to see what you\'ve done')

    def showabout(self):
        from about.aboutview import AboutView
        self.about = AboutView()
        print('loaded no window data for about: uwu (expected)')
        self.about.show()

    def setuwucheck(self):
        self.uwuify_btn.setChecked(True)
        print('loaded prefs data for: uwu')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = PrefsView()
    w.show()
    sys.exit(app.exec())
