import sys
import data
import os
from PySide6 import QtWidgets as qtw
from PySide6.QtWidgets import QTextBrowser

from about.UI.about import Ui_AboutWindow


class AboutView(qtw.QWidget, Ui_AboutWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.fetch_data()
        self.quit_btn.clicked.connect(self.close)

    def uwuify_about(self):
        self.quit_btn.setText('cwose')
        self.setWindowTitle('about | wandomize me')

    def fetch_data(self):
        self.fetch_ver()
        try:
            self.fetch_license()
        except:
            self.license_text.setText('Error: license data is missing or corrupted. Please restart or reinstall.')
        try:
            self.fetch_attributions()
        except:
            self.attribution_text.setText('Error: attribution data is missing or corrupted. Please restart or reinstall.')

    def fetch_ver(self):  # checks prefs file for version (loaded on UI setup)
        import re
        open(data.getModulePath('prefs'), 'a').close()
        # check version
        try:
            with open(data.getModulePath('data'), 'r') as file:
                contents = file.read()
                match = re.search(r'APP_VER=(\d*.\d*.\d*)', contents)
                if match:
                    verdata = match.group(1)
                    print('loaded version as ' + str(verdata))  # debug
                    if (verdata != '') and (verdata is not None):
                        self.ver_label.setText('Randomize Me! ver. ' + str(verdata))
                    else:
                        self.ver_label.setText('version data invalid')
                else:
                    self.ver_label.setText('no version data')
        except:
            self.ver_label.setText('version data missing or corrupted')

    def fetch_license(self):
        filepath = ''
        if data.getsysname() == 'Windows':
            filepath = os.path.join(os.getenv('appdata'), 'RandomizeMe/LICENSE.html')
        elif data.getsysname() == 'Darwin':
            filepath = os.path.join(os.path.expanduser('~/Library/Application Support'),
                                    'RandomizeMe/LICENSE.html')

        with open(filepath, 'r') as file:
            html_content = file.read()
            self.license_text.setHtml(html_content)

    def fetch_attributions(self):
        filepath = ''
        if data.getsysname() == 'Windows':
            filepath = os.path.join(os.getenv('appdata'), 'RandomizeMe/attributions.html')
        elif data.getsysname() == 'Darwin':
            filepath = os.path.join(os.path.expanduser('~/Library/Application Support'),
                                    'RandomizeMe/attributions.html')

        with open(filepath, 'r') as file:
            html_content = file.read()
            self.attribution_text.setOpenExternalLinks(True)
            self.attribution_text.setHtml(html_content)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = AboutView()
    w.show()
    sys.exit(app.exec())
