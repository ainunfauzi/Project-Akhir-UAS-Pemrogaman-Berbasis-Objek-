import pygame
import random
# --- Globals ---

# Warna yang terdapat
BLACK = (0, 0, 0)
WHITE = (100, 100, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (211, 211, 20)
MAROON = (128,0,0)

# mengatur lebar dan tinggi di dalam bagian ular
segment_width = 20
segment_height = 20

# margin diantara setiap bagian
segment_margin = 0

# mengatur inisialisasi kecepatan
x_change = segment_width + segment_margin
y_change = 0
WALL_THICKNESS = 25
font_name = pygame.font.match_font('arial')

 
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # memanggil pusat pembangun game
        super().__init__()
        # mengaturlebar dan tinggi
        width = 40
        height = 80
        self.image = pygame.image.load("sisik.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        #membuat atas-kiri kita pas diposisi.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def check_collision(self, sprite1):
        return pygame.sprite.collide_rect(self, sprite1)
 
# membuat inisialisasi dari ular
class Snake:
    def __init__(self,length):
        super().__init__()
        self.allspriteslist = pygame.sprite.Group()
        self.snake_segments = []
        self.length = length
        for i in range(self.length):
            x = 350 - (segment_width + segment_margin) * i
            y = 250
            segment = Segment(x, y)
            self.snake_segments.append(segment)
            self.allspriteslist.add(segment)
    def add_segment(self, x, y, index=None):
        if index is None:
            index = self.length
        segment = Segment(x, y)
        self.snake_segments.insert(index, segment)
        self.length += 1
    def Kepala(self):
        return (self.snake_segments[0])
    def Buntut(self):
        return (self.snake_segments[1:])
    def move(self,X,Y):
        #mendapatkan bagian terakhir dari ularnya
        #mengambil() perintah menghapus item terakhir (bagian)
        old_segment = self.snake_segments.pop()
        self.last_removed = old_segment
        self.allspriteslist.remove(old_segment)
        #gambar hilang jika ada bagian baru
        x = self.snake_segments[0].rect.x + X
        y = self.snake_segments[0].rect.y + Y
        if x > 800 :
            x = 0
        if x < 0 :
            x = 800
        if y > 600 :
            y = 25
        if y < 25 :
            y = 600
        segment = Segment(x, y)
        #menambahkan bagian baru kedalam list
        self.snake_segments.insert(0, segment)
        self.allspriteslist.add(segment)
        
    def collides(self, sprite1):
        #hanya Kepala yang akan bertabrakan dengan sprite
        return self.Kepala().check_collision(sprite1)
    def collides_any(self, group):
        for sprite in group:
            if self.collides(sprite):
                return True
        return False
    def grow(self):
        self.add_segment(self.last_removed.rect.x, self.last_removed.rect.y)

class Food(pygame.sprite.Sprite):
    def __init__(self, x_bound, y_bound):
        super().__init__()
        #menggunakan ukuran yang sama dalam setiap bagian ular
        width = 40
        height = 80
        self.image = pygame.image.load("ciken.png")
        self.image = pygame.transform.scale(self.image,(30,30))
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
       
        self.x_bound = x_bound
        self.y_bound = y_bound

    #menimbulkan bagian baru pada snake   
    def spawn(self):
        #Scale the bounds to segment size
        segmentx_size = segment_width + segment_margin
        segmenty_size = segment_height + segment_margin
        randx = random.randint(self.x_bound[0] // segmentx_size, self.x_bound[1] // segmentx_size - 1)
        randy = random.randint(self.y_bound[0] // segmenty_size, self.y_bound[1] // segmenty_size - 1)
        self.rect.x = (randx - 1) * segmentx_size + segment_margin + WALL_THICKNESS
        self.rect.y = (randy - 1) * segmenty_size + segment_margin + WALL_THICKNESS
        if self.rect.y >= 150 and self.rect.y <= 175 :
            self.rect.y = random.randint(175,375)
        if self.rect.y >= 400 and self.rect.y <= 425 :
            self.rect.y = random.randint(175,375)    
    def draw(self, screen):
        #print(self.rect)
        screen.blit(self.image, self.rect)

class Wall(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.wall1 = pygame.Surface([800,25])
        self.wall2= pygame.Surface([25,600])
        self.wall3= pygame.Surface([800,25])
        self.wall4= pygame.Surface([25,600])
        self.wall1.fill(BLACK)
        self.wall2.fill(BLACK)
        self.wall3.fill(BLACK)
        self.wall4.fill(BLACK)
        self.rect1=self.wall1.get_rect()
        self.rect2=self.wall2.get_rect()
        self.rect3=self.wall3.get_rect()
        self.rect4=self.wall4.get_rect()
        self.allWallslist = pygame.sprite.Group()
        
    def Wall1(self,screen):
        self.wall1 = pygame.Surface([20,300])
        self.wall2= pygame.Surface([20,300])
        self.wall1.fill(BLACK)
        self.wall2.fill(BLACK)
        self.rect1.x=200;self.rect1.y=150
        self.rect2.x=600;self.rect2.y=150
        wall = [[self.wall1,self.rect1],[self.wall2,self.rect2]]
        for i in wall:
            screen.blit(i[0],i[1])
##            self.allWallslist.add(i[0])
            
    def Wall2(self,screen) :
        self.wall1 = pygame.Surface([800,25])
        self.wall5= pygame.Surface([25,600])
        self.rect5=self.wall5.get_rect()
        self.wall1.fill(BLACK)
        self.wall5.fill(BLACK)        
        self.rect1.x=0;self.rect1.y=25
        self.rect5x=25;self.rect5.y=0
        self.rect3.x=0;self.rect3.y=575
        self.rect4.x=775;self.rect4.y=0
        wall = [[self.wall1,self.rect1],[self.wall2,self.rect2],[self.wall3,self.rect3],[self.wall4,self.rect4],[self.wall5,self.rect5]]
        for i in wall:
            screen.blit(i[0],i[1])
    

    def cekColl(self,x,y,level):
        wallPos = [25 , 575, 775]
        if y >= 150 and y <= 450 and level == 3 : #wall lvl 3 Kiri
            if x >= 200 and x <= 220 :
                return True
        if y >= 150 and y <= 450 and level ==3: # Wall lvl 3 Kanan
            if x >= 600 and x <= 620 :
                return True
        elif level<=3 and level >=2  :
            if y <= 25 or y >= 575 :
                return True
            if x <= 0 or x >= 775:
                return True
        
        else :
            return False
                
        
        
class APP:
    def __init__(self):
        # panggil fungsi ini sehingga pygame meginisialisasi dirinya
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(font_name , 30)
        # Create an 800x600 sized screen
        self.screen = pygame.display.set_mode([800, 600])
        # mengatur judul layar
        pygame.display.set_caption('Snake')
        self.snake = Snake(2)
        self.clock = pygame.time.Clock()
        self.done = False
    def game_init(self) :
        self.game_bound = {
            'min_x'  : 0,
            'max_x' : 600,
            'min_y' : 50,
            'max_y' : 400 }
        self.food = Food((self.game_bound['min_x'] + WALL_THICKNESS, self.game_bound['max_x']-WALL_THICKNESS),
                        (self.game_bound['min_y'] + WALL_THICKNESS, self.game_bound['max_y']-WALL_THICKNESS))
        self.food.spawn()
        self.score = 0
        self.level = 1
        self.wall = Wall()

    def scoreBoard(self):
        self.running = True
        background = pygame.image.load('score.jpg').convert()
        background_rect = background.get_rect()
        background_rect.x=0;background_rect.y=0
        self.screen.blit(background,background_rect)
        self.screen.blit(self.font.render("Score : "+str(self.score), True, (255,255,0)), (20, 30))
        self.screen.blit(self.font.render("Level  : "+str(self.level), True, (255,255,0)), (20, 0))
        pygame.display.update()

    #jalannya ular
    def Running(self):
         self.game_init()
         x_change = segment_width + segment_margin
         y_change = 0
         while self.done != True :
             for event in pygame.event.get():
                 if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_LEFT:
                         x_change = (segment_width + segment_margin) * -1
                         y_change = 0
                     if event.key == pygame.K_RIGHT:
                         x_change = (segment_width + segment_margin) 
                         y_change = 0
                     if event.key == pygame.K_UP:
                         x_change = 0
                         y_change = (segment_height + segment_margin) * -1
                     if event.key == pygame.K_DOWN:
                         x_change = 0
                         y_change = (segment_height + segment_margin) 
             self.snake.move(x_change, y_change)
             #Draw everything
             #Clear screen
             self.screen.fill(WHITE)
             if self.level == 2 :
                 self.wall.Wall2(self.screen)
             if self.level == 3 :
                 self.wall.Wall2(self.screen)
                 self.wall.Wall1(self.screen)
                 
             if self.level == 4 :
                 self.wall.Wall2(self.screen)
                 self.wall.Wall1(self.screen)
                 self.wall.Wall3(self.screen)
            
                 
             self.scoreBoard()
             self.snake.allspriteslist.draw(self.screen)
             self.food.draw(self.screen)
             if self.score >= 4 :
                 self.level = 2
             if self.score >= 6 :
                 self.level = 3
             elif self.score >= 10 :
                 self.level = 4
             #Flip screen
             pygame.display.flip()
             pygame.display.update()
             #Eating food
             if self.snake.collides(self.food):
                 #self.eat_sound.play()
                 self.score += 1
                 self.snake.grow()
                 self.food.spawn()
             #Snake Hit it self
             if self.snake.collides_any(self.snake.Buntut()) :
                print('lose')
                self.done = True
             xnew = self.snake.snake_segments[0].rect.x+x_change
             ynew =self.snake.snake_segments[0].rect.y+y_change 
             if self.wall.cekColl(xnew,ynew,self.level):
                print('lose')
                self.done = True
             #Pause
             self.clock.tick(6)
         self.restart()

    def restart(self):
        background = pygame.image.load('rumput.jpg').convert()
        background_rect = background.get_rect()
        background_rect.x=0;background_rect.y=200
        self.screen.blit(background,background_rect)
        ScoreText = self.screen.blit(self.font.render("Score : "+str(self.score), True, (0,0,0)), (50, 200))
        ChoiceToRestart1 = self.screen.blit(self.font.render("Mau main lagi tekan : Y", True, (0,0,0)), (50, 250))
        ChoiceToRestart1 = self.screen.blit(self.font.render("Keluar tekan : N", True, (0,0,0)), (50, 300))
        pygame.display.update()
        end = True
        while end:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_y:
                             self.snake = Snake(2)
                             self.level = 1
                             self.score = 0
                             self.done = False
                             self.Running()
                         if event.key == pygame.K_n:
                             pygame.quit()
            self.clock.tick(6)
            
        
game = APP()
game.Running()
