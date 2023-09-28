# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/Leonhard Tilly/Documents/GitHub/Small-PC-Tools/MP4toOGV/MP4toOGV3.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['C:/Users/Leonhard', 'import', 'Tilly/Documents/GitHub/Small-PC-Tools/MP4toOGV/MP4toOGV3.py:49:30:', "'total_videos'", 'used;', 'but', 'names', 'never', "'VideoFileClip'", 'is', 'be', 'defined', 'Tilly/Documents/GitHub/Small-PC-Tools/MP4toOGV/MP4toOGV3.py:42:13:', 'detect', 'to', 'assigned', 'used', "'from", 'or', "'exit_on_done_var'", 'star', 'Tilly/Documents/GitHub/Small-PC-Tools/MP4toOGV/MP4toOGV3.py:6:1:', "'moviepy'", 'undefined', 'variable', 'Tilly/Documents/GitHub/Small-PC-Tools/MP4toOGV/MP4toOGV3.py:64:30:', 'may', 'undefined,', "*'", 'imported', 'moviepy.editor', 'Tilly/Documents/GitHub/Small-PC-Tools/MP4toOGV/MP4toOGV3.py:86:9:', 'imports:', 'unable', "'converting'", 'unused', 'local', 'from', 'Tilly/Documents/GitHub/Small-PC-Tools/MP4toOGV/MP4toOGV3.py:76:12:', 'Tilly/Documents/GitHub/Small-PC-Tools/MP4toOGV/MP4toOGV3.py:13:11:'],
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
    name='MP4toOGV3',
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
)
