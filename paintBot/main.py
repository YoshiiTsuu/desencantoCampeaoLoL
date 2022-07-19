import pyautogui

#pyautogui.hotkey('alt', 'tab')

import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

# i = 0;
# while i< 5:
#         pyautogui.click(3200,410);
#         pyautogui.click(4326,944);
#         pyautogui.click(4289,1031);
#         i+=1;



