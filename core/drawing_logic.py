import sys
from PySide6.QtCore import QObject, Slot, Signal, QPointF
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class DrawingLogic(QObject):
    # Signal that will be emitted with the line to be drawn
    line_drawn = Signal(list)

    def __init__(self):
        super().__init__()
        self._points = []
        self._is_drawing = False

    @Slot(float, float)
    def press(self, x, y):
        self._is_drawing = True
        self._points = [QPointF(x, y)]

    @Slot(float, float)
    def move(self, x, y):
        if self._is_drawing:
            self._points.append(QPointF(x, y))

            # Emit signal with last 2 points to draw a line segment
            self.line_drawn.emit(self._points[-2:])

    @Slot()
    def release(self):
        self._is_drawing = False
        self._points = []

    @Slot()
    def clear(self):
        pass
