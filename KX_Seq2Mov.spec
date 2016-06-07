# -*- mode: python -*-
# -*- coding: utf-8 -*-
added_files = [('ffmpeg.exe','E:\\Scripts\\Eclipse\\Seq2Mov\\ffmpeg.exe', 'DATA')]
a = Analysis(['showUI.py'],
             pathex=['E:\\Scripts\\Eclipse\\Seq2Mov'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=u'腾清序列转mov工具.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='E:\\Scripts\\Eclipse\\Seq2Mov\\TenQing.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas+added_files,
               strip=None,
               upx=True,
               name=u'腾清序列转mov工具')
