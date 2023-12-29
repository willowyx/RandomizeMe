#modern ui
!include MUI2.nsh

OutFile "RandomizeMeSetup.exe"

InstallDir $PROGRAMFILES64\RandomizeMe

!define APPDATA "$APPDATA\RandomizeMe"

!define APPNAME "Randomize Me"
!define APPNAMEANDVERSION "Randomize Me Installer v1"

name "${APPNAME}"

!define MUI_ICON "appdata\logo.ico"
!define MUI_UNICON "appdata\unins.ico"

!define MUI_WELCOMEFINISHPAGE_BITMAP "appdata\Construction_worker.bmp"
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "appdata\cat.bmp"
!define MUI_HEADERIMAGE_RIGHT

!insertmacro MUI_PAGE_WELCOME

!insertmacro MUI_PAGE_LICENSE "appdata\LICENSE.txt"

!insertmacro MUI_PAGE_DIRECTORY

!insertmacro MUI_PAGE_INSTFILES

Function createdeskicon
CreateShortcut "$desktop\Randomize Me.lnk" "$instdir\app.exe"
FunctionEnd

!define MUI_FINISHPAGE_SHOWREADME ""
!define MUI_FINISHPAGE_SHOWREADME_NOTCHECKED
!define MUI_FINISHPAGE_SHOWREADME_TEXT "Create Desktop Shortcut"
!define MUI_FINISHPAGE_SHOWREADME_FUNCTION createdeskicon

!define MUI_FINISHPAGE_NOAUTOCLOSE
!define MUI_FINISHPAGE_RUN "$INSTDIR\app.exe"
!define MUI_FINISHPAGE_RUN_TEXT "Run Randomize Me"
!define MUI_FINISHPAGE_RUN_NOTCHECKED

!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_WELCOME

!insertmacro MUI_UNPAGE_CONFIRM

!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

# default section start
Section

# define output path
SetOutPath $INSTDIR
File appdata\app.exe
File appdata\LICENSE.txt
File appdata\README.md
File appdata\attributions.txt

;SetOutPath $INSTDIR\data
SetOutPath $APPDATA\RandomizeMe
File appdata\__init__.py
File appdata\lists.py
File appdata\logo.png
File appdata\logo.ico
File appdata\unins.png
File appdata\unins.ico

# define uninstaller name
WriteUninstaller $INSTDIR\unins000.exe

#-------
# default section end

SectionEnd

# create a section to define what the uninstaller does.
# the section will always be named "Uninstall"
Section "Uninstall"

# Delete installed file
Delete $INSTDIR\app.exe
Delete $INSTDIR\LICENSE.txt
Delete $INSTDIR\README.md
Delete $INSTDIR\attributions.txt

Delete $APPDATA\RandomizeMe\lists.py
Delete $APPDATA\RandomizeMe\logo.png
Delete $APPDATA\RandomizeMe\logo.ico
Delete $APPDATA\RandomizeMe\unins.png
Delete $APPDATA\RandomizeMe\unins.ico
Delete $APPDATA\RandomizeMe\sval.txt
Delete $APPDATA\RandomizeMe\__init__.py
Delete $APPDATA\RandomizeMe\__pycache__\lists.cpython-38.pyc
Delete "$desktop\Randomize Me.lnk"

# Delete the uninstaller
Delete $INSTDIR\unins000.exe

# Delete directories
RMDir $APPDATA\RandomizeMe\__pycache__
RMDir $APPDATA\RandomizeMe
RMDir $INSTDIR
SectionEnd
