# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_submodules
import os

# Absolute paths to required local files
db_file = os.path.abspath("animals.db")
logo_file = os.path.abspath("Grazioso Salvare Logo.png")

# Collect dash_leaflet static assets and submodules
dash_leaflet_datas = collect_data_files("dash_leaflet")
dash_leaflet_hiddenimports = collect_submodules("dash_leaflet")
plotly_datas = collect_data_files('plotly', include_py_files=False)

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        (db_file, '.'),                     # Include database
        (logo_file, '.'),                   # Include logo
    ] + dash_leaflet_datas + plotly_datas, # Include dash_leaflet & plotly resources
    hiddenimports=dash_leaflet_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to False if you don’t want the terminal to appear
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)