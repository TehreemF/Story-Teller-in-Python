from tkinter import *
from winsound import *

def Play(ps, img):
    global w4
    w4 = Toplevel()
    w4.attributes('-fullscreen', True)
    w4.title('{}'.format(ps))

    apkaaj_canvas = Canvas(w4)
    apkaaj_canvas.pack(expand=True, fill='both')
    apkaaj_image = PhotoImage(file= img+'.png')
    apkaaj_canvas.image = apkaaj_image #keep a link to the image to stop the image being garbage collected
    apkaaj_canvas.create_image(0, 0, anchor=NW, image=apkaaj_image)
    
    play = Button(apkaaj_canvas, text='Play', width=20, bg='green', fg='black',
                  font='Helvetica 14 bold italic', command=lambda: PlaySound(ps+'.wav', SND_ASYNC))
    pause = Button(apkaaj_canvas, text='Pause', width=20, bg='red', fg='white',
                   font='Helvetica 14 bold italic', command=lambda: PlaySound(None, SND_PURGE))
    back = Button(apkaaj_canvas, text='< Back', width=20, bg='black', fg='white',
                  font='Helvetica 14 bold italic', command = lambda: w4.destroy())
    play.place(x=600, y=100);pause.place(x=600, y=200);back.place(x=600, y=300)
    
def Back(t):
    PlaySound(None, SND_PURGE)
    t.destroy()
    
def Urdu():
    w2 = Toplevel(main_window)
    w2.attributes('-fullscreen', True)
    
    urdu_canvas = Canvas(w2)
    urdu_canvas.pack(expand=True, fill='both')
    urdu_image = PhotoImage(file='urdu bg.png')
    urdu_canvas.image = urdu_image #keep a link to the image to stop the image being garbage collected
    urdu_canvas.create_image(0, 0, anchor=NW, image=urdu_image)
    
    story1 = Button(urdu_canvas, text = 'Ap kaaj maha kaaj', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Ap_kaaj_maha_kaaj', 'ap kaaj'))
    story1.place(x=415, y=350)
    story2 = Button(urdu_canvas, text = 'Apni bala doosron k sarr', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Apni_bala_doosron_k_sarr', 'apni bala'))
    story2.place(x=415, y=400)
    story3 = Button(urdu_canvas, text = 'Azaadi ki khushi', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Azaadi_ki_khushi', 'azaadi'))
    story3.place(x=415, y=450)
    story4 = Button(urdu_canvas, text = 'Bahaana', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Bahaana'))
    story4.place(x=415, y=500)
    story5 = Button(urdu_canvas, text = 'Dhoka buri bala', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Dhoka_buri_bala'))
    story5.place(x=570, y=550)
    story6 = Button(urdu_canvas, text = 'Jesa Karoge Wesa Bharoge', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Jesa_Karoge_Wesa_Bharoge'))
    story6.place(x=705, y=350)
    story7 = Button(urdu_canvas, text = 'Jhoot ki saza', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Jhoot_ki_saza'))
    story7.place(x=705, y=400)
    story8 = Button(urdu_canvas, text = 'Jitni Koshish Utna Ajar', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Jitni_Koshish_Utna_Ajar'))
    story8.place(x=705, y=450)
    story9 = Button(urdu_canvas, text = 'Phanda', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Phanda'))
    story9.place(x=705, y=500)

    end = Button(urdu_canvas, text='< Back', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 10 bold italic', command = lambda: Back(w2))
    end.place(x=0, y=700)
    
def English():
    w3 = Toplevel(main_window)
    w3.attributes('-fullscreen', True)

    english_canvas = Canvas(w3)
    english_canvas.pack(expand=True, fill='both')
    english_image = PhotoImage(file='english bg.png')
    english_canvas.image = english_image     
    english_canvas.create_image(0, 0, anchor=NW, image=english_image)
    
    story10 = Button(english_canvas, text = 'Aladdin and his Magic Lamp', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Aladdin_and_his_Magic_Lamp', 'aladdin'))
    story10.place(x=410, y=300)
    story11 = Button(english_canvas, text = 'A Meal With A Magician', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('A_Meal_With_A_Magician'))
    story11.place(x=410, y=350)
    story12 = Button(english_canvas, text = 'Boffy and the Teacher Eater', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Boffy_and_the_Teacher_Eater'))
    story12.place(x=410, y=400)
    story13 = Button(english_canvas, text = 'Dragon Child', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Dragon_Child'))
    story13.place(x=410, y=450)
    story14 = Button(english_canvas, text = 'George and the Dragon', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('George_and_the_Dragon'))
    story14.place(x=410, y=500)
    story15 = Button(english_canvas, text = 'Pinocchio', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Pinocchio', 'pinocchio'))
    story15.place(x=700, y=300)
    story16 = Button(english_canvas, text = 'The Great Pie Contest', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('The_Great_Pie_Contest'))
    story16.place(x=700, y=350)
    story17 = Button(english_canvas, text = 'The Magic Porridge Pot', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('The_Magic_Porridge_Pot'))
    story17.place(x=700, y=400)
    story18 = Button(english_canvas, text = 'The Snow Queen', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('The_Snow_Queen'))
    story18.place(x=700, y=450)
    story19 = Button(english_canvas, text = 'Thumbelina', width=22, bg='floral white', fg='saddle brown',
                     font='Helvetica 14 bold italic', command = lambda: Play('Thumbelina'))
    story19.place(x=700, y=500)
    
    end = Button(english_canvas, text='< Back', width=22, bg='floral white', fg='saddle brown',
                 font='Helvetica 10 bold italic', command=lambda: Back(w3))
    end.place(x=0, y=700)
    
def Title():
    w1 = Toplevel()
    w1.attributes('-fullscreen', True)

    menu_canvas = Canvas(w1)
    menu_canvas.pack(expand=True, fill='both')
    menu_image = PhotoImage(file='title.png')
    menu_canvas.image = menu_image     
    menu_canvas.create_image(0, 0, anchor=NW, image=menu_image)
    
    label = Label(menu_canvas, width=22, bg='black', fg='snow',  relief='flat',
                  font='Helvetica 18 bold italic', text='Choose your language:')
    label.place(x=560, y=100)
    urdu = Button(menu_canvas, width=22, bg='black', fg='snow', relief='flat',
                  font='Helvetica 16 bold italic', text='Urdu', command=Urdu)
    urdu.place(x=580, y=150)
    english = Button(menu_canvas, width=22, bg='black', fg='snow', relief='flat',
                     font='Helvetica 16 bold italic', text='English', command=English)
    english.place(x=580, y=200)
    end = Button(menu_canvas, width=22, bg='black', fg='snow', relief='flat',
                 font='Helvetica 12 bold italic', text='Quit', command=lambda: main_window.destroy())
    end.place(x=610, y=300)
    
main_window = Tk()
main_window.attributes('-fullscreen', True)

title_image = PhotoImage(file='Storyteller.png')
title = Button(main_window, text='Click to continue', fg='white', bg='sienna', font='Helvetica 10 bold italic',
               relief='flat', image=title_image, command=Title)
title.pack()

main_window.mainloop()
