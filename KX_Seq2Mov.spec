# -*- mode: python -*-
added_files=[('ffmpeg.exe','E:\\Scripts\\Eclipse\\Seq2Mov\\ffmpeg.exe', 'DATA')]
a = Analysis(['showUI.py'],
             pathex=['E:\\Scripts\\Eclipse\\Seq2Mov'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.datas,
          exclude_binaries=True,
          name='KX_Seq2Mov.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='E:\\Scripts\\Eclipse\\Seq2Mov\\KX_Seq2Mov.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas+added_files,
               strip=None,
               upx=True,
               name='KX_Seq2Mov')
