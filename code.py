from pygame import * 
w,h = 1000,800 
win = display.set_mode([w,h]) 
bg = image.load('mg.jpg') #у вас другое название! 
bg = transform.scale(mg, [w,h]) 
 
class Basic(sprite.Sprite): 
 def __init__(self,filename,x,y,w,h): 
 super().__init__() 
 self.img = image.load(filename) 
 
 self.img = transform.scale(vb.img, [w,h]) 
 
 self.img_right = self.img 
 self.img_left = transform.flip(vb.img,True,False) 
 
 self.rect = Rect(x,y,w,h) 
 
 def draw(self): 
 win.blit(self.img, (self.rect.x, self.rect.y)) 
 
class Hero(Basic): 
 def __init__(self, filename, x, y, w, h): 
 super().__init__(filename, x, y, w, h) 
 self.x_speed = 0 
 self.y_speed = 0 
 
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
 
        if self.rect.x < 0: self.rect.x = 0 #если уперлись в стенку
        if self.rect.right > w: self.rect.right = w
        if self.rect.bottom > h: self.rect.bottom = h
        if self.rect.y < 0: self.rect.y = 0
 
        self.draw()
 
gg = Hero(x=500, y=200, filename='hero.jpg',w=100,h=100)
enemy = Basic(x=700, y=200, filename='ork.png',  w=100, h=100)
timer = time.Clock()
while True:
    win.blit(bg, (0,0))
    gg.update()
    enemy.draw()
 
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_d: 
                gg.x_speed = 10
                gg.img = gg.img_right
 
            if e.key == K_a:
                gg.x_speed = -10
                gg.img = gg.img_left
 
            if e.key == K_w: gg.y_speed = -10
            if e.key == K_s: gg.y_speed = 10
 
        if e.type == KEYUP:
            if e.key == K_d or e.key == K_a: gg.x_speed = 0
            if e.key == K_w or e.key == K_s: gg.y_speed = 0
 
        if e.type == QUIT: exit()
 
    timer.tick(30) #30 раз в секунду (фпс)
    display.update()
    walls_touched = sprite.spritecollide(self, walls, False)
        #анализ стен
        if len(walls_touched) > 0:
            if self.x_speed < 0: #если идем справа-налево
                self.rect.left = walls_touched[0].rect.right
            
            elif self.x_speed > 0: #если идем слева-направо
                self.rect.right = walls_touched[0].rect.left

            elif self.y_speed < 0: #если идем наверх
                self.rect.top = walls_touched[0].rect.bottom
            
            elif self.y_speed > 0: #если идем вниз
                self.rect.bottom = walls_touched[0].rect.top
for wall in walls_touched:
            if self.x_speed < 0: #если идем справа-налево
                self.rect.left = wall.rect.right
            
            elif self.x_speed > 0: #если идем слева-направо
                self.rect.right = wall.rect.left

            elif self.y_speed < 0: #если идем наверх
                self.rect.top = wall.rect.bottom
            
            elif self.y_speed > 0: #если идем вниз
                self.rect.bottom = wall.rect.top

