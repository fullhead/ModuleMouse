import keyboard
import mouse

# Перемещение объектов
keyboard.add_hotkey('G', lambda: mouse.move(1245, 118, duration=0.01)),
keyboard.add_hotkey('G', lambda: mouse.click("left")),
keyboard.add_hotkey('G', lambda: mouse.move(504, 191, duration=0.1)),
keyboard.add_hotkey('G', lambda: mouse.click("left")),
keyboard.add_hotkey('G', lambda: mouse.move(766, 444, duration=0.01)),

# Редактирование атрибутов объектов
keyboard.add_hotkey('F', lambda: mouse.move(1245, 118, duration=0.01)),
keyboard.add_hotkey('F', lambda: mouse.click("left")),
keyboard.add_hotkey('F', lambda: mouse.move(528, 215, duration=0.1)),
keyboard.add_hotkey('F', lambda: mouse.click("left")),
keyboard.add_hotkey('F', lambda: mouse.move(766, 444, duration=0.01)),

# Удаление объектов
keyboard.add_hotkey('E', lambda: mouse.move(1245, 118, duration=0.01)),
keyboard.add_hotkey('E', lambda: mouse.click("left")),
keyboard.add_hotkey('E', lambda: mouse.move(506, 289, duration=0.1)),
keyboard.add_hotkey('E', lambda: mouse.click("left")),
keyboard.add_hotkey('E', lambda: mouse.move(766, 444, duration=0.01)),

# Режим непрерывного редактирования
keyboard.add_hotkey('Y', lambda: mouse.move(1245, 118, duration=0.01)),
keyboard.add_hotkey('Y', lambda: mouse.click("left")),
keyboard.add_hotkey('Y', lambda: mouse.move(468, 337, duration=0.1)),
keyboard.add_hotkey('Y', lambda: mouse.click("left")),
keyboard.add_hotkey('Y', lambda: mouse.move(1245, 118, duration=0.01)),
keyboard.add_hotkey('Y', lambda: mouse.click("left")),
keyboard.add_hotkey('Y', lambda: mouse.move(766, 444, duration=0.01)),

# Желые дома 1161, 116
keyboard.add_hotkey('G', lambda: mouse.move(1161, 116, duration=0.01)),
keyboard.add_hotkey('G', lambda: mouse.click("left")),
keyboard.add_hotkey('G', lambda: mouse.move(1266, 290, duration=0.1)),
keyboard.add_hotkey('G', lambda: mouse.click("left")),
keyboard.add_hotkey('G', lambda: mouse.move(766, 444, duration=0.01)),

keyboard.wait('Ctrl + Alt + Q')
