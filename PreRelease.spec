# myapp.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
        ('C:/Program Files/STMicroelectronics/STM32Cube/STM32CubeProgrammer/bin/CubeProgrammer_Api.dll', '.'),
        ('C:/Users/blufuf-pc/Desktop/api-ms-win-core-path-l1-1-0.dll', '.'),
        ('C:/Users/blufuf-pc/AppData/Local/Programs/Python/Python39/python39.dll', '.')
    ],
    datas=[
        ('board1_window.py', '.'),
        ('board2_window.py', '.'),
        ('board3_window.py', '.'),
        ('board4_window.py', '.'),
        ('ai_sid.txt', '.'),
        ('ai_sid_dicts.txt', '.'),
        ('ai_mid.txt', '.'),
        ('ai_mid_dicts.txt', '.'),
        ('di_sid.txt', '.'),
        ('di_sid_dicts.txt', '.'),
        ('di_mid.txt', '.'),
        ('di_mid_dicts.txt', '.'),
        ('dicts_log.txt', '.'),
        ('terminal.py', '.'),
        ('terminal2.py', '.')
    ],
    hiddenimports=['tabulate'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PreRelease',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PreRelease'
)
