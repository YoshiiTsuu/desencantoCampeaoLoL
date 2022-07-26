import pyautogui
import pyautogui, sys
import time

# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

i = 0;
while i< 4:
        pyautogui.click(430,414);
        time.sleep(1);
        pyautogui.click(661,450);
        time.sleep(1);
        pyautogui.click(848,673);
        i+=1;



