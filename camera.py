# класс камеры
class Camera:
    def __init__(self, field_size, width, height):
        self.dx = 0
        self.dy = 0
        self.field_size = field_size
        self.w = width
        self.h = height

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self.w // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - self.h // 2)
