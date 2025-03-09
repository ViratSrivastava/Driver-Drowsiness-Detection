# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['package\\run.py'],
    pathex=[],
    binaries=[],
    datas=[('package/models/shape_predictor_68_face_landmarks.dat', 'models'), ('package/audio/warning-buzzer-the-foundation-4-4-00-16.mp3', 'audio')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='run',
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
