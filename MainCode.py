import pygame
import time

pygame.init()
ekran_genislik = 1280
ekran_yukseklik = 720
ekranOlcusu = pygame.display.set_mode((ekran_genislik,ekran_yukseklik))
pygame.display.set_caption("ARXOST")
clock = pygame.time.Clock()
### PLATFORM ###
platform1_genislik=128
platform1_yukseklik=93
platform1_sol = pygame.image.load(r"Texture_Paketi\Tiles\13.png")
platform1_orta = pygame.image.load(r"Texture_Paketi\Tiles\14.png")
platform1_sag = pygame.image.load(r"Texture_Paketi\Tiles\15.png")
#####################################################################

### OBJELER ###



enemy1_1=pygame.image.load(r"Texture_Paketi_3\PNG\Enemies\enemyFlying_1.png")
enemy1_3=pygame.image.load(r"Texture_Paketi_3\PNG\Enemies\enemyFlying_3.png")
enemy1_max_sprite =2
enemy1_current_sprite=0


karakter_current_sprite = 0
karakter_saf = pygame.image.load(r"Esyalar\minus.png")
karakter_saf=pygame.transform.smoothscale(karakter_saf,(50,50))
karakter_seker = pygame.image.load(r"Esyalar\seker.png")
karakter_seker=pygame.transform.smoothscale(karakter_seker,(50,50))

oklu_levha = pygame.image.load(r"Texture_Paketi\Object\Sign_2.png")
oklu_levha=pygame.transform.smoothscale(oklu_levha,(93,96))
oklu_levha_yazisi_1 = pygame.image.load(r"Yazilar\oklu_tabela_yazisi_1.png")
oklu_levha_yazisi_1=pygame.transform.scale(oklu_levha_yazisi_1,(128,64))
agac0 = pygame.image.load(r"Texture_Paketi\Object\Tree_2.png")
sapka = pygame.image.load(r"Esyalar\witcher_hat.png")
sapka=pygame.transform.smoothscale(sapka,(64,64))
sapka2 = pygame.image.load(r"Esyalar\sapka.png")

kalp = pygame.image.load(r"Esyalar\kalp.png")
kalp=pygame.transform.smoothscale(kalp,(64,64))
agac1 = pygame.image.load(r"Texture_Paketi_2\PNG\Default size\foliagePack_022.png")
agac1=pygame.transform.smoothscale(agac1,(84,276))
kazan = pygame.image.load(r"Texture_Paketi\Object\kazan.png")
kazan=pygame.transform.smoothscale(kazan,(100,100))
ot = pygame.image.load(r"Texture_Paketi\Object\Bush (3).png")
ot=pygame.transform.smoothscale(ot,(120,70))
kesik_agac = pygame.image.load(r"Texture_Paketi\Object\Tree_1.png")



ev = pygame.image.load(r"Esyalar\ev.png")
ev=pygame.transform.smoothscale(ev,(300,300))

patlama = pygame.image.load(r"Esyalar\patlama.png")
patlama=pygame.transform.smoothscale(patlama,(210,270))

portal = pygame.image.load(r"Esyalar\Portal.png")
#patlama=pygame.transform.smoothscale(patlama,(134,140))
#toprak1 = pygame.image.load(r"Texture_Paketi_2\PNG\Default size\Leaves\foliagePack_leaves_010.png")
tas1 = pygame.image.load(r"Ground&Stone\Stone\tas1.png")
####################################################################
platform1_sag=pygame.transform.scale(platform1_sag,(int(platform1_genislik/1.2),int(platform1_yukseklik/1.2)))
platform1_orta=pygame.transform.scale(platform1_orta,(int(platform1_genislik/1.2),int(platform1_yukseklik/1.2)))
platform1_sol=pygame.transform.scale(platform1_sol,(int(platform1_genislik/1.2),int(platform1_yukseklik/1.2)))

arkaplan_uzay=pygame.image.load(r"Arkaplanlar\background5.jpg")
arkaplan = pygame.image.load(r"Arkaplanlar\background4.jpg")
arkaplan_gece = pygame.image.load(r"Arkaplanlar\background2.png")
arkaplan_gece=pygame.transform.scale(arkaplan_gece,(1280,800))

cadi = pygame.image.load(r"Esyalar\witch.png")
cadi=pygame.transform.smoothscale(cadi,(134,140))
cadi = pygame.transform.flip(cadi, True, False)

karakter_sprite = pygame.image.load("Karakterler\ghost.png")
karakter_sprite_left = pygame.image.load("Karakterler\ghost_left.png")

karakter_sprite_left_hikaye = pygame.image.load("Karakterler\ghost_left.png")
karakter_sprite_left_hikaye=pygame.transform.smoothscale(karakter_sprite_left_hikaye,(50,50))
karakter_sprite_number = 29
karakter_current_sprite = 0

ters_animasyon=False
pygame.display.set_icon(karakter_saf)
sag=True
sol=False

bolum=1

#araba1=pygame.transform.rotate(araba1,-90)
karakter_genislik=105      #319
karakter_yukseklik= 107    #306

death_number=0

ucus_suresi=0

yazi_durum=0

can=3

yana_kayma_x = 0

mod='Yürüme (Not: Hayalet Modunda nesnelerin içinden geçebilirsiniz)'


def karakter(x,y,sag_yon):
    if sag_yon==True:
        ekranOlcusu.blit(karakter_sprite,(x,y),(karakter_current_sprite*karakter_genislik,0,karakter_genislik,karakter_yukseklik))
    else:
        ekranOlcusu.blit(karakter_sprite_left, (x, y),(karakter_current_sprite * karakter_genislik, 0, karakter_genislik, karakter_yukseklik))

def dikdortgen(dikdortgen_x,dikdortgen_y,dikdortgen_width,dikdortgen_height,dikdortgen_color):
    ekranOlcusu.blit(platform1_sol,(dikdortgen_x,dikdortgen_y))
    ekranOlcusu.blit(platform1_orta, (dikdortgen_x+platform1_genislik-27, dikdortgen_y))
    ekranOlcusu.blit(platform1_sag, (dikdortgen_x+platform1_genislik*2-54, dikdortgen_y))

def obje(obje_x,bolum_sec):
    global can
    if bolum_sec==1:
        ekranOlcusu.blit(oklu_levha, (50+obje_x, 236-32))
        ekranOlcusu.blit(oklu_levha_yazisi_1,(30+obje_x,236-22))
        ekranOlcusu.blit(agac0, (800+obje_x, 240))
        ekranOlcusu.blit(sapka, (1400+obje_x, 95))
    elif bolum_sec==2:
        ekranOlcusu.blit(sapka2, (900+obje_x, 150))
        ekranOlcusu.blit(portal, (2100 + obje_x, 0))
        ekranOlcusu.blit(sapka, (2200 + obje_x, 100))


    if can==3:
        ekranOlcusu.blit(kalp, (ekran_genislik-64, 0))
        ekranOlcusu.blit(kalp, (ekran_genislik-128, 0))
        ekranOlcusu.blit(kalp, (ekran_genislik - 192, 0))
    elif can==2:
        ekranOlcusu.blit(kalp, (ekran_genislik - 64, 0))
        ekranOlcusu.blit(kalp, (ekran_genislik - 128, 0))
    elif can==1:
        ekranOlcusu.blit(kalp, (ekran_genislik - 64, 0))
    elif can==0:
        can=3
        death()

white=(255, 255, 255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
sky_blue=(67,190,215)
pink=(255,20,147)

def death():
    pygame.mixer.music.load('Musics\Just Go(12).mp3')
    pygame.mixer.music.play(-1)
    global death_number
    death_number+=1
    mesaj("Oyun "+str(death_number)+" Kere Bitti")



def zipla_fonk():
    global ucus_suresi
    ucus_suresi+=1/30


def game_loop():

    kontrol=False

    global enemy1_max_sprite
    global enemy1_current_sprite

    global bolum
    global yana_kayma_x
    global obje_yana_kayma_x
    global can
    global mod
    global ucus_suresi
    global karakter_current_sprite
    global ters_animasyon

    global sag
    global sol
    ters_animasyon=False

    asansor_y=0

    zipla=False

    karakter_yon=1


    canavar_x=0
    canavar_x_degisimi = 0
    canavar_kontrol=False

    x_degisimi = 0
    y_degisimi=0
    yer_cekimi=0
    x = 0
    y = 0
    speed=6
    gameExit = False

    arkaplan_x=0

    dikdortgen_width = 310
    dikdortgen_height = 10
    dikdortgen1_x=0
    dikdortgen1_y =300

    obje_x=0

    while gameExit == False:  # False olduğu sürece:

        ### HAREKET MESELELERI ###

       if x < karakter_genislik/2:
           yana_kayma_x=0
           x=karakter_genislik/2

       if y <= 10 and bolum==2:
           y = 20


       if x > ekran_genislik-karakter_genislik / 1.5:
           yana_kayma_x = 0
           x = ekran_genislik-karakter_genislik / 1.5

       if canavar_kontrol==False:
           canavar_x_degisimi=8

       if canavar_x >= 250:
           canavar_kontrol=True
       if canavar_x <= -50:
           canavar_kontrol = False

       if canavar_kontrol==True:
           canavar_x_degisimi = -8

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()

           if event.type == pygame.KEYDOWN:

               if event.key == pygame.K_UP :
                   zipla=True

               if event.key == pygame.K_RIGHT :
                   if sol==True:
                       x += karakter_genislik / 2

                   if x < ekran_genislik - karakter_genislik / 1.5:
                       yana_kayma_x = -speed

                   x_degisimi = speed

               if event.key == pygame.K_LEFT:
                   if sag == True:
                       x -= karakter_genislik/2

                   if x > karakter_genislik / 2:

                       yana_kayma_x = speed


                   x_degisimi = -speed

           if event.type == pygame.KEYUP:

               if event.key == pygame.K_UP :
                   yana_kayma_x=0
                   ucus_suresi=0
                   zipla=False


               if event.key == pygame.K_RIGHT:
                   yana_kayma_x = 0
                   x_degisimi = 0
                   karakter_yon=1
               if event.key == pygame.K_LEFT:
                   yana_kayma_x = 0
                   x_degisimi = 0
                   karakter_yon=0
        ################################






       if zipla==True:
           yazi_durum=21
           mod='Hayalet Modu (Not: Hayalet Modunda nesnelerin içinden geçebilirsiniz)'
           zipla_fonk()
           y-=10
       elif zipla==False:
           yazi_durum = 0
           mod = 'Yürüme (Not: Hayalet Modunda nesnelerin içinden geçebilirsiniz)'

       if ucus_suresi>=0.5:
           zipla=False
       if bolum!=3:
           if sag==True and zipla==False and bolum==1:
               if y + karakter_yukseklik + 18 >= dikdortgen1_y and y + karakter_yukseklik < dikdortgen1_y and (
                       x  <= dikdortgen1_x + dikdortgen_width and x + (
                       karakter_genislik / 4) > dikdortgen1_x):
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 80 and y + karakter_yukseklik < dikdortgen1_y + 80 and (
                       x  <= dikdortgen1_x + 350 + dikdortgen_width and x + (
                       karakter_genislik / 4) > dikdortgen1_x + 350):
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 240 and y + karakter_yukseklik < dikdortgen1_y + 240 and (
                       x  <= dikdortgen1_x + 800 + dikdortgen_width and x + (
                       karakter_genislik / 4) > dikdortgen1_x + 800):
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 240 and y + karakter_yukseklik < dikdortgen1_y + 240 and (
                       x  <= dikdortgen1_x + 1500 + dikdortgen_width and x + (
                       karakter_genislik / 4) > dikdortgen1_x + 1500):
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 80 and y + karakter_yukseklik < dikdortgen1_y + 80 and (
                       x  <= dikdortgen1_x + 1600 + dikdortgen_width and x + (
                       karakter_genislik / 4) > dikdortgen1_x + 1600):
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 80-canavar_x/2 and y + karakter_yukseklik < dikdortgen1_y + 80-canavar_x/2 and (
                       x <= dikdortgen1_x + 1900 + dikdortgen_width and x + (
                       karakter_genislik / 4) > dikdortgen1_x + 1900):
                   asansor_y=8
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y -150 and y + karakter_yukseklik < dikdortgen1_y -150 and (
                       x  <= dikdortgen1_x + 1400 + dikdortgen_width and x + (
                       karakter_genislik / 4) > dikdortgen1_x + 1400):
                   y_degisimi = 0

               else:
                   y_degisimi += yer_cekimi
                   asansor_y = 0

           if sol==True and zipla==False and bolum==1:
               if y + karakter_yukseklik + 18 >= dikdortgen1_y and y + karakter_yukseklik < dikdortgen1_y and (
                       x + (karakter_genislik ) <= dikdortgen1_x + dikdortgen_width and x + (
                       karakter_genislik ) > dikdortgen1_x):
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 80 and y + karakter_yukseklik < dikdortgen1_y + 80 and (
                       x + (karakter_genislik ) <= dikdortgen1_x + 350 + dikdortgen_width and x + (
                       karakter_genislik ) > dikdortgen1_x + 350):
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 240 and y + karakter_yukseklik < dikdortgen1_y + 240 and (
                       x + (karakter_genislik ) <= dikdortgen1_x + 800 + dikdortgen_width and x + (
                       karakter_genislik ) > dikdortgen1_x + 800):
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 240 and y + karakter_yukseklik < dikdortgen1_y + 240 and (
                       x + (karakter_genislik ) <= dikdortgen1_x + 1500 + dikdortgen_width and x + (
                       karakter_genislik ) > dikdortgen1_x + 1500):
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 80 and y + karakter_yukseklik < dikdortgen1_y + 80 and (
                       x + (karakter_genislik ) <= dikdortgen1_x + 1600 + dikdortgen_width and x + (
                       karakter_genislik ) > dikdortgen1_x + 1600):
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 80-canavar_x/2 and y + karakter_yukseklik < dikdortgen1_y + 80-canavar_x/2 and (
                       x + (karakter_genislik ) <= dikdortgen1_x + 1900 + dikdortgen_width and x + (
                       karakter_genislik ) > dikdortgen1_x + 1900):
                   asansor_y = 8
                   y_degisimi = 0

               elif y + karakter_yukseklik + 18 >= dikdortgen1_y -150 and y + karakter_yukseklik < dikdortgen1_y -150 and (
                       x + (karakter_genislik ) <= dikdortgen1_x + 1400 + dikdortgen_width and x + (
                       karakter_genislik ) > dikdortgen1_x + 1400):
                   y_degisimi = 0


               else:
                   y_degisimi += yer_cekimi
                   asansor_y=0

           if sag == True and zipla == False and bolum == 2:
                if y + karakter_yukseklik + 18 >= dikdortgen1_y  and y + karakter_yukseklik < dikdortgen1_y  and (
                        x <= dikdortgen1_x + dikdortgen_width and x + (
                        karakter_genislik / 4) > dikdortgen1_x):
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y - 80 and y + karakter_yukseklik < dikdortgen1_y - 80 and (
                        x <= dikdortgen1_x + 350 + dikdortgen_width and x + (
                        karakter_genislik / 4) > dikdortgen1_x + 350):
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 140 and y + karakter_yukseklik < dikdortgen1_y + 140 and (
                        x <= dikdortgen1_x + 600 + dikdortgen_width and x + (
                        karakter_genislik / 4) > dikdortgen1_x + 600):
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y  and y + karakter_yukseklik < dikdortgen1_y  and (
                        x <= dikdortgen1_x + 900 + dikdortgen_width and x + (
                        karakter_genislik / 4) > dikdortgen1_x + 900):
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 150 and y + karakter_yukseklik < dikdortgen1_y + 150 and (
                        x <= dikdortgen1_x + 1400 + dikdortgen_width and x + (
                        karakter_genislik / 4) > dikdortgen1_x + 1400):
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y  -20 - canavar_x / 2 and y + karakter_yukseklik < dikdortgen1_y -20 - canavar_x / 2 and (
                        x <= dikdortgen1_x + 1900 + dikdortgen_width and x + (
                        karakter_genislik / 4) > dikdortgen1_x + 1900):
                    asansor_y = 8
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y  and y + karakter_yukseklik < dikdortgen1_y  and (
                        x <= dikdortgen1_x + 1600 + dikdortgen_width and x + (
                        karakter_genislik / 4) > dikdortgen1_x + 1600):
                    y_degisimi = 0

                else:
                    y_degisimi += yer_cekimi
                    asansor_y = 0

           if sol == True and zipla == False and bolum == 2:
                if y + karakter_yukseklik + 18 >= dikdortgen1_y  and y + karakter_yukseklik < dikdortgen1_y  and (
                        x + (karakter_genislik) <= dikdortgen1_x + dikdortgen_width and x + (
                        karakter_genislik) > dikdortgen1_x):
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y - 80 and y + karakter_yukseklik < dikdortgen1_y - 80 and (
                        x + (karakter_genislik) <= dikdortgen1_x + 350 + dikdortgen_width and x + (
                        karakter_genislik) > dikdortgen1_x + 350):
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 140 and y + karakter_yukseklik < dikdortgen1_y + 440 and (
                        x + (karakter_genislik) <= dikdortgen1_x + 600 + dikdortgen_width and x + (
                        karakter_genislik) > dikdortgen1_x + 600):
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y  and y + karakter_yukseklik < dikdortgen1_y  and (
                        x + (karakter_genislik) <= dikdortgen1_x + 900 + dikdortgen_width and x + (
                        karakter_genislik) > dikdortgen1_x + 900):
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y + 150 and y + karakter_yukseklik < dikdortgen1_y + 150 and (
                        x + (karakter_genislik) <= dikdortgen1_x + 1400 + dikdortgen_width and x + (
                        karakter_genislik) > dikdortgen1_x + 1400):
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y  -20 - canavar_x / 2 and y + karakter_yukseklik < dikdortgen1_y -20 - canavar_x / 2 and (
                        x + (karakter_genislik) <= dikdortgen1_x + 1900 + dikdortgen_width and x + (
                        karakter_genislik) > dikdortgen1_x + 1900):
                    asansor_y = 8
                    y_degisimi = 0

                elif y + karakter_yukseklik + 18 >= dikdortgen1_y  and y + karakter_yukseklik < dikdortgen1_y  and (
                        x + (karakter_genislik) <= dikdortgen1_x + 1600 + dikdortgen_width and x + (
                        karakter_genislik) > dikdortgen1_x + 1600):
                    y_degisimi = 0


                else:
                    y_degisimi += yer_cekimi
                    asansor_y = 0
            #############################
       dikdortgen1_x+=yana_kayma_x
       obje_x+=yana_kayma_x
       y+= y_degisimi-asansor_y
       x += x_degisimi
       print(x,",",y)

       arkaplan_x+=yana_kayma_x
       canavar_x+=canavar_x_degisimi





    ############################
       if bolum == 1:
           yer_cekimi=1
           ekranOlcusu.blit(arkaplan, (arkaplan_x + yana_kayma_x, 0))
           if y <= 50 and round(x, -1) == 730:
               bolum = 2

               mesaj("Bölüm 1 Tamamlandı ! ")

           if enemy1_current_sprite < enemy1_max_sprite and kontrol==False:
               enemy1_current_sprite = enemy1_current_sprite+1

           if enemy1_current_sprite == enemy1_max_sprite:
               kontrol = True

           if kontrol==True:
               enemy1_current_sprite = enemy1_current_sprite - 1

           if enemy1_current_sprite == 0:
               kontrol = False



           dikdortgen(dikdortgen1_x, dikdortgen1_y, dikdortgen_width, dikdortgen_height, blue)
           dikdortgen(dikdortgen1_x+350, dikdortgen1_y+80, dikdortgen_width, dikdortgen_height, blue)
           dikdortgen(dikdortgen1_x + 800, dikdortgen1_y + 240, dikdortgen_width, dikdortgen_height, blue)
           dikdortgen(dikdortgen1_x + 1500, dikdortgen1_y + 240, dikdortgen_width, dikdortgen_height, blue)
           dikdortgen(dikdortgen1_x + 1600, dikdortgen1_y +80, dikdortgen_width, dikdortgen_height, blue)
           dikdortgen(dikdortgen1_x + 1900, dikdortgen1_y + 80-canavar_x/2, dikdortgen_width, dikdortgen_height, blue)
           dikdortgen(dikdortgen1_x + 1400, dikdortgen1_y -150 , dikdortgen_width, dikdortgen_height, blue)
           obje(obje_x,1)

           if  enemy1_current_sprite==0:
               ekranOlcusu.blit(enemy1_1, (dikdortgen1_x + 830 + yana_kayma_x + canavar_x, dikdortgen1_y + 160))
           elif enemy1_current_sprite==1 :
               ekranOlcusu.blit(enemy1_3, (dikdortgen1_x + 830 + yana_kayma_x + canavar_x, dikdortgen1_y + 160))



           if round(int(x), -2) == round(dikdortgen1_x + 830 + yana_kayma_x + canavar_x, -2) and round(int(y),-2) == round(dikdortgen1_y + 100, -2):
               can -= 1
               mesaj('GEBERDIN')
               time.sleep(1)
               game_loop()


           durum_mesaji("Mod : "+mod,280+yazi_durum,20,black,16)

        ### KARAKTER YUZ YONU ###
           if 0 < x_degisimi:
               sag=True
               sol=False
               karakter(x, y,True)
           elif  0 > x_degisimi:
               sol=True
               sag=False
               karakter(x, y, False)
           elif karakter_yon==1:
               sag = True
               sol = False
               karakter(x, y, True)
           elif karakter_yon == 0:
               sol = True
               sag = False
               karakter(x, y, False)
    ############################
       if bolum == 2:
           yer_cekimi=1
           ekranOlcusu.blit(arkaplan_uzay, (arkaplan_x + yana_kayma_x, 0))
           obje(obje_x, 2)
           if  y>=70 and round(x, -1) >= 1100:
               bolum = 3
               bolumSonu()

               #########################################################


               hikaye1("Ve ihtiyar büyücüyle Minuslar sonsuza kadar mutlu yaşadılar.. ", ekran_genislik / 2, 200,white, 22)
               ekranOlcusu.blit(ev, (ekran_genislik / 2 - 500, ekran_yukseklik / 2 - 65))

           if enemy1_current_sprite < enemy1_max_sprite and kontrol == False:
               enemy1_current_sprite = enemy1_current_sprite + 1

           if enemy1_current_sprite == enemy1_max_sprite:
               kontrol = True

           if kontrol == True:
               enemy1_current_sprite = enemy1_current_sprite - 1

           if enemy1_current_sprite == 0:
               kontrol = False

           if bolum!=3:
               dikdortgen(dikdortgen1_x, dikdortgen1_y, dikdortgen_width, dikdortgen_height, blue)
               dikdortgen(dikdortgen1_x + 350, dikdortgen1_y + -80, dikdortgen_width, dikdortgen_height, blue)
               dikdortgen(dikdortgen1_x + 600, dikdortgen1_y + 140, dikdortgen_width, dikdortgen_height, blue)
               dikdortgen(dikdortgen1_x + 900, dikdortgen1_y , dikdortgen_width, dikdortgen_height, blue)
               dikdortgen(dikdortgen1_x + 1400, dikdortgen1_y + 150, dikdortgen_width, dikdortgen_height, blue)
               dikdortgen(dikdortgen1_x + 1900, dikdortgen1_y - 20 - canavar_x / 2, dikdortgen_width, dikdortgen_height,blue)
               dikdortgen(dikdortgen1_x + 1600, dikdortgen1_y , dikdortgen_width, dikdortgen_height, blue)




               if enemy1_current_sprite == 0:
                   ekranOlcusu.blit(enemy1_1, (dikdortgen1_x + 1400 + yana_kayma_x + canavar_x, dikdortgen1_y + 55))
               elif enemy1_current_sprite == 1:
                   ekranOlcusu.blit(enemy1_3, (dikdortgen1_x + 1400 + yana_kayma_x + canavar_x, dikdortgen1_y + 55))


               if enemy1_current_sprite == 0:
                   ekranOlcusu.blit(enemy1_1, (dikdortgen1_x + 1130 + yana_kayma_x - canavar_x, dikdortgen1_y -100))
               elif enemy1_current_sprite == 1:
                   ekranOlcusu.blit(enemy1_3, (dikdortgen1_x + 1130 + yana_kayma_x - canavar_x, dikdortgen1_y -100))

               durum_mesaji("Mod : " + mod, 280 + yazi_durum, 20, black, 16)

               ### KARAKTER YUZ YONU ###
               if 0 < x_degisimi:
                   sag = True
                   sol = False
                   karakter(x, y, True)
               elif 0 > x_degisimi:
                   sol = True
                   sag = False
                   karakter(x, y, False)
               elif karakter_yon == 1:
                   sag = True
                   sol = False
                   karakter(x, y, True)
               elif karakter_yon == 0:
                   sol = True
                   sag = False
                   karakter(x, y, False)

               if round(int(x), -2) == round(dikdortgen1_x + 1404 + yana_kayma_x + canavar_x, -2) and round(int(y),
                                                                                                            -2) == round(
                       dikdortgen1_y + 20, -2):
                   can -= 1
                   mesaj('GEBERDIN')
                   time.sleep(1)
                   game_loop()

               if round(int(x), -2) == round(dikdortgen1_x + 1134 + yana_kayma_x - canavar_x, -2) and round(int(y),
                                                                                                            -2) == round(
                       178, -2):
                   can -= 1
                   mesaj('GEBERDIN')
                   time.sleep(1)
                   game_loop()


       if karakter_sprite_number == karakter_current_sprite:

           ters_animasyon=True

       if ters_animasyon==True and karakter_current_sprite !=0:
           karakter_current_sprite -=1
       else:
           karakter_current_sprite+=1
           ters_animasyon=False

           ### COLLISION MESELELERI ###
       if y > ekran_yukseklik:

           can -= 1
           mesaj('Hiçliğe Düştün..')
           clock.sleep(1)
           game_loop()



           ###############################




       pygame.display.update()  # Eğer içine bir şey yazılmazsa bütün surface  i yeniler
       clock.tick(30)  # FPS


def mesaj(text):
    font = pygame.font.Font('freesansbold.ttf', 96)
    fontRender = font.render( text, True, red)
    font_rect=fontRender.get_rect()
    font_rect.center=(ekran_genislik/2,ekran_yukseklik/2)
    ekranOlcusu.blit(fontRender,(font_rect))
    pygame.display.update()
    time.sleep(1)
    game_loop()

def durum_mesaji(text,x,y,renk,boyut):
    font = pygame.font.Font('freesansbold.ttf', boyut)
    fontRender = font.render( text, True, renk)
    font_rect=fontRender.get_rect()
    font_rect.center=(x,y)
    ekranOlcusu.blit(fontRender,(font_rect))

def hikaye1(text,x,y,renk,boyut):
    font = pygame.font.Font('freesansbold.ttf', boyut)
    fontRender = font.render( text, True, renk)
    font_rect=fontRender.get_rect()
    font_rect.center=(x,y)
    ekranOlcusu.blit(fontRender,(font_rect))

def bolum1():

    hikaye1("ARXOST : The Beginning", ekran_genislik / 2, ekran_yukseklik / 2, red, 64)

    pygame.mixer.music.load('Musics\Deniz.mp3')
    pygame.display.update()  # Eğer içine bir şey yazılmazsa bütün surface  i yeniler
    clock.tick(30)  # FPS
    time.sleep(0.5)
    yazi_sayac = 0
    pygame.mixer.music.play(-1)

    while 1:

        ekranOlcusu.blit(arkaplan_gece, (0, -50))

        ## OBJELER ##
        ekranOlcusu.blit(agac1, (ekran_genislik / 2, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 - 300, ekran_yukseklik - 385))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 - 150, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 - 600, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 - 400, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 - 500, ekran_yukseklik - 385))

        ekranOlcusu.blit(agac1, (ekran_genislik / 2 + 300, ekran_yukseklik - 385))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 + 150, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 + 600, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 + 400, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 + 500, ekran_yukseklik - 385))


        ekranOlcusu.blit(ot, (-20, ekran_yukseklik - 200))
        ekranOlcusu.blit(ot, (ekran_genislik - 50, ekran_yukseklik - 200))

        ########################################################

        ## OBJELER ##
        ekranOlcusu.blit(agac1, (ekran_genislik / 2, ekran_yukseklik - 405))

        ekranOlcusu.blit(ot, (-20, ekran_yukseklik - 200))
        ekranOlcusu.blit(ot, (ekran_genislik - 50, ekran_yukseklik - 200))

        ########################################################

        ## ZEMIN DIZAYNI ##
        ekranOlcusu.blit(platform1_orta, (0, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (105, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (210, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (315, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (420, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (525, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (630, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (735, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (840, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (945, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (1050, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (1100, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (1175, ekran_yukseklik - 130))

        ekranOlcusu.blit(tas1, (-5, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (210, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (418, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (622, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (824, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (1026, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (1218, ekran_yukseklik - 111))

        ekranOlcusu.blit(kesik_agac, (150, ekran_yukseklik - 172))
        #########################################################
        ## HIKAYE ##
        if yazi_sayac == 0:
            ekranOlcusu.blit(kazan, (ekran_genislik / 2 - 100, ekran_yukseklik - 210))
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 - 200, ekran_yukseklik / 2 + 100))
            hikaye1("Dünyanın büyüyle yeni yeni tanışmaya başladığı zamanlarda.. (Geçmek için Boşluk tuşunu kullanın)", ekran_genislik / 2, 200, white, 22)

        elif yazi_sayac == 1:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 - 200, ekran_yukseklik / 2 + 100))
            ekranOlcusu.blit(kazan, (ekran_genislik / 2 - 100, ekran_yukseklik - 210))
            hikaye1("Bir Büyücü, yaşadığı ormandaki en yaşlı çınar ağacını büyüyle besliyordu..", ekran_genislik / 2,200, white, 22)

        elif yazi_sayac == 2:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 - 200, ekran_yukseklik / 2 + 100))
            ekranOlcusu.blit(kazan, (ekran_genislik / 2 - 100, ekran_yukseklik - 210))
            hikaye1("Fakat işler yolunda gitmedi..", ekran_genislik / 2, 200, white, 22)
            ekranOlcusu.blit(patlama, (ekran_genislik / 2 - 150, ekran_yukseklik/2))

        elif yazi_sayac == 3:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 - 200, ekran_yukseklik / 2 + 100))
            hikaye1("Ve aniden bir portal oluştu..", ekran_genislik / 2, 200, white, 22)
            ekranOlcusu.blit(portal, (ekran_genislik / 2 +300, ekran_yukseklik / 2))

        elif yazi_sayac == 4:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 - 200, ekran_yukseklik / 2 + 100))
            hikaye1("Büyücü anlamıştır işlerin ters gittiğini ve artık çok geçtir..", ekran_genislik / 2, 200, white, 22)
            ekranOlcusu.blit(portal, (ekran_genislik / 2 + 300, ekran_yukseklik / 2))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 250, ekran_yukseklik / 2+170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 280, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 180, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 210, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 320, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 350, ekran_yukseklik / 2 + 165))

        elif yazi_sayac == 5:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 - 200, ekran_yukseklik / 2 + 100))
            hikaye1("Ve portaldan Minus adında küçük ama güçlü büyü gücüne sahip hayaletler çıktı.. ", ekran_genislik / 2, 200, white,22)
            ekranOlcusu.blit(portal, (ekran_genislik / 2 + 300, ekran_yukseklik / 2))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 250, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 280, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 180, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 210, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 320, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 350, ekran_yukseklik / 2 + 165))

        elif yazi_sayac == 6:

            hikaye1("Büyücü Minus'lara evini açtı ve onlarla uzun bir süre yaşadı.. ",ekran_genislik / 2, 200, white, 22)
            ekranOlcusu.blit(ev, (ekran_genislik / 2-500 , ekran_yukseklik / 2-65))

        elif yazi_sayac == 7:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 , ekran_yukseklik / 2 + 100))
            ekranOlcusu.blit(ev, (ekran_genislik / 2 - 500, ekran_yukseklik / 2 - 65))
            ekranOlcusu.blit(kazan, (ekran_genislik / 2 + 100, ekran_yukseklik - 210))
            hikaye1("Minus'ların büyü gücüyle ormanı tekrar canlandırmak isteyen büyücü, bir deney yaptı..", ekran_genislik / 2, 200, white,22)
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 250, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 280, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 180, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 210, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 320, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 350, ekran_yukseklik / 2 + 165))

        elif yazi_sayac == 8:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 , ekran_yukseklik / 2 + 100))
            ekranOlcusu.blit(ev, (ekran_genislik / 2 - 500, ekran_yukseklik / 2 - 65))
            ekranOlcusu.blit(kazan, (ekran_genislik / 2 + 100, ekran_yukseklik - 210))
            hikaye1("Ancak Minus'lardan birinin burnu kaşındı ve deney çok ters gitti..", ekran_genislik / 2, 200, white,22)
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 250, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 280, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 180, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 210, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 320, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 350, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(patlama, (ekran_genislik / 2 + 50, ekran_yukseklik / 2))

        elif yazi_sayac == 9:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 , ekran_yukseklik / 2 + 100))
            ekranOlcusu.blit(ev, (ekran_genislik / 2 - 500, ekran_yukseklik / 2 - 65))
            ekranOlcusu.blit(kazan, (ekran_genislik / 2 + 100, ekran_yukseklik - 210))
            hikaye1("Hata sonucu Aynüd gezegeninden Nasni'ler gelmeye başladı..", ekran_genislik / 2, 200, white,22)
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 250, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 280, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 180, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 210, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 320, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 350, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(patlama, (ekran_genislik / 2 + 50, ekran_yukseklik / 2))
            ekranOlcusu.blit(portal, (ekran_genislik / 2 + 400, ekran_yukseklik / 2))
            ekranOlcusu.blit(enemy1_1, (ekran_genislik / 2 + 300, ekran_yukseklik / 2))
            ekranOlcusu.blit(enemy1_3, (ekran_genislik / 2 + 420, ekran_yukseklik / 2+50))

        elif yazi_sayac == 10:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 , ekran_yukseklik / 2 + 100))
            ekranOlcusu.blit(ev, (ekran_genislik / 2 - 500, ekran_yukseklik / 2 - 65))
            ekranOlcusu.blit(kazan, (ekran_genislik / 2 + 100, ekran_yukseklik - 210))
            hikaye1("Büyücünün seçeneği kalmamıştı..  Minus'ları hatalarını düzeltmeleri için Aynüd' hapsetti", ekran_genislik / 2, 200, white,22)
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 350, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 380, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 280, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 310, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 420, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 450, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(portal, (ekran_genislik / 2 + 400, ekran_yukseklik / 2))
            ekranOlcusu.blit(enemy1_3, (ekran_genislik / 2 + 330, ekran_yukseklik / 2+20))
            ekranOlcusu.blit(enemy1_1, (ekran_genislik / 2 + 450, ekran_yukseklik / 2+30))

        elif yazi_sayac == 11:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 , ekran_yukseklik / 2 + 100))
            ekranOlcusu.blit(ev, (ekran_genislik / 2 - 500, ekran_yukseklik / 2 - 65))
            ekranOlcusu.blit(kazan, (ekran_genislik / 2 + 100, ekran_yukseklik - 210))
            hikaye1("Ve hepsi bi anda Aynüd'e hapsoldular.. Büyücü yıkılmıştı.. Yine yalnızdı.. Ama Minus'lar için macera başlamıştı..", ekran_genislik / 2, 200, white,22)
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 450, ekran_yukseklik / 2 +200))


        elif yazi_sayac == 12:
            game_loop()
        ###############################################################

        pygame.display.update()  # Eğer içine bir şey yazılmazsa bütün surface  i yeniler
        clock.tick(30)  # FPS




        ### HAREKET MESELELERI ###

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    ekranOlcusu.blit(arkaplan_gece, (0, -50))



                    ## ZEMIN DIZAYNI ##
                    ekranOlcusu.blit(platform1_orta, (0, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (105, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (210, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (315, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (420, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (525, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (630, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (735, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (840, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (945, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (1050, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (1100, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (1175, ekran_yukseklik - 130))

                    ekranOlcusu.blit(tas1, (-5, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (210, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (418, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (622, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (824, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (1026, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (1218, ekran_yukseklik - 111))

                    ekranOlcusu.blit(kesik_agac, (150, ekran_yukseklik - 172))
                    #########################################################

                    ekranOlcusu.blit(cadi, (ekran_genislik / 2 - 200, ekran_yukseklik / 2 + 100))

                    yazi_sayac+=1


                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    pass

                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass

        ################################


def bolumSonu():
    pygame.mixer.music.load(r'Musics\twist.mp3')
    pygame.mixer.music.play(-1)
    yazi_sayac = 0

    while 1:

        ekranOlcusu.blit(arkaplan_gece, (0, -50))

        ## OBJELER ##
        ekranOlcusu.blit(agac1, (ekran_genislik / 2, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 - 300, ekran_yukseklik - 385))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 - 150, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 - 600, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 - 400, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 - 500, ekran_yukseklik - 385))

        ekranOlcusu.blit(agac1, (ekran_genislik / 2 + 300, ekran_yukseklik - 385))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 + 150, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 + 600, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 + 400, ekran_yukseklik - 405))
        ekranOlcusu.blit(agac1, (ekran_genislik / 2 + 500, ekran_yukseklik - 385))

        ekranOlcusu.blit(ot, (-20, ekran_yukseklik - 200))
        ekranOlcusu.blit(ot, (ekran_genislik - 50, ekran_yukseklik - 200))

        ########################################################

        ## OBJELER ##
        ekranOlcusu.blit(agac1, (ekran_genislik / 2, ekran_yukseklik - 405))

        ekranOlcusu.blit(ot, (-20, ekran_yukseklik - 200))
        ekranOlcusu.blit(ot, (ekran_genislik - 50, ekran_yukseklik - 200))

        ########################################################

        ## ZEMIN DIZAYNI ##
        ekranOlcusu.blit(platform1_orta, (0, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (105, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (210, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (315, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (420, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (525, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (630, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (735, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (840, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (945, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (1050, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (1100, ekran_yukseklik - 130))
        ekranOlcusu.blit(platform1_orta, (1175, ekran_yukseklik - 130))

        ekranOlcusu.blit(tas1, (-5, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (210, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (418, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (622, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (824, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (1026, ekran_yukseklik - 111))
        ekranOlcusu.blit(tas1, (1218, ekran_yukseklik - 111))

        ekranOlcusu.blit(kesik_agac, (150, ekran_yukseklik - 172))


        ekranOlcusu.blit(ev, (ekran_genislik / 2 - 500, ekran_yukseklik / 2 - 65))






        #ekranOlcusu.blit(cadi, (ekran_genislik / 2 + 100, ekran_yukseklik / 2 + 100))
        #ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 150, ekran_yukseklik / 2 + 170))
        #ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 180, ekran_yukseklik / 2 + 165))
        #ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 80, ekran_yukseklik / 2 + 170))
        #ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 110, ekran_yukseklik / 2 + 165))
        #ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 220, ekran_yukseklik / 2 + 170))
        #ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 250, ekran_yukseklik / 2 + 165))

        #########################################################
        ## HIKAYE ##
        if yazi_sayac == 0:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 -100, ekran_yukseklik / 2 + 100))
            ekranOlcusu.blit(portal, (ekran_genislik / 2 + 300, ekran_yukseklik / 2))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 250, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 280, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 200, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 230, ekran_yukseklik / 2 + 165))

            hikaye1("Yaşlı Büyücü, Portaldan çıkmayı başaran Minus'ları görünce çok sevindi.. (Geçmek için Boşluk tuşunu kullanın)", ekran_genislik / 2, 200, white, 22)

        elif yazi_sayac == 1:
            ekranOlcusu.blit(cadi, (ekran_genislik / 2 + 100, ekran_yukseklik / 2 + 100))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 150, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 180, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 80, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 110, ekran_yukseklik / 2 + 165))
            ekranOlcusu.blit(karakter_saf, (ekran_genislik / 2 + 220, ekran_yukseklik / 2 + 170))
            ekranOlcusu.blit(karakter_seker, (ekran_genislik / 2 + 250, ekran_yukseklik / 2 + 165))
            hikaye1("Ve Sonsuza kadar mutlu yaşadılar...", ekran_genislik / 2,200, white, 22)

        elif yazi_sayac == 2:

            hikaye1("Kodlama : Emre ŞAHİN   Hikaye : Burak BAŞDAĞ   Müzik : Emre ŞAHİN  Texture : iconfinder.com", ekran_genislik / 2, 200, white, 22)


        elif yazi_sayac == 3:
            hikaye1("Tamamen Python ve PyGame ile yazılmıştır. Oynadığınız için teşekkürler..",ekran_genislik / 2, 200, white, 22)

        elif yazi_sayac == 4:
            hikaye1("Survander Games 2018   survandergames.blogspot.com", ekran_genislik / 2, 200,white, 22)

        elif yazi_sayac == 5:
            quit()
            exit()


        ###############################################################

        pygame.display.update()  # Eğer içine bir şey yazılmazsa bütün surface  i yeniler
        clock.tick(30)  # FPS




        ### HAREKET MESELELERI ###

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    ekranOlcusu.blit(arkaplan_gece, (0, -50))



                    ## ZEMIN DIZAYNI ##
                    ekranOlcusu.blit(platform1_orta, (0, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (105, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (210, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (315, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (420, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (525, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (630, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (735, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (840, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (945, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (1050, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (1100, ekran_yukseklik - 130))
                    ekranOlcusu.blit(platform1_orta, (1175, ekran_yukseklik - 130))

                    ekranOlcusu.blit(tas1, (-5, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (210, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (418, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (622, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (824, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (1026, ekran_yukseklik - 111))
                    ekranOlcusu.blit(tas1, (1218, ekran_yukseklik - 111))

                    ekranOlcusu.blit(kesik_agac, (150, ekran_yukseklik - 172))
                    #########################################################

                    ekranOlcusu.blit(cadi, (ekran_genislik / 2 - 200, ekran_yukseklik / 2 + 100))

                    yazi_sayac+=1

        ################################

bolum1()
pygame.quit()
quit()