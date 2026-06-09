import pygame

pygame.init()
mw = pygame.display.set_mode((500,500))
mw.fill((1,1,100))
clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0,y=0, width=9, height=9, color=(255,255,255)):
        self.rect = pygame.Rect(x,y,width, height)
        self.fill_color = color

    def fill(self):
        pygame.draw.rect(mw,self.fill_color, self.rect)

    def color(self, new):
        self.fill_color = new

    def line(self, color, width):
        pygame.draw.rect(mw, color, self.rect, width)

    def collide1(self, rect):
        return self.rect.colliderect(rect)
    
    

class Label(Area):
    
    def set_text(self, text, size, color):
        self.image = pygame.font.Font(None, size).render(text,True, color)

    def draw(self,shiftx=0, shifty=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shiftx, self.rect.y + shifty))

class Picture(Area):

    def __init__(self,x,y,width,height,color,file_name):
        super().__init__(x,y,width,height,color)
        self.image = pygame.image.load(file_name)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

pl = Picture(50,400,100,30,(1,1,100), "platform.png")
ball = Picture(50,320,50,50,(1,1,100), "ball.png")

game = True 

enemies  = []
x_start = 5 
y_start = 5
n = 9
move_right = False
move_left = False

for i in range(3):
    x = x_start + 27 * i
    y = y_start + 55 * i
    for h in range(n):
        enemy = Picture(x,y,50,50,(1,1,100), "enemy.png")
        enemies.append(enemy)
        x += 55
    n -= 1

speed_x = 3
speed_y = 3

while game:
    pl.fill()
    ball.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    if move_right:
        pl.rect.x += 3
    if move_left:
        pl.rect.x -= 3

    ball.rect.x += speed_x 
    ball.rect.y += speed_y 

    if ball.collide1(pl.rect) or ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1

    for enemy in enemies:
        enemy.draw()
    

    ball.draw()
    pl.draw()
    pygame.display.update()
    clock.tick(40)
