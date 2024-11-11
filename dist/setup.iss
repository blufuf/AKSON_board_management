[Setup]
AppName=АКСОН board management
AppVersion=1.0
DefaultDirName={pf}\АКСОНboardmanagement
DefaultGroupName=АКСОН board management
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
; Основной исполняемый файл
Source: "C:\Users\blufuf-pc\work\pythonProject\dist\PreRelease\PreRelease.exe"; DestDir: "{app}"; Flags: ignoreversion

; Все текстовые файлы
Source: "C:\Users\blufuf-pc\work\pythonProject\dist\PreRelease\*.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\blufuf-pc\work\pythonProject\dist\PreRelease\_internal\*.txt"; DestDir: "{app}"; Flags: ignoreversion

; Файлы из папки _internal
Source: "C:\Users\blufuf-pc\work\pythonProject\dist\PreRelease\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\АКСОН board management"; Filename: "{app}\PreRelease.exe"

[Run]
Filename: "{app}\PreRelease.exe"; Description: "Launch АКСОН board management"; Flags: nowait postinstall skipifsilent
