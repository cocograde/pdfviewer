# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [
    ('app\\static', 'app\\static'),
    ('app\\templates', 'app\\templates'),
]

hidden_imports = [
    'app.routes',
]

paths = [
    '.\\',
    '.\\app',
]

a = Analysis(
    ['pdfviewer.py'],
    pathex=paths,
    binaries=[],
    datas=added_files,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='pdfviewer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='app\\static\\assets\\favicon.ico',
)
