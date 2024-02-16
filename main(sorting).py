import os
import shutil
import time
import win32clipboard
import keyboard as kb

while True:
    kb.wait('ctrl+j')
    if kb.is_pressed('ctrl+j') == True:

        path = ''

        time.sleep(0.2)
        kb.send('ctrl+c')
        time.sleep(0.2)
        win32clipboard.OpenClipboard()
        path = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        files = os.listdir(path)

        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]

            if os.path.exists(path+'/'+extension):
                shutil.move(path+'/'+file, path+'/' + extension+'/'+file)
            else:
                os.makedirs(path+'/'+extension)
                shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

