import pygame, sys
import random

pygame.init()

WIDTH,HEIGHT=1200,600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MyChoo")

#Update image
Login_image = pygame.image.load("Mychoo/Login.png")

FB = pygame.image.load("Mychoo/Facebook.png")
FB = pygame.transform.scale(FB,(45 ,45)) 

GG= pygame.image.load("Mychoo/Google.png")
GG = pygame.transform.scale(GG,(40 ,40)) 

BG = pygame.image.load("Mychoo/Mainmenu.png")

profile_image = pygame.image.load("Mychoo/Profile.png")

answers_image = pygame.image.load("Mychoo/Answers.png")

admissions_image = pygame.image.load("Mychoo/Uni.png")

more_image = pygame.image.load("Mychoo/More.png")

icon = pygame.image.load("Mychoo/Icon.png")
icon= pygame.transform.scale(icon, (180, 180))

back = pygame.image.load("Mychoo/Back.png")
back = pygame.transform.scale(back, (50, 50))

image=pygame.image.load("Mychoo/Quit Rect.png")
image = pygame.transform.scale(image,(200, 55))

add = pygame.image.load("Mychoo/Add.png")
add = pygame.transform.scale(add,(52, 56))

tube1_image = pygame.image.load("Mychoo/1.png")
tube2_image = pygame.image.load("Mychoo/2.png")
tube3_image = pygame.image.load("Mychoo/3.png")

find_image = pygame.image.load("Mychoo/Find.png")

banner = pygame.image.load("Mychoo/Banner.png")

m1 = pygame.image.load("Mychoo/M1.png")
m2 = pygame.image.load("Mychoo/M2.png")
m3 = pygame.image.load("Mychoo/M3.png")

fb_image= pygame.image.load("Mychoo/Feedback.png")

running = True
class Button():
   def __init__(self, image, pos, text_input, font, base_color, hovering_color):
      self.image = image
      self.x_pos = pos[0]
      self.y_pos = pos[1]
      self.font = font
      self.base_color, self.hovering_color = base_color, hovering_color
      self.text_input = text_input
      self.text = self.font.render(self.text_input, True, self.base_color)
      if self.image is None:
         self.image = self.text
      self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
      self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

   def update(self, screen):
      if self.image is not None:
         screen.blit(self.image, self.rect)
      screen.blit(self.text, self.text_rect)

   def checkForInput(self, position):
      if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
         return True
      return False

   def changeColor(self, position):
      if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
         self.text = self.font.render(self.text_input, True, self.hovering_color)
      else:
         self.text = self.font.render(self.text_input, True, self.base_color)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("BreeSerif.otf", size)
#Trang cá nhân
def Profile():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(profile_image,(0,0))
        BACK_BUTTON = Button(image=back, pos=(1170, 30), 
                            text_input="", font=get_font(25), base_color="White", hovering_color="Green")
        EXIT_BUTTON = Button(image=None, pos=(60, 580), 
                            text_input="Đăng Xuất", font=get_font(25), base_color="Red", hovering_color="White")

        for button in [BACK_BUTTON, EXIT_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Main_menu()
                if EXIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Login()
        pygame.display.update()
# Chức năng chia sẻ
def Share():
    while True:
        SHARE_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(banner,(0,0))
        screen.blit(tube1_image,(0,125))
        BACK = Button(image=back, pos=(1160, 35), 
                            text_input="", font=get_font(25), base_color="Black", hovering_color="Red")
        BAC = Button(image=None, pos=(260, 110), 
                          text_input="MIỀN BẮC", font=get_font(25), base_color="Black", hovering_color="Red")
        TRUNG = Button(image=None, pos=(600, 110), 
                            text_input="MIỀN TRUNG", font=get_font(25), base_color="Black", hovering_color="Red")
        NAM = Button(image=None, pos=(910, 110), 
                            text_input="MIỀN NAM", font=get_font(25), base_color="Black", hovering_color="Red")
    
        for button in [BACK, BAC,TRUNG , NAM]:
            button.changeColor(SHARE_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(SHARE_MOUSE_POS):
                    Main_menu()
                if  BAC.checkForInput(SHARE_MOUSE_POS):
                    North()
                if  TRUNG.checkForInput(SHARE_MOUSE_POS):
                    Centralregion()  
                if  NAM.checkForInput(SHARE_MOUSE_POS):
                    Southern()               
        pygame.display.update()
#Miền bắc       
def North():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(banner,(0,0))
        screen.blit(tube1_image,(0,125))
        BACK_BUTTON = Button(image=back, pos=(1160, 30), 
                            text_input="", font=get_font(25), base_color="White", hovering_color="Green")
        BAC = Button(image=None, pos=(260, 110), 
                          text_input="MIỀN BẮC", font=get_font(25), base_color="Black", hovering_color="Red")
        TRUNG = Button(image=None, pos=(600, 110), 
                            text_input="MIỀN TRUNG", font=get_font(25), base_color="Black", hovering_color="Red")
        NAM = Button(image=None, pos=(910, 110), 
                            text_input="MIỀN NAM", font=get_font(25), base_color="Black", hovering_color="Red")
        FEEDBACK = Button(image=None, pos=(600,200), 
                            text_input="            ", font=get_font(25), base_color="Black", hovering_color="Red")
        for button in [BACK_BUTTON,BAC, TRUNG ,NAM,FEEDBACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Main_menu()
                if NAM.checkForInput(PLAY_MOUSE_POS):
                    Southern()
                if TRUNG.checkForInput(PLAY_MOUSE_POS):
                    Centralregion()
                if FEEDBACK.checkForInput(PLAY_MOUSE_POS):
                    Feedback()
                         
        pygame.display.update()
#Miền Trung
def Centralregion():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(banner,(0,0))
        screen.blit(tube2_image,(0,125))
        BACK_BUTTON = Button(image=back, pos=(1160, 30), 
                            text_input="", font=get_font(25), base_color="White", hovering_color="Green")
        BAC = Button(image=None, pos=(260, 110), 
                          text_input="MIỀN BẮC", font=get_font(25), base_color="Black", hovering_color="Red")
        TRUNG = Button(image=None, pos=(600, 110), 
                            text_input="MIỀN TRUNG", font=get_font(25), base_color="Black", hovering_color="Red")
        NAM = Button(image=None, pos=(910, 110), 
                            text_input="MIỀN NAM", font=get_font(25), base_color="Black", hovering_color="Red")
        for button in [BACK_BUTTON,BAC, TRUNG ,NAM ]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Main_menu()
                if BAC.checkForInput(PLAY_MOUSE_POS):
                    North()
                if NAM.checkForInput(PLAY_MOUSE_POS):
                    Southern()

        pygame.display.update()
#Miền Nam
def Southern():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(banner,(0,0))
        screen.blit(tube3_image,(0,125))
        BACK_BUTTON = Button(image=back, pos=(1160, 30), 
                            text_input="", font=get_font(25), base_color="White", hovering_color="Green")
        BAC = Button(image=None, pos=(260, 110), 
                          text_input="MIỀN BẮC", font=get_font(25), base_color="Black", hovering_color="Red")
        TRUNG = Button(image=None, pos=(600, 110), 
                            text_input="MIỀN TRUNG", font=get_font(25), base_color="Black", hovering_color="Red")
        NAM = Button(image=None, pos=(910, 110), 
                            text_input="MIỀN NAM", font=get_font(25), base_color="Black", hovering_color="Red")
        for button in [BACK_BUTTON, BAC,TRUNG ,NAM ]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Main_menu()
                if TRUNG.checkForInput(PLAY_MOUSE_POS):
                    Centralregion()
                if BAC.checkForInput(PLAY_MOUSE_POS):
                    North()
        pygame.display.update()
#Cảm nhận:
def Feedback():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(fb_image,(0,0))
        BACK_BUTTON = Button(image=back, pos=(1160, 30), 
                            text_input="", font=get_font(25), base_color="White", hovering_color="Green")       
        for button in [BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Share()            
        pygame.display.update()                       
def Admissions():
    while True:       
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(admissions_image,(0,0))       
        BACK = Button(image=back, pos=(1160,30), 
                            text_input="", font=get_font(75), base_color="Black", hovering_color="Green")
        FIND = Button(image=None, pos=(1040,80), 
                            text_input=" ", font=get_font(75), base_color="Red", hovering_color="Yellow")
        for button in [ BACK,FIND]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  BACK.checkForInput(PLAY_MOUSE_POS):
                    Main_menu()
                if  FIND.checkForInput(PLAY_MOUSE_POS):
                    Find()
        pygame.display.update()
#Tìm kiếm thông tin:
def Find():
    while True:        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(find_image,(600,0))        
        BACK = Button(image=None, pos=(630,30), 
                            text_input="Back", font=get_font(25), base_color="Black", hovering_color="Red")        
        for button in [BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  BACK.checkForInput(PLAY_MOUSE_POS):
                    Admissions()
        pygame.display.update()
#Hỏi đáp
def Answers():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(answers_image, (0, 0))
        BACK = Button(image=back, pos=(1160, 30), 
                            text_input="", font=get_font(25), base_color="Black", hovering_color="Green")
        SENT = Button(image=None, pos=(175, 145), 
                            text_input="ĐÃ GỬI", font=get_font(25), base_color="Black", hovering_color="Red")
        PROCESSING = Button(image=None, pos=(425, 145), 
                            text_input="ĐANG XỬ LÍ", font=get_font(25), base_color="Black", hovering_color="Yellow")
        SUCCESS = Button(image=None, pos=(625, 145), 
                            text_input="Đã xử lí", font=get_font(25), base_color="Black", hovering_color="Green")
        for button in [BACK,SENT, PROCESSING,SUCCESS]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(PLAY_MOUSE_POS):
                    Main_menu()

        pygame.display.update()
#Các tiện ích khác:
def More():
    while True:
        MORE_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(more_image, (0, 0))      
        BACK = Button(image=back, pos=(1160, 30), 
                            text_input="", font=get_font(45), base_color="Black", hovering_color="Red")
        SHOPPING = Button(image=None, pos=(295,125), 
                            text_input="MUA SẮM", font=get_font(30), base_color="Black", hovering_color="Red")
        RELAX = Button(image=None, pos=(590,125), 
                            text_input="GIẢI TRÍ", font=get_font(30), base_color="Black", hovering_color="Red")
        MORE = Button(image=None, pos=(920,125), 
                            text_input="TIỆN ÍCH", font=get_font(30), base_color="Black", hovering_color="Red")
        M1 = Button(image=add, pos=(345,380), 
                            text_input="     ", font=get_font(30), base_color="Black", hovering_color="Red")
        M2 = Button(image=add, pos=(655,385), 
                            text_input="     ", font=get_font(30), base_color="Black", hovering_color="Red")
        M3 = Button(image=add, pos=(980,385), 
                            text_input="      ", font=get_font(30), base_color="Black", hovering_color="Red")
        for button in [BACK, SHOPPING,RELAX,MORE, M1, M2,M3]:
            button.changeColor(MORE_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MORE_MOUSE_POS):
                    Main_menu()
                if M1.checkForInput(MORE_MOUSE_POS):
                    Mone()
                if M2.checkForInput(MORE_MOUSE_POS):
                    Mtwo()
                if M3.checkForInput(MORE_MOUSE_POS):
                    Mthree()
        pygame.display.update()

def Mone():
    while True:
        MORE_MOUSE_POS = pygame.mouse.get_pos()
        
        screen.blit(m1, (390, 100))      
        BACK = Button(image=None, pos=(430, 125), 
                            text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Red")
       
        for button in [BACK]:
            button.changeColor(MORE_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MORE_MOUSE_POS):
                    More()

        pygame.display.update()

def Mtwo():
    while True:
        MORE_MOUSE_POS = pygame.mouse.get_pos()
        
        screen.blit(m2, (700, 100))      
        BACK = Button(image=None, pos=(735, 125), 
                            text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Red")   

        for button in [BACK]:
            button.changeColor(MORE_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MORE_MOUSE_POS):
                    More()

        pygame.display.update()

def Mthree():
    while True:
        MORE_MOUSE_POS = pygame.mouse.get_pos()
        
        screen.blit(m3, (715, 100))      
        BACK = Button(image=None, pos=(750, 125), 
                            text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Red")

        for button in [BACK]:
            button.changeColor(MORE_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MORE_MOUSE_POS):
                    More()

        pygame.display.update()
#Màn hình chính:
def Main_menu():
    while True:
        screen.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(60).render("MYCHOO", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(630, 85))

        PROFILE_BUTTON = Button(image=icon, pos=(170, 135), 
                            text_input="", font=get_font(25), base_color="#d7fcd4", hovering_color="Green")
        SHARE_BUTTON = Button(image=image, pos=(170, 270), 
                            text_input="CHIA SẺ", font=get_font(25), base_color="#d7fcd4", hovering_color="Yellow")
        ADMISSIONS_BUTTON = Button(image=image, pos=(170, 350), 
                            text_input="TUYỂN SINH", font=get_font(25), base_color="#d7fcd4", hovering_color="Brown")
        MORE_BUTTON = Button(image=image, pos=(170, 430), 
                            text_input="KHÁM PHÁ", font=get_font(25), base_color="#d7fcd4", hovering_color="Red")
        ANSWERS_BUTTON = Button(image=image, pos=(170, 510), 
                            text_input="HỎI ĐÁP", font=get_font(25), base_color="#d7fcd4", hovering_color="Pink")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [SHARE_BUTTON, ADMISSIONS_BUTTON, MORE_BUTTON,ANSWERS_BUTTON,PROFILE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PROFILE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Profile()
                if SHARE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Share()
                if ADMISSIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Admissions()
                if ANSWERS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Answers()
                if MORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    More()                  
        pygame.display.update()
#Trang chủ    
def Login():
    while True:
        screen.blit(Login_image, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        TINTUC = Button(image=None, pos=(200, 35), 
                            text_input="Tin Tức", font=get_font(35), base_color="Black", hovering_color="Red")
        KIENTHUC = Button(image=None, pos=(400, 35), 
                            text_input="Kiến Thức", font=get_font(35), base_color="Black", hovering_color="Red")
        HOTRO = Button(image=None, pos=(600, 35), 
                            text_input="Hỗ Trợ", font=get_font(35), base_color="Black", hovering_color="Red")
        KIENTHUC = Button(image=None, pos=(400, 35), 
                            text_input="Kiến Thức", font=get_font(35), base_color="Black", hovering_color="Red")
        FACEBOOK_BUTTON = Button(image=FB, pos=(910, 485), 
                            text_input=None, font=get_font(25), base_color="#d7fcd4", hovering_color="Green")
        GOOGLE_BUTTON = Button(image=GG, pos=(990, 486), 
                            text_input=None, font=get_font(25), base_color="#d7fcd4", hovering_color="Yellow")
        LOGIN_BUTTON = Button(image=None, pos=(960, 413), 
                            text_input="Đăng Nhập", font=get_font(25), base_color="#d7fcd4", hovering_color="Red")
        SIGNUP_BUTTON = Button(image=None, pos=(1080, 35), 
                            text_input="Đăng Kí", font=get_font(25), base_color="#d7fcd4", hovering_color="Blue")
        for button in [FACEBOOK_BUTTON,GOOGLE_BUTTON,LOGIN_BUTTON, SIGNUP_BUTTON,TINTUC,KIENTHUC,HOTRO]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FACEBOOK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Main_menu()
                if GOOGLE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Main_menu()
                if LOGIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Main_menu()          
        pygame.display.update()

if __name__ == '__main__':
        Login()