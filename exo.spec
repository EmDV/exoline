# -*- mode: python -*-
a = Analysis(['exoline\\exo.py'],
             pathex=['C:\\Users\\danw\\Source\\Repos\\exoline'],
             hiddenimports=['exoline.plugins'],
             hookspath=None,
             runtime_hooks=None)
a.datas += [
    ('jsonschema\schemas\draft3.json', 'c:\python27\lib\site-packages\jsonschema\schemas\draft3.json', 'DATA'),
    ('jsonschema\schemas\draft4.json', 'c:\python27\lib\site-packages\jsonschema\schemas\draft4.json', 'DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='exo.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='exo')
