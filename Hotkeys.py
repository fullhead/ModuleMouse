import keyboard
import mouse

# Перемещение объектов
keyboard.add_hotkey('W', lambda: mouse.move(1245, 118, duration=0.01)),
keyboard.add_hotkey('W', lambda: mouse.click("left")),
keyboard.add_hotkey('W', lambda: mouse.move(504, 191, duration=0.1)),
keyboard.add_hotkey('W', lambda: mouse.click("left")),
keyboard.add_hotkey('W', lambda: mouse.move(766, 444, duration=0.01)),

# Редактирование атрибутов объектов
keyboard.add_hotkey('Y', lambda: mouse.move(1245, 118, duration=0.01)),
keyboard.add_hotkey('Y', lambda: mouse.click("left")),
keyboard.add_hotkey('Y', lambda: mouse.move(528, 215, duration=0.1)),
keyboard.add_hotkey('Y', lambda: mouse.click("left")),
keyboard.add_hotkey('Y', lambda: mouse.move(766, 444, duration=0.01)),

# Режим непрерывного редактирования
keyboard.add_hotkey('R', lambda: mouse.move(1245, 118, duration=0.01)),
keyboard.add_hotkey('R', lambda: mouse.click("left")),
keyboard.add_hotkey('R', lambda: mouse.move(468, 337, duration=0.1)),
keyboard.add_hotkey('R', lambda: mouse.click("left")),
keyboard.add_hotkey('R', lambda: mouse.move(1245, 118, duration=0.01)),
keyboard.add_hotkey('R', lambda: mouse.click("left")),
keyboard.add_hotkey('R', lambda: mouse.move(766, 444, duration=0.01)),

# Удаление объектов
keyboard.add_hotkey('T', lambda: mouse.move(1245, 118, duration=0.01)),
keyboard.add_hotkey('T', lambda: mouse.click("left")),
keyboard.add_hotkey('T', lambda: mouse.move(506, 289, duration=0.1)),
keyboard.add_hotkey('T', lambda: mouse.click("left")),
keyboard.add_hotkey('T', lambda: mouse.move(766, 444, duration=0.01)),

# Желые дома
keyboard.add_hotkey('D', lambda: mouse.move(1161, 116, duration=0.01)),
keyboard.add_hotkey('D', lambda: mouse.click("left")),
keyboard.add_hotkey('D', lambda: mouse.move(1266, 290, duration=0.1)),
keyboard.add_hotkey('D', lambda: mouse.click("left")),
keyboard.add_hotkey('D', lambda: mouse.move(1280, 343, duration=0.01)),
keyboard.add_hotkey('D', lambda: mouse.click("left")),

# Постройка
keyboard.add_hotkey('F', lambda: mouse.move(1161, 116, duration=0.01)),
keyboard.add_hotkey('F', lambda: mouse.click("left")),
keyboard.add_hotkey('F', lambda: mouse.move(1266, 290, duration=0.01)),
keyboard.add_hotkey('F', lambda: mouse.click("left")),
keyboard.add_hotkey('F', lambda: mouse.move(1212, 232, duration=0.01)),
keyboard.add_hotkey('F', lambda: mouse.click("left")),
keyboard.add_hotkey('F', lambda: mouse.move(1254, 355, duration=0.01)),
keyboard.add_hotkey('F', lambda: mouse.click("left")),
keyboard.add_hotkey('F', lambda: mouse.move(1280, 341, duration=0.2)),
keyboard.add_hotkey('F', lambda: mouse.click("left")),

# Образование
keyboard.add_hotkey('G', lambda: mouse.move(1161, 116, duration=0.01)),
keyboard.add_hotkey('G', lambda: mouse.click("left")),
keyboard.add_hotkey('G', lambda: mouse.move(1266, 290, duration=0.01)),
keyboard.add_hotkey('G', lambda: mouse.click("left")),
keyboard.add_hotkey('G', lambda: mouse.move(1212, 232, duration=0.01)),
keyboard.add_hotkey('G', lambda: mouse.click("left")),
keyboard.add_hotkey('G', lambda: mouse.move(1235, 467, duration=0.01)),
keyboard.add_hotkey('G', lambda: mouse.click("left")),
keyboard.add_hotkey('G', lambda: mouse.move(1280, 341, duration=0.2)),
keyboard.add_hotkey('G', lambda: mouse.click("left")),

# Религия
keyboard.add_hotkey('H', lambda: mouse.move(1161, 116, duration=0.01)),
keyboard.add_hotkey('H', lambda: mouse.click("left")),
keyboard.add_hotkey('H', lambda: mouse.move(1266, 290, duration=0.01)),
keyboard.add_hotkey('H', lambda: mouse.click("left")),
keyboard.add_hotkey('H', lambda: mouse.move(1212, 232, duration=0.01)),
keyboard.add_hotkey('H', lambda: mouse.click("left")),
keyboard.add_hotkey('H', lambda: mouse.move(1234, 472, duration=0.01)),
keyboard.add_hotkey('H', lambda: mouse.click("left")),
keyboard.add_hotkey('H', lambda: mouse.move(1280, 341, duration=0.2)),
keyboard.add_hotkey('H', lambda: mouse.click("left")),

keyboard.wait('Ctrl + Alt + Q')
