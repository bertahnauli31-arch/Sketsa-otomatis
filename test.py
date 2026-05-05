import pyautogui

screenWidth, ScreenHeight = pyautogui.size()
print(screenWidth, ScreenHeight)

currentMouseX, currentMouseY = pyautogui.position()

print(currentMouseX, currentMouseY)


canvas_start_ratio_x = 10.0/1920
canvas_start_ratio_y = 180.0/1080

canvas_size_ratio_x = 1070.0/1920
canvas_size_ratio_y = 670.0/1080

canvas_start_x = screenWidth*canvas_start_ratio_x
canvas_start_y = ScreenHeight*canvas_start_ratio_y

canvas_end_x = canvas_start_x + canvas_size_ratio_x*screenWidth
canvas_end_y = canvas_start_y + canvas_size_ratio_y*screenWidth

print(canvas_start_x,canvas_start_y)
print(canvas_end_x,canvas_end_y)
