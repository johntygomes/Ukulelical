from pygame import mixer
mixer.init()
from tkinter import *
root=Tk()
root.title("UKULELICAL")
root.geometry('1360x700')
root.iconbitmap(default="ukulele.ico")
c=Canvas(root,background='#b53b35',width=1355,height=2000)
c.place(x=0,y=0)
#####################WELCONE MESSAGE#####
print("#####################")
print("1.Now Newbies Can Jam")
print("2.Chords At Your Fingertips")
print("3.Know Your Triads")
print("###########################################################")
print("HELLO FROM JOHNTY GOMES.")
print("Whatsapp or call at: +91 9773211427")
print("Email: johntygomes30@gmail.com")
print("Facebook: https://www.facebook.com/guitarical.guy.7")
print("Insta: https://www.instagram.com/johntygomes7/")
print("Youtube Tutorial: https://www.youtube.com/watch?v=EW2u2uC0KBo")
print("###########################################################")
print("Ukulelical Windows Application(.exe):: https://drive.google.com/file/d/1NQIbhvkkrrxgqGVieRgUTwK6ipMOV81J/view?usp=sharing")
#######  Major Frame and Minor   #####
frame_major=Frame(c,background='#b53b35')
frame_major.place(x=0,y=50,width=1355,height=130)

major_scale_label=Label(frame_major,text='Major and Minor Scale Notes',font=40)
major_scale_label.place(x=0,y=0)
#######   Scale Label  ######
scale_label=Label(c,text='Scale Notes',font=40)
scale_label.place(x=1330/2,y=0)

######   Find Chords in Your Scale   #######
frame_chord=Frame(c,background='black')
frame_chord.place(x=0,y=170,width=1355,height=100)

minor_scale_label=Label(frame_chord,text='Chords',font=40)
minor_scale_label.place(x=0,y=0)
orig_color = minor_scale_label.cget("background")
triad=Label(frame_chord,text='triad',bg='white',font=80)
triad.place(x=750,y=45)
#############CHORDMUTE
def chordmute():
    mixer.Channel(64).stop()
    mixer.Channel(65).stop()
    mixer.Channel(66).stop()
    mixer.Channel(67).stop()
################RESET FLASH
def resetflash():
    def flashb1(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-z>', flashb1)

    def flashb2(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-x>', flashb2)

    def flashb3(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-c>', flashb3)

    def flashb4(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-v>', flashb4)

    def flashb5(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-b>', flashb5)

    def flashb6(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-n>', flashb6)

    def flashb7(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-m>', flashb7)

    def flashb8(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-,>', flashb8)

    def flashb9(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-.>', flashb9)

    def flashb10(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-/>', flashb10)

    def flashb11(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Left>', flashb11)

    def flashb12(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Down>', flashb12)

    def flashb13(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Right>', flashb13)

    def flashb14(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Z>', flashb14)

    def flashb15(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-X>', flashb15)

    def flashb16(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-C>', flashb16)

    def flashb17(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-V>', flashb17)

    def flashb18(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-B>', flashb18)

    def flashb19(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-N>', flashb19)

    def flashb20(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-<>', flashb20)

    def flashb21(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress->>', flashb21)

    def flashb22(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-?>', flashb22)

    def flashb23(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-a>', flashb23)

    def flashb24(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-s>', flashb24)

    def flashb25(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-d>', flashb25)

    def flashb26(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-f>', flashb26)

    def flashb27(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-g>', flashb27)

    def flashb28(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-h>', flashb28)

    def flashb29(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-j>', flashb29)
    def flashb30(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-k>', flashb30)

    def flashb31(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-l>', flashb31)

    def flashb32(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-;>', flashb32)

    def flashb33(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind("<KeyPress-'>", flashb33)

    def flashb34(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Return>', flashb34)

    def flashb35(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Delete>', flashb35)

    def flashb36(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-A>', flashb36)

    def flashb37(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-S>', flashb37)

    def flashb38(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-D>', flashb38)

    def flashb39(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-F>', flashb39)

    def flashb40(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-G>', flashb40)

    def flashb41(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-H>', flashb41)

    def flashb42(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-J>', flashb42)

    def flashb43(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-K>', flashb43)

    def flashb44(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-L>', flashb44)

    def flashb45(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-:>', flashb45)

    def flashb46(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-">', flashb46)

    def flashb47(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-q>', flashb47)

    def flashb48(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-w>', flashb48)

    def flashb49(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-e>', flashb49)

    def flashb50(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-r>', flashb50)

    def flashb51(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-t>', flashb51)

    def flashb52(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-y>', flashb52)

    def flashb53(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-u>', flashb53)

    def flashb54(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-i>', flashb54)

    def flashb55(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-o>', flashb55)

    def flashb56(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-p>', flashb56)

    def flashb57(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-[>', flashb57)

    def flashb58(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-]>', flashb58)

    def flashb59(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-\>', flashb59)

    def flashb60(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Q>', flashb60)

    def flashb61(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-W>', flashb61)

    def flashb62(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-E>', flashb62)

    def flashb63(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-R>', flashb63)

    def flashb64(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-T>', flashb64)

    def flashb65(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Y>', flashb65)

    def flashb66(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-U>', flashb66)

    def flashb67(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-I>', flashb67)

    def flashb68(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-O>', flashb68)

    def flashb69(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-P>', flashb69)

    def flashb70(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-{>', flashb70)

    def flashb71(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-{>', flashb71)

    def flashb72(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-}>', flashb72)

    def flashb73(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-|>', flashb73)

    def flashb74(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-`>', flashb74)
    def flashb75(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-1>', flashb75)

    def flashb76(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-2>', flashb76)

    def flashb77(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-3>', flashb77)

    def flashb78(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-4>', flashb78)

    def flashb79(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-5>', flashb79)

    def flashb80(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-6>', flashb80)

    def flashb81(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-7>', flashb81)

    def flashb82(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-8>', flashb82)

    def flashb83(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-9>', flashb83)

    def flashb84(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-0>', flashb84)

    def flashb85(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('-', flashb85)

    def flashb86(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-=>', flashb86)

    def flashb87(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Escape>', flashb87)

    def flashb88(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-F1>', flashb88)

    def flashb89(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-F2>', flashb89)
    def flashb90(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-F3>', flashb90)

    def flashb91(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-F4>', flashb91)

    def flashb92(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-F5>', flashb92)

    def flashb93(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-F6>', flashb93)

    def flashb94(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-F7>', flashb94)

    def flashb95(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-F8>', flashb95)

    def flashb96(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Insert>', flashb96)

    def flashb97(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Home>', flashb97)

    def flashb98(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Prior>', flashb98)

    def flashb99(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-~>', flashb99)

    def flashb100(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-!>', flashb100)
    def flashb101(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-@>', flashb101)

    def flashb102(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-#>', flashb102)

    def flashb103(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-$>', flashb103)

    def flashb104(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-%>', flashb104)

    def flashb105(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-^>', flashb105)

    def flashb106(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-&>', flashb106)

    def flashb107(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-*>', flashb107)

    def flashb108(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-*>', flashb108)

    def flashb109(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-(>', flashb109)

    def flashb110(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-)>', flashb110)
    def flashb111(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-_>', flashb111)

    def flashb112(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-+>', flashb112)

    def flashb113(event):
       scale_label.config(bg = orig_color)
       root.after(175, lambda: scale_label.config(bg = orig_color))
    root.bind('<KeyPress-Delete>', flashb113)

################Reset Guitar Buttons############################
def resetguitar():
    b1g4.configure(background=orig_color)
    b2g4.configure(background=orig_color)
    b3g4.configure(background=orig_color)
    b4g4.configure(background=orig_color)
    b5g4.configure(background=orig_color)
    b6g4.configure(background=orig_color)
    b7g4.configure(background=orig_color)
    b8g4.configure(background=orig_color)
    b9g4.configure(background=orig_color)
    b10g4.configure(background=orig_color)
    b11g4.configure(background=orig_color)
    b12g4.configure(background=orig_color)
    b13g4.configure(background=orig_color)
    b14g4.configure(background=orig_color)
    b15g4.configure(background=orig_color)
    b16g4.configure(background=orig_color)

    b1g3.configure(background=orig_color)
    b2g3.configure(background=orig_color)
    b3g3.configure(background=orig_color)
    b4g3.configure(background=orig_color)
    b5g3.configure(background=orig_color)
    b6g3.configure(background=orig_color)
    b7g3.configure(background=orig_color)
    b8g3.configure(background=orig_color)
    b9g3.configure(background=orig_color)
    b10g3.configure(background=orig_color)
    b11g3.configure(background=orig_color)
    b12g3.configure(background=orig_color)
    b13g3.configure(background=orig_color)
    b14g3.configure(background=orig_color)
    b15g3.configure(background=orig_color)
    b16g3.configure(background=orig_color)

    b1g2.configure(background=orig_color)
    b2g2.configure(background=orig_color)
    b3g2.configure(background=orig_color)
    b4g2.configure(background=orig_color)
    b5g2.configure(background=orig_color)
    b6g2.configure(background=orig_color)
    b7g2.configure(background=orig_color)
    b8g2.configure(background=orig_color)
    b9g2.configure(background=orig_color)
    b10g2.configure(background=orig_color)
    b11g2.configure(background=orig_color)
    b12g2.configure(background=orig_color)
    b13g2.configure(background=orig_color)
    b14g2.configure(background=orig_color)
    b15g2.configure(background=orig_color)
    b16g2.configure(background=orig_color)

    b1g1.configure(background=orig_color)
    b2g1.configure(background=orig_color)
    b3g1.configure(background=orig_color)
    b4g1.configure(background=orig_color)
    b5g1.configure(background=orig_color)
    b6g1.configure(background=orig_color)
    b7g1.configure(background=orig_color)
    b8g1.configure(background=orig_color)
    b9g1.configure(background=orig_color)
    b10g1.configure(background=orig_color)
    b11g1.configure(background=orig_color)
    b12g1.configure(background=orig_color)
    b13g1.configure(background=orig_color)
    b14g1.configure(background=orig_color)
    b15g1.configure(background=orig_color)
    b16g1.configure(background=orig_color)
def defaultboard():
    resetguitar()
    resetflash()
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)  
    def flashb1g3(event):
       b1g3.config(bg = 'green')
       root.after(175, lambda: b1g3.config(bg = 'pink'))
       g31()
    root.bind('<KeyPress-1>', flashb1g3)
    def flashb2g3(event):
       b2g3.config(bg = 'green')
       root.after(175, lambda: b2g3.config(bg = 'pink'))
       g32()
    root.bind('<KeyPress-2>', flashb2g3)
    def flashb3g3(event):
       b3g3.config(bg = 'green')
       root.after(175, lambda: b3g3.config(bg = 'pink'))
       g33()
    root.bind('<KeyPress-3>', flashb3g3)
    def flashb4g3(event):
       b4g3.config(bg = 'green')
       root.after(175, lambda: b4g3.config(bg = 'pink'))
       g34()
    root.bind('<KeyPress-4>', flashb4g3)

    def flashb1g2(event):
       b1g2.config(bg = 'green')
       root.after(175, lambda: b1g2.config(bg = 'pink'))
       g21()
    root.bind('<KeyPress-q>', flashb1g2)
    def flashb2g2(event):
       b2g2.config(bg = 'green')
       root.after(175, lambda: b2g2.config(bg = 'pink'))
       g22()
    root.bind('<KeyPress-w>', flashb2g2)
    def flashb3g2(event):
       b3g2.config(bg = 'green')
       root.after(175, lambda: b3g2.config(bg = 'pink'))
       g23()
    root.bind('<KeyPress-e>', flashb3g2)
    def flashb4g2(event):
       b4g2.config(bg = 'green')
       root.after(175, lambda: b4g2.config(bg = 'pink'))
       g24()
    root.bind('<KeyPress-r>', flashb4g2)
    def flashb5g2(event):
       b5g2.config(bg = 'green')
       root.after(175, lambda: b5g2.config(bg = 'pink'))
       g25()
    root.bind('<KeyPress-t>', flashb5g2)
    def flashb1g1(event):
       b1g1.config(bg = 'green')
       root.after(175, lambda: b1g1.config(bg = 'pink'))
       g11()
    root.bind('<KeyPress-a>', flashb1g1)
    def flashb2g1(event):
       b2g1.config(bg = 'green')
       root.after(175, lambda: b2g1.config(bg = 'pink'))
       g12()
    root.bind('<KeyPress-s>', flashb2g1)
    def flashb3g1(event):
       b3g1.config(bg = 'green')
       root.after(175, lambda: b3g1.config(bg = 'pink'))
       g13()
    root.bind('<KeyPress-d>', flashb3g1)
    def flashb4g1(event):
       b4g1.config(bg = 'green')
       root.after(175, lambda: b4g1.config(bg = 'pink'))
       g14()
    root.bind('<KeyPress-f>', flashb4g1)
    def flashb5g1(event):
       b5g1.config(bg = 'green')
       root.after(175, lambda: b5g1.config(bg = 'pink'))
       g15()
    root.bind('<KeyPress-g>', flashb5g1)
    def flashb6g1(event):
       b6g1.config(bg = 'green')
       root.after(175, lambda: b6g1.config(bg = 'pink'))
       g16()
    root.bind('<KeyPress-h>', flashb6g1)
    def flashb7g1(event):
       b7g1.config(bg = 'green')
       root.after(175, lambda: b7g1.config(bg = 'pink'))
       g17()
    root.bind('<KeyPress-j>', flashb7g1)
    def flashb8g1(event):
       b8g1.config(bg = 'green')
       root.after(175, lambda: b8g1.config(bg = 'pink'))
       g18()
    root.bind('<KeyPress-k>', flashb8g1)
    def flashb9g1(event):
       b9g1.config(bg = 'green')
       root.after(175, lambda: b9g1.config(bg = 'pink'))
       g19()
    root.bind('<KeyPress-l>', flashb9g1)
    def flashb10g1(event):
       b10g1.config(bg = 'green')
       root.after(175, lambda: b10g1.config(bg = 'pink'))
       g110()
    root.bind('<KeyPress-z>', flashb10g1)
    def flashb11g1(event):
       b11g1.config(bg = 'green')
       root.after(175, lambda: b11g1.config(bg = 'pink'))
       g111()
    root.bind('<KeyPress-x>', flashb11g1)
    def flashb12g1(event):
       b12g1.config(bg = 'green')
       root.after(175, lambda: b12g1.config(bg = 'pink'))
       g112()
    root.bind('<KeyPress-c>', flashb12g1)
    def flashb13g1(event):
       b13g1.config(bg = 'green')
       root.after(175, lambda: b13g1.config(bg = 'pink'))
       g113()
    root.bind('<KeyPress-v>', flashb13g1)
    def flashb14g1(event):
       b14g1.config(bg = 'green')
       root.after(175, lambda: b14g1.config(bg = 'pink'))
       g114()
    root.bind('<KeyPress-b>', flashb14g1)
    def flashb15g1(event):
       b15g1.config(bg = 'green')
       root.after(175, lambda: b15g1.config(bg = 'pink'))
       g115()
    root.bind('<KeyPress-n>', flashb15g1)
    def flashb16g1(event):
       b16g1.config(bg = 'green')
       root.after(175, lambda: b16g1.config(bg = 'pink'))
       g116()
    root.bind('<KeyPress-m>', flashb16g1)
    b1g3.configure(background='pink')
    b2g3.configure(background='pink')
    b3g3.configure(background='pink')
    b4g3.configure(background='pink')
    b1g2.configure(background='pink')
    b2g2.configure(background='pink')
    b3g2.configure(background='pink')
    b4g2.configure(background='pink')
    b5g2.configure(background='pink')
    b1g1.configure(background='pink')
    b2g1.configure(background='pink')
    b3g1.configure(background='pink')
    b4g1.configure(background='pink')
    b5g1.configure(background='pink')
    b6g1.configure(background='pink')
    b7g1.configure(background='pink')
    b8g1.configure(background='pink')
    b9g1.configure(background='pink')
    b10g1.configure(background='pink')
    b11g1.configure(background='pink')
    b12g1.configure(background='pink')
    b13g1.configure(background='pink')
    b14g1.configure(background='pink')
    b15g1.configure(background='pink')
    b16g1.configure(background='pink')
###############BUTTON FOR RESET GUITAR
reset_johnty_guitar=Button(c,text='reset',command=resetguitar)
reset_johnty_guitar.place(x=300,y=0,width=100,height=50)
#######################RESET CHORDS
def resetchords():
    c1.place_forget()
    c2.place_forget()
    c3.place_forget()
    c4.place_forget()
    c5.place_forget()
    c6.place_forget()
    c7.place_forget()
    c8.place_forget()
    c9.place_forget()
    c10.place_forget()
    c11.place_forget()
    c12.place_forget()
    c13.place_forget()
    c14.place_forget()
    c15.place_forget()
    c16.place_forget()
    c17.place_forget()
    c18.place_forget()
    c19.place_forget()
    c20.place_forget()
    c21.place_forget()
    c22.place_forget()
    c23.place_forget()
    c24.place_forget()
    c25.place_forget()
    c26.place_forget()
    c27.place_forget()
    c28.place_forget()
    c29.place_forget()
    c30.place_forget()
    c31.place_forget()
    c32.place_forget()
    c33.place_forget()
    c34.place_forget()
    c35.place_forget()
    c36.place_forget()
    c37.place_forget()
    c38.place_forget()
    c39.place_forget()
    c40.place_forget()
    c41.place_forget()
    c42.place_forget()
    c43.place_forget()
    c44.place_forget()
    c45.place_forget()
    c46.place_forget()
    c47.place_forget()
    c48.place_forget()
    c49.place_forget()
    c50.place_forget()
    c51.place_forget()
    c52.place_forget()
    c53.place_forget()
    c54.place_forget()
    c55.place_forget()
    c56.place_forget()
    c57.place_forget()
    c58.place_forget()
    c59.place_forget()
    c60.place_forget()
    c61.place_forget()
    c62.place_forget()
    c63.place_forget()
    c64.place_forget()
    c65.place_forget()
    c66.place_forget()
    c67.place_forget()
    c68.place_forget()
    c69.place_forget()
    c70.place_forget()
    c71.place_forget()
    c72.place_forget()
    c73.place_forget()
    c74.place_forget()
    c75.place_forget()
    c76.place_forget()
    c77.place_forget()
    c78.place_forget()
    c79.place_forget()
    c80.place_forget()
    c81.place_forget()
    c82.place_forget()
    c83.place_forget()
    c84.place_forget()
##############default scale buton############
default_scale=Button(frame_major,text='All notes mode',command=defaultboard)
default_scale.place(x=1200,y=45,height=50,width=150)
###################setting number of channels in mixer
mixer.set_num_channels(1000)
#################################CHORD FUNCTIONS
def chordC():
    triad.configure(text='C-E-G')
    b1g4.configure(background='purple')
    b1g3.configure(background='purple')
    b1g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C0.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E0.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))
def chordD():
    triad.configure(text='D-F#-A')
    b3g4.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    b6g1.configure(background='purple')    
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A5.wav'))

def chordE():
    triad.configure(text='E-G#-B')
    b5g4.configure(background='purple')
    b5g3.configure(background='purple')
    b5g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))
def chordF():
    triad.configure(text='F-A-C')
    b3g4.configure(background='purple')
    b1g3.configure(background='purple')
    b2g2.configure(background='purple')
    b1g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C0.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A0.wav'))
def chordG():
    triad.configure(text='G-B-D')
    b1g4.configure(background='purple')
    b3g3.configure(background='purple')
    b4g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))
def chordA():
    triad.configure(text='A-C#-E')
    b3g4.configure(background='purple')
    b2g3.configure(background='purple')
    b1g2.configure(background='purple')
    b1g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E0.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A0.wav'))
def chordB():
    triad.configure(text='B-D#-F#')
    b5g4.configure(background='purple')
    b4g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))
def chordCminor():
    triad.configure(text='C-D#-G')
    b1g4.configure(background='purple')
    b4g3.configure(background='purple')
    b4g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))        
def chordDminor():
    triad.configure(text='D-F-A')
    b3g4.configure(background='purple')
    b3g3.configure(background='purple')
    b2g2.configure(background='purple')
    b1g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A0.wav'))
def chordEminor():
    triad.configure(text='E-G-B')
    b1g4.configure(background='purple')
    b5g3.configure(background='purple')
    b4g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))
def chordFminor():
    triad.configure(text='F-G#-C')
    b2g4.configure(background='purple')
    b1g3.configure(background='purple')
    b2g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C0.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))    
def chordGminor():
    triad.configure(text='G-A#-D')
    b1g4.configure(background='purple')
    b3g3.configure(background='purple')
    b4g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))    
def chordAminor():
    triad.configure(text='A-C-E')
    b3g4.configure(background='purple')
    b1g3.configure(background='purple')
    b1g2.configure(background='purple')
    b1g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C0.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E0.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A0.wav'))
def chordBminor():
    triad.configure(text='B-D-F#')
    b3g4.configure(background='purple')
    b5g4.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')    
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))
def chordCsharp():
    triad.configure(text='C#-F-G#')
    b2g1.configure(background='purple')
    b2g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))
def chordDsharp():
    triad.configure(text='D#-G-A#')
    b1g4.configure(background='purple')
    b4g3.configure(background='purple')
    b4g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))
def chordFsharp():
    triad.configure(text='F#-A#-C#')
    b4g4.configure(background='purple')
    b2g4.configure(background='purple')
    b2g2.configure(background='purple')
    b2g3.configure(background='purple')
    b3g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))
def chordGsharp():
    triad.configure(text='G#-C-D#')
    b2g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    b4g3.configure(background='purple')
    b5g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))
def chordAsharp():
    triad.configure(text='A#-D-F')
    b4g4.configure(background='purple')
    b3g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))
def chordCsharpminor():
    triad.configure(text='C#-E-G#')
    b2g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    b5g3.configure(background='purple')
    b5g2.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))    
def chordDsharpminor():
    triad.configure(text='D#-F#-A#')
    b4g4.configure(background='purple')
    b4g3.configure(background='purple')
    b3g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))    
def chordFsharpminor():
    triad.configure(text='F#-A-C#')
    b3g4.configure(background='purple')
    b2g3.configure(background='purple')
    b3g2.configure(background='purple')
    b1g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A0.wav'))    
def chordGsharpminor():
    triad.configure(text='G#-B-D#')
    b5g4.configure(background='purple')
    b4g3.configure(background='purple')
    b5g2.configure(background='purple')
    b3g4.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))   
def chordAsharpminor():
    triad.configure(text='A#-C#-F')
    b4g4.configure(background='purple')
    b2g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))
def chordCdiminished():
    triad.configure(text='C-D#-F#')
    b4g3.configure(background='purple')
    b3g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))
def chordDdiminished():
    triad.configure(text='D-F-G#')
    b6g3.configure(background='purple')
    b5g2.configure(background='purple')
    b6g1.configure(background='purple') 
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/C5.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/A5.wav'))

def chordEdiminished():
    triad.configure(text='E-G-A#')
    b4g4.configure(background='purple')
    b5g3.configure(background='purple')
    b4g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))
def chordFdiminished():
    triad.configure(text='F-G#-B')
    b5g4.configure(background='purple')
    b6g3.configure(background='purple')
    b5g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C5.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))
def chordGdiminished():
    triad.configure(text='G-A#-C#')
    b1g4.configure(background='purple')
    b2g3.configure(background='purple')
    b4g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))
def chordAdiminished():
    triad.configure(text='A-C-D#')
    b4g3.configure(background='purple')
    b6g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E5.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav')) 
def chordBdiminished():
    triad.configure(text='B-D-F')
    b3g3.configure(background='purple')
    b2g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))

def chordCsharpdiminished():
    triad.configure(text='C#-E-G')
    b5g3.configure(background='purple')
    b4g2.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))
def chordDsharpdiminished():   
    triad.configure(text='D#-F#-A')
    b7g3.configure(background='purple')
    b6g2.configure(background='purple')
    b7g1.configure(background='purple') 
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/C6.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/E5.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/A6.wav'))
def chordFsharpdiminished():
    triad.configure(text='F#-A-C')
    b6g4.configure(background='purple')
    b7g3.configure(background='purple')
    b6g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G5.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C6.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E5.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))
def chordGsharpdiminished():
    triad.configure(text='G#-B-D')
    b3g3.configure(background='purple')
    b5g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))
def chordAsharpdiminished():
    triad.configure(text='A#-C#-E')
    b5g3.configure(background='purple')
    b7g2.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E6.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav')) 
def chordCmajor7():
    triad.configure(text='C-E-G-B')
    b1g4.configure(background='purple')
    b1g3.configure(background='purple')
    b1g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C0.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E0.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav')) 
def chordDmajor7():
    triad.configure(text='D-F#-A-C#')
    b3g4.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav')) 
def chordEmajor7():
    triad.configure(text='E-G#-B-D#')
    b5g4.configure(background='purple')
    b5g3.configure(background='purple')
    b5g2.configure(background='purple')
    b5g1.configure(background='purple')
    b7g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A6.wav')) 
def chordFmajor7():
    triad.configure(text='F-A-C-E')
    b6g4.configure(background='purple')
    b6g3.configure(background='purple')
    b1g2.configure(background='purple')
    b1g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G5.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C5.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E0.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A0.wav')) 
def chordGmajor7():
    triad.configure(text='G-B-D-F#')
    b1g4.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav')) 
def chordAmajor7():
    triad.configure(text='A-C#-E-G#')
    b3g4.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    b5g3.configure(background='purple')
    b5g2.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))  
def chordBmajor7():
    triad.configure(text='B-D#-F#-A#')
    b5g4.configure(background='purple')
    b5g3.configure(background='purple')
    b5g2.configure(background='purple')
    b5g1.configure(background='purple')
    b7g3.configure(background='purple')
    b7g2.configure(background='purple')
    b7g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C6.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E6.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A6.wav'))  
def chordCsharpmajor7():
    triad.configure(text='C#-F-G#-C')
    b2g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav')) 
def chordDsharpmajor7():
    triad.configure(text='D#-G-A#-D')
    b4g4.configure(background='purple')
    b4g3.configure(background='purple')
    b4g2.configure(background='purple')
    b4g1.configure(background='purple')
    b6g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A5.wav')) 
def chordFsharpmajor7():
    triad.configure(text='F#-A#-C#-F')
    b4g4.configure(background='purple')
    b6g3.configure(background='purple')
    b3g2.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C5.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))
def chordGsharpmajor7():
    triad.configure(text='G#-C-D#-G')
    b2g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    b4g3.configure(background='purple')
    b4g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav')) 
def chordAsharpmajor7():
    triad.configure(text='A#-D-F-A')
    b4g4.configure(background='purple')
    b4g3.configure(background='purple')
    b4g2.configure(background='purple')
    b4g1.configure(background='purple')
    b6g3.configure(background='purple')
    b6g2.configure(background='purple')
    b6g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C5.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E5.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A5.wav'))  
def chordCminor7():
    triad.configure(text='C-D#-G-A#')
    b4g4.configure(background='purple')
    b4g3.configure(background='purple')
    b4g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))  
def chordDminor7():
    triad.configure(text='D-F-A-C')
    b6g4.configure(background='purple')
    b6g3.configure(background='purple')
    b6g2.configure(background='purple')
    b6g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G5.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C5.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E5.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A5.wav'))  
def chordEminor7():
    triad.configure(text='E-G-B-D')
    b1g4.configure(background='purple')
    b3g3.configure(background='purple')
    b1g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E0.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))  
def chordFminor7():
    triad.configure(text='F-G#-C-D#')
    b2g4.configure(background='purple')
    b4g3.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))  
def chordGminor7():
    triad.configure(text='G-A#-D-F')
    b4g4.configure(background='purple')
    b6g3.configure(background='purple')
    b4g3.configure(background='purple')    
    b4g2.configure(background='purple')
    b4g1.configure(background='purple')
    b6g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C5.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A5.wav')) 
def chordAminor7():
    triad.configure(text='A-C-E-G')
    b1g4.configure(background='purple')
    b1g3.configure(background='purple')
    b1g2.configure(background='purple')
    b1g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C0.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E0.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A0.wav'))  
def chordBminor7():
    triad.configure(text='B-D-F#-A')
    b3g4.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))  
def chordCsharpminor7():
    triad.configure(text='C#-E-G#-B')
    b5g4.configure(background='purple')
    b5g3.configure(background='purple')
    b5g2.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))  
def chordDsharpminor7():
    triad.configure(text='D#-F#-A#-C#')
    b7g4.configure(background='purple')
    b7g3.configure(background='purple')
    b7g2.configure(background='purple')
    b7g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G6.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C6.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E6.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A6.wav'))  
def chordFsharpminor7():
    triad.configure(text='F#-A-C#-E')
    b3g4.configure(background='purple')
    b5g3.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))  
def chordGsharpminor7():
    triad.configure(text='G#-B-D#-F#')
    b5g4.configure(background='purple')
    b7g3.configure(background='purple')
    b5g3.configure(background='purple')    
    b5g2.configure(background='purple')
    b5g1.configure(background='purple')
    b7g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C6.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A6.wav'))  
def chordAsharpminor7():
    triad.configure(text='A#-C#-F-G#')
    b2g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))  
def chordCdominant7():
    triad.configure(text='C-E-G-A#')
    b1g4.configure(background='purple')
    b1g3.configure(background='purple')
    b1g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C0.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E0.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))  
def chordDdominant7():
    triad.configure(text='D-F#-A-C')
    b3g4.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))  
def chordEdominant7():
    triad.configure(text='E-G#-B-D')
    b5g4.configure(background='purple')
    b5g3.configure(background='purple')
    b5g2.configure(background='purple')
    b5g1.configure(background='purple')
    b6g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A5.wav')) 
def chordFdominant7():
    triad.configure(text='F-A-C-D#')
    b6g4.configure(background='purple')
    b6g3.configure(background='purple')
    b6g2.configure(background='purple')
    b6g1.configure(background='purple')
    b7g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G5.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C5.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E5.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A6.wav')) 
def chordGdominant7():
    triad.configure(text='G-B-D-F')
    b1g4.configure(background='purple')
    b3g3.configure(background='purple')
    b2g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav')) 
def chordAdominant7():
    triad.configure(text='A-C#-E-G')
    b1g4.configure(background='purple')
    b2g3.configure(background='purple')
    b1g2.configure(background='purple')
    b1g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E0.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A0.wav')) 
def chordBdominant7():
    triad.configure(text='B-D#-F#-A')
    b3g4.configure(background='purple')
    b3g3.configure(background='purple')    
    b4g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav')) 
def chordCsharpdominant7():
    triad.configure(text='C#-F-G#-B')
    b2g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))  
def chordDsharpdominant7():
    triad.configure(text='D#-G-A#-C#')
    b4g4.configure(background='purple')
    b4g3.configure(background='purple')
    b4g2.configure(background='purple')
    b4g1.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))  
def chordFsharpdominant7():
    triad.configure(text='F#-A#-C#-E')
    b4g4.configure(background='purple')
    b5g3.configure(background='purple')
    b3g2.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))  
def chordGsharpdominant7():
    triad.configure(text='G#-C-D#-F#')
    b2g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    b4g3.configure(background='purple')
    b3g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav')) 
def chordAsharpdominant7():
    triad.configure(text='A#-D-F-G#')
    b2g4.configure(background='purple')
    b3g3.configure(background='purple')
    b2g3.configure(background='purple')    
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav')) 
def chordCminor7flat5():
    triad.configure(text='C-D#-F#-A#')
    b6g4.configure(background='purple')
    b6g3.configure(background='purple')
    b6g2.configure(background='purple')
    b6g1.configure(background='purple')
    b7g3.configure(background='purple')
    b7g2.configure(background='purple')
    b7g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G5.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C6.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E6.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A6.wav'))      
def chordDminor7flat5():
    triad.configure(text='D-F-G#-C')
    b2g4.configure(background='purple')
    b2g1.configure(background='purple')
    b2g3.configure(background='purple')
    b3g3.configure(background='purple')
    b2g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))  
def chordEminor7flat5():
    triad.configure(text='E-G-A#-D')
    b4g4.configure(background='purple')
    b4g1.configure(background='purple')
    b4g3.configure(background='purple')
    b5g3.configure(background='purple')
    b4g2.configure(background='purple')
    b6g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A5.wav'))  
def chordFminor7flat5():
    triad.configure(text='F-G#-B-D#')
    b5g4.configure(background='purple')
    b5g1.configure(background='purple')
    b5g3.configure(background='purple')
    b6g3.configure(background='purple')
    b5g2.configure(background='purple')
    b7g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C5.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A6.wav'))  
def chordGminor7flat5():
    triad.configure(text='G-A#-C#-F')
    b1g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E1.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A1.wav'))  
def chordAminor7flat5():
    triad.configure(text='A-C-D#-G')
    b3g4.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    b4g3.configure(background='purple')
    b4g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E3.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))  
def chordBminor7flat5():
    triad.configure(text='B-D-F-A')
    b5g4.configure(background='purple')
    b5g3.configure(background='purple')
    b5g2.configure(background='purple')
    b5g1.configure(background='purple')
    b6g3.configure(background='purple')
    b6g2.configure(background='purple')
    b6g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G4.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C5.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E5.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A5.wav'))     
def chordCsharpminor7flat5():
    triad.configure(text='C#-E-G-B')
    b1g4.configure(background='purple')
    b1g1.configure(background='purple')
    b2g3.configure(background='purple')
    b1g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G0.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C1.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E0.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))  
def chordDsharpminor7flat5():
    triad.configure(text='D#-F#-A-C#')
    b3g4.configure(background='purple')
    b3g1.configure(background='purple')
    b3g3.configure(background='purple')
    b4g3.configure(background='purple')
    b3g2.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C3.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))  
def chordFsharpminor7flat5():
    triad.configure(text='F#-A-C-E')
    b3g1.configure(background='purple')
    b3g3.configure(background='purple')
    b3g4.configure(background='purple')
    b5g3.configure(background='purple')
    b3g2.configure(background='purple')
    b4g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G2.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A3.wav'))     

def chordGsharpminor7flat5():
    triad.configure(text='G#-B-D-F#')
    b2g4.configure(background='purple')
    b2g3.configure(background='purple')
    b2g2.configure(background='purple')
    b2g1.configure(background='purple')
    b3g3.configure(background='purple')
    b3g2.configure(background='purple')
    b3g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G1.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C2.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E2.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A2.wav'))  
def chordAsharpminor7flat5():
    triad.configure(text='A#-C#-E-G#')
    b4g4.configure(background='purple')
    b4g3.configure(background='purple')
    b4g2.configure(background='purple')
    b4g1.configure(background='purple')
    b5g3.configure(background='purple')
    b5g2.configure(background='purple')
    b5g1.configure(background='purple')
    chordmute()
    mixer.Channel(64).play(mixer.Sound('Audio/G3.wav'))
    mixer.Channel(65).play(mixer.Sound('Audio/C4.wav'))
    mixer.Channel(66).play(mixer.Sound('Audio/E4.wav'))
    mixer.Channel(67).play(mixer.Sound('Audio/A4.wav'))   
#############flag variable##############################
flag=0  
#################################Chord Scale Button Function##########################################
def c1f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordC() 
def c2f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharp()
def c3f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordD()
def c4f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharp()
def c5f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordE()
def c6f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordF()
def c7f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharp()
def c8f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordG()
def c9f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharp()
def c10f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordA()
def c11f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharp()
def c12f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordB()
def c13f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCminor()
def c14f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpminor()
def c15f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDminor()
def c16f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpminor()
def c17f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEminor()
def c18f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFminor()
def c19f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpminor()
def c20f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGminor()
def c21f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpminor()
def c22f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAminor()
def c23f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpminor()
def c24f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBminor()
def c25f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCdiminished()
def c26f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpdiminished()
def c27f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDdiminished()
def c28f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpdiminished()
def c29f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEdiminished()
def c30f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFdiminished()
def c31f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpdiminished()
def c32f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGdiminished()
def c33f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpdiminished()
def c34f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAdiminished()
def c35f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpdiminished()
def c36f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBdiminished()
def c37f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCmajor7()
def c38f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpmajor7()
def c39f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDmajor7()
def c40f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpmajor7()
def c41f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEmajor7()
def c42f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFmajor7()
def c43f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpmajor7()
def c44f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGmajor7()
def c45f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpmajor7()
def c46f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAmajor7()
def c47f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpmajor7()
def c48f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBmajor7()
def c49f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCminor7()
def c50f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpminor7()
def c51f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDminor7()
def c52f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpminor7()
def c53f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEminor7()
def c54f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFminor7()
def c55f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpminor7()
def c56f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGminor7()
def c57f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpminor7()
def c58f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAminor7()
def c59f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpminor7()
def c60f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBminor7()
def c61f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCdominant7()
def c62f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpdominant7()
def c63f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDdominant7()
def c64f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpdominant7()
def c65f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEdominant7()
def c66f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFdominant7()
def c67f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpdominant7()
def c68f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGdominant7()
def c69f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpdominant7()
def c70f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAdominant7()
def c71f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpdominant7()
def c72f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBdominant7()
def c73f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCminor7flat5()
def c74f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordCsharpminor7flat5()
def c75f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDminor7flat5()
def c76f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordDsharpminor7flat5()
def c77f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordEminor7flat5()
def c78f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFminor7flat5()
def c79f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordFsharpminor7flat5()
def c80f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGminor7flat5()
def c81f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordGsharpminor7flat5()
def c82f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAminor7flat5()
def c83f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordAsharpminor7flat5()
def c84f():
    resetguitar()
    if(flag==1):
        c_major_show()
    elif(flag==2):
        c_sharp_major_show()
    elif(flag==3):
        d_major_show()
    elif(flag==4):
        d_sharp_major_show()
    elif(flag==5):
        e_major_show()
    elif(flag==6):
        f_major_show()
    elif(flag==7):
        f_sharp_major_show()
    elif(flag==8):
        g_major_show()
    elif(flag==9):
        g_sharp_major_show()
    elif(flag==10):
        a_major_show()
    elif(flag==11):
        a_sharp_major_show()
    elif(flag==12):
        b_major_show()
    chordBminor7flat5()
#################################Chord Scale Button ##########################################
c1=Button(frame_chord,text='C',command=c1f)
c2=Button(frame_chord,text='C#',command=c2f)
c3=Button(frame_chord,text='D',command=c3f)
c4=Button(frame_chord,text='D#',command=c4f)
c5=Button(frame_chord,text='E',command=c5f)
c6=Button(frame_chord,text='F',command=c6f)
c7=Button(frame_chord,text='F#',command=c7f)
c8=Button(frame_chord,text='G',command=c8f)
c9=Button(frame_chord,text='G#',command=c9f)
c10=Button(frame_chord,text='A',command=c10f)
c11=Button(frame_chord,text='A#',command=c11f)
c12=Button(frame_chord,text='B',command=c12f)
c13=Button(frame_chord,text='Cm',command=c13f)
c14=Button(frame_chord,text='C#m',command=c14f)
c15=Button(frame_chord,text='Dm',command=c15f)
c16=Button(frame_chord,text='D#m',command=c16f)
c17=Button(frame_chord,text='Em',command=c17f)
c18=Button(frame_chord,text='Fm',command=c18f)
c19=Button(frame_chord,text='F#m',command=c19f)
c20=Button(frame_chord,text='Gm',command=c20f)
c21=Button(frame_chord,text='G#m',command=c21f)
c22=Button(frame_chord,text='Am',command=c22f)
c23=Button(frame_chord,text='A#m',command=c23f)
c24=Button(frame_chord,text='Bm',command=c24f)
c25=Button(frame_chord,text='Cdim',command=c25f)
c26=Button(frame_chord,text='C#dim',command=c26f)
c27=Button(frame_chord,text='Ddim',command=c27f)
c28=Button(frame_chord,text='D#dim',command=c28f)
c29=Button(frame_chord,text='Edim',command=c29f)
c30=Button(frame_chord,text='Fdim',command=c30f)
c31=Button(frame_chord,text='F#dim',command=c31f)
c32=Button(frame_chord,text='Gdim',command=c32f)
c33=Button(frame_chord,text='G#dim',command=c33f)
c34=Button(frame_chord,text='Adim',command=c34f)
c35=Button(frame_chord,text='A#dim',command=c35f)
c36=Button(frame_chord,text='Bdim',command=c36f)
c37=Button(frame_chord,text='Cmaj7',command=c37f)
c38=Button(frame_chord,text='C#maj7',command=c38f)
c39=Button(frame_chord,text='Dmaj7',command=c39f)
c40=Button(frame_chord,text='D#maj7',command=c40f)
c41=Button(frame_chord,text='Emaj7',command=c41f)
c42=Button(frame_chord,text='Fmaj7',command=c42f)
c43=Button(frame_chord,text='F#maj7',command=c43f)
c44=Button(frame_chord,text='Gmaj7',command=c44f)
c45=Button(frame_chord,text='G#maj7',command=c45f)
c46=Button(frame_chord,text='Amaj7',command=c46f)
c47=Button(frame_chord,text='A#maj7',command=c47f)
c48=Button(frame_chord,text='Bmaj7',command=c48f)
c49=Button(frame_chord,text='Cmin7',command=c49f)
c50=Button(frame_chord,text='C#min7',command=c50f)
c51=Button(frame_chord,text='Dmin7',command=c51f)
c52=Button(frame_chord,text='D#min7',command=c52f)
c53=Button(frame_chord,text='Emin7',command=c53f)
c54=Button(frame_chord,text='Fmin7',command=c54f)
c55=Button(frame_chord,text='F#min7',command=c55f)
c56=Button(frame_chord,text='Gmin7',command=c56f)
c57=Button(frame_chord,text='G#min7',command=c57f)
c58=Button(frame_chord,text='Amin7',command=c58f)
c59=Button(frame_chord,text='A#min7',command=c59f)
c60=Button(frame_chord,text='Bmin7',command=c60f) 
c61=Button(frame_chord,text='Cdom7',command=c61f)
c62=Button(frame_chord,text='C#dom7',command=c62f)
c63=Button(frame_chord,text='Ddom7',command=c63f)
c64=Button(frame_chord,text='D#dom7',command=c64f)
c65=Button(frame_chord,text='Edom7',command=c65f)
c66=Button(frame_chord,text='Fdom7',command=c66f)
c67=Button(frame_chord,text='F#dom7',command=c67f)
c68=Button(frame_chord,text='Gdom7',command=c68f)
c69=Button(frame_chord,text='G#dom7',command=c69f)
c70=Button(frame_chord,text='Adom7',command=c70f)
c71=Button(frame_chord,text='A#dom7',command=c71f)
c72=Button(frame_chord,text='Bdom7',command=c72f)
c73=Button(frame_chord,text='Cmin7b5',command=c73f)
c74=Button(frame_chord,text='C#min7b5',command=c74f)
c75=Button(frame_chord,text='Dmin7b5',command=c75f)
c76=Button(frame_chord,text='D#min7b5',command=c76f)
c77=Button(frame_chord,text='Emin7b5',command=c77f)
c78=Button(frame_chord,text='Fmin7b5',command=c78f)
c79=Button(frame_chord,text='F#min7b5',command=c79f)
c80=Button(frame_chord,text='Gmin7b5',command=c80f)
c81=Button(frame_chord,text='G#min7b5',command=c81f)
c82=Button(frame_chord,text='Amin7b5',command=c82f)
c83=Button(frame_chord,text='A#min7b5',command=c83f)
c84=Button(frame_chord,text='Bmin7b5',command=c84f)
########################show scale
def showscale1():
    resetchords()
    resetguitar()
    global flag
    flag=1
    c_major_show()
    c1.config(bg='yellow')
    def flashb1(event):
       c1.config(bg = 'green')
       root.after(175, lambda: c1.config(bg = 'yellow'))
       c1f()
    root.bind('<KeyPress-F1>', flashb1)
    c1.place(x=0,y=30,height=30,width=80)
    c15.config(bg='yellow')
    def flashb2(event):
       c15.config(bg = 'green')
       root.after(175, lambda: c15.config(bg = 'yellow'))
       c15f()
    root.bind('<KeyPress-F2>', flashb2)
    c15.place(x=90,y=30,height=30,width=80)
    c17.config(bg='yellow')
    def flashb3(event):
       c17.config(bg = 'green')
       root.after(175, lambda: c17.config(bg = 'yellow'))
       c17f()
    root.bind('<KeyPress-F3>', flashb3)
    c17.place(x=180,y=30,height=30,width=80)
    c6.config(bg='yellow')
    def flashb4(event):
       c6.config(bg = 'green')
       root.after(175, lambda: c6.config(bg = 'yellow'))
       c6f()
    root.bind('<KeyPress-F4>', flashb4)
    c6.place(x=270,y=30,height=30,width=80)
    c8.config(bg='yellow')
    def flashb5(event):
       c8.config(bg = 'green')
       root.after(175, lambda: c8.config(bg = 'yellow'))
       c8f()
    root.bind('<KeyPress-F5>', flashb5)
    c8.place(x=360,y=30,height=30,width=80)
    c22.config(bg='yellow')
    def flashb6(event):
       c22.config(bg = 'green')
       root.after(175, lambda: c22.config(bg = 'yellow'))
       c22f()
    root.bind('<KeyPress-F6>', flashb6)
    c22.place(x=450,y=30,height=30,width=80)
    c36.config(bg='yellow')
    def flashb7(event):
       c36.config(bg = 'green')
       root.after(175, lambda: c36.config(bg = 'yellow'))
       c36f()
    root.bind('<KeyPress-F7>', flashb7)
    c36.place(x=560,y=30,height=30,width=80)
    c37.config(bg='yellow')
    def flashb8(event):
       c37.config(bg = 'green')
       root.after(175, lambda: c37.config(bg = 'yellow'))
       c37f()
    root.bind('<KeyPress-Q>', flashb8)
    c37.place(x=0,y=60,height=30,width=80)
    c51.config(bg='yellow')
    def flashb9(event):
       c51.config(bg = 'green')
       root.after(175, lambda: c51.config(bg = 'yellow'))
       c51f()
    root.bind('<KeyPress-W>', flashb9)
    c51.place(x=90,y=60,height=30,width=80)
    c53.config(bg='yellow')
    def flashb10(event):
       c53.config(bg = 'green')
       root.after(175, lambda: c53.config(bg = 'yellow'))
       c53f()
    root.bind('<KeyPress-E>', flashb10)
    c53.place(x=180,y=60,height=30,width=80)
    c42.config(bg='yellow')
    def flashb11(event):
       c42.config(bg = 'green')
       root.after(175, lambda: c42.config(bg = 'yellow'))
       c42f()
    root.bind('<KeyPress-R>', flashb11)
    c42.place(x=270,y=60,height=30,width=80)
    c68.config(bg='yellow')
    def flashb12(event):
       c68.config(bg = 'green')
       root.after(175, lambda: c68.config(bg = 'yellow'))
       c68f()
    root.bind('<KeyPress-T>', flashb12)
    c68.place(x=360,y=60,height=30,width=80)
    c58.config(bg='yellow')
    def flashb13(event):
       c58.config(bg = 'green')
       root.after(175, lambda: c58.config(bg = 'yellow'))
       c58f()
    root.bind('<KeyPress-Y>', flashb13)
    c58.place(x=450,y=60,height=30,width=80)
    c84.config(bg='yellow')
    def flashb14(event):
       c84.config(bg = 'green')
       root.after(175, lambda: c84.config(bg = 'yellow'))
       c84f()
    root.bind('<KeyPress-U>', flashb14)
    c84.place(x=560,y=60,height=30,width=80)
def showscale2():
    resetchords()
    resetguitar()
    global flag
    flag=2
    c_sharp_major_show()
    c2.config(bg='orange')
    def flashb1(event):
       c2.config(bg = 'green')
       root.after(175, lambda: c2.config(bg = 'orange'))
       c2f()
    root.bind('<KeyPress-F1>', flashb1)
    c2.place(x=0,y=30,height=30,width=80)
    c16.config(bg='orange')
    def flashb2(event):
       c16.config(bg = 'green')
       root.after(175, lambda: c16.config(bg = 'orange'))
       c16f()
    root.bind('<KeyPress-F2>', flashb2)
    c16.place(x=90,y=30,height=30,width=80)
    c18.config(bg='orange')
    def flashb3(event):
       c18.config(bg = 'green')
       root.after(175, lambda: c18.config(bg = 'orange'))
       c18f()
    root.bind('<KeyPress-F3>', flashb3)
    c18.place(x=180,y=30,height=30,width=80)
    c7.config(bg='orange')
    def flashb4(event):
       c7.config(bg = 'green')
       root.after(175, lambda: c7.config(bg = 'orange'))
       c7f()
    root.bind('<KeyPress-F4>', flashb4)
    c7.place(x=270,y=30,height=30,width=80)
    c9.config(bg='orange')
    def flashb5(event):
       c9.config(bg = 'green')
       root.after(175, lambda: c9.config(bg = 'orange'))
       c9f()
    root.bind('<KeyPress-F5>', flashb5)
    c9.place(x=360,y=30,height=30,width=80)
    c23.config(bg='orange')
    def flashb6(event):
       c23.config(bg = 'green')
       root.after(175, lambda: c23.config(bg = 'orange'))
       c23f()
    root.bind('<KeyPress-F6>', flashb6)
    c23.place(x=450,y=30,height=30,width=80)
    c25.config(bg='orange')
    def flashb7(event):
       c25.config(bg = 'green')
       root.after(175, lambda: c25.config(bg = 'orange'))
       c25f()
    root.bind('<KeyPress-F7>', flashb7)
    c25.place(x=560,y=30,height=30,width=80)
    c38.config(bg='orange')
    def flashb8(event):
       c38.config(bg = 'green')
       root.after(175, lambda: c38.config(bg = 'orange'))
       c38f()
    root.bind('<KeyPress-Q>', flashb8)
    c38.place(x=0,y=60,height=30,width=80)
    c52.config(bg='orange')
    def flashb9(event):
       c52.config(bg = 'green')
       root.after(175, lambda: c52.config(bg = 'orange'))
       c52f()
    root.bind('<KeyPress-W>', flashb9)
    c52.place(x=90,y=60,height=30,width=80)
    c54.config(bg='orange')
    def flashb10(event):
       c54.config(bg = 'green')
       root.after(175, lambda: c54.config(bg = 'orange'))
       c54f()
    root.bind('<KeyPress-E>', flashb10)
    c54.place(x=180,y=60,height=30,width=80)
    c43.config(bg='orange')
    def flashb11(event):
       c43.config(bg = 'green')
       root.after(175, lambda: c43.config(bg = 'orange'))
       c43f()
    root.bind('<KeyPress-R>', flashb11)
    c43.place(x=270,y=60,height=30,width=80)
    c69.config(bg='orange')
    def flashb12(event):
       c69.config(bg = 'green')
       root.after(175, lambda: c69.config(bg = 'orange'))
       c69f()
    root.bind('<KeyPress-T>', flashb12)
    c69.place(x=360,y=60,height=30,width=80)
    c59.config(bg='orange')
    def flashb13(event):
       c59.config(bg = 'green')
       root.after(175, lambda: c59.config(bg = 'orange'))
       c59f()
    root.bind('<KeyPress-Y>', flashb13)
    c59.place(x=450,y=60,height=30,width=80)
    c73.config(bg='orange')
    def flashb14(event):
       c73.config(bg = 'green')
       root.after(175, lambda: c73.config(bg = 'orange'))
       c73f()
    root.bind('<KeyPress-U>', flashb14)
    c73.place(x=560,y=60,height=30,width=80)
def showscale3():
    resetchords()
    resetguitar()
    global flag
    flag=3
    d_major_show()
    c3.config(bg='#944187')
    def flashb1(event):
       c3.config(bg = 'green')
       root.after(175, lambda: c3.config(bg = '#944187'))
       c3f()
    root.bind('<KeyPress-F1>', flashb1)
    c3.place(x=0,y=30,height=30,width=80)
    c17.config(bg='#944187')
    def flashb2(event):
       c17.config(bg = 'green')
       root.after(175, lambda: c17.config(bg = '#944187'))
       c17f()
    root.bind('<KeyPress-F2>', flashb2)
    c17.place(x=90,y=30,height=30,width=80)
    c19.config(bg='#944187')
    def flashb3(event):
       c19.config(bg = 'green')
       root.after(175, lambda: c19.config(bg = '#944187'))
       c19f()
    root.bind('<KeyPress-F3>', flashb3)
    c19.place(x=180,y=30,height=30,width=80)
    c8.config(bg='#944187')
    def flashb4(event):
       c8.config(bg = 'green')
       root.after(175, lambda: c8.config(bg = '#944187'))
       c8f()
    root.bind('<KeyPress-F4>', flashb4)
    c8.place(x=270,y=30,height=30,width=80)
    c10.config(bg='#944187')
    def flashb5(event):
       c10.config(bg = 'green')
       root.after(175, lambda: c10.config(bg = '#944187'))
       c10f()
    root.bind('<KeyPress-F5>', flashb5)
    c10.place(x=360,y=30,height=30,width=80)
    c24.config(bg='#944187')
    def flashb6(event):
       c24.config(bg = 'green')
       root.after(175, lambda: c24.config(bg = '#944187'))
       c24f()
    root.bind('<KeyPress-F6>', flashb6)
    c24.place(x=450,y=30,height=30,width=80)
    c26.config(bg='#944187')
    def flashb7(event):
       c26.config(bg = 'green')
       root.after(175, lambda: c26.config(bg = '#944187'))
       c26f()
    root.bind('<KeyPress-F7>', flashb7)
    c26.place(x=560,y=30,height=30,width=80)
    c39.config(bg='#944187')
    def flashb8(event):
       c39.config(bg = 'green')
       root.after(175, lambda: c39.config(bg = '#944187'))
       c39f()
    root.bind('<KeyPress-Q>', flashb8)
    c39.place(x=0,y=60,height=30,width=80)
    c53.config(bg='#944187')
    def flashb9(event):
       c53.config(bg = 'green')
       root.after(175, lambda: c53.config(bg = '#944187'))
       c53f()
    root.bind('<KeyPress-W>', flashb9)
    c53.place(x=90,y=60,height=30,width=80)
    c55.config(bg='#944187')
    def flashb10(event):
       c55.config(bg = 'green')
       root.after(175, lambda: c55.config(bg = '#944187'))
       c55f()
    root.bind('<KeyPress-E>', flashb10)
    c55.place(x=180,y=60,height=30,width=80)
    c44.config(bg='#944187')
    def flashb11(event):
       c44.config(bg = 'green')
       root.after(175, lambda: c44.config(bg = '#944187'))
       c44f()
    root.bind('<KeyPress-R>', flashb11)
    c44.place(x=270,y=60,height=30,width=80)
    c70.config(bg='#944187')
    def flashb12(event):
       c70.config(bg = 'green')
       root.after(175, lambda: c70.config(bg = '#944187'))
       c70f()
    root.bind('<KeyPress-T>', flashb12)
    c70.place(x=360,y=60,height=30,width=80)
    c60.config(bg='#944187')
    def flashb13(event):
       c60.config(bg = 'green')
       root.after(175, lambda: c60.config(bg = '#944187'))
       c60f()
    root.bind('<KeyPress-Y>', flashb13)
    c60.place(x=450,y=60,height=30,width=80)
    c74.config(bg='#944187')
    def flashb14(event):
       c74.config(bg = 'green')
       root.after(175, lambda: c74.config(bg = '#944187'))
       c74f()
    root.bind('<KeyPress-U>', flashb14)
    c74.place(x=560,y=60,height=30,width=80)
def showscale4():
    resetchords()
    resetguitar()
    global flag
    flag=4
    d_sharp_major_show()
    c4.config(bg='#6fedd0')
    def flashb1(event):
       c4.config(bg = 'green')
       root.after(175, lambda: c4.config(bg = '#6fedd0'))
       c4f()
    root.bind('<KeyPress-F1>', flashb1)
    c4.place(x=0,y=30,height=30,width=80)
    c18.config(bg='#6fedd0')
    def flashb2(event):
       c18.config(bg = 'green')
       root.after(175, lambda: c18.config(bg = '#6fedd0'))
       c18f()
    root.bind('<KeyPress-F2>', flashb2)
    c18.place(x=90,y=30,height=30,width=80)
    c20.config(bg='#6fedd0')
    def flashb3(event):
       c20.config(bg = 'green')
       root.after(175, lambda: c20.config(bg = '#6fedd0'))
       c20f()
    root.bind('<KeyPress-F3>', flashb3)
    c20.place(x=180,y=30,height=30,width=80)
    c9.config(bg='#6fedd0')
    def flashb4(event):
       c9.config(bg = 'green')
       root.after(175, lambda: c9.config(bg = '#6fedd0'))
       c9f()
    root.bind('<KeyPress-F4>', flashb4)
    c9.place(x=270,y=30,height=30,width=80)
    c11.config(bg='#6fedd0')
    def flashb5(event):
       c11.config(bg = 'green')
       root.after(175, lambda: c11.config(bg = '#6fedd0'))
       c11f()
    root.bind('<KeyPress-F5>', flashb5)
    c11.place(x=360,y=30,height=30,width=80)
    c13.config(bg='#6fedd0')
    def flashb6(event):
       c13.config(bg = 'green')
       root.after(175, lambda: c13.config(bg = '#6fedd0'))
       c13f()
    root.bind('<KeyPress-F6>', flashb6)
    c13.place(x=450,y=30,height=30,width=80)
    c27.config(bg='#6fedd0')
    def flashb7(event):
       c27.config(bg = 'green')
       root.after(175, lambda: c27.config(bg = '#6fedd0'))
       c27f()
    root.bind('<KeyPress-F7>', flashb7)
    c27.place(x=560,y=30,height=30,width=80)
    c40.config(bg='#6fedd0')
    def flashb8(event):
       c40.config(bg = 'green')
       root.after(175, lambda: c40.config(bg = '#6fedd0'))
       c40f()
    root.bind('<KeyPress-Q>', flashb8)
    c40.place(x=0,y=60,height=30,width=80)
    c54.config(bg='#6fedd0')
    def flashb9(event):
       c54.config(bg = 'green')
       root.after(175, lambda: c54.config(bg = '#6fedd0'))
       c54f()
    root.bind('<KeyPress-W>', flashb9)
    c54.place(x=90,y=60,height=30,width=80)
    c56.config(bg='#6fedd0')
    def flashb10(event):
       c56.config(bg = 'green')
       root.after(175, lambda: c56.config(bg = '#6fedd0'))
       c56f()
    root.bind('<KeyPress-E>', flashb10)
    c56.place(x=180,y=60,height=30,width=80)
    c45.config(bg='#6fedd0')
    def flashb11(event):
       c45.config(bg = 'green')
       root.after(175, lambda: c45.config(bg = '#6fedd0'))
       c45f()
    root.bind('<KeyPress-R>', flashb11)
    c45.place(x=270,y=60,height=30,width=80)
    c71.config(bg='#6fedd0')
    def flashb12(event):
       c71.config(bg = 'green')
       root.after(175, lambda: c71.config(bg = '#6fedd0'))
       c71f()
    root.bind('<KeyPress-T>', flashb12)
    c71.place(x=360,y=60,height=30,width=80)
    c49.config(bg='#6fedd0')
    def flashb13(event):
       c49.config(bg = 'green')
       root.after(175, lambda: c49.config(bg = '#6fedd0'))
       c49f()
    root.bind('<KeyPress-Y>', flashb13)
    c49.place(x=450,y=60,height=30,width=80)
    c75.config(bg='#6fedd0')
    def flashb14(event):
       c75.config(bg = 'green')
       root.after(175, lambda: c75.config(bg = '#6fedd0'))
       c75f()
    root.bind('<KeyPress-U>', flashb14)
    c75.place(x=560,y=60,height=30,width=80)
def showscale5():
    resetchords()
    resetguitar()
    global flag
    flag=5
    e_major_show()
    c5.config(bg='#e39ad8')
    def flashb1(event):
       c5.config(bg = 'green')
       root.after(175, lambda: c5.config(bg = '#e39ad8'))
       c5f()
    root.bind('<KeyPress-F1>', flashb1)
    c5.place(x=0,y=30,height=30,width=80)
    c19.config(bg='#e39ad8')
    def flashb2(event):
       c19.config(bg = 'green')
       root.after(175, lambda: c19.config(bg = '#e39ad8'))
       c19f()
    root.bind('<KeyPress-F2>', flashb2)
    c19.place(x=90,y=30,height=30,width=80)
    c21.config(bg='#e39ad8')
    def flashb3(event):
       c21.config(bg = 'green')
       root.after(175, lambda: c21.config(bg = '#e39ad8'))
       c21f()
    root.bind('<KeyPress-F3>', flashb3)
    c21.place(x=180,y=30,height=30,width=80)
    c10.config(bg='#e39ad8')
    def flashb4(event):
       c10.config(bg = 'green')
       root.after(175, lambda: c10.config(bg = '#e39ad8'))
       c10f()
    root.bind('<KeyPress-F4>', flashb4)
    c10.place(x=270,y=30,height=30,width=80)
    c12.config(bg='#e39ad8')
    def flashb5(event):
       c12.config(bg = 'green')
       root.after(175, lambda: c12.config(bg = '#e39ad8'))
       c12f()
    root.bind('<KeyPress-F5>', flashb5)
    c12.place(x=360,y=30,height=30,width=80)
    c14.config(bg='#e39ad8')
    def flashb6(event):
       c14.config(bg = 'green')
       root.after(175, lambda: c14.config(bg = '#e39ad8'))
       c14f()
    root.bind('<KeyPress-F6>', flashb6)
    c14.place(x=450,y=30,height=30,width=80)
    c28.config(bg='#e39ad8')
    def flashb7(event):
       c28.config(bg = 'green')
       root.after(175, lambda: c28.config(bg = '#e39ad8'))
       c28f()
    root.bind('<KeyPress-F7>', flashb7)
    c28.place(x=560,y=30,height=30,width=80)
    c41.config(bg='#e39ad8')
    def flashb8(event):
       c41.config(bg = 'green')
       root.after(175, lambda: c41.config(bg = '#e39ad8'))
       c41f()
    root.bind('<KeyPress-Q>', flashb8)
    c41.place(x=0,y=60,height=30,width=80)
    c55.config(bg='#e39ad8')
    def flashb9(event):
       c55.config(bg = 'green')
       root.after(175, lambda: c55.config(bg = '#e39ad8'))
       c55f()
    root.bind('<KeyPress-W>', flashb9)
    c55.place(x=90,y=60,height=30,width=80)
    c57.config(bg='#e39ad8')
    def flashb10(event):
       c57.config(bg = 'green')
       root.after(175, lambda: c57.config(bg = '#e39ad8'))
       c57f()
    root.bind('<KeyPress-E>', flashb10)
    c57.place(x=180,y=60,height=30,width=80)
    c46.config(bg='#e39ad8')
    def flashb11(event):
       c46.config(bg = 'green')
       root.after(175, lambda: c46.config(bg = '#e39ad8'))
       c46f()
    root.bind('<KeyPress-R>', flashb11)
    c46.place(x=270,y=60,height=30,width=80)
    c72.config(bg='#e39ad8')
    def flashb12(event):
       c72.config(bg = 'green')
       root.after(175, lambda: c72.config(bg = '#e39ad8'))
       c72f()
    root.bind('<KeyPress-T>', flashb12)
    c72.place(x=360,y=60,height=30,width=80)
    c50.config(bg='#e39ad8')
    def flashb13(event):
       c50.config(bg = 'green')
       root.after(175, lambda: c50.config(bg = '#e39ad8'))
       c50f()
    root.bind('<KeyPress-Y>', flashb13)
    c50.place(x=450,y=60,height=30,width=80)
    c76.config(bg='#e39ad8')
    def flashb14(event):
       c76.config(bg = 'green')
       root.after(175, lambda: c76.config(bg = '#e39ad8'))
       c76f()
    root.bind('<KeyPress-U>', flashb14)
    c76.place(x=560,y=60,height=30,width=80)
def showscale6():
    resetchords()
    resetguitar()
    global flag
    flag=6
    f_major_show()
    c6.config(bg='#ffc830')
    def flashb1(event):
       c6.config(bg = 'green')
       root.after(175, lambda: c6.config(bg = '#ffc830'))
       c6f()
    root.bind('<KeyPress-F1>', flashb1)
    c6.place(x=0,y=30,height=30,width=80)
    c20.config(bg='#ffc830')
    def flashb2(event):
       c20.config(bg = 'green')
       root.after(175, lambda: c20.config(bg = '#ffc830'))
       c20f()
    root.bind('<KeyPress-F2>', flashb2)
    c20.place(x=90,y=30,height=30,width=80)
    c22.config(bg='#ffc830')
    def flashb3(event):
       c22.config(bg = 'green')
       root.after(175, lambda: c22.config(bg = '#ffc830'))
       c22f()
    root.bind('<KeyPress-F3>', flashb3)
    c22.place(x=180,y=30,height=30,width=80)
    c11.config(bg='#ffc830')
    def flashb4(event):
       c11.config(bg = 'green')
       root.after(175, lambda: c11.config(bg = '#ffc830'))
       c11f()
    root.bind('<KeyPress-F4>', flashb4)
    c11.place(x=270,y=30,height=30,width=80)
    c1.config(bg='#ffc830')
    def flashb5(event):
       c1.config(bg = 'green')
       root.after(175, lambda: c1.config(bg = '#ffc830'))
       c1f()
    root.bind('<KeyPress-F5>', flashb5)
    c1.place(x=360,y=30,height=30,width=80)
    c15.config(bg='#ffc830')
    def flashb6(event):
       c15.config(bg = 'green')
       root.after(175, lambda: c15.config(bg = '#ffc830'))
       c15f()
    root.bind('<KeyPress-F6>', flashb6)
    c15.place(x=450,y=30,height=30,width=80)
    c29.config(bg='#ffc830')
    def flashb7(event):
       c29.config(bg = 'green')
       root.after(175, lambda: c29.config(bg = '#ffc830'))
       c29f()
    root.bind('<KeyPress-F7>', flashb7)
    c29.place(x=560,y=30,height=30,width=80)
    c42.config(bg='#ffc830')
    def flashb8(event):
       c42.config(bg = 'green')
       root.after(175, lambda: c42.config(bg = '#ffc830'))
       c42f()
    root.bind('<KeyPress-Q>', flashb8)
    c42.place(x=0,y=60,height=30,width=80)
    c56.config(bg='#ffc830')
    def flashb9(event):
       c56.config(bg = 'green')
       root.after(175, lambda: c56.config(bg = '#ffc830'))
       c56f()
    root.bind('<KeyPress-W>', flashb9)
    c56.place(x=90,y=60,height=30,width=80)
    c58.config(bg='#ffc830')
    def flashb10(event):
       c58.config(bg = 'green')
       root.after(175, lambda: c58.config(bg = '#ffc830'))
       c58f()
    root.bind('<KeyPress-E>', flashb10)
    c58.place(x=180,y=60,height=30,width=80)
    c47.config(bg='#ffc830')
    def flashb11(event):
       c47.config(bg = 'green')
       root.after(175, lambda: c47.config(bg = '#ffc830'))
       c47f()
    root.bind('<KeyPress-R>', flashb11)
    c47.place(x=270,y=60,height=30,width=80)
    c61.config(bg='#ffc830')
    def flashb12(event):
       c61.config(bg = 'green')
       root.after(175, lambda: c61.config(bg = '#ffc830'))
       c61f()
    root.bind('<KeyPress-T>', flashb12)
    c61.place(x=360,y=60,height=30,width=80)
    c51.config(bg='#ffc830')
    def flashb13(event):
       c51.config(bg = 'green')
       root.after(175, lambda: c51.config(bg = '#ffc830'))
       c51f()
    root.bind('<KeyPress-Y>', flashb13)
    c51.place(x=450,y=60,height=30,width=80)
    c77.config(bg='#ffc830')
    def flashb14(event):
       c77.config(bg = 'green')
       root.after(175, lambda: c77.config(bg = '#ffc830'))
       c77f()
    root.bind('<KeyPress-U>', flashb14)
    c77.place(x=560,y=60,height=30,width=80)
def showscale7():
    resetchords()
    resetguitar()
    global flag
    flag=7
    f_sharp_major_show()
    c7.config(bg='#f7929a')
    def flashb1(event):
       c7.config(bg = 'green')
       root.after(175, lambda: c7.config(bg = '#f7929a'))
       c7f()
    root.bind('<KeyPress-F1>', flashb1)
    c7.place(x=0,y=30,height=30,width=80)
    c21.config(bg='#f7929a')
    def flashb2(event):
       c21.config(bg = 'green')
       root.after(175, lambda: c21.config(bg = '#f7929a'))
       c21f()
    root.bind('<KeyPress-F2>', flashb2)
    c21.place(x=90,y=30,height=30,width=80)
    c23.config(bg='#f7929a')
    def flashb3(event):
       c23.config(bg = 'green')
       root.after(175, lambda: c23.config(bg = '#f7929a'))
       c23f()
    root.bind('<KeyPress-F3>', flashb3)
    c23.place(x=180,y=30,height=30,width=80)
    c12.config(bg='#f7929a')
    def flashb4(event):
       c12.config(bg = 'green')
       root.after(175, lambda: c12.config(bg = '#f7929a'))
       c12f()
    root.bind('<KeyPress-F4>', flashb4)
    c12.place(x=270,y=30,height=30,width=80)
    c2.config(bg='#f7929a')
    def flashb5(event):
       c2.config(bg = 'green')
       root.after(175, lambda: c2.config(bg = '#f7929a'))
       c2f()
    root.bind('<KeyPress-F5>', flashb5)
    c2.place(x=360,y=30,height=30,width=80)
    c16.config(bg='#f7929a')
    def flashb6(event):
       c16.config(bg = 'green')
       root.after(175, lambda: c16.config(bg = '#f7929a'))
       c16f()
    root.bind('<KeyPress-F6>', flashb6)
    c16.place(x=450,y=30,height=30,width=80)
    c30.config(bg='#f7929a')
    def flashb7(event):
       c30.config(bg = 'green')
       root.after(175, lambda: c30.config(bg = '#f7929a'))
       c30f()
    root.bind('<KeyPress-F7>', flashb7)
    c30.place(x=560,y=30,height=30,width=80)
    c43.config(bg='#f7929a')
    def flashb8(event):
       c43.config(bg = 'green')
       root.after(175, lambda: c43.config(bg = '#f7929a'))
       c43f()
    root.bind('<KeyPress-Q>', flashb8)
    c43.place(x=0,y=60,height=30,width=80)
    c57.config(bg='#f7929a')
    def flashb9(event):
       c57.config(bg = 'green')
       root.after(175, lambda: c57.config(bg = '#f7929a'))
       c57f()
    root.bind('<KeyPress-W>', flashb9)
    c57.place(x=90,y=60,height=30,width=80)
    c59.config(bg='#f7929a')
    def flashb10(event):
       c59.config(bg = 'green')
       root.after(175, lambda: c59.config(bg = '#f7929a'))
       c59f()
    root.bind('<KeyPress-E>', flashb10)
    c59.place(x=180,y=60,height=30,width=80)
    c48.config(bg='#f7929a')
    def flashb11(event):
       c48.config(bg = 'green')
       root.after(175, lambda: c48.config(bg = '#f7929a'))
       c48f()
    root.bind('<KeyPress-R>', flashb11)
    c48.place(x=270,y=60,height=30,width=80)
    c62.config(bg='#f7929a')
    def flashb12(event):
       c62.config(bg = 'green')
       root.after(175, lambda: c62.config(bg = '#f7929a'))
       c62f()
    root.bind('<KeyPress-T>', flashb12)
    c62.place(x=360,y=60,height=30,width=80)
    c52.config(bg='#f7929a')
    def flashb13(event):
       c52.config(bg = 'green')
       root.after(175, lambda: c52.config(bg = '#f7929a'))
       c52f()
    root.bind('<KeyPress-Y>', flashb13)
    c52.place(x=450,y=60,height=30,width=80)
    c78.config(bg='#f7929a')
    def flashb14(event):
       c78.config(bg = 'green')
       root.after(175, lambda: c78.config(bg = '#f7929a'))
       c78f()
    root.bind('<KeyPress-U>', flashb14)
    c78.place(x=560,y=60,height=30,width=80)
def showscale8():
    resetchords()
    resetguitar()
    global flag
    flag=8
    g_major_show()
    c8.config(bg='#a8edaf')
    def flashb1(event):
       c8.config(bg = 'green')
       root.after(175, lambda: c8.config(bg = '#a8edaf'))
       c8f()
    root.bind('<KeyPress-F1>', flashb1)
    c8.place(x=0,y=30,height=30,width=80)
    c22.config(bg='#a8edaf')
    def flashb2(event):
       c22.config(bg = 'green')
       root.after(175, lambda: c22.config(bg = '#a8edaf'))
       c22f()
    root.bind('<KeyPress-F2>', flashb2)
    c22.place(x=90,y=30,height=30,width=80)
    c24.config(bg='#a8edaf')
    def flashb3(event):
       c24.config(bg = 'green')
       root.after(175, lambda: c24.config(bg = '#a8edaf'))
       c24f()
    root.bind('<KeyPress-F3>', flashb3)
    c24.place(x=180,y=30,height=30,width=80)
    c1.config(bg='#a8edaf')
    def flashb4(event):
       c1.config(bg = 'green')
       root.after(175, lambda: c1.config(bg = '#a8edaf'))
       c1f()
    root.bind('<KeyPress-F4>', flashb4)
    c1.place(x=270,y=30,height=30,width=80)
    c3.config(bg='#a8edaf')
    def flashb5(event):
       c3.config(bg = 'green')
       root.after(175, lambda: c3.config(bg = '#a8edaf'))
       c3f()
    root.bind('<KeyPress-F5>', flashb5)
    c3.place(x=360,y=30,height=30,width=80)
    c17.config(bg='#a8edaf')
    def flashb6(event):
       c17.config(bg = 'green')
       root.after(175, lambda: c17.config(bg = '#a8edaf'))
       c17f()
    root.bind('<KeyPress-F6>', flashb6)
    c17.place(x=450,y=30,height=30,width=80)
    c31.config(bg='#a8edaf')
    def flashb7(event):
       c31.config(bg = 'green')
       root.after(175, lambda: c31.config(bg = '#a8edaf'))
       c31f()
    root.bind('<KeyPress-F7>', flashb7)
    c31.place(x=560,y=30,height=30,width=80)
    c44.config(bg='#a8edaf')
    def flashb8(event):
       c44.config(bg = 'green')
       root.after(175, lambda: c44.config(bg = '#a8edaf'))
       c44f()
    root.bind('<KeyPress-Q>', flashb8)
    c44.place(x=0,y=60,height=30,width=80)
    c58.config(bg='#a8edaf')
    def flashb9(event):
       c58.config(bg = 'green')
       root.after(175, lambda: c58.config(bg = '#a8edaf'))
       c58f()
    root.bind('<KeyPress-W>', flashb9)
    c58.place(x=90,y=60,height=30,width=80)
    c60.config(bg='#a8edaf')
    def flashb10(event):
       c60.config(bg = 'green')
       root.after(175, lambda: c60.config(bg = '#a8edaf'))
       c60f()
    root.bind('<KeyPress-E>', flashb10)
    c60.place(x=180,y=60,height=30,width=80)
    c37.config(bg='#a8edaf')
    def flashb11(event):
       c37.config(bg = 'green')
       root.after(175, lambda: c37.config(bg = '#a8edaf'))
       c37f()
    root.bind('<KeyPress-R>', flashb11)
    c37.place(x=270,y=60,height=30,width=80)
    c63.config(bg='#a8edaf')
    def flashb12(event):
       c63.config(bg = 'green')
       root.after(175, lambda: c63.config(bg = '#a8edaf'))
       c63f()
    root.bind('<KeyPress-T>', flashb12)
    c63.place(x=360,y=60,height=30,width=80)
    c53.config(bg='#a8edaf')
    def flashb13(event):
       c53.config(bg = 'green')
       root.after(175, lambda: c53.config(bg = '#a8edaf'))
       c53f()
    root.bind('<KeyPress-Y>', flashb13)
    c53.place(x=450,y=60,height=30,width=80)
    c79.config(bg='#a8edaf')
    def flashb14(event):
       c79.config(bg = 'green')
       root.after(175, lambda: c79.config(bg = '#a8edaf'))
       c79f()
    root.bind('<KeyPress-U>', flashb14)
    c79.place(x=560,y=60,height=30,width=80)
def showscale9():
    resetchords()
    resetguitar()
    global flag
    flag=9
    g_sharp_major_show()
    c9.config(bg='#d9a49a')
    def flashb1(event):
       c9.config(bg = 'green')
       root.after(175, lambda: c9.config(bg = '#d9a49a'))
       c9f()
    root.bind('<KeyPress-F1>', flashb1)
    c9.place(x=0,y=30,height=30,width=80)
    c23.config(bg='#d9a49a')
    def flashb2(event):
       c23.config(bg = 'green')
       root.after(175, lambda: c23.config(bg = '#d9a49a'))
       c23f()
    root.bind('<KeyPress-F2>', flashb2)
    c23.place(x=90,y=30,height=30,width=80)
    c13.config(bg='#d9a49a')
    def flashb3(event):
       c13.config(bg = 'green')
       root.after(175, lambda: c13.config(bg = '#d9a49a'))
       c13f()
    root.bind('<KeyPress-F3>', flashb3)
    c13.place(x=180,y=30,height=30,width=80)
    c2.config(bg='#d9a49a')
    def flashb4(event):
       c2.config(bg = 'green')
       root.after(175, lambda: c2.config(bg = '#d9a49a'))
       c2f()
    root.bind('<KeyPress-F4>', flashb4)
    c2.place(x=270,y=30,height=30,width=80)
    c4.config(bg='#d9a49a')
    def flashb5(event):
       c4.config(bg = 'green')
       root.after(175, lambda: c4.config(bg = '#d9a49a'))
       c4f()
    root.bind('<KeyPress-F5>', flashb5)
    c4.place(x=360,y=30,height=30,width=80)
    c18.config(bg='#d9a49a')
    def flashb6(event):
       c18.config(bg = 'green')
       root.after(175, lambda: c18.config(bg = '#d9a49a'))
       c18f()
    root.bind('<KeyPress-F6>', flashb6)
    c18.place(x=450,y=30,height=30,width=80)
    c32.config(bg='#d9a49a')
    def flashb7(event):
       c32.config(bg = 'green')
       root.after(175, lambda: c32.config(bg = '#d9a49a'))
       c32f()
    root.bind('<KeyPress-F7>', flashb7)
    c32.place(x=560,y=30,height=30,width=80)
    c45.config(bg='#d9a49a')
    def flashb8(event):
       c45.config(bg = 'green')
       root.after(175, lambda: c45.config(bg = '#d9a49a'))
       c45f()
    root.bind('<KeyPress-Q>', flashb8)
    c45.place(x=0,y=60,height=30,width=80)
    c59.config(bg='#d9a49a')
    def flashb9(event):
       c59.config(bg = 'green')
       root.after(175, lambda: c59.config(bg = '#d9a49a'))
       c59f()
    root.bind('<KeyPress-W>', flashb9)
    c59.place(x=90,y=60,height=30,width=80)
    c49.config(bg='#d9a49a')
    def flashb10(event):
       c49.config(bg = 'green')
       root.after(175, lambda: c49.config(bg = '#d9a49a'))
       c49f()
    root.bind('<KeyPress-E>', flashb10)
    c49.place(x=180,y=60,height=30,width=80)
    c38.config(bg='#d9a49a')
    def flashb11(event):
       c38.config(bg = 'green')
       root.after(175, lambda: c38.config(bg = '#d9a49a'))
       c38f()
    root.bind('<KeyPress-R>', flashb11)
    c38.place(x=270,y=60,height=30,width=80)
    c64.config(bg='#d9a49a')
    def flashb12(event):
       c64.config(bg = 'green')
       root.after(175, lambda: c64.config(bg = '#d9a49a'))
       c64f()
    root.bind('<KeyPress-T>', flashb12)
    c64.place(x=360,y=60,height=30,width=80)
    c54.config(bg='#d9a49a')
    def flashb13(event):
       c54.config(bg = 'green')
       root.after(175, lambda: c54.config(bg = '#d9a49a'))
       c54f()
    root.bind('<KeyPress-Y>', flashb13)
    c54.place(x=450,y=60,height=30,width=80)
    c80.config(bg='#d9a49a')
    def flashb14(event):
       c80.config(bg = 'green')
       root.after(175, lambda: c80.config(bg = '#d9a49a'))
       c80f()
    root.bind('<KeyPress-U>', flashb14)
    c80.place(x=560,y=60,height=30,width=80)
def showscale10():
    resetchords()
    resetguitar()
    global flag
    flag=10
    a_major_show()
    c10.config(bg='#e6d375')
    def flashb1(event):
       c10.config(bg = 'green')
       root.after(175, lambda: c10.config(bg = '#e6d375'))
       c10f()
    root.bind('<KeyPress-F1>', flashb1)
    c10.place(x=0,y=30,height=30,width=80)
    c24.config(bg='#e6d375')
    def flashb2(event):
       c24.config(bg = 'green')
       root.after(175, lambda: c24.config(bg = '#e6d375'))
       c24f()
    root.bind('<KeyPress-F2>', flashb2)
    c24.place(x=90,y=30,height=30,width=80)
    c14.config(bg='#e6d375')
    def flashb3(event):
       c14.config(bg = 'green')
       root.after(175, lambda: c14.config(bg = '#e6d375'))
       c14f()
    root.bind('<KeyPress-F3>', flashb3)
    c14.place(x=180,y=30,height=30,width=80)
    c3.config(bg='#e6d375')
    def flashb4(event):
       c3.config(bg = 'green')
       root.after(175, lambda: c3.config(bg = '#e6d375'))
       c3f()
    root.bind('<KeyPress-F4>', flashb4)
    c3.place(x=270,y=30,height=30,width=80)
    c5.config(bg='#e6d375')
    def flashb5(event):
       c5.config(bg = 'green')
       root.after(175, lambda: c5.config(bg = '#e6d375'))
       c5f()
    root.bind('<KeyPress-F5>', flashb5)
    c5.place(x=360,y=30,height=30,width=80)
    c19.config(bg='#e6d375')
    def flashb6(event):
       c19.config(bg = 'green')
       root.after(175, lambda: c19.config(bg = '#e6d375'))
       c19f()
    root.bind('<KeyPress-F6>', flashb6)
    c19.place(x=450,y=30,height=30,width=80)
    c33.config(bg='#e6d375')
    def flashb7(event):
       c33.config(bg = 'green')
       root.after(175, lambda: c33.config(bg = '#e6d375'))
       c33f()
    root.bind('<KeyPress-F7>', flashb7)
    c33.place(x=560,y=30,height=30,width=80)
    c46.config(bg='#e6d375')
    def flashb8(event):
       c46.config(bg = 'green')
       root.after(175, lambda: c46.config(bg = '#e6d375'))
       c46f()
    root.bind('<KeyPress-Q>', flashb8)
    c46.place(x=0,y=60,height=30,width=80)
    c60.config(bg='#e6d375')
    def flashb9(event):
       c60.config(bg = 'green')
       root.after(175, lambda: c60.config(bg = '#e6d375'))
       c60f()
    root.bind('<KeyPress-W>', flashb9)
    c60.place(x=90,y=60,height=30,width=80)
    c50.config(bg='#e6d375')
    def flashb10(event):
       c50.config(bg = 'green')
       root.after(175, lambda: c50.config(bg = '#e6d375'))
       c50f()
    root.bind('<KeyPress-E>', flashb10)
    c50.place(x=180,y=60,height=30,width=80)
    c39.config(bg='#e6d375')
    def flashb11(event):
       c39.config(bg = 'green')
       root.after(175, lambda: c39.config(bg = '#e6d375'))
       c39f()
    root.bind('<KeyPress-R>', flashb11)
    c39.place(x=270,y=60,height=30,width=80)
    c65.config(bg='#e6d375')
    def flashb12(event):
       c65.config(bg = 'green')
       root.after(175, lambda: c65.config(bg = '#e6d375'))
       c65f()
    root.bind('<KeyPress-T>', flashb12)
    c65.place(x=360,y=60,height=30,width=80)
    c55.config(bg='#e6d375')
    def flashb13(event):
       c55.config(bg = 'green')
       root.after(175, lambda: c55.config(bg = '#e6d375'))
       c55f()
    root.bind('<KeyPress-Y>', flashb13)
    c55.place(x=450,y=60,height=30,width=80)
    c81.config(bg='#e6d375')
    def flashb14(event):
       c81.config(bg = 'green')
       root.after(175, lambda: c81.config(bg = '#e6d375'))
       c81f()
    root.bind('<KeyPress-U>', flashb14)
    c81.place(x=560,y=60,height=30,width=80)
def showscale11():
    resetchords()
    resetguitar()
    global flag
    flag=11
    a_sharp_major_show()
    c11.config(bg='#a0eb38')
    def flashb1(event):
       c11.config(bg = 'green')
       root.after(175, lambda: c11.config(bg = '#a0eb38'))
       c11f()
    root.bind('<KeyPress-F1>', flashb1)
    c11.place(x=0,y=30,height=30,width=80)
    c13.config(bg='#a0eb38')
    def flashb2(event):
       c13.config(bg = 'green')
       root.after(175, lambda: c13.config(bg = '#a0eb38'))
       c13f()
    root.bind('<KeyPress-F2>', flashb2)
    c13.place(x=90,y=30,height=30,width=80)
    c15.config(bg='#a0eb38')
    def flashb3(event):
       c15.config(bg = 'green')
       root.after(175, lambda: c15.config(bg = '#a0eb38'))
       c15f()
    root.bind('<KeyPress-F3>', flashb3)
    c15.place(x=180,y=30,height=30,width=80)
    c4.config(bg='#a0eb38')
    def flashb4(event):
       c4.config(bg = 'green')
       root.after(175, lambda: c4.config(bg = '#a0eb38'))
       c4f()
    root.bind('<KeyPress-F4>', flashb4)
    c4.place(x=270,y=30,height=30,width=80)
    c6.config(bg='#a0eb38')
    def flashb5(event):
       c6.config(bg = 'green')
       root.after(175, lambda: c6.config(bg = '#a0eb38'))
       c6f()
    root.bind('<KeyPress-F5>', flashb5)
    c6.place(x=360,y=30,height=30,width=80)
    c20.config(bg='#a0eb38')
    def flashb6(event):
       c20.config(bg = 'green')
       root.after(175, lambda: c20.config(bg = '#a0eb38'))
       c20f()
    root.bind('<KeyPress-F6>', flashb6)
    c20.place(x=450,y=30,height=30,width=80)
    c34.config(bg='#a0eb38')
    def flashb7(event):
       c34.config(bg = 'green')
       root.after(175, lambda: c34.config(bg = '#a0eb38'))
       c34f()
    root.bind('<KeyPress-F7>', flashb7)
    c34.place(x=560,y=30,height=30,width=80)
    c47.config(bg='#a0eb38')
    def flashb8(event):
       c47.config(bg = 'green')
       root.after(175, lambda: c47.config(bg = '#a0eb38'))
       c47f()
    root.bind('<KeyPress-Q>', flashb8)
    c47.place(x=0,y=60,height=30,width=80)
    c49.config(bg='#a0eb38')
    def flashb9(event):
       c49.config(bg = 'green')
       root.after(175, lambda: c49.config(bg = '#a0eb38'))
       c49f()
    root.bind('<KeyPress-W>', flashb9)
    c49.place(x=90,y=60,height=30,width=80)
    c51.config(bg='#a0eb38')
    def flashb10(event):
       c51.config(bg = 'green')
       root.after(175, lambda: c51.config(bg = '#a0eb38'))
       c51f()
    root.bind('<KeyPress-E>', flashb10)
    c51.place(x=180,y=60,height=30,width=80)
    c40.config(bg='#a0eb38')
    def flashb11(event):
       c40.config(bg = 'green')
       root.after(175, lambda: c40.config(bg = '#a0eb38'))
       c40f()
    root.bind('<KeyPress-R>', flashb11)
    c40.place(x=270,y=60,height=30,width=80)
    c66.config(bg='#a0eb38')
    def flashb12(event):
       c66.config(bg = 'green')
       root.after(175, lambda: c66.config(bg = '#a0eb38'))
       c66f()
    root.bind('<KeyPress-T>', flashb12)
    c66.place(x=360,y=60,height=30,width=80)
    c56.config(bg='#a0eb38')
    def flashb13(event):
       c56.config(bg = 'green')
       root.after(175, lambda: c56.config(bg = '#a0eb38'))
       c56f()
    root.bind('<KeyPress-Y>', flashb13)
    c56.place(x=450,y=60,height=30,width=80)
    c82.config(bg='#a0eb38')
    def flashb14(event):
       c82.config(bg = 'green')
       root.after(175, lambda: c82.config(bg = '#a0eb38'))
       c82f()
    root.bind('<KeyPress-U>', flashb14)
    c82.place(x=560,y=60,height=30,width=80)
def showscale12():
    resetchords()
    resetguitar()
    global flag
    flag=12
    b_major_show()
    c12.config(bg='#e3bcbd')
    def flashb1(event):
       c12.config(bg = 'green')
       root.after(175, lambda: c12.config(bg = '#e3bcbd'))
       c12f()
    root.bind('<KeyPress-F1>', flashb1)
    c12.place(x=0,y=30,height=30,width=80)
    c14.config(bg='#e3bcbd')
    def flashb2(event):
       c14.config(bg = 'green')
       root.after(175, lambda: c14.config(bg = '#e3bcbd'))
       c14f()
    root.bind('<KeyPress-F2>', flashb2)
    c14.place(x=90,y=30,height=30,width=80)
    c16.config(bg='#e3bcbd')
    def flashb3(event):
       c16.config(bg = 'green')
       root.after(175, lambda: c16.config(bg = '#e3bcbd'))
       c16f()
    root.bind('<KeyPress-F3>', flashb3)
    c16.place(x=180,y=30,height=30,width=80)
    c5.config(bg='#e3bcbd')
    def flashb4(event):
       c5.config(bg = 'green')
       root.after(175, lambda: c5.config(bg = '#e3bcbd'))
       c5f()
    root.bind('<KeyPress-F4>', flashb4)
    c5.place(x=270,y=30,height=30,width=80)
    c7.config(bg='#e3bcbd')
    def flashb5(event):
       c7.config(bg = 'green')
       root.after(175, lambda: c7.config(bg = '#e3bcbd'))
       c7f()
    root.bind('<KeyPress-F5>', flashb5)
    c7.place(x=360,y=30,height=30,width=80)
    c21.config(bg='#e3bcbd')
    def flashb6(event):
       c21.config(bg = 'green')
       root.after(175, lambda: c21.config(bg = '#e3bcbd'))
       c21f()
    root.bind('<KeyPress-F6>', flashb6)
    c21.place(x=450,y=30,height=30,width=80)
    c35.config(bg='#e3bcbd')
    def flashb7(event):
       c35.config(bg = 'green')
       root.after(175, lambda: c35.config(bg = '#e3bcbd'))
       c35f()
    root.bind('<KeyPress-F7>', flashb7)
    c35.place(x=560,y=30,height=30,width=80)
    c48.config(bg='#e3bcbd')
    def flashb8(event):
       c48.config(bg = 'green')
       root.after(175, lambda: c48.config(bg = '#e3bcbd'))
       c48f()
    root.bind('<KeyPress-Q>', flashb8)
    c48.place(x=0,y=60,height=30,width=80)
    c50.config(bg='#e3bcbd')
    def flashb9(event):
       c50.config(bg = 'green')
       root.after(175, lambda: c50.config(bg = '#e3bcbd'))
       c50f()
    root.bind('<KeyPress-W>', flashb9)
    c50.place(x=90,y=60,height=30,width=80)
    c52.config(bg='#e3bcbd')
    def flashb10(event):
       c52.config(bg = 'green')
       root.after(175, lambda: c52.config(bg = '#e3bcbd'))
       c52f()
    root.bind('<KeyPress-E>', flashb10)
    c52.place(x=180,y=60,height=30,width=80)
    c41.config(bg='#e3bcbd')
    def flashb11(event):
       c41.config(bg = 'green')
       root.after(175, lambda: c41.config(bg = '#e3bcbd'))
       c41f()
    root.bind('<KeyPress-R>', flashb11)
    c41.place(x=270,y=60,height=30,width=80)
    c67.config(bg='#e3bcbd')
    def flashb12(event):
       c67.config(bg = 'green')
       root.after(175, lambda: c67.config(bg = '#e3bcbd'))
       c67f()
    root.bind('<KeyPress-T>', flashb12)
    c67.place(x=360,y=60,height=30,width=80)
    c57.config(bg='#e3bcbd')
    def flashb13(event):
       c57.config(bg = 'green')
       root.after(175, lambda: c57.config(bg = '#e3bcbd'))
       c57f()
    root.bind('<KeyPress-Y>', flashb13)
    c57.place(x=450,y=60,height=30,width=80)
    c83.config(bg='#e3bcbd')
    def flashb14(event):
       c83.config(bg = 'green')
       root.after(175, lambda: c83.config(bg = '#e3bcbd'))
       c83f()
    root.bind('<KeyPress-U>', flashb14)
    c83.place(x=560,y=60,height=30,width=80)
##############main chord radio button bunction to chane guitar note color#######################
############################Radio Button for chords###############################################################
scale1show=Button(frame_chord,text='C',command=showscale1)
scale1show.place(x=60,y=0,width=80,height=25)

scale2show=Button(frame_chord,text='C#/Db',command=showscale2)
scale2show.place(x=145,y=0,width=80,height=25)

scale3show=Button(frame_chord,text='D',command=showscale3)
scale3show.place(x=230,y=0,width=80,height=25)

scale4show=Button(frame_chord,text='D#/Eb',command=showscale4)    
scale4show.place(x=315,y=0,width=80,height=25)

scale5show=Button(frame_chord,text='E',command=showscale5)    
scale5show.place(x=400,y=0,width=80,height=25)

scale6show=Button(frame_chord,text='F',command=showscale6)    
scale6show.place(x=485,y=0,width=80,height=25)

scale7show=Button(frame_chord,text='F#/Gb',command=showscale7)    
scale7show.place(x=570,y=0,width=80,height=25)

scale8show=Button(frame_chord,text='G',command=showscale8)    
scale8show.place(x=655,y=0,width=80,height=25)

scale9show=Button(frame_chord,text='G#/Ab',command=showscale9)    
scale9show.place(x=740,y=0,width=80,height=25)

scale10show=Button(frame_chord,text='A',command=showscale10)    
scale10show.place(x=825,y=0,width=80,height=25)

scale11show=Button(frame_chord,text='A#/Bb',command=showscale11)    
scale11show.place(x=910,y=0,width=80,height=25)

scale12show=Button(frame_chord,text='B',command=showscale12)    
scale12show.place(x=995,y=0,width=80,height=25)
    
################################MAJOR SHOW HIDE FUNCTIONS
################################SCALES SHOW HERE
def c_major_show():
    b_c.place_forget()
    b_c_h.place(x=0,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)  
    def flashb1g1(event):
       b1g1.config(bg = 'green')
       root.after(175, lambda: b1g1.config(bg = 'yellow'))
       g11()
    root.bind('<KeyPress-z>', flashb1g1)
    def flashb3g1(event):
       b3g1.config(bg = 'green')
       root.after(175, lambda: b3g1.config(bg = 'yellow'))
       g13()
    root.bind('<KeyPress-x>', flashb3g1)
    def flashb4g1(event):
       b4g1.config(bg = 'green')
       root.after(175, lambda: b4g1.config(bg = 'yellow'))
       g14()
    root.bind('<KeyPress-c>', flashb4g1)
    def flashb6g1(event):
       b6g1.config(bg = 'green')
       root.after(175, lambda: b6g1.config(bg = 'yellow'))
       g16()
    root.bind('<KeyPress-v>', flashb6g1)
    def flashb8g1(event):
       b8g1.config(bg = 'green')
       root.after(175, lambda: b8g1.config(bg = 'yellow'))
       g18()
    root.bind('<KeyPress-b>', flashb8g1)
    def flashb9g1(event):
       b9g1.config(bg = 'green')
       root.after(175, lambda: b9g1.config(bg = 'yellow'))
       g19()
    root.bind('<KeyPress-n>', flashb9g1)
    def flashb11g1(event):
       b11g1.config(bg = 'green')
       root.after(175, lambda: b11g1.config(bg = 'yellow'))
       g111()
    root.bind('<KeyPress-m>', flashb11g1)
    def flashb13g1(event):
       b13g1.config(bg = 'green')
       root.after(175, lambda: b13g1.config(bg = 'yellow'))
       g113()
    root.bind('<KeyPress-,>', flashb13g1)
    def flashb15g1(event):
       b15g1.config(bg = 'green')
       root.after(175, lambda: b15g1.config(bg = 'yellow'))
       g115()
    root.bind('<KeyPress-.>', flashb15g1)
    def flashb16g1(event):
       b16g1.config(bg = 'green')
       root.after(175, lambda: b16g1.config(bg = 'yellow'))
       g116()
    root.bind('<KeyPress-/>', flashb16g1)



    def flashb1g2(event):
       b1g2.config(bg = 'green')
       root.after(175, lambda: b1g2.config(bg = 'yellow'))
       g21()
    root.bind('<KeyPress-a>', flashb1g2)
    def flashb2g2(event):
       b2g2.config(bg = 'green')
       root.after(175, lambda: b2g2.config(bg = 'yellow'))
       g22()
    root.bind('<KeyPress-s>', flashb2g2)
    def flashb4g2(event):
       b4g2.config(bg = 'green')
       root.after(175, lambda: b4g2.config(bg = 'yellow'))
       g24()
    root.bind('<KeyPress-d>', flashb4g2)
    def flashb6g2(event):
       b6g2.config(bg = 'green')
       root.after(175, lambda: b6g2.config(bg = 'yellow'))
       g26()
    root.bind('<KeyPress-f>', flashb6g2)
    def flashb8g2(event):
       b8g2.config(bg = 'green')
       root.after(175, lambda: b8g2.config(bg = 'yellow'))
       g28()
    root.bind('<KeyPress-g>', flashb8g2)
    def flashb9g2(event):
       b9g2.config(bg = 'green')
       root.after(175, lambda: b9g2.config(bg = 'yellow'))
       g29()
    root.bind('<KeyPress-h>', flashb9g2)
    def flashb11g2(event):
       b11g2.config(bg = 'green')
       root.after(175, lambda: b11g2.config(bg = 'yellow'))
       g211()
    root.bind('<KeyPress-j>', flashb11g2)
    def flashb13g2(event):
       b13g2.config(bg = 'green')
       root.after(175, lambda: b13g2.config(bg = 'yellow'))
       g213()
    root.bind('<KeyPress-k>', flashb13g2)
    def flashb14g2(event):
       b14g2.config(bg = 'green')
       root.after(175, lambda: b14g2.config(bg = 'yellow'))
       g214()
    root.bind('<KeyPress-l>', flashb14g2)
    def flashb16g2(event):
       b16g2.config(bg = 'green')
       root.after(175, lambda: b16g2.config(bg = 'yellow'))
       g216()
    root.bind('<KeyPress-;>', flashb16g2)


    def flashb1g3(event):
       b1g3.config(bg = 'green')
       root.after(175, lambda: b1g3.config(bg = 'yellow'))
       g31()
    root.bind('<KeyPress-q>', flashb1g3)
    def flashb3g3(event):
       b3g3.config(bg = 'green')
       root.after(175, lambda: b3g3.config(bg = 'yellow'))
       g33()
    root.bind('<KeyPress-w>', flashb3g3)
    def flashb5g3(event):
       b5g3.config(bg = 'green')
       root.after(175, lambda: b5g3.config(bg = 'yellow'))
       g35()
    root.bind('<KeyPress-e>', flashb5g3)
    def flashb6g3(event):
       b6g3.config(bg = 'green')
       root.after(175, lambda: b6g3.config(bg = 'yellow'))
       g36()
    root.bind('<KeyPress-r>', flashb6g3)
    def flashb8g3(event):
       b8g3.config(bg = 'green')
       root.after(175, lambda: b8g3.config(bg = 'yellow'))
       g38()
    root.bind('<KeyPress-t>', flashb8g3)
    def flashb10g3(event):
       b10g3.config(bg = 'green')
       root.after(175, lambda: b10g3.config(bg = 'yellow'))
       g310()
    root.bind('<KeyPress-y>', flashb10g3)
    def flashb12g3(event):
       b12g3.config(bg = 'green')
       root.after(175, lambda: b12g3.config(bg = 'yellow'))
       g312()
    root.bind('<KeyPress-u>', flashb12g3)
    def flashb13g3(event):
       b13g3.config(bg = 'green')
       root.after(175, lambda: b13g3.config(bg = 'yellow'))
       g313()
    root.bind('<KeyPress-i>', flashb13g3)
    def flashb15g3(event):
       b15g3.config(bg = 'green')
       root.after(175, lambda: b15g3.config(bg = 'yellow'))
       g315()
    root.bind('<KeyPress-o>', flashb15g3)

    def flashb1g4(event):
       b1g4.config(bg = 'green')
       root.after(175, lambda: b1g4.config(bg = 'yellow'))
       g41()
    root.bind('<KeyPress-1>', flashb1g4)
    def flashb3g4(event):
       b3g4.config(bg = 'green')
       root.after(175, lambda: b3g4.config(bg = 'yellow'))
       g43()
    root.bind('<KeyPress-2>', flashb3g4)
    def flashb5g4(event):
       b5g4.config(bg = 'green')
       root.after(175, lambda: b5g4.config(bg = 'yellow'))
       g45()
    root.bind('<KeyPress-3>', flashb5g4)
    def flashb6g4(event):
       b6g4.config(bg = 'green')
       root.after(175, lambda: b6g4.config(bg = 'yellow'))
       g46()
    root.bind('<KeyPress-4>', flashb6g4)
    def flashb8g4(event):
       b8g4.config(bg = 'green')
       root.after(175, lambda: b8g4.config(bg = 'yellow'))
       g48()
    root.bind('<KeyPress-5>', flashb8g4)
    def flashb10g4(event):
       b10g4.config(bg = 'green')
       root.after(175, lambda: b10g4.config(bg = 'yellow'))
       g410()
    root.bind('<KeyPress-6>', flashb10g4)
    def flashb11g4(event):
       b11g4.config(bg = 'green')
       root.after(175, lambda: b11g4.config(bg = 'yellow'))
       g411()
    root.bind('<KeyPress-7>', flashb11g4)
    def flashb13g4(event):
       b13g4.config(bg = 'green')
       root.after(175, lambda: b13g4.config(bg = 'yellow'))
       g413()
    root.bind('<KeyPress-8>', flashb13g4)
    def flashb15g4(event):
       b15g4.config(bg = 'green')
       root.after(175, lambda: b15g4.config(bg = 'yellow'))
       g415()
    root.bind('<KeyPress-9>', flashb15g4)

    
    b1g4.configure(background="yellow")
    b3g4.configure(background="yellow")
    b5g4.configure(background="yellow")
    b6g4.configure(background="yellow")
    b8g4.configure(background="yellow")
    b10g4.configure(background="yellow")
    b11g4.configure(background="yellow")
    b13g4.configure(background="yellow")
    b15g4.configure(background="yellow")

    b1g3.configure(background="yellow")
    b3g3.configure(background="yellow")
    b5g3.configure(background="yellow")
    b6g3.configure(background="yellow")
    b8g3.configure(background="yellow")
    b10g3.configure(background="yellow")
    b12g3.configure(background="yellow")
    b13g3.configure(background="yellow")
    b15g3.configure(background="yellow")

    b1g2.configure(background="yellow")
    b2g2.configure(background="yellow")
    b4g2.configure(background="yellow")
    b6g2.configure(background="yellow")
    b8g2.configure(background="yellow")
    b9g2.configure(background="yellow")
    b11g2.configure(background="yellow")
    b13g2.configure(background="yellow")
    b14g2.configure(background="yellow")
    b16g2.configure(background="yellow")

    b1g1.configure(background="yellow")
    b3g1.configure(background="yellow")
    b4g1.configure(background="yellow")
    b6g1.configure(background="yellow")
    b8g1.configure(background="yellow")
    b9g1.configure(background="yellow")
    b11g1.configure(background="yellow")
    b13g1.configure(background="yellow")
    b15g1.configure(background="yellow")
    b16g1.configure(background="yellow")
def c_major_yellow():
    b_c_h.place_forget()
    b_c.place(x=0,y=50,width=80)
    resetflash()
    b1g4.configure(background=orig_color)
    b3g4.configure(background=orig_color)
    b5g4.configure(background=orig_color)
    b6g4.configure(background=orig_color)
    b8g4.configure(background=orig_color)
    b10g4.configure(background=orig_color)
    b11g4.configure(background=orig_color)
    b13g4.configure(background=orig_color)
    b15g4.configure(background=orig_color)

    b1g3.configure(background=orig_color)
    b3g3.configure(background=orig_color)
    b5g3.configure(background=orig_color)
    b6g3.configure(background=orig_color)
    b8g3.configure(background=orig_color)
    b10g3.configure(background=orig_color)
    b12g3.configure(background=orig_color)
    b13g3.configure(background=orig_color)
    b15g3.configure(background=orig_color)

    b1g2.configure(background=orig_color)
    b2g2.configure(background=orig_color)
    b4g2.configure(background=orig_color)
    b6g2.configure(background=orig_color)
    b8g2.configure(background=orig_color)
    b9g2.configure(background=orig_color)
    b11g2.configure(background=orig_color)
    b13g2.configure(background=orig_color)
    b14g2.configure(background=orig_color)
    b16g2.configure(background=orig_color)

    b1g1.configure(background=orig_color)
    b3g1.configure(background=orig_color)
    b4g1.configure(background=orig_color)
    b6g1.configure(background=orig_color)
    b8g1.configure(background=orig_color)
    b9g1.configure(background=orig_color)
    b11g1.configure(background=orig_color)
    b13g1.configure(background=orig_color)
    b15g1.configure(background=orig_color)
    b16g1.configure(background=orig_color)

def c_sharp_major_show():
    b_c_sharp.place_forget()
    b_c_sharp_h.place(x=100,y=50,width=80)
######################
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)  
    def flashb2g1(event):
       b2g1.config(bg = 'green')
       root.after(175, lambda: b2g1.config(bg = 'orange'))
       g12()
    root.bind('<KeyPress-z>', flashb2g1)
    def flashb4g1(event):
       b4g1.config(bg = 'green')
       root.after(175, lambda: b4g1.config(bg = 'orange'))
       g14()
    root.bind('<KeyPress-x>', flashb4g1)
    def flashb5g1(event):
       b5g1.config(bg = 'green')
       root.after(175, lambda: b5g1.config(bg = 'orange'))
       g15()
    root.bind('<KeyPress-c>', flashb5g1)
    def flashb7g1(event):
       b7g1.config(bg = 'green')
       root.after(175, lambda: b7g1.config(bg = 'orange'))
       g17()
    root.bind('<KeyPress-v>', flashb7g1)
    def flashb9g1(event):
       b9g1.config(bg = 'green')
       root.after(175, lambda: b9g1.config(bg = 'orange'))
       g19()
    root.bind('<KeyPress-b>', flashb9g1)
    def flashb10g1(event):
       b10g1.config(bg = 'green')
       root.after(175, lambda: b10g1.config(bg = 'orange'))
       g110()
    root.bind('<KeyPress-n>', flashb10g1)
    def flashb12g1(event):
       b12g1.config(bg = 'green')
       root.after(175, lambda: b12g1.config(bg = 'orange'))
       g112()
    root.bind('<KeyPress-m>', flashb12g1)
    def flashb14g1(event):
       b14g1.config(bg = 'green')
       root.after(175, lambda: b14g1.config(bg = 'orange'))
       g114()
    root.bind('<KeyPress-,>', flashb14g1)
    def flashb16g1(event):
       b16g1.config(bg = 'green')
       root.after(175, lambda: b16g1.config(bg = 'orange'))
       g116()
    root.bind('<KeyPress-.>', flashb16g1)
############################STRING 2 ################################

    def flashb2g2(event):
       b2g2.config(bg = 'green')
       root.after(175, lambda: b2g2.config(bg = 'orange'))
       g22()
    root.bind('<KeyPress-a>', flashb2g2)
    def flashb3g2(event):
       b3g2.config(bg = 'green')
       root.after(175, lambda: b3g2.config(bg = 'orange'))
       g23()
    root.bind('<KeyPress-s>', flashb3g2)
    def flashb5g2(event):
       b5g2.config(bg = 'green')
       root.after(175, lambda: b5g2.config(bg = 'orange'))
       g25()
    root.bind('<KeyPress-d>', flashb5g2)
    def flashb7g2(event):
       b7g2.config(bg = 'green')
       root.after(175, lambda: b7g2.config(bg = 'orange'))
       g27()
    root.bind('<KeyPress-f>', flashb7g2)
    def flashb9g2(event):
       b9g2.config(bg = 'green')
       root.after(175, lambda: b9g2.config(bg = 'orange'))
       g29()
    root.bind('<KeyPress-g>', flashb9g2)
    def flashb10g2(event):
       b10g2.config(bg = 'green')
       root.after(175, lambda: b10g2.config(bg = 'orange'))
       g210()
    root.bind('<KeyPress-h>', flashb10g2)
    def flashb12g2(event):
       b12g2.config(bg = 'green')
       root.after(175, lambda: b12g2.config(bg = 'orange'))
       g212()
    root.bind('<KeyPress-j>', flashb12g2)
    def flashb14g2(event):
       b14g2.config(bg = 'green')
       root.after(175, lambda: b14g2.config(bg = 'orange'))
       g214()
    root.bind('<KeyPress-k>', flashb14g2)
    def flashb15g2(event):
       b15g2.config(bg = 'green')
       root.after(175, lambda: b15g2.config(bg = 'orange'))
       g215()
    root.bind('<KeyPress-l>', flashb15g2)
#########################STRING 3################################

    def flashb1g3(event):
       b1g3.config(bg = 'green')
       root.after(175, lambda: b1g3.config(bg = 'orange'))
       g31()
    root.bind('<KeyPress-q>', flashb1g3)
    def flashb2g3(event):
       b2g3.config(bg = 'green')
       root.after(175, lambda: b2g3.config(bg = 'orange'))
       g32()
    root.bind('<KeyPress-w>', flashb2g3)
    def flashb4g3(event):
       b4g3.config(bg = 'green')
       root.after(175, lambda: b4g3.config(bg = 'orange'))
       g34()
    root.bind('<KeyPress-e>', flashb4g3)
    def flashb6g3(event):
       b6g3.config(bg = 'green')
       root.after(175, lambda: b6g3.config(bg = 'orange'))
       g36()
    root.bind('<KeyPress-r>', flashb6g3)
    def flashb7g3(event):
       b7g3.config(bg = 'green')
       root.after(175, lambda: b7g3.config(bg = 'orange'))
       g37()
    root.bind('<KeyPress-t>', flashb7g3)
    def flashb9g3(event):
       b9g3.config(bg = 'green')
       root.after(175, lambda: b9g3.config(bg = 'orange'))
       g39()
    root.bind('<KeyPress-y>', flashb9g3)
    def flashb11g3(event):
       b11g3.config(bg = 'green')
       root.after(175, lambda: b11g3.config(bg = 'orange'))
       g311()
    root.bind('<KeyPress-u>', flashb11g3)
    def flashb13g3(event):
       b13g3.config(bg = 'green')
       root.after(175, lambda: b13g3.config(bg = 'orange'))
       g313()
    root.bind('<KeyPress-i>', flashb13g3)
    def flashb14g3(event):
       b14g3.config(bg = 'green')
       root.after(175, lambda: b14g3.config(bg = 'orange'))
       g314()
    root.bind('<KeyPress-o>', flashb14g3)
    def flashb16g3(event):
       b16g3.config(bg = 'green')
       root.after(175, lambda: b16g3.config(bg = 'orange'))
       g316()
    root.bind('<KeyPress-p>', flashb16g3)
#########################STRING 4################################

    def flashb2g4(event):
       b2g4.config(bg = 'green')
       root.after(175, lambda: b2g4.config(bg = 'orange'))
       g42()
    root.bind('<KeyPress-1>', flashb2g4)
    def flashb4g4(event):
       b4g4.config(bg = 'green')
       root.after(175, lambda: b4g4.config(bg = 'orange'))
       g44()
    root.bind('<KeyPress-2>', flashb4g4)
    def flashb6g4(event):
       b6g4.config(bg = 'green')
       root.after(175, lambda: b6g4.config(bg = 'orange'))
       g46()
    root.bind('<KeyPress-3>', flashb6g4)
    def flashb7g4(event):
       b7g4.config(bg = 'green')
       root.after(175, lambda: b7g4.config(bg = 'orange'))
       g47()
    root.bind('<KeyPress-4>', flashb7g4)
    def flashb9g4(event):
       b9g4.config(bg = 'green')
       root.after(175, lambda: b9g4.config(bg = 'orange'))
       g49()
    root.bind('<KeyPress-5>', flashb9g4)
    def flashb11g4(event):
       b11g4.config(bg = 'green')
       root.after(175, lambda: b11g4.config(bg = 'orange'))
       g411()
    root.bind('<KeyPress-6>', flashb11g4)
    def flashb12g4(event):
       b12g4.config(bg = 'green')
       root.after(175, lambda: b12g4.config(bg = 'orange'))
       g412()
    root.bind('<KeyPress-7>', flashb12g4)
    def flashb14g4(event):
       b14g4.config(bg = 'green')
       root.after(175, lambda: b14g4.config(bg = 'orange'))
       g414()
    root.bind('<KeyPress-8>', flashb14g4)
    def flashb16g4(event):
       b16g4.config(bg = 'green')
       root.after(175, lambda: b16g4.config(bg = 'orange'))
       g416()
    root.bind('<KeyPress-9>', flashb16g4)
     

    b2g1.configure(background='orange')
    b4g1.configure(background='orange')
    b5g1.configure(background='orange')
    b7g1.configure(background='orange')
    b9g1.configure(background='orange')
    b10g1.configure(background='orange')
    b12g1.configure(background='orange')
    b14g1.configure(background='orange')
    b16g1.configure(background='orange')
############################STRING 2 ################################
    b2g2.configure(background='orange')
    b3g2.configure(background='orange')
    b5g2.configure(background='orange')
    b7g2.configure(background='orange')
    b9g2.configure(background='orange')
    b10g2.configure(background='orange')
    b12g2.configure(background='orange')
    b14g2.configure(background='orange')
    b15g2.configure(background='orange')
#########################STRING 3################################
    b1g3.configure(background='orange')
    b2g3.configure(background='orange')
    b4g3.configure(background='orange')
    b6g3.configure(background='orange')
    b7g3.configure(background='orange')
    b9g3.configure(background='orange')
    b11g3.configure(background='orange')
    b13g3.configure(background='orange')
    b14g3.configure(background='orange')
    b16g3.configure(background='orange')
#########################STRING 4################################
    b2g4.configure(background='orange')
    b4g4.configure(background='orange')
    b6g4.configure(background='orange')
    b7g4.configure(background='orange')
    b9g4.configure(background='orange')
    b11g4.configure(background='orange')
    b12g4.configure(background='orange')
    b14g4.configure(background='orange')
    b16g4.configure(background='orange')    
def c_sharp_major_orange():
    b_c_sharp_h.place_forget()
    b_c_sharp.place(x=100,y=50,width=80)
    resetflash()
    b2g1.configure(background=orig_color)
    b4g1.configure(background=orig_color)
    b5g1.configure(background=orig_color)
    b7g1.configure(background=orig_color)
    b9g1.configure(background=orig_color)
    b10g1.configure(background=orig_color)
    b12g1.configure(background=orig_color)
    b14g1.configure(background=orig_color)
    b16g1.configure(background=orig_color)
############################STRING 2 ################################
    b2g2.configure(background=orig_color)
    b3g2.configure(background=orig_color)
    b5g2.configure(background=orig_color)
    b7g2.configure(background=orig_color)
    b9g2.configure(background=orig_color)
    b10g2.configure(background=orig_color)
    b12g2.configure(background=orig_color)
    b14g2.configure(background=orig_color)
    b15g2.configure(background=orig_color)
#########################STRING 3################################
    b1g3.configure(background=orig_color)
    b2g3.configure(background=orig_color)
    b4g3.configure(background=orig_color)
    b6g3.configure(background=orig_color)
    b7g3.configure(background=orig_color)
    b9g3.configure(background=orig_color)
    b11g3.configure(background=orig_color)
    b13g3.configure(background=orig_color)
    b14g3.configure(background=orig_color)
    b16g3.configure(background=orig_color)
#########################STRING 4################################
    b2g4.configure(background=orig_color)
    b4g4.configure(background=orig_color)
    b6g4.configure(background=orig_color)
    b7g4.configure(background=orig_color)
    b9g4.configure(background=orig_color)
    b11g4.configure(background=orig_color)
    b12g4.configure(background=orig_color)
    b14g4.configure(background=orig_color)
    b16g4.configure(background=orig_color)    

def d_major_show():
    b_d.place_forget()
    b_d_h.place(x=200,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)
    
    def flashb1g1(event):
       b1g1.config(bg = 'green')
       root.after(175, lambda: b1g1.config(bg = '#944187'))
       g11()
    root.bind('<KeyPress-z>', flashb1g1)
    def flashb3g1(event):
       b3g1.config(bg = 'green')
       root.after(175, lambda: b3g1.config(bg = '#944187'))
       g13()
    root.bind('<KeyPress-x>', flashb3g1)
    def flashb5g1(event):
       b5g1.config(bg = 'green')
       root.after(175, lambda: b5g1.config(bg = '#944187'))
       g15()
    root.bind('<KeyPress-c>', flashb5g1)
    def flashb6g1(event):
       b6g1.config(bg = 'green')
       root.after(175, lambda: b6g1.config(bg = '#944187'))
       g16()
    root.bind('<KeyPress-v>', flashb6g1)
    def flashb8g1(event):
       b8g1.config(bg = 'green')
       root.after(175, lambda: b8g1.config(bg = '#944187'))
       g18()
    root.bind('<KeyPress-b>', flashb8g1)
    def flashb10g1(event):
       b10g1.config(bg = 'green')
       root.after(175, lambda: b10g1.config(bg = '#944187'))
       g110()
    root.bind('<KeyPress-n>', flashb10g1)
    def flashb11g1(event):
       b11g1.config(bg = 'green')
       root.after(175, lambda: b11g1.config(bg = '#944187'))
       g111()
    root.bind('<KeyPress-m>', flashb11g1)
    def flashb13g1(event):
       b13g1.config(bg = 'green')
       root.after(175, lambda: b13g1.config(bg = '#944187'))
       g113()
    root.bind('<KeyPress-,>', flashb13g1)
    def flashb15g1(event):
       b15g1.config(bg = 'green')
       root.after(175, lambda: b15g1.config(bg = '#944187'))
       g115()
    root.bind('<KeyPress-.>', flashb15g1)
############################STRING 2 ################################
    def flashb1g2(event):
       b1g2.config(bg = 'green')
       root.after(175, lambda: b1g2.config(bg = '#944187'))
       g21()
    root.bind('<KeyPress-a>', flashb1g2)
    def flashb3g2(event):
       b3g2.config(bg = 'green')
       root.after(175, lambda: b3g2.config(bg = '#944187'))
       g23()
    root.bind('<KeyPress-s>', flashb3g2)
    def flashb4g2(event):
       b4g2.config(bg = 'green')
       root.after(175, lambda: b4g2.config(bg = '#944187'))
       g24()
    root.bind('<KeyPress-d>', flashb4g2)
    def flashb6g2(event):
       b6g2.config(bg = 'green')
       root.after(175, lambda: b6g2.config(bg = '#944187'))
       g26()
    root.bind('<KeyPress-f>', flashb6g2)
    def flashb8g2(event):
       b8g2.config(bg = 'green')
       root.after(175, lambda: b8g2.config(bg = '#944187'))
       g28()
    root.bind('<KeyPress-g>', flashb8g2)
    def flashb10g2(event):
       b10g2.config(bg = 'green')
       root.after(175, lambda: b10g2.config(bg = '#944187'))
       g210()
    root.bind('<KeyPress-h>', flashb10g2)
    def flashb11g2(event):
       b11g2.config(bg = 'green')
       root.after(175, lambda: b11g2.config(bg = '#944187'))
       g211()
    root.bind('<KeyPress-j>', flashb11g2)
    def flashb13g2(event):
       b13g2.config(bg = 'green')
       root.after(175, lambda: b13g2.config(bg = '#944187'))
       g213()
    root.bind('<KeyPress-k>', flashb13g2)
    def flashb15g2(event):
       b15g2.config(bg = 'green')
       root.after(175, lambda: b15g2.config(bg = '#944187'))
       g215()
    root.bind('<KeyPress-l>', flashb15g2)
    def flashb16g2(event):
       b16g2.config(bg = 'green')
       root.after(175, lambda: b16g2.config(bg = '#944187'))
       g216()
    root.bind('<KeyPress-;>', flashb16g2)
#########################STRING 3################################
    def flashb2g3(event):
       b2g3.config(bg = 'green')
       root.after(175, lambda: b2g3.config(bg = '#944187'))
       g32()
    root.bind('<KeyPress-q>', flashb2g3)
    def flashb3g3(event):
       b3g3.config(bg = 'green')
       root.after(175, lambda: b3g3.config(bg = '#944187'))
       g33()
    root.bind('<KeyPress-w>', flashb3g3)
    def flashb5g3(event):
       b5g3.config(bg = 'green')
       root.after(175, lambda: b5g3.config(bg = '#944187'))
       g35()
    root.bind('<KeyPress-e>', flashb5g3)
    def flashb7g3(event):
       b7g3.config(bg = 'green')
       root.after(175, lambda: b7g3.config(bg = '#944187'))
       g37()
    root.bind('<KeyPress-r>', flashb7g3)
    def flashb8g3(event):
       b8g3.config(bg = 'green')
       root.after(175, lambda: b8g3.config(bg = '#944187'))
       g38()
    root.bind('<KeyPress-t>', flashb8g3)
    def flashb10g3(event):
       b10g3.config(bg = 'green')
       root.after(175, lambda: b10g3.config(bg = '#944187'))
       g310()
    root.bind('<KeyPress-y>', flashb10g3)
    def flashb12g3(event):
       b12g3.config(bg = 'green')
       root.after(175, lambda: b12g3.config(bg = '#944187'))
       g312()
    root.bind('<KeyPress-u>', flashb12g3)
    def flashb14g3(event):
       b14g3.config(bg = 'green')
       root.after(175, lambda: b14g3.config(bg = '#944187'))
       g314()
    root.bind('<KeyPress-i>', flashb14g3)
    def flashb15g3(event):
       b15g3.config(bg = 'green')
       root.after(175, lambda: b15g3.config(bg = '#944187'))
       g315()
    root.bind('<KeyPress-o>', flashb15g3)
#########################STRING 4################################
    def flashb1g4(event):
       b1g4.config(bg = 'green')
       root.after(175, lambda: b1g4.config(bg = '#944187'))
       g41()
    root.bind('<KeyPress-1>', flashb1g4)
    def flashb3g4(event):
       b3g4.config(bg = 'green')
       root.after(175, lambda: b3g4.config(bg = '#944187'))
       g43()
    root.bind('<KeyPress-2>', flashb3g4)
    def flashb5g4(event):
       b5g4.config(bg = 'green')
       root.after(175, lambda: b5g4.config(bg = '#944187'))
       g45()
    root.bind('<KeyPress-3>', flashb5g4)
    def flashb7g4(event):
       b7g4.config(bg = 'green')
       root.after(175, lambda: b7g4.config(bg = '#944187'))
       g47()
    root.bind('<KeyPress-4>', flashb7g4)
    def flashb8g4(event):
       b8g4.config(bg = 'green')
       root.after(175, lambda: b8g4.config(bg = '#944187'))
       g48()
    root.bind('<KeyPress-5>', flashb8g4)
    def flashb10g4(event):
       b10g4.config(bg = 'green')
       root.after(175, lambda: b10g4.config(bg = '#944187'))
       g410()
    root.bind('<KeyPress-6>', flashb10g4)
    def flashb12g4(event):
       b12g4.config(bg = 'green')
       root.after(175, lambda: b12g4.config(bg = '#944187'))
       g412()
    root.bind('<KeyPress-7>', flashb12g4)
    def flashb13g4(event):
       b13g4.config(bg = 'green')
       root.after(175, lambda: b13g4.config(bg = '#944187'))
       g413()
    root.bind('<KeyPress-8>', flashb13g4)
    def flashb15g4(event):
       b15g4.config(bg = 'green')
       root.after(175, lambda: b15g4.config(bg = '#944187'))
       g415()
    root.bind('<KeyPress-9>', flashb15g4)


    b1g1.configure(background='#944187')
    b3g1.configure(background='#944187')
    b5g1.configure(background='#944187')
    b6g1.configure(background='#944187')
    b8g1.configure(background='#944187')
    b10g1.configure(background='#944187')
    b11g1.configure(background='#944187')
    b13g1.configure(background='#944187')
    b15g1.configure(background='#944187')
############################STRING 2 ################################
    b1g2.configure(background='#944187')
    b3g2.configure(background='#944187')
    b4g2.configure(background='#944187')
    b6g2.configure(background='#944187')
    b8g2.configure(background='#944187')
    b10g2.configure(background='#944187')
    b11g2.configure(background='#944187')
    b13g2.configure(background='#944187')
    b15g2.configure(background='#944187')
    b16g2.configure(background='#944187')
#########################STRING 3################################
    b2g3.configure(background='#944187')
    b3g3.configure(background='#944187')
    b5g3.configure(background='#944187')
    b7g3.configure(background='#944187')
    b8g3.configure(background='#944187')
    b10g3.configure(background='#944187')
    b12g3.configure(background='#944187')
    b14g3.configure(background='#944187')
    b15g3.configure(background='#944187')
#########################STRING 4################################
    b1g4.configure(background='#944187')
    b3g4.configure(background='#944187')
    b5g4.configure(background='#944187')
    b7g4.configure(background='#944187')
    b8g4.configure(background='#944187')
    b10g4.configure(background='#944187')
    b12g4.configure(background='#944187')
    b13g4.configure(background='#944187')
    b15g4.configure(background='#944187')
    
def d_major_e64040():
    b_d_h.place_forget()
    b_d.place(x=200,y=50,width=80)
    resetflash()
    
    b1g1.configure(background=orig_color)
    b3g1.configure(background=orig_color)
    b5g1.configure(background=orig_color)
    b6g1.configure(background=orig_color)
    b8g1.configure(background=orig_color)
    b10g1.configure(background=orig_color)
    b11g1.configure(background=orig_color)
    b13g1.configure(background=orig_color)
    b15g1.configure(background=orig_color)
############################STRING 2 ################################
    b1g2.configure(background=orig_color)
    b3g2.configure(background=orig_color)
    b4g2.configure(background=orig_color)
    b6g2.configure(background=orig_color)
    b8g2.configure(background=orig_color)
    b10g2.configure(background=orig_color)
    b11g2.configure(background=orig_color)
    b13g2.configure(background=orig_color)
    b15g2.configure(background=orig_color)
    b16g2.configure(background=orig_color)
#########################STRING 3################################
    b2g3.configure(background=orig_color)
    b3g3.configure(background=orig_color)
    b5g3.configure(background=orig_color)
    b7g3.configure(background=orig_color)
    b8g3.configure(background=orig_color)
    b10g3.configure(background=orig_color)
    b12g3.configure(background=orig_color)
    b14g3.configure(background=orig_color)
    b15g3.configure(background=orig_color)
#########################STRING 4################################
    b1g4.configure(background=orig_color)
    b3g4.configure(background=orig_color)
    b5g4.configure(background=orig_color)
    b7g4.configure(background=orig_color)
    b8g4.configure(background=orig_color)
    b10g4.configure(background=orig_color)
    b12g4.configure(background=orig_color)
    b13g4.configure(background=orig_color)
    b15g4.configure(background=orig_color) 
def d_sharp_major_show():
    b_d_sharp.place_forget()
    b_d_sharp_h.place(x=300,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)
    
    def flashb2g1(event):
       b2g1.config(bg = 'green')
       root.after(175, lambda: b2g1.config(bg = '#6fedd0'))
       g12()
    root.bind('<KeyPress-z>', flashb2g1)
    def flashb4g1(event):
       b4g1.config(bg = 'green')
       root.after(175, lambda: b4g1.config(bg = '#6fedd0'))
       g14()
    root.bind('<KeyPress-x>', flashb4g1)
    def flashb6g1(event):
       b6g1.config(bg = 'green')
       root.after(175, lambda: b6g1.config(bg = '#6fedd0'))
       g16()
    root.bind('<KeyPress-c>', flashb6g1)
    def flashb7g1(event):
       b7g1.config(bg = 'green')
       root.after(175, lambda: b7g1.config(bg = '#6fedd0'))
       g17()
    root.bind('<KeyPress-v>', flashb7g1)
    def flashb9g1(event):
       b9g1.config(bg = 'green')
       root.after(175, lambda: b9g1.config(bg = '#6fedd0'))
       g19()
    root.bind('<KeyPress-b>', flashb9g1)
    def flashb11g1(event):
       b11g1.config(bg = 'green')
       root.after(175, lambda: b11g1.config(bg = '#6fedd0'))
       g111()
    root.bind('<KeyPress-n>', flashb11g1)
    def flashb12g1(event):
       b12g1.config(bg = 'green')
       root.after(175, lambda: b12g1.config(bg = '#6fedd0'))
       g112()
    root.bind('<KeyPress-m>', flashb12g1)
    def flashb14g1(event):
       b14g1.config(bg = 'green')
       root.after(175, lambda: b14g1.config(bg = '#6fedd0'))
       g114()
    root.bind('<KeyPress-,>', flashb14g1)
    def flashb16g1(event):
       b16g1.config(bg = 'green')
       root.after(175, lambda: b16g1.config(bg = '#6fedd0'))
       g116()
    root.bind('<KeyPress-.>', flashb16g1)
############################STRING 2 ################################
    def flashb2g2(event):
       b2g2.config(bg = 'green')
       root.after(175, lambda: b2g2.config(bg = '#6fedd0'))
       g22()
    root.bind('<KeyPress-a>', flashb2g2)
    def flashb4g2(event):
       b4g2.config(bg = 'green')
       root.after(175, lambda: b4g2.config(bg = '#6fedd0'))
       g24()
    root.bind('<KeyPress-s>', flashb4g2)
    def flashb5g2(event):
       b5g2.config(bg = 'green')
       root.after(175, lambda: b5g2.config(bg = '#6fedd0'))
       g25()
    root.bind('<KeyPress-d>', flashb5g2)
    def flashb7g2(event):
       b7g2.config(bg = 'green')
       root.after(175, lambda: b7g2.config(bg = '#6fedd0'))
       g27()
    root.bind('<KeyPress-f>', flashb7g2)
    def flashb9g2(event):
       b9g2.config(bg = 'green')
       root.after(175, lambda: b9g2.config(bg = '#6fedd0'))
       g29()
    root.bind('<KeyPress-g>', flashb9g2)
    def flashb11g2(event):
       b11g2.config(bg = 'green')
       root.after(175, lambda: b11g2.config(bg = '#6fedd0'))
       g211()
    root.bind('<KeyPress-h>', flashb11g2)
    def flashb12g2(event):
       b12g2.config(bg = 'green')
       root.after(175, lambda: b12g2.config(bg = '#6fedd0'))
       g212()
    root.bind('<KeyPress-j>', flashb12g2)
    def flashb14g2(event):
       b14g2.config(bg = 'green')
       root.after(175, lambda: b14g2.config(bg = '#6fedd0'))
       g214()
    root.bind('<KeyPress-k>', flashb14g2)
    def flashb16g2(event):
       b16g2.config(bg = 'green')
       root.after(175, lambda: b16g2.config(bg = '#6fedd0'))
       g216()
    root.bind('<KeyPress-l>', flashb16g2)
#########################STRING 3################################
    def flashb1g3(event):
       b1g3.config(bg = 'green')
       root.after(175, lambda: b1g3.config(bg = '#6fedd0'))
       g31()
    root.bind('<KeyPress-q>', flashb1g3)
    def flashb3g3(event):
       b3g3.config(bg = 'green')
       root.after(175, lambda: b3g3.config(bg = '#6fedd0'))
       g33()
    root.bind('<KeyPress-w>', flashb3g3)
    def flashb4g3(event):
       b4g3.config(bg = 'green')
       root.after(175, lambda: b4g3.config(bg = '#6fedd0'))
       g34()
    root.bind('<KeyPress-e>', flashb4g3)
    def flashb6g3(event):
       b6g3.config(bg = 'green')
       root.after(175, lambda: b6g3.config(bg = '#6fedd0'))
       g36()
    root.bind('<KeyPress-r>', flashb6g3)
    def flashb8g3(event):
       b8g3.config(bg = 'green')
       root.after(175, lambda: b8g3.config(bg = '#6fedd0'))
       g38()
    root.bind('<KeyPress-t>', flashb8g3)
    def flashb9g3(event):
       b9g3.config(bg = 'green')
       root.after(175, lambda: b9g3.config(bg = '#6fedd0'))
       g39()
    root.bind('<KeyPress-y>', flashb9g3)
    def flashb11g3(event):
       b11g3.config(bg = 'green')
       root.after(175, lambda: b11g3.config(bg = '#6fedd0'))
       g311()
    root.bind('<KeyPress-u>', flashb11g3)
    def flashb13g3(event):
       b13g3.config(bg = 'green')
       root.after(175, lambda: b13g3.config(bg = '#6fedd0'))
       g313()
    root.bind('<KeyPress-i>', flashb13g3)
    def flashb15g3(event):
       b15g3.config(bg = 'green')
       root.after(175, lambda: b15g3.config(bg = '#6fedd0'))
       g315()
    root.bind('<KeyPress-o>', flashb15g3)
    def flashb16g3(event):
       b16g3.config(bg = 'green')
       root.after(175, lambda: b16g3.config(bg = '#6fedd0'))
       g316()
    root.bind('<KeyPress-p>', flashb16g3)
#########################STRING 4################################
    def flashb1g4(event):
       b1g4.config(bg = 'green')
       root.after(175, lambda: b1g4.config(bg = '#6fedd0'))
       g41()
    root.bind('<KeyPress-1>', flashb1g4)
    def flashb2g4(event):
       b2g4.config(bg = 'green')
       root.after(175, lambda: b2g4.config(bg = '#6fedd0'))
       g42()
    root.bind('<KeyPress-2>', flashb2g4)
    def flashb4g4(event):
       b4g4.config(bg = 'green')
       root.after(175, lambda: b4g4.config(bg = '#6fedd0'))
       g44()
    root.bind('<KeyPress-3>', flashb4g4)
    def flashb6g4(event):
       b6g4.config(bg = 'green')
       root.after(175, lambda: b6g4.config(bg = '#6fedd0'))
       g46()
    root.bind('<KeyPress-4>', flashb6g4)
    def flashb8g4(event):
       b8g4.config(bg = 'green')
       root.after(175, lambda: b8g4.config(bg = '#6fedd0'))
       g48()
    root.bind('<KeyPress-5>', flashb8g4)
    def flashb9g4(event):
       b9g4.config(bg = 'green')
       root.after(175, lambda: b9g4.config(bg = '#6fedd0'))
       g49()
    root.bind('<KeyPress-6>', flashb9g4)
    def flashb11g4(event):
       b11g4.config(bg = 'green')
       root.after(175, lambda: b11g4.config(bg = '#6fedd0'))
       g411()
    root.bind('<KeyPress-7>', flashb11g4)
    def flashb13g4(event):
       b13g4.config(bg = 'green')
       root.after(175, lambda: b13g4.config(bg = '#6fedd0'))
       g413()
    root.bind('<KeyPress-8>', flashb13g4)
    def flashb14g4(event):
       b14g4.config(bg = 'green')
       root.after(175, lambda: b14g4.config(bg = '#6fedd0'))
       g414()
    root.bind('<KeyPress-9>', flashb14g4)
    def flashb16g4(event):
       b16g4.config(bg = 'green')
       root.after(175, lambda: b16g4.config(bg = '#6fedd0'))
       g416()
    root.bind('<KeyPress-0>', flashb16g4)
    
    b2g1.configure(background='#6fedd0')
    b4g1.configure(background='#6fedd0')
    b6g1.configure(background='#6fedd0')
    b7g1.configure(background='#6fedd0')
    b9g1.configure(background='#6fedd0')
    b11g1.configure(background='#6fedd0')
    b12g1.configure(background='#6fedd0')
    b14g1.configure(background='#6fedd0')
    b16g1.configure(background='#6fedd0')
############################STRING 2 ################################
    b2g2.configure(background='#6fedd0')
    b4g2.configure(background='#6fedd0')
    b5g2.configure(background='#6fedd0')
    b7g2.configure(background='#6fedd0')
    b9g2.configure(background='#6fedd0')
    b11g2.configure(background='#6fedd0')
    b12g2.configure(background='#6fedd0')
    b14g2.configure(background='#6fedd0')
    b16g2.configure(background='#6fedd0')
#########################STRING 3################################
    b1g3.configure(background='#6fedd0')
    b3g3.configure(background='#6fedd0')
    b4g3.configure(background='#6fedd0')
    b6g3.configure(background='#6fedd0')
    b8g3.configure(background='#6fedd0')
    b9g3.configure(background='#6fedd0')
    b11g3.configure(background='#6fedd0')
    b13g3.configure(background='#6fedd0')
    b15g3.configure(background='#6fedd0')
    b16g3.configure(background='#6fedd0')
#########################STRING 4################################
    b1g4.configure(background='#6fedd0')
    b2g4.configure(background='#6fedd0')
    b4g4.configure(background='#6fedd0')
    b6g4.configure(background='#6fedd0')
    b8g4.configure(background='#6fedd0')
    b9g4.configure(background='#6fedd0')
    b11g4.configure(background='#6fedd0')
    b13g4.configure(background='#6fedd0')
    b14g4.configure(background='#6fedd0')
    b16g4.configure(background='#6fedd0')
def d_sharp_major_6fedd0():
    b_d_sharp_h.place_forget()
    b_d_sharp.place(x=300,y=50,width=80)
    resetflash()
    
    b2g1.configure(background=orig_color)
    b4g1.configure(background=orig_color)
    b6g1.configure(background=orig_color)
    b7g1.configure(background=orig_color)
    b9g1.configure(background=orig_color)
    b11g1.configure(background=orig_color)
    b12g1.configure(background=orig_color)
    b14g1.configure(background=orig_color)
    b16g1.configure(background=orig_color)
############################STRING 2 ################################
    b2g2.configure(background=orig_color)
    b4g2.configure(background=orig_color)
    b5g2.configure(background=orig_color)
    b7g2.configure(background=orig_color)
    b9g2.configure(background=orig_color)
    b11g2.configure(background=orig_color)
    b12g2.configure(background=orig_color)
    b14g2.configure(background=orig_color)
    b16g2.configure(background=orig_color)
#########################STRING 3################################
    b1g3.configure(background=orig_color)
    b3g3.configure(background=orig_color)
    b4g3.configure(background=orig_color)
    b6g3.configure(background=orig_color)
    b8g3.configure(background=orig_color)
    b9g3.configure(background=orig_color)
    b11g3.configure(background=orig_color)
    b13g3.configure(background=orig_color)
    b15g3.configure(background=orig_color)
    b16g3.configure(background=orig_color)
#########################STRING 4################################
    b1g4.configure(background=orig_color)
    b2g4.configure(background=orig_color)
    b4g4.configure(background=orig_color)
    b6g4.configure(background=orig_color)
    b8g4.configure(background=orig_color)
    b9g4.configure(background=orig_color)
    b11g4.configure(background=orig_color)
    b13g4.configure(background=orig_color)
    b14g4.configure(background=orig_color)
    b16g4.configure(background=orig_color)


def e_major_show():
    b_e.place_forget()
    b_e_h.place(x=400,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)
    
    def flashb1g1(event):
       b1g1.config(bg = 'green')
       root.after(175, lambda: b1g1.config(bg = '#e39ad8'))
       g11()
    root.bind('<KeyPress-z>', flashb1g1)
    def flashb3g1(event):
       b3g1.config(bg = 'green')
       root.after(175, lambda: b3g1.config(bg = '#e39ad8'))
       g13()
    root.bind('<KeyPress-x>', flashb3g1)
    def flashb5g1(event):
       b5g1.config(bg = 'green')
       root.after(175, lambda: b5g1.config(bg = '#e39ad8'))
       g15()
    root.bind('<KeyPress-c>', flashb5g1)
    def flashb7g1(event):
       b7g1.config(bg = 'green')
       root.after(175, lambda: b7g1.config(bg = '#e39ad8'))
       g17()
    root.bind('<KeyPress-v>', flashb7g1)
    def flashb8g1(event):
       b8g1.config(bg = 'green')
       root.after(175, lambda: b8g1.config(bg = '#e39ad8'))
       g18()
    root.bind('<KeyPress-b>', flashb8g1)
    def flashb10g1(event):
       b10g1.config(bg = 'green')
       root.after(175, lambda: b10g1.config(bg = '#e39ad8'))
       g110()
    root.bind('<KeyPress-n>', flashb10g1)
    def flashb12g1(event):
       b12g1.config(bg = 'green')
       root.after(175, lambda: b12g1.config(bg = '#e39ad8'))
       g112()
    root.bind('<KeyPress-m>', flashb12g1)
    def flashb13g1(event):
       b13g1.config(bg = 'green')
       root.after(175, lambda: b13g1.config(bg = '#e39ad8'))
       g113()
    root.bind('<KeyPress-,>', flashb13g1)
    def flashb15g1(event):
       b15g1.config(bg = 'green')
       root.after(175, lambda: b15g1.config(bg = '#e39ad8'))
       g115()
    root.bind('<KeyPress-.>', flashb15g1)
############################STRING 2 ################################
    def flashb1g2(event):
       b1g2.config(bg = 'green')
       root.after(175, lambda: b1g2.config(bg = '#e39ad8'))
       g21()
    root.bind('<KeyPress-a>', flashb1g2)
    def flashb3g2(event):
       b3g2.config(bg = 'green')
       root.after(175, lambda: b3g2.config(bg = '#e39ad8'))
       g23()
    root.bind('<KeyPress-s>', flashb3g2)
    def flashb5g2(event):
       b5g2.config(bg = 'green')
       root.after(175, lambda: b5g2.config(bg = '#e39ad8'))
       g25()
    root.bind('<KeyPress-d>', flashb5g2)
    def flashb6g2(event):
       b6g2.config(bg = 'green')
       root.after(175, lambda: b6g2.config(bg = '#e39ad8'))
       g26()
    root.bind('<KeyPress-f>', flashb6g2)
    def flashb8g2(event):
       b8g2.config(bg = 'green')
       root.after(175, lambda: b8g2.config(bg = '#e39ad8'))
       g28()
    root.bind('<KeyPress-g>', flashb8g2)
    def flashb10g2(event):
       b10g2.config(bg = 'green')
       root.after(175, lambda: b10g2.config(bg = '#e39ad8'))
       g210()
    root.bind('<KeyPress-h>', flashb10g2)
    def flashb12g2(event):
       b12g2.config(bg = 'green')
       root.after(175, lambda: b12g2.config(bg = '#e39ad8'))
       g212()
    root.bind('<KeyPress-j>', flashb12g2)
    def flashb13g2(event):
       b13g2.config(bg = 'green')
       root.after(175, lambda: b13g2.config(bg = '#e39ad8'))
       g213()
    root.bind('<KeyPress-k>', flashb13g2)
    def flashb15g2(event):
       b15g2.config(bg = 'green')
       root.after(175, lambda: b15g2.config(bg = '#e39ad8'))
       g215()
    root.bind('<KeyPress-l>', flashb15g2)
#########################STRING 3################################
    def flashb2g3(event):
       b2g3.config(bg = 'green')
       root.after(175, lambda: b2g3.config(bg = '#e39ad8'))
       g32()
    root.bind('<KeyPress-q>', flashb2g3)
    def flashb4g3(event):
       b4g3.config(bg = 'green')
       root.after(175, lambda: b4g3.config(bg = '#e39ad8'))
       g34()
    root.bind('<KeyPress-w>', flashb4g3)
    def flashb5g3(event):
       b5g3.config(bg = 'green')
       root.after(175, lambda: b5g3.config(bg = '#e39ad8'))
       g35()
    root.bind('<KeyPress-e>', flashb5g3)
    def flashb7g3(event):
       b7g3.config(bg = 'green')
       root.after(175, lambda: b7g3.config(bg = '#e39ad8'))
       g37()
    root.bind('<KeyPress-r>', flashb7g3)
    def flashb9g3(event):
       b9g3.config(bg = 'green')
       root.after(175, lambda: b9g3.config(bg = '#e39ad8'))
       g39()
    root.bind('<KeyPress-t>', flashb9g3)
    def flashb10g3(event):
       b10g3.config(bg = 'green')
       root.after(175, lambda: b10g3.config(bg = '#e39ad8'))
       g310()
    root.bind('<KeyPress-y>', flashb10g3)
    def flashb12g3(event):
       b12g3.config(bg = 'green')
       root.after(175, lambda: b12g3.config(bg = '#e39ad8'))
       g312()
    root.bind('<KeyPress-u>', flashb12g3)
    def flashb14g3(event):
       b14g3.config(bg = 'green')
       root.after(175, lambda: b14g3.config(bg = '#e39ad8'))
       g314()
    root.bind('<KeyPress-i>', flashb14g3)
    def flashb16g3(event):
       b16g3.config(bg = 'green')
       root.after(175, lambda: b16g3.config(bg = '#e39ad8'))
       g316()
    root.bind('<KeyPress-o>', flashb16g3)
#########################STRING 4################################
    def flashb2g4(event):
       b2g4.config(bg = 'green')
       root.after(175, lambda: b2g4.config(bg = '#e39ad8'))
       g42()
    root.bind('<KeyPress-1>', flashb2g4)
    def flashb3g4(event):
       b3g4.config(bg = 'green')
       root.after(175, lambda: b3g4.config(bg = '#e39ad8'))
       g43()
    root.bind('<KeyPress-2>', flashb3g4)
    def flashb5g4(event):
       b5g4.config(bg = 'green')
       root.after(175, lambda: b5g4.config(bg = '#e39ad8'))
       g45()
    root.bind('<KeyPress-3>', flashb5g4)
    def flashb7g4(event):
       b7g4.config(bg = 'green')
       root.after(175, lambda: b7g4.config(bg = '#e39ad8'))
       g47()
    root.bind('<KeyPress-4>', flashb7g4)
    def flashb9g4(event):
       b9g4.config(bg = 'green')
       root.after(175, lambda: b9g4.config(bg = '#e39ad8'))
       g49()
    root.bind('<KeyPress-5>', flashb9g4)
    def flashb10g4(event):
       b10g4.config(bg = 'green')
       root.after(175, lambda: b10g4.config(bg = '#e39ad8'))
       g410()
    root.bind('<KeyPress-6>', flashb10g4)
    def flashb12g4(event):
       b12g4.config(bg = 'green')
       root.after(175, lambda: b12g4.config(bg = '#e39ad8'))
       g412()
    root.bind('<KeyPress-7>', flashb12g4)
    def flashb14g4(event):
       b14g4.config(bg = 'green')
       root.after(175, lambda: b14g4.config(bg = '#e39ad8'))
       g414()
    root.bind('<KeyPress-8>', flashb14g4)
    def flashb15g4(event):
       b15g4.config(bg = 'green')
       root.after(175, lambda: b15g4.config(bg = '#e39ad8'))
       g415()
    root.bind('<KeyPress-9>', flashb15g4)
    b1g1.configure(background='#e39ad8')
    b3g1.configure(background='#e39ad8')
    b5g1.configure(background='#e39ad8')
    b7g1.configure(background='#e39ad8')
    b8g1.configure(background='#e39ad8')
    b10g1.configure(background='#e39ad8')
    b12g1.configure(background='#e39ad8')
    b13g1.configure(background='#e39ad8')
    b15g1.configure(background='#e39ad8')
############################STRING 2 ################################
    b1g2.configure(background='#e39ad8')
    b3g2.configure(background='#e39ad8')
    b5g2.configure(background='#e39ad8')
    b6g2.configure(background='#e39ad8')
    b8g2.configure(background='#e39ad8')
    b10g2.configure(background='#e39ad8')
    b12g2.configure(background='#e39ad8')
    b13g2.configure(background='#e39ad8')
    b15g2.configure(background='#e39ad8')
#########################STRING 3################################
    b2g3.configure(background='#e39ad8')
    b4g3.configure(background='#e39ad8')
    b5g3.configure(background='#e39ad8')
    b7g3.configure(background='#e39ad8')
    b9g3.configure(background='#e39ad8')
    b10g3.configure(background='#e39ad8')
    b12g3.configure(background='#e39ad8')
    b14g3.configure(background='#e39ad8')
    b16g3.configure(background='#e39ad8')
#########################STRING 4################################
    b2g4.configure(background='#e39ad8')
    b3g4.configure(background='#e39ad8')
    b5g4.configure(background='#e39ad8')
    b7g4.configure(background='#e39ad8')
    b9g4.configure(background='#e39ad8')
    b10g4.configure(background='#e39ad8')
    b12g4.configure(background='#e39ad8')
    b14g4.configure(background='#e39ad8')
    b15g4.configure(background='#e39ad8')
def e_major_e39ad8():
    b_e_h.place_forget()
    b_e.place(x=400,y=50,width=80)
    resetflash()
    b1g1.configure(background=orig_color)
    b3g1.configure(background=orig_color)
    b5g1.configure(background=orig_color)
    b7g1.configure(background=orig_color)
    b8g1.configure(background=orig_color)
    b10g1.configure(background=orig_color)
    b12g1.configure(background=orig_color)
    b13g1.configure(background=orig_color)
    b15g1.configure(background=orig_color)
############################STRING 2 ################################
    b1g2.configure(background=orig_color)
    b3g2.configure(background=orig_color)
    b5g2.configure(background=orig_color)
    b6g2.configure(background=orig_color)
    b8g2.configure(background=orig_color)
    b10g2.configure(background=orig_color)
    b12g2.configure(background=orig_color)
    b13g2.configure(background=orig_color)
    b15g2.configure(background=orig_color)
#########################STRING 3################################
    b2g3.configure(background=orig_color)
    b4g3.configure(background=orig_color)
    b5g3.configure(background=orig_color)
    b7g3.configure(background=orig_color)
    b9g3.configure(background=orig_color)
    b10g3.configure(background=orig_color)
    b12g3.configure(background=orig_color)
    b14g3.configure(background=orig_color)
    b16g3.configure(background=orig_color)
#########################STRING 4################################
    b2g4.configure(background=orig_color)
    b3g4.configure(background=orig_color)
    b5g4.configure(background=orig_color)
    b7g4.configure(background=orig_color)
    b9g4.configure(background=orig_color)
    b10g4.configure(background=orig_color)
    b12g4.configure(background=orig_color)
    b14g4.configure(background=orig_color)
    b15g4.configure(background=orig_color)
def f_major_show():
    b_f.place_forget()
    b_f_h.place(x=500,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)
    
    def flashb1g1(event):
       b1g1.config(bg = 'green')
       root.after(175, lambda: b1g1.config(bg = '#ffc830'))
       g11()
    root.bind('<KeyPress-z>', flashb1g1)
    def flashb2g1(event):
       b2g1.config(bg = 'green')
       root.after(175, lambda: b2g1.config(bg = '#ffc830'))
       g12()
    root.bind('<KeyPress-x>', flashb2g1)
    def flashb4g1(event):
       b4g1.config(bg = 'green')
       root.after(175, lambda: b4g1.config(bg = '#ffc830'))
       g14()
    root.bind('<KeyPress-c>', flashb4g1)
    def flashb6g1(event):
       b6g1.config(bg = 'green')
       root.after(175, lambda: b6g1.config(bg = '#ffc830'))
       g16()
    root.bind('<KeyPress-v>', flashb6g1)
    def flashb8g1(event):
       b8g1.config(bg = 'green')
       root.after(175, lambda: b8g1.config(bg = '#ffc830'))
       g18()
    root.bind('<KeyPress-b>', flashb8g1)
    def flashb9g1(event):
       b9g1.config(bg = 'green')
       root.after(175, lambda: b9g1.config(bg = '#ffc830'))
       g19()
    root.bind('<KeyPress-n>', flashb9g1)
    def flashb11g1(event):
       b11g1.config(bg = 'green')
       root.after(175, lambda: b11g1.config(bg = '#ffc830'))
       g111()
    root.bind('<KeyPress-m>', flashb11g1)
    def flashb13g1(event):
       b13g1.config(bg = 'green')
       root.after(175, lambda: b13g1.config(bg = '#ffc830'))
       g113()
    root.bind('<KeyPress-,>', flashb13g1)
    def flashb14g1(event):
       b14g1.config(bg = 'green')
       root.after(175, lambda: b14g1.config(bg = '#ffc830'))
       g114()
    root.bind('<KeyPress-.>', flashb14g1)
    def flashb16g1(event):
       b16g1.config(bg = 'green')
       root.after(175, lambda: b16g1.config(bg = '#ffc830'))
       g116()
    root.bind('<KeyPress-/>', flashb16g1)
############################STRING 2 ################################
    def flashb1g2(event):
       b1g2.config(bg = 'green')
       root.after(175, lambda: b1g2.config(bg = '#ffc830'))
       g21()
    root.bind('<KeyPress-a>', flashb1g2)
    def flashb2g2(event):
       b2g2.config(bg = 'green')
       root.after(175, lambda: b2g2.config(bg = '#ffc830'))
       g22()
    root.bind('<KeyPress-s>', flashb2g2)
    def flashb4g2(event):
       b4g2.config(bg = 'green')
       root.after(175, lambda: b4g2.config(bg = '#ffc830'))
       g24()
    root.bind('<KeyPress-d>', flashb4g2)
    def flashb6g2(event):
       b6g2.config(bg = 'green')
       root.after(175, lambda: b6g2.config(bg = '#ffc830'))
       g26()
    root.bind('<KeyPress-f>', flashb6g2)
    def flashb7g2(event):
       b7g2.config(bg = 'green')
       root.after(175, lambda: b7g2.config(bg = '#ffc830'))
       g27()
    root.bind('<KeyPress-g>', flashb7g2)
    def flashb9g2(event):
       b9g2.config(bg = 'green')
       root.after(175, lambda: b9g2.config(bg = '#ffc830'))
       g29()
    root.bind('<KeyPress-h>', flashb9g2)
    def flashb11g2(event):
       b11g2.config(bg = 'green')
       root.after(175, lambda: b11g2.config(bg = '#ffc830'))
       g211()
    root.bind('<KeyPress-j>', flashb11g2)
    def flashb13g2(event):
       b13g2.config(bg = 'green')
       root.after(175, lambda: b13g2.config(bg = '#ffc830'))
       g213()
    root.bind('<KeyPress-k>', flashb13g2)
    def flashb14g2(event):
       b14g2.config(bg = 'green')
       root.after(175, lambda: b14g2.config(bg = '#ffc830'))
       g214()
    root.bind('<KeyPress-l>', flashb14g2)
    def flashb16g2(event):
       b16g2.config(bg = 'green')
       root.after(175, lambda: b16g2.config(bg = '#ffc830'))
       g216()
    root.bind('<KeyPress-;>', flashb16g2)
#########################STRING 3################################
    def flashb1g3(event):
       b1g3.config(bg = 'green')
       root.after(175, lambda: b1g3.config(bg = '#ffc830'))
       g31()
    root.bind('<KeyPress-q>', flashb1g3)
    def flashb3g3(event):
       b3g3.config(bg = 'green')
       root.after(175, lambda: b3g3.config(bg = '#ffc830'))
       g33()
    root.bind('<KeyPress-w>', flashb3g3)
    def flashb5g3(event):
       b5g3.config(bg = 'green')
       root.after(175, lambda: b5g3.config(bg = '#ffc830'))
       g35()
    root.bind('<KeyPress-e>', flashb5g3)
    def flashb6g3(event):
       b6g3.config(bg = 'green')
       root.after(175, lambda: b6g3.config(bg = '#ffc830'))
       g36()
    root.bind('<KeyPress-r>', flashb6g3)
    def flashb8g3(event):
       b8g3.config(bg = 'green')
       root.after(175, lambda: b8g3.config(bg = '#ffc830'))
       g38()
    root.bind('<KeyPress-t>', flashb8g3)
    def flashb10g3(event):
       b10g3.config(bg = 'green')
       root.after(175, lambda: b10g3.config(bg = '#ffc830'))
       g310()
    root.bind('<KeyPress-y>', flashb10g3)
    def flashb11g3(event):
       b11g3.config(bg = 'green')
       root.after(175, lambda: b11g3.config(bg = '#ffc830'))
       g311()
    root.bind('<KeyPress-u>', flashb11g3)
    def flashb13g3(event):
       b13g3.config(bg = 'green')
       root.after(175, lambda: b13g3.config(bg = '#ffc830'))
       g313()
    root.bind('<KeyPress-i>', flashb13g3)
    def flashb15g3(event):
       b15g3.config(bg = 'green')
       root.after(175, lambda: b15g3.config(bg = '#ffc830'))
       g315()
    root.bind('<KeyPress-o>', flashb15g3)
#########################STRING 4################################
    def flashb1g4(event):
       b1g4.config(bg = 'green')
       root.after(175, lambda: b1g4.config(bg = '#ffc830'))
       g41()
    root.bind('<KeyPress-1>', flashb1g4)
    def flashb3g4(event):
       b3g4.config(bg = 'green')
       root.after(175, lambda: b3g4.config(bg = '#ffc830'))
       g43()
    root.bind('<KeyPress-2>', flashb3g4)
    def flashb4g4(event):
       b4g4.config(bg = 'green')
       root.after(175, lambda: b4g4.config(bg = '#ffc830'))
       g44()
    root.bind('<KeyPress-3>', flashb4g4)
    def flashb6g4(event):
       b6g4.config(bg = 'green')
       root.after(175, lambda: b6g4.config(bg = '#ffc830'))
       g46()
    root.bind('<KeyPress-4>', flashb6g4)
    def flashb8g4(event):
       b8g4.config(bg = 'green')
       root.after(175, lambda: b8g4.config(bg = '#ffc830'))
       g48()
    root.bind('<KeyPress-5>', flashb8g4)
    def flashb10g4(event):
       b10g4.config(bg = 'green')
       root.after(175, lambda: b10g4.config(bg = '#ffc830'))
       g410()
    root.bind('<KeyPress-6>', flashb10g4)
    def flashb11g4(event):
       b11g4.config(bg = 'green')
       root.after(175, lambda: b11g4.config(bg = '#ffc830'))
       g411()
    root.bind('<KeyPress-7>', flashb11g4)
    def flashb13g4(event):
       b13g4.config(bg = 'green')
       root.after(175, lambda: b13g4.config(bg = '#ffc830'))
       g413()
    root.bind('<KeyPress-8>', flashb13g4)
    def flashb15g4(event):
       b15g4.config(bg = 'green')
       root.after(175, lambda: b15g4.config(bg = '#ffc830'))
       g415()
    root.bind('<KeyPress-9>', flashb15g4)
    def flashb16g4(event):
       b16g4.config(bg = 'green')
       root.after(175, lambda: b16g4.config(bg = '#ffc830'))
       g416()
    root.bind('<KeyPress-0>', flashb16g4)
    b1g1.configure(background='#ffc830')
    b2g1.configure(background='#ffc830')
    b4g1.configure(background='#ffc830')
    b6g1.configure(background='#ffc830')
    b8g1.configure(background='#ffc830')
    b9g1.configure(background='#ffc830')
    b11g1.configure(background='#ffc830')
    b13g1.configure(background='#ffc830')
    b14g1.configure(background='#ffc830')
    b16g1.configure(background='#ffc830')
############################STRING 2 ################################
    b1g2.configure(background='#ffc830')
    b2g2.configure(background='#ffc830')
    b4g2.configure(background='#ffc830')
    b6g2.configure(background='#ffc830')
    b7g2.configure(background='#ffc830')
    b9g2.configure(background='#ffc830')
    b11g2.configure(background='#ffc830')
    b13g2.configure(background='#ffc830')
    b14g2.configure(background='#ffc830')
    b16g2.configure(background='#ffc830')
#########################STRING 3################################
    b1g3.configure(background='#ffc830')
    b3g3.configure(background='#ffc830')
    b5g3.configure(background='#ffc830')
    b6g3.configure(background='#ffc830')
    b8g3.configure(background='#ffc830')
    b10g3.configure(background='#ffc830')
    b11g3.configure(background='#ffc830')
    b13g3.configure(background='#ffc830')
    b15g3.configure(background='#ffc830')
#########################STRING 4################################
    b1g4.configure(background='#ffc830')
    b3g4.configure(background='#ffc830')
    b4g4.configure(background='#ffc830')
    b6g4.configure(background='#ffc830')
    b8g4.configure(background='#ffc830')
    b10g4.configure(background='#ffc830')
    b11g4.configure(background='#ffc830')
    b13g4.configure(background='#ffc830')
    b15g4.configure(background='#ffc830')
    b16g4.configure(background='#ffc830')
def f_major_ffc830():
    b_f_h.place_forget()
    b_f.place(x=500,y=50,width=80)
    resetflash()
    b1g1.configure(background=orig_color)
    b2g1.configure(background=orig_color)
    b4g1.configure(background=orig_color)
    b6g1.configure(background=orig_color)
    b8g1.configure(background=orig_color)
    b9g1.configure(background=orig_color)
    b11g1.configure(background=orig_color)
    b13g1.configure(background=orig_color)
    b14g1.configure(background=orig_color)
    b16g1.configure(background=orig_color)
############################STRING 2 ################################
    b1g2.configure(background=orig_color)
    b2g2.configure(background=orig_color)
    b4g2.configure(background=orig_color)
    b6g2.configure(background=orig_color)
    b7g2.configure(background=orig_color)
    b9g2.configure(background=orig_color)
    b11g2.configure(background=orig_color)
    b13g2.configure(background=orig_color)
    b14g2.configure(background=orig_color)
    b16g2.configure(background=orig_color)
#########################STRING 3################################
    b1g3.configure(background=orig_color)
    b3g3.configure(background=orig_color)
    b5g3.configure(background=orig_color)
    b6g3.configure(background=orig_color)
    b8g3.configure(background=orig_color)
    b10g3.configure(background=orig_color)
    b11g3.configure(background=orig_color)
    b13g3.configure(background=orig_color)
    b15g3.configure(background=orig_color)
#########################STRING 4################################
    b1g4.configure(background=orig_color)
    b3g4.configure(background=orig_color)
    b4g4.configure(background=orig_color)
    b6g4.configure(background=orig_color)
    b8g4.configure(background=orig_color)
    b10g4.configure(background=orig_color)
    b11g4.configure(background=orig_color)
    b13g4.configure(background=orig_color)
    b15g4.configure(background=orig_color)
    b16g4.configure(background=orig_color)


def f_sharp_major_show():
    b_f_sharp.place_forget()
    b_f_sharp_h.place(x=600,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)
    
    def flashb2g1(event):
       b2g1.config(bg = 'green')
       root.after(175, lambda: b2g1.config(bg = '#f7929a'))
       g12()
    root.bind('<KeyPress-z>', flashb2g1)
    def flashb3g1(event):
       b3g1.config(bg = 'green')
       root.after(175, lambda: b3g1.config(bg = '#f7929a'))
       g13()
    root.bind('<KeyPress-x>', flashb3g1)
    def flashb5g1(event):
       b5g1.config(bg = 'green')
       root.after(175, lambda: b5g1.config(bg = '#f7929a'))
       g15()
    root.bind('<KeyPress-c>', flashb5g1)
    def flashb7g1(event):
       b7g1.config(bg = 'green')
       root.after(175, lambda: b7g1.config(bg = '#f7929a'))
       g17()
    root.bind('<KeyPress-v>', flashb7g1)
    def flashb9g1(event):
       b9g1.config(bg = 'green')
       root.after(175, lambda: b9g1.config(bg = '#f7929a'))
       g19()
    root.bind('<KeyPress-b>', flashb9g1)
    def flashb10g1(event):
       b10g1.config(bg = 'green')
       root.after(175, lambda: b10g1.config(bg = '#f7929a'))
       g110()
    root.bind('<KeyPress-n>', flashb10g1)
    def flashb12g1(event):
       b12g1.config(bg = 'green')
       root.after(175, lambda: b12g1.config(bg = '#f7929a'))
       g112()
    root.bind('<KeyPress-m>', flashb12g1)
    def flashb14g1(event):
       b14g1.config(bg = 'green')
       root.after(175, lambda: b14g1.config(bg = '#f7929a'))
       g114()
    root.bind('<KeyPress-,>', flashb14g1)
    def flashb15g1(event):
       b15g1.config(bg = 'green')
       root.after(175, lambda: b15g1.config(bg = '#f7929a'))
       g115()
    root.bind('<KeyPress-.>', flashb15g1)
############################STRING 2 ################################
    def flashb2g2(event):
       b2g2.config(bg = 'green')
       root.after(175, lambda: b2g2.config(bg = '#f7929a'))
       g22()
    root.bind('<KeyPress-a>', flashb2g2)
    def flashb3g2(event):
       b3g2.config(bg = 'green')
       root.after(175, lambda: b3g2.config(bg = '#f7929a'))
       g23()
    root.bind('<KeyPress-s>', flashb3g2)
    def flashb5g2(event):
       b5g2.config(bg = 'green')
       root.after(175, lambda: b5g2.config(bg = '#f7929a'))
       g25()
    root.bind('<KeyPress-d>', flashb5g2)
    def flashb7g2(event):
       b7g2.config(bg = 'green')
       root.after(175, lambda: b7g2.config(bg = '#f7929a'))
       g27()
    root.bind('<KeyPress-f>', flashb7g2)
    def flashb8g2(event):
       b8g2.config(bg = 'green')
       root.after(175, lambda: b8g2.config(bg = '#f7929a'))
       g28()
    root.bind('<KeyPress-g>', flashb8g2)
    def flashb10g2(event):
       b10g2.config(bg = 'green')
       root.after(175, lambda: b10g2.config(bg = '#f7929a'))
       g210()
    root.bind('<KeyPress-h>', flashb10g2)
    def flashb12g2(event):
       b12g2.config(bg = 'green')
       root.after(175, lambda: b12g2.config(bg = '#f7929a'))
       g212()
    root.bind('<KeyPress-j>', flashb12g2)
    def flashb14g2(event):
       b14g2.config(bg = 'green')
       root.after(175, lambda: b14g2.config(bg = '#f7929a'))
       g214()
    root.bind('<KeyPress-k>', flashb14g2)
    def flashb15g2(event):
       b15g2.config(bg = 'green')
       root.after(175, lambda: b15g2.config(bg = '#f7929a'))
       g215()
    root.bind('<KeyPress-l>', flashb15g2)
#########################STRING 3################################
    def flashb2g3(event):
       b2g3.config(bg = 'green')
       root.after(175, lambda: b2g3.config(bg = '#f7929a'))
       g32()
    root.bind('<KeyPress-q>', flashb2g3)
    def flashb4g3(event):
       b4g3.config(bg = 'green')
       root.after(175, lambda: b4g3.config(bg = '#f7929a'))
       g34()
    root.bind('<KeyPress-w>', flashb4g3)
    def flashb6g3(event):
       b6g3.config(bg = 'green')
       root.after(175, lambda: b6g3.config(bg = '#f7929a'))
       g36()
    root.bind('<KeyPress-e>', flashb6g3)
    def flashb7g3(event):
       b7g3.config(bg = 'green')
       root.after(175, lambda: b7g3.config(bg = '#f7929a'))
       g37()
    root.bind('<KeyPress-r>', flashb7g3)
    def flashb9g3(event):
       b9g3.config(bg = 'green')
       root.after(175, lambda: b9g3.config(bg = '#f7929a'))
       g39()
    root.bind('<KeyPress-t>', flashb9g3)
    def flashb11g3(event):
       b11g3.config(bg = 'green')
       root.after(175, lambda: b11g3.config(bg = '#f7929a'))
       g311()
    root.bind('<KeyPress-y>', flashb11g3)
    def flashb12g3(event):
       b12g3.config(bg = 'green')
       root.after(175, lambda: b12g3.config(bg = '#f7929a'))
       g312()
    root.bind('<KeyPress-u>', flashb12g3)
    def flashb14g3(event):
       b14g3.config(bg = 'green')
       root.after(175, lambda: b14g3.config(bg = '#f7929a'))
       g314()
    root.bind('<KeyPress-i>', flashb14g3)
    def flashb16g3(event):
       b16g3.config(bg = 'green')
       root.after(175, lambda: b16g3.config(bg = '#f7929a'))
       g316()
    root.bind('<KeyPress-o>', flashb16g3)
#########################STRING 4################################
    def flashb2g4(event):
       b2g4.config(bg = 'green')
       root.after(175, lambda: b2g4.config(bg = '#f7929a'))
       g42()
    root.bind('<KeyPress-1>', flashb2g4)
    def flashb4g4(event):
       b4g4.config(bg = 'green')
       root.after(175, lambda: b4g4.config(bg = '#f7929a'))
       g44()
    root.bind('<KeyPress-2>', flashb4g4)
    def flashb5g4(event):
       b5g4.config(bg = 'green')
       root.after(175, lambda: b5g4.config(bg = '#f7929a'))
       g45()
    root.bind('<KeyPress-3>', flashb5g4)
    def flashb7g4(event):
       b7g4.config(bg = 'green')
       root.after(175, lambda: b7g4.config(bg = '#f7929a'))
       g47()
    root.bind('<KeyPress-4>', flashb7g4)
    def flashb9g4(event):
       b9g4.config(bg = 'green')
       root.after(175, lambda: b9g4.config(bg = '#f7929a'))
       g49()
    root.bind('<KeyPress-5>', flashb9g4)
    def flashb11g4(event):
       b11g4.config(bg = 'green')
       root.after(175, lambda: b11g4.config(bg = '#f7929a'))
       g411()
    root.bind('<KeyPress-6>', flashb11g4)
    def flashb12g4(event):
       b12g4.config(bg = 'green')
       root.after(175, lambda: b12g4.config(bg = '#f7929a'))
       g412()
    root.bind('<KeyPress-7>', flashb12g4)
    def flashb14g4(event):
       b14g4.config(bg = 'green')
       root.after(175, lambda: b14g4.config(bg = '#f7929a'))
       g414()
    root.bind('<KeyPress-8>', flashb14g4)
    def flashb16g4(event):
       b16g4.config(bg = 'green')
       root.after(175, lambda: b16g4.config(bg = '#f7929a'))
       g416()
    root.bind('<KeyPress-9>', flashb16g4)
    b2g1.configure(background='#f7929a')
    b3g1.configure(background='#f7929a')
    b5g1.configure(background='#f7929a')
    b7g1.configure(background='#f7929a')
    b9g1.configure(background='#f7929a')
    b10g1.configure(background='#f7929a')
    b12g1.configure(background='#f7929a')
    b14g1.configure(background='#f7929a')
    b15g1.configure(background='#f7929a')
############################STRING 2 ################################
    b2g2.configure(background='#f7929a')
    b3g2.configure(background='#f7929a')
    b5g2.configure(background='#f7929a')
    b7g2.configure(background='#f7929a')
    b8g2.configure(background='#f7929a')
    b10g2.configure(background='#f7929a')
    b12g2.configure(background='#f7929a')
    b14g2.configure(background='#f7929a')
    b15g2.configure(background='#f7929a')
#########################STRING 3################################
    b2g3.configure(background='#f7929a')
    b4g3.configure(background='#f7929a')
    b6g3.configure(background='#f7929a')
    b7g3.configure(background='#f7929a')
    b9g3.configure(background='#f7929a')
    b11g3.configure(background='#f7929a')
    b12g3.configure(background='#f7929a')
    b14g3.configure(background='#f7929a')
    b16g3.configure(background='#f7929a')
#########################STRING 4################################
    b2g4.configure(background='#f7929a')
    b4g4.configure(background='#f7929a')
    b5g4.configure(background='#f7929a')
    b7g4.configure(background='#f7929a')
    b9g4.configure(background='#f7929a')
    b11g4.configure(background='#f7929a')
    b12g4.configure(background='#f7929a')
    b14g4.configure(background='#f7929a')
    b16g4.configure(background='#f7929a')
def f_sharp_major_f7929a():
    b_f_sharp_h.place_forget()
    b_f_sharp.place(x=600,y=50,width=80)
    resetflash()
    b2g1.configure(background=orig_color)
    b3g1.configure(background=orig_color)
    b5g1.configure(background=orig_color)
    b7g1.configure(background=orig_color)
    b9g1.configure(background=orig_color)
    b10g1.configure(background=orig_color)
    b12g1.configure(background=orig_color)
    b14g1.configure(background=orig_color)
    b15g1.configure(background=orig_color)
############################STRING 2 ################################
    b2g2.configure(background=orig_color)
    b3g2.configure(background=orig_color)
    b5g2.configure(background=orig_color)
    b7g2.configure(background=orig_color)
    b8g2.configure(background=orig_color)
    b10g2.configure(background=orig_color)
    b12g2.configure(background=orig_color)
    b14g2.configure(background=orig_color)
    b15g2.configure(background=orig_color)
#########################STRING 3################################
    b2g3.configure(background=orig_color)
    b4g3.configure(background=orig_color)
    b6g3.configure(background=orig_color)
    b7g3.configure(background=orig_color)
    b9g3.configure(background=orig_color)
    b11g3.configure(background=orig_color)
    b12g3.configure(background=orig_color)
    b14g3.configure(background=orig_color)
    b16g3.configure(background=orig_color)
#########################STRING 4################################
    b2g4.configure(background=orig_color)
    b4g4.configure(background=orig_color)
    b5g4.configure(background=orig_color)
    b7g4.configure(background=orig_color)
    b9g4.configure(background=orig_color)
    b11g4.configure(background=orig_color)
    b12g4.configure(background=orig_color)
    b14g4.configure(background=orig_color)
    b16g4.configure(background=orig_color)
    
def g_major_show():
    b_g.place_forget()
    b_g_h.place(x=700,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)
    
    def flashb1g1(event):
       b1g1.config(bg = 'green')
       root.after(175, lambda: b1g1.config(bg = '#a8edaf'))
       g11()
    root.bind('<KeyPress-z>', flashb1g1)
    def flashb3g1(event):
       b3g1.config(bg = 'green')
       root.after(175, lambda: b3g1.config(bg = '#a8edaf'))
       g13()
    root.bind('<KeyPress-x>', flashb3g1)
    def flashb4g1(event):
       b4g1.config(bg = 'green')
       root.after(175, lambda: b4g1.config(bg = '#a8edaf'))
       g14()
    root.bind('<KeyPress-c>', flashb4g1)
    def flashb6g1(event):
       b6g1.config(bg = 'green')
       root.after(175, lambda: b6g1.config(bg = '#a8edaf'))
       g16()
    root.bind('<KeyPress-v>', flashb6g1)
    def flashb8g1(event):
       b8g1.config(bg = 'green')
       root.after(175, lambda: b8g1.config(bg = '#a8edaf'))
       g18()
    root.bind('<KeyPress-b>', flashb8g1)
    def flashb10g1(event):
       b10g1.config(bg = 'green')
       root.after(175, lambda: b10g1.config(bg = '#a8edaf'))
       g110()
    root.bind('<KeyPress-n>', flashb10g1)
    def flashb11g1(event):
       b11g1.config(bg = 'green')
       root.after(175, lambda: b11g1.config(bg = '#a8edaf'))
       g111()
    root.bind('<KeyPress-m>', flashb11g1)
    def flashb13g1(event):
       b13g1.config(bg = 'green')
       root.after(175, lambda: b13g1.config(bg = '#a8edaf'))
       g113()
    root.bind('<KeyPress-,>', flashb13g1)
    def flashb15g1(event):
       b15g1.config(bg = 'green')
       root.after(175, lambda: b15g1.config(bg = '#a8edaf'))
       g115()
    root.bind('<KeyPress-.>', flashb15g1)
    def flashb16g1(event):
       b16g1.config(bg = 'green')
       root.after(175, lambda: b16g1.config(bg = '#a8edaf'))
       g116()
    root.bind('<KeyPress-/>', flashb16g1)
############################STRING 2 ################################
    def flashb1g2(event):
       b1g2.config(bg = 'green')
       root.after(175, lambda: b1g2.config(bg = '#a8edaf'))
       g21()
    root.bind('<KeyPress-a>', flashb1g2)
    def flashb3g2(event):
       b3g2.config(bg = 'green')
       root.after(175, lambda: b3g2.config(bg = '#a8edaf'))
       g23()
    root.bind('<KeyPress-s>', flashb3g2)
    def flashb4g2(event):
       b4g2.config(bg = 'green')
       root.after(175, lambda: b4g2.config(bg = '#a8edaf'))
       g24()
    root.bind('<KeyPress-d>', flashb4g2)
    def flashb6g2(event):
       b6g2.config(bg = 'green')
       root.after(175, lambda: b6g2.config(bg = '#a8edaf'))
       g26()
    root.bind('<KeyPress-f>', flashb6g2)
    def flashb8g2(event):
       b8g2.config(bg = 'green')
       root.after(175, lambda: b8g2.config(bg = '#a8edaf'))
       g28()
    root.bind('<KeyPress-g>', flashb8g2)
    def flashb9g2(event):
       b9g2.config(bg = 'green')
       root.after(175, lambda: b9g2.config(bg = '#a8edaf'))
       g29()
    root.bind('<KeyPress-h>', flashb9g2)
    def flashb11g2(event):
       b11g2.config(bg = 'green')
       root.after(175, lambda: b11g2.config(bg = '#a8edaf'))
       g211()
    root.bind('<KeyPress-j>', flashb11g2)
    def flashb13g2(event):
       b13g2.config(bg = 'green')
       root.after(175, lambda: b13g2.config(bg = '#a8edaf'))
       g213()
    root.bind('<KeyPress-k>', flashb13g2)
    def flashb15g2(event):
       b15g2.config(bg = 'green')
       root.after(175, lambda: b15g2.config(bg = '#a8edaf'))
       g215()
    root.bind('<KeyPress-l>', flashb15g2)
    def flashb16g2(event):
       b16g2.config(bg = 'green')
       root.after(175, lambda: b16g2.config(bg = '#a8edaf'))
       g216()
    root.bind('<KeyPress-;>', flashb16g2)
#########################STRING 3################################
    def flashb1g3(event):
       b1g3.config(bg = 'green')
       root.after(175, lambda: b1g3.config(bg = '#a8edaf'))
       g31()
    root.bind('<KeyPress-q>', flashb1g3)
    def flashb3g3(event):
       b3g3.config(bg = 'green')
       root.after(175, lambda: b3g3.config(bg = '#a8edaf'))
       g33()
    root.bind('<KeyPress-w>', flashb3g3)
    def flashb5g3(event):
       b5g3.config(bg = 'green')
       root.after(175, lambda: b5g3.config(bg = '#a8edaf'))
       g35()
    root.bind('<KeyPress-e>', flashb5g3)
    def flashb7g3(event):
       b7g3.config(bg = 'green')
       root.after(175, lambda: b7g3.config(bg = '#a8edaf'))
       g37()
    root.bind('<KeyPress-r>', flashb7g3)
    def flashb8g3(event):
       b8g3.config(bg = 'green')
       root.after(175, lambda: b8g3.config(bg = '#a8edaf'))
       g38()
    root.bind('<KeyPress-t>', flashb8g3)
    def flashb10g3(event):
       b10g3.config(bg = 'green')
       root.after(175, lambda: b10g3.config(bg = '#a8edaf'))
       g310()
    root.bind('<KeyPress-y>', flashb10g3)
    def flashb12g3(event):
       b12g3.config(bg = 'green')
       root.after(175, lambda: b12g3.config(bg = '#a8edaf'))
       g312()
    root.bind('<KeyPress-u>', flashb12g3)
    def flashb13g3(event):
       b13g3.config(bg = 'green')
       root.after(175, lambda: b13g3.config(bg = '#a8edaf'))
       g313()
    root.bind('<KeyPress-i>', flashb13g3)
    def flashb15g3(event):
       b15g3.config(bg = 'green')
       root.after(175, lambda: b15g3.config(bg = '#a8edaf'))
       g315()
    root.bind('<KeyPress-o>', flashb15g3)
#########################STRING 4################################
    def flashb1g4(event):
       b1g4.config(bg = 'green')
       root.after(175, lambda: b1g4.config(bg = '#a8edaf'))
       g41()
    root.bind('<KeyPress-1>', flashb1g4)
    def flashb3g4(event):
       b3g4.config(bg = 'green')
       root.after(175, lambda: b3g4.config(bg = '#a8edaf'))
       g43()
    root.bind('<KeyPress-2>', flashb3g4)
    def flashb5g4(event):
       b5g4.config(bg = 'green')
       root.after(175, lambda: b5g4.config(bg = '#a8edaf'))
       g45()
    root.bind('<KeyPress-3>', flashb5g4)
    def flashb6g4(event):
       b6g4.config(bg = 'green')
       root.after(175, lambda: b6g4.config(bg = '#a8edaf'))
       g46()
    root.bind('<KeyPress-4>', flashb6g4)
    def flashb8g4(event):
       b8g4.config(bg = 'green')
       root.after(175, lambda: b8g4.config(bg = '#a8edaf'))
       g48()
    root.bind('<KeyPress-5>', flashb8g4)
    def flashb10g4(event):
       b10g4.config(bg = 'green')
       root.after(175, lambda: b10g4.config(bg = '#a8edaf'))
       g410()
    root.bind('<KeyPress-6>', flashb10g4)
    def flashb12g4(event):
       b12g4.config(bg = 'green')
       root.after(175, lambda: b12g4.config(bg = '#a8edaf'))
       g412()
    root.bind('<KeyPress-7>', flashb12g4)
    def flashb13g4(event):
       b13g4.config(bg = 'green')
       root.after(175, lambda: b13g4.config(bg = '#a8edaf'))
       g413()
    root.bind('<KeyPress-8>', flashb13g4)
    def flashb15g4(event):
       b15g4.config(bg = 'green')
       root.after(175, lambda: b15g4.config(bg = '#a8edaf'))
       g415()
    root.bind('<KeyPress-9>', flashb15g4)
    b1g1.configure(background='#a8edaf')
    b3g1.configure(background='#a8edaf')
    b4g1.configure(background='#a8edaf')
    b6g1.configure(background='#a8edaf')
    b8g1.configure(background='#a8edaf')
    b10g1.configure(background='#a8edaf')
    b11g1.configure(background='#a8edaf')
    b13g1.configure(background='#a8edaf')
    b15g1.configure(background='#a8edaf')
    b16g1.configure(background='#a8edaf')
############################STRING 2 ################################
    b1g2.configure(background='#a8edaf')
    b3g2.configure(background='#a8edaf')
    b4g2.configure(background='#a8edaf')
    b6g2.configure(background='#a8edaf')
    b8g2.configure(background='#a8edaf')
    b9g2.configure(background='#a8edaf')
    b11g2.configure(background='#a8edaf')
    b13g2.configure(background='#a8edaf')
    b15g2.configure(background='#a8edaf')
    b16g2.configure(background='#a8edaf')
#########################STRING 3################################
    b1g3.configure(background='#a8edaf')
    b3g3.configure(background='#a8edaf')
    b5g3.configure(background='#a8edaf')
    b7g3.configure(background='#a8edaf')
    b8g3.configure(background='#a8edaf')
    b10g3.configure(background='#a8edaf')
    b12g3.configure(background='#a8edaf')
    b13g3.configure(background='#a8edaf')
    b15g3.configure(background='#a8edaf')
#########################STRING 4################################
    b1g4.configure(background='#a8edaf')
    b3g4.configure(background='#a8edaf')
    b5g4.configure(background='#a8edaf')
    b6g4.configure(background='#a8edaf')
    b8g4.configure(background='#a8edaf')
    b10g4.configure(background='#a8edaf')
    b12g4.configure(background='#a8edaf')
    b13g4.configure(background='#a8edaf')
    b15g4.configure(background='#a8edaf')

def g_major_a8edaf():
    b_g_h.place_forget()
    b_g.place(x=700,y=50,width=80)
    resetflash()
    b1g1.configure(background=orig_color)
    b3g1.configure(background=orig_color)
    b4g1.configure(background=orig_color)
    b6g1.configure(background=orig_color)
    b8g1.configure(background=orig_color)
    b10g1.configure(background=orig_color)
    b11g1.configure(background=orig_color)
    b13g1.configure(background=orig_color)
    b15g1.configure(background=orig_color)
    b16g1.configure(background=orig_color)
############################STRING 2 ################################
    b1g2.configure(background=orig_color)
    b3g2.configure(background=orig_color)
    b4g2.configure(background=orig_color)
    b6g2.configure(background=orig_color)
    b8g2.configure(background=orig_color)
    b9g2.configure(background=orig_color)
    b11g2.configure(background=orig_color)
    b13g2.configure(background=orig_color)
    b15g2.configure(background=orig_color)
    b16g2.configure(background=orig_color)
#########################STRING 3################################
    b1g3.configure(background=orig_color)
    b3g3.configure(background=orig_color)
    b5g3.configure(background=orig_color)
    b7g3.configure(background=orig_color)
    b8g3.configure(background=orig_color)
    b10g3.configure(background=orig_color)
    b12g3.configure(background=orig_color)
    b13g3.configure(background=orig_color)
    b15g3.configure(background=orig_color)
#########################STRING 4################################
    b1g4.configure(background=orig_color)
    b3g4.configure(background=orig_color)
    b5g4.configure(background=orig_color)
    b6g4.configure(background=orig_color)
    b8g4.configure(background=orig_color)
    b10g4.configure(background=orig_color)
    b12g4.configure(background=orig_color)
    b13g4.configure(background=orig_color)
    b15g4.configure(background=orig_color)
def g_sharp_major_show():
    b_g_sharp.place_forget()
    b_g_sharp_h.place(x=800,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)
    
    def flashb2g1(event):
       b2g1.config(bg = 'green')
       root.after(175, lambda: b2g1.config(bg = '#d9a49a'))
       g12()
    root.bind('<KeyPress-z>', flashb2g1)
    def flashb4g1(event):
       b4g1.config(bg = 'green')
       root.after(175, lambda: b4g1.config(bg = '#d9a49a'))
       g14()
    root.bind('<KeyPress-x>', flashb4g1)
    def flashb5g1(event):
       b5g1.config(bg = 'green')
       root.after(175, lambda: b5g1.config(bg = '#d9a49a'))
       g15()
    root.bind('<KeyPress-c>', flashb5g1)
    def flashb7g1(event):
       b7g1.config(bg = 'green')
       root.after(175, lambda: b7g1.config(bg = '#d9a49a'))
       g17()
    root.bind('<KeyPress-v>', flashb7g1)
    def flashb9g1(event):
       b9g1.config(bg = 'green')
       root.after(175, lambda: b9g1.config(bg = '#d9a49a'))
       g19()
    root.bind('<KeyPress-b>', flashb9g1)
    def flashb11g1(event):
       b11g1.config(bg = 'green')
       root.after(175, lambda: b11g1.config(bg = '#d9a49a'))
       g111()
    root.bind('<KeyPress-n>', flashb11g1)
    def flashb12g1(event):
       b12g1.config(bg = 'green')
       root.after(175, lambda: b12g1.config(bg = '#d9a49a'))
       g112()
    root.bind('<KeyPress-m>', flashb12g1)
    def flashb14g1(event):
       b14g1.config(bg = 'green')
       root.after(175, lambda: b14g1.config(bg = '#d9a49a'))
       g114()
    root.bind('<KeyPress-,>', flashb14g1)
    def flashb16g1(event):
       b16g1.config(bg = 'green')
       root.after(175, lambda: b16g1.config(bg = '#d9a49a'))
       g116()
    root.bind('<KeyPress-.>', flashb16g1)
############################STRING 2 ################################
    def flashb2g2(event):
       b2g2.config(bg = 'green')
       root.after(175, lambda: b2g2.config(bg = '#d9a49a'))
       g22()
    root.bind('<KeyPress-a>', flashb2g2)
    def flashb4g2(event):
       b4g2.config(bg = 'green')
       root.after(175, lambda: b4g2.config(bg = '#d9a49a'))
       g24()
    root.bind('<KeyPress-s>', flashb4g2)
    def flashb5g2(event):
       b5g2.config(bg = 'green')
       root.after(175, lambda: b5g2.config(bg = '#d9a49a'))
       g25()
    root.bind('<KeyPress-d>', flashb5g2)
    def flashb7g2(event):
       b7g2.config(bg = 'green')
       root.after(175, lambda: b7g2.config(bg = '#d9a49a'))
       g27()
    root.bind('<KeyPress-f>', flashb7g2)
    def flashb9g2(event):
       b9g2.config(bg = 'green')
       root.after(175, lambda: b9g2.config(bg = '#d9a49a'))
       g29()
    root.bind('<KeyPress-g>', flashb9g2)
    def flashb10g2(event):
       b10g2.config(bg = 'green')
       root.after(175, lambda: b10g2.config(bg = '#d9a49a'))
       g210()
    root.bind('<KeyPress-h>', flashb10g2)
    def flashb12g2(event):
       b12g2.config(bg = 'green')
       root.after(175, lambda: b12g2.config(bg = '#d9a49a'))
       g212()
    root.bind('<KeyPress-j>', flashb12g2)
    def flashb14g2(event):
       b14g2.config(bg = 'green')
       root.after(175, lambda: b14g2.config(bg = '#d9a49a'))
       g214()
    root.bind('<KeyPress-k>', flashb14g2)
    def flashb16g2(event):
       b16g2.config(bg = 'green')
       root.after(175, lambda: b16g2.config(bg = '#d9a49a'))
       g216()
    root.bind('<KeyPress-l>', flashb16g2)
#########################STRING 3################################
    def flashb1g3(event):
       b1g3.config(bg = 'green')
       root.after(175, lambda: b1g3.config(bg = '#d9a49a'))
       g31()
    root.bind('<KeyPress-q>', flashb1g3)
    def flashb2g3(event):
       b2g3.config(bg = 'green')
       root.after(175, lambda: b2g3.config(bg = '#d9a49a'))
       g32()
    root.bind('<KeyPress-w>', flashb2g3)
    def flashb4g3(event):
       b4g3.config(bg = 'green')
       root.after(175, lambda: b4g3.config(bg = '#d9a49a'))
       g34()
    root.bind('<KeyPress-e>', flashb4g3)
    def flashb6g3(event):
       b6g3.config(bg = 'green')
       root.after(175, lambda: b6g3.config(bg = '#d9a49a'))
       g36()
    root.bind('<KeyPress-r>', flashb6g3)
    def flashb8g3(event):
       b8g3.config(bg = 'green')
       root.after(175, lambda: b8g3.config(bg = '#d9a49a'))
       g38()
    root.bind('<KeyPress-t>', flashb8g3)
    def flashb9g3(event):
       b9g3.config(bg = 'green')
       root.after(175, lambda: b9g3.config(bg = '#d9a49a'))
       g39()
    root.bind('<KeyPress-y>', flashb9g3)
    def flashb11g3(event):
       b11g3.config(bg = 'green')
       root.after(175, lambda: b11g3.config(bg = '#d9a49a'))
       g311()
    root.bind('<KeyPress-u>', flashb11g3)
    def flashb13g3(event):
       b13g3.config(bg = 'green')
       root.after(175, lambda: b13g3.config(bg = '#d9a49a'))
       g313()
    root.bind('<KeyPress-i>', flashb13g3)
    def flashb14g3(event):
       b14g3.config(bg = 'green')
       root.after(175, lambda: b14g3.config(bg = '#d9a49a'))
       g314()
    root.bind('<KeyPress-o>', flashb14g3)
    def flashb16g3(event):
       b16g3.config(bg = 'green')
       root.after(175, lambda: b16g3.config(bg = '#d9a49a'))
       g316()
    root.bind('<KeyPress-p>', flashb16g3)
#########################STRING 4################################
    def flashb1g4(event):
       b1g4.config(bg = 'green')
       root.after(175, lambda: b1g4.config(bg = '#d9a49a'))
       g41()
    root.bind('<KeyPress-1>', flashb1g4)
    def flashb2g4(event):
       b2g4.config(bg = 'green')
       root.after(175, lambda: b2g4.config(bg = '#d9a49a'))
       g42()
    root.bind('<KeyPress-2>', flashb2g4)
    def flashb4g4(event):
       b4g4.config(bg = 'green')
       root.after(175, lambda: b4g4.config(bg = '#d9a49a'))
       g44()
    root.bind('<KeyPress-3>', flashb4g4)
    def flashb6g4(event):
       b6g4.config(bg = 'green')
       root.after(175, lambda: b6g4.config(bg = '#d9a49a'))
       g46()
    root.bind('<KeyPress-4>', flashb6g4)
    def flashb7g4(event):
       b7g4.config(bg = 'green')
       root.after(175, lambda: b7g4.config(bg = '#d9a49a'))
       g47()
    root.bind('<KeyPress-5>', flashb7g4)
    def flashb9g4(event):
       b9g4.config(bg = 'green')
       root.after(175, lambda: b9g4.config(bg = '#d9a49a'))
       g49()
    root.bind('<KeyPress-6>', flashb9g4)
    def flashb11g4(event):
       b11g4.config(bg = 'green')
       root.after(175, lambda: b11g4.config(bg = '#d9a49a'))
       g411()
    root.bind('<KeyPress-7>', flashb11g4)
    def flashb13g4(event):
       b13g4.config(bg = 'green')
       root.after(175, lambda: b13g4.config(bg = '#d9a49a'))
       g413()
    root.bind('<KeyPress-8>', flashb13g4)
    def flashb14g4(event):
       b14g4.config(bg = 'green')
       root.after(175, lambda: b14g4.config(bg = '#d9a49a'))
       g414()
    root.bind('<KeyPress-9>', flashb14g4)
    def flashb16g4(event):
       b16g4.config(bg = 'green')
       root.after(175, lambda: b16g4.config(bg = '#d9a49a'))
       g416()
    root.bind('<KeyPress-0>', flashb16g4)
    b2g1.configure(background='#d9a49a')
    b4g1.configure(background='#d9a49a')
    b5g1.configure(background='#d9a49a')
    b7g1.configure(background='#d9a49a')
    b9g1.configure(background='#d9a49a')
    b11g1.configure(background='#d9a49a')
    b12g1.configure(background='#d9a49a')
    b14g1.configure(background='#d9a49a')
    b16g1.configure(background='#d9a49a')
############################STRING 2 ################################
    b2g2.configure(background='#d9a49a')
    b4g2.configure(background='#d9a49a')
    b5g2.configure(background='#d9a49a')
    b7g2.configure(background='#d9a49a')
    b9g2.configure(background='#d9a49a')
    b10g2.configure(background='#d9a49a')
    b12g2.configure(background='#d9a49a')
    b14g2.configure(background='#d9a49a')
    b16g2.configure(background='#d9a49a')
#########################STRING 3################################
    b1g3.configure(background='#d9a49a')
    b2g3.configure(background='#d9a49a')
    b4g3.configure(background='#d9a49a')
    b6g3.configure(background='#d9a49a')
    b8g3.configure(background='#d9a49a')
    b9g3.configure(background='#d9a49a')
    b11g3.configure(background='#d9a49a')
    b13g3.configure(background='#d9a49a')
    b14g3.configure(background='#d9a49a')
    b16g3.configure(background='#d9a49a')
#########################STRING 4################################
    b1g4.configure(background='#d9a49a')
    b2g4.configure(background='#d9a49a')
    b4g4.configure(background='#d9a49a')
    b6g4.configure(background='#d9a49a')
    b7g4.configure(background='#d9a49a')
    b9g4.configure(background='#d9a49a')
    b11g4.configure(background='#d9a49a')
    b13g4.configure(background='#d9a49a')
    b14g4.configure(background='#d9a49a')
    b16g4.configure(background='#d9a49a')    
def g_sharp_major_d9a49a():
    b_g_sharp_h.place_forget()
    b_g_sharp.place(x=800,y=50,width=80)
    resetflash()    
    b2g1.configure(background=orig_color)
    b4g1.configure(background=orig_color)
    b5g1.configure(background=orig_color)
    b7g1.configure(background=orig_color)
    b9g1.configure(background=orig_color)
    b11g1.configure(background=orig_color)
    b12g1.configure(background=orig_color)
    b14g1.configure(background=orig_color)
    b16g1.configure(background=orig_color)
############################STRING 2 ################################
    b2g2.configure(background=orig_color)
    b4g2.configure(background=orig_color)
    b5g2.configure(background=orig_color)
    b7g2.configure(background=orig_color)
    b9g2.configure(background=orig_color)
    b10g2.configure(background=orig_color)
    b12g2.configure(background=orig_color)
    b14g2.configure(background=orig_color)
    b16g2.configure(background=orig_color)
#########################STRING 3################################
    b1g3.configure(background=orig_color)
    b2g3.configure(background=orig_color)
    b4g3.configure(background=orig_color)
    b6g3.configure(background=orig_color)
    b8g3.configure(background=orig_color)
    b9g3.configure(background=orig_color)
    b11g3.configure(background=orig_color)
    b13g3.configure(background=orig_color)
    b14g3.configure(background=orig_color)
    b16g3.configure(background=orig_color)
#########################STRING 4################################
    b1g4.configure(background=orig_color)
    b2g4.configure(background=orig_color)
    b4g4.configure(background=orig_color)
    b6g4.configure(background=orig_color)
    b7g4.configure(background=orig_color)
    b9g4.configure(background=orig_color)
    b11g4.configure(background=orig_color)
    b13g4.configure(background=orig_color)
    b14g4.configure(background=orig_color)
    b16g4.configure(background=orig_color)    

def a_major_show():
    b_a.place_forget()
    b_a_h.place(x=900,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)
    
    def flashb1g1(event):
       b1g1.config(bg = 'green')
       root.after(175, lambda: b1g1.config(bg = '#e6d375'))
       g11()
    root.bind('<KeyPress-z>', flashb1g1)
    def flashb3g1(event):
       b3g1.config(bg = 'green')
       root.after(175, lambda: b3g1.config(bg = '#e6d375'))
       g13()
    root.bind('<KeyPress-x>', flashb3g1)
    def flashb5g1(event):
       b5g1.config(bg = 'green')
       root.after(175, lambda: b5g1.config(bg = '#e6d375'))
       g15()
    root.bind('<KeyPress-c>', flashb5g1)
    def flashb6g1(event):
       b6g1.config(bg = 'green')
       root.after(175, lambda: b6g1.config(bg = '#e6d375'))
       g16()
    root.bind('<KeyPress-v>', flashb6g1)
    def flashb8g1(event):
       b8g1.config(bg = 'green')
       root.after(175, lambda: b8g1.config(bg = '#e6d375'))
       g18()
    root.bind('<KeyPress-b>', flashb8g1)
    def flashb10g1(event):
       b10g1.config(bg = 'green')
       root.after(175, lambda: b10g1.config(bg = '#e6d375'))
       g110()
    root.bind('<KeyPress-n>', flashb10g1)
    def flashb12g1(event):
       b12g1.config(bg = 'green')
       root.after(175, lambda: b12g1.config(bg = '#e6d375'))
       g112()
    root.bind('<KeyPress-m>', flashb12g1)
    def flashb13g1(event):
       b13g1.config(bg = 'green')
       root.after(175, lambda: b13g1.config(bg = '#e6d375'))
       g113()
    root.bind('<KeyPress-,>', flashb13g1)
    def flashb15g1(event):
       b15g1.config(bg = 'green')
       root.after(175, lambda: b15g1.config(bg = '#e6d375'))
       g115()
    root.bind('<KeyPress-.>', flashb15g1)
############################STRING 2 ################################
    def flashb1g2(event):
       b1g2.config(bg = 'green')
       root.after(175, lambda: b1g2.config(bg = '#e6d375'))
       g21()
    root.bind('<KeyPress-a>', flashb1g2)
    def flashb3g2(event):
       b3g2.config(bg = 'green')
       root.after(175, lambda: b3g2.config(bg = '#e6d375'))
       g23()
    root.bind('<KeyPress-s>', flashb3g2)
    def flashb5g2(event):
       b5g2.config(bg = 'green')
       root.after(175, lambda: b5g2.config(bg = '#e6d375'))
       g25()
    root.bind('<KeyPress-d>', flashb5g2)
    def flashb6g2(event):
       b6g2.config(bg = 'green')
       root.after(175, lambda: b6g2.config(bg = '#e6d375'))
       g26()
    root.bind('<KeyPress-f>', flashb6g2)
    def flashb8g2(event):
       b8g2.config(bg = 'green')
       root.after(175, lambda: b8g2.config(bg = '#e6d375'))
       g28()
    root.bind('<KeyPress-g>', flashb8g2)
    def flashb10g2(event):
       b10g2.config(bg = 'green')
       root.after(175, lambda: b10g2.config(bg = '#e6d375'))
       g210()
    root.bind('<KeyPress-h>', flashb10g2)
    def flashb11g2(event):
       b11g2.config(bg = 'green')
       root.after(175, lambda: b11g2.config(bg = '#e6d375'))
       g211()
    root.bind('<KeyPress-j>', flashb11g2)
    def flashb13g2(event):
       b13g2.config(bg = 'green')
       root.after(175, lambda: b13g2.config(bg = '#e6d375'))
       g213()
    root.bind('<KeyPress-k>', flashb13g2)
    def flashb15g2(event):
       b15g2.config(bg = 'green')
       root.after(175, lambda: b15g2.config(bg = '#e6d375'))
       g215()
    root.bind('<KeyPress-l>', flashb15g2)
#########################STRING 3################################
    def flashb2g3(event):
       b2g3.config(bg = 'green')
       root.after(175, lambda: b2g3.config(bg = '#e6d375'))
       g32()
    root.bind('<KeyPress-q>', flashb2g3)
    def flashb3g3(event):
       b3g3.config(bg = 'green')
       root.after(175, lambda: b3g3.config(bg = '#e6d375'))
       g33()
    root.bind('<KeyPress-w>', flashb3g3)
    def flashb5g3(event):
       b5g3.config(bg = 'green')
       root.after(175, lambda: b5g3.config(bg = '#e6d375'))
       g35()
    root.bind('<KeyPress-e>', flashb5g3)
    def flashb7g3(event):
       b7g3.config(bg = 'green')
       root.after(175, lambda: b7g3.config(bg = '#e6d375'))
       g37()
    root.bind('<KeyPress-r>', flashb7g3)
    def flashb9g3(event):
       b9g3.config(bg = 'green')
       root.after(175, lambda: b9g3.config(bg = '#e6d375'))
       g39()
    root.bind('<KeyPress-t>', flashb9g3)
    def flashb10g3(event):
       b10g3.config(bg = 'green')
       root.after(175, lambda: b10g3.config(bg = '#e6d375'))
       g310()
    root.bind('<KeyPress-y>', flashb10g3)
    def flashb12g3(event):
       b12g3.config(bg = 'green')
       root.after(175, lambda: b12g3.config(bg = '#e6d375'))
       g312()
    root.bind('<KeyPress-u>', flashb12g3)
    def flashb14g3(event):
       b14g3.config(bg = 'green')
       root.after(175, lambda: b14g3.config(bg = '#e6d375'))
       g314()
    root.bind('<KeyPress-i>', flashb14g3)
    def flashb15g3(event):
       b15g3.config(bg = 'green')
       root.after(175, lambda: b15g3.config(bg = '#e6d375'))
       g315()
    root.bind('<KeyPress-o>', flashb15g3)
#########################STRING 4################################
    def flashb2g4(event):
       b2g4.config(bg = 'green')
       root.after(175, lambda: b2g4.config(bg = '#e6d375'))
       g42()
    root.bind('<KeyPress-1>', flashb2g4)
    def flashb3g4(event):
       b3g4.config(bg = 'green')
       root.after(175, lambda: b3g4.config(bg = '#e6d375'))
       g43()
    root.bind('<KeyPress-2>', flashb3g4)
    def flashb5g4(event):
       b5g4.config(bg = 'green')
       root.after(175, lambda: b5g4.config(bg = '#e6d375'))
       g45()
    root.bind('<KeyPress-3>', flashb5g4)
    def flashb7g4(event):
       b7g4.config(bg = 'green')
       root.after(175, lambda: b7g4.config(bg = '#e6d375'))
       g47()
    root.bind('<KeyPress-4>', flashb7g4)
    def flashb8g4(event):
       b8g4.config(bg = 'green')
       root.after(175, lambda: b8g4.config(bg = '#e6d375'))
       g48()
    root.bind('<KeyPress-5>', flashb8g4)
    def flashb10g4(event):
       b10g4.config(bg = 'green')
       root.after(175, lambda: b10g4.config(bg = '#e6d375'))
       g410()
    root.bind('<KeyPress-6>', flashb10g4)
    def flashb12g4(event):
       b12g4.config(bg = 'green')
       root.after(175, lambda: b12g4.config(bg = '#e6d375'))
       g412()
    root.bind('<KeyPress-7>', flashb12g4)
    def flashb14g4(event):
       b14g4.config(bg = 'green')
       root.after(175, lambda: b14g4.config(bg = '#e6d375'))
       g414()
    root.bind('<KeyPress-8>', flashb14g4)
    def flashb15g4(event):
       b15g4.config(bg = 'green')
       root.after(175, lambda: b15g4.config(bg = '#e6d375'))
       g415()
    root.bind('<KeyPress-9>', flashb15g4)
    b1g1.configure(background='#e6d375')
    b3g1.configure(background='#e6d375')
    b5g1.configure(background='#e6d375')
    b6g1.configure(background='#e6d375')
    b8g1.configure(background='#e6d375')
    b10g1.configure(background='#e6d375')
    b12g1.configure(background='#e6d375')
    b13g1.configure(background='#e6d375')
    b15g1.configure(background='#e6d375')
############################STRING 2 ################################
    b1g2.configure(background='#e6d375')
    b3g2.configure(background='#e6d375')
    b5g2.configure(background='#e6d375')
    b6g2.configure(background='#e6d375')
    b8g2.configure(background='#e6d375')
    b10g2.configure(background='#e6d375')
    b11g2.configure(background='#e6d375')
    b13g2.configure(background='#e6d375')
    b15g2.configure(background='#e6d375')
#########################STRING 3################################
    b2g3.configure(background='#e6d375')
    b3g3.configure(background='#e6d375')
    b5g3.configure(background='#e6d375')
    b7g3.configure(background='#e6d375')
    b9g3.configure(background='#e6d375')
    b10g3.configure(background='#e6d375')
    b12g3.configure(background='#e6d375')
    b14g3.configure(background='#e6d375')
    b15g3.configure(background='#e6d375')
#########################STRING 4################################
    b2g4.configure(background='#e6d375')
    b3g4.configure(background='#e6d375')
    b5g4.configure(background='#e6d375')
    b7g4.configure(background='#e6d375')
    b8g4.configure(background='#e6d375')
    b10g4.configure(background='#e6d375')
    b12g4.configure(background='#e6d375')
    b14g4.configure(background='#e6d375')
    b15g4.configure(background='#e6d375')
def a_major_e6d375():
    b_a_h.place_forget()
    b_a.place(x=900,y=50,width=80)
    resetflash()
    b1g1.configure(background=orig_color)
    b3g1.configure(background=orig_color)
    b5g1.configure(background=orig_color)
    b6g1.configure(background=orig_color)
    b8g1.configure(background=orig_color)
    b10g1.configure(background=orig_color)
    b12g1.configure(background=orig_color)
    b13g1.configure(background=orig_color)
    b15g1.configure(background=orig_color)
############################STRING 2 ################################
    b1g2.configure(background=orig_color)
    b3g2.configure(background=orig_color)
    b5g2.configure(background=orig_color)
    b6g2.configure(background=orig_color)
    b8g2.configure(background=orig_color)
    b10g2.configure(background=orig_color)
    b11g2.configure(background=orig_color)
    b13g2.configure(background=orig_color)
    b15g2.configure(background=orig_color)
#########################STRING 3################################
    b2g3.configure(background=orig_color)
    b3g3.configure(background=orig_color)
    b5g3.configure(background=orig_color)
    b7g3.configure(background=orig_color)
    b9g3.configure(background=orig_color)
    b10g3.configure(background=orig_color)
    b12g3.configure(background=orig_color)
    b14g3.configure(background=orig_color)
    b15g3.configure(background=orig_color)
#########################STRING 4################################
    b2g4.configure(background=orig_color)
    b3g4.configure(background=orig_color)
    b5g4.configure(background=orig_color)
    b7g4.configure(background=orig_color)
    b8g4.configure(background=orig_color)
    b10g4.configure(background=orig_color)
    b12g4.configure(background=orig_color)
    b14g4.configure(background=orig_color)
    b15g4.configure(background=orig_color)

def a_sharp_major_show():
    b_a_sharp.place_forget()
    b_a_sharp_h.place(x=1000,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)
    
    def flashb1g1(event):
       b1g1.config(bg = 'green')
       root.after(175, lambda: b1g1.config(bg = '#a0eb38'))
       g11()
    root.bind('<KeyPress-z>', flashb1g1)
    def flashb2g1(event):
       b2g1.config(bg = 'green')
       root.after(175, lambda: b2g1.config(bg = '#a0eb38'))
       g12()
    root.bind('<KeyPress-x>', flashb2g1)
    def flashb4g1(event):
       b4g1.config(bg = 'green')
       root.after(175, lambda: b4g1.config(bg = '#a0eb38'))
       g14()
    root.bind('<KeyPress-c>', flashb4g1)
    def flashb6g1(event):
       b6g1.config(bg = 'green')
       root.after(175, lambda: b6g1.config(bg = '#a0eb38'))
       g16()
    root.bind('<KeyPress-v>', flashb6g1)
    def flashb7g1(event):
       b7g1.config(bg = 'green')
       root.after(175, lambda: b7g1.config(bg = '#a0eb38'))
       g17()
    root.bind('<KeyPress-b>', flashb7g1)
    def flashb9g1(event):
       b9g1.config(bg = 'green')
       root.after(175, lambda: b9g1.config(bg = '#a0eb38'))
       g19()
    root.bind('<KeyPress-n>', flashb9g1)
    def flashb11g1(event):
       b11g1.config(bg = 'green')
       root.after(175, lambda: b11g1.config(bg = '#a0eb38'))
       g111()
    root.bind('<KeyPress-m>', flashb11g1)
    def flashb13g1(event):
       b13g1.config(bg = 'green')
       root.after(175, lambda: b13g1.config(bg = '#a0eb38'))
       g113()
    root.bind('<KeyPress-,>', flashb13g1)
    def flashb14g1(event):
       b14g1.config(bg = 'green')
       root.after(175, lambda: b14g1.config(bg = '#a0eb38'))
       g114()
    root.bind('<KeyPress-.>', flashb14g1)
    def flashb16g1(event):
       b16g1.config(bg = 'green')
       root.after(175, lambda: b16g1.config(bg = '#a0eb38'))
       g116()
    root.bind('<KeyPress-/>', flashb16g1)
############################STRING 2 ################################
    def flashb2g2(event):
       b2g2.config(bg = 'green')
       root.after(175, lambda: b2g2.config(bg = '#a0eb38'))
       g22()
    root.bind('<KeyPress-a>', flashb2g2)
    def flashb4g2(event):
       b4g2.config(bg = 'green')
       root.after(175, lambda: b4g2.config(bg = '#a0eb38'))
       g24()
    root.bind('<KeyPress-s>', flashb4g2)
    def flashb6g2(event):
       b6g2.config(bg = 'green')
       root.after(175, lambda: b6g2.config(bg = '#a0eb38'))
       g26()
    root.bind('<KeyPress-d>', flashb6g2)
    def flashb7g2(event):
       b7g2.config(bg = 'green')
       root.after(175, lambda: b7g2.config(bg = '#a0eb38'))
       g27()
    root.bind('<KeyPress-f>', flashb7g2)
    def flashb9g2(event):
       b9g2.config(bg = 'green')
       root.after(175, lambda: b9g2.config(bg = '#a0eb38'))
       g29()
    root.bind('<KeyPress-g>', flashb9g2)
    def flashb11g2(event):
       b11g2.config(bg = 'green')
       root.after(175, lambda: b11g2.config(bg = '#a0eb38'))
       g211()
    root.bind('<KeyPress-h>', flashb11g2)
    def flashb12g2(event):
       b12g2.config(bg = 'green')
       root.after(175, lambda: b12g2.config(bg = '#a0eb38'))
       g212()
    root.bind('<KeyPress-j>', flashb12g2)
    def flashb14g2(event):
       b14g2.config(bg = 'green')
       root.after(175, lambda: b14g2.config(bg = '#a0eb38'))
       g214()
    root.bind('<KeyPress-k>', flashb14g2)
    def flashb16g2(event):
       b16g2.config(bg = 'green')
       root.after(175, lambda: b16g2.config(bg = '#a0eb38'))
       g216()
    root.bind('<KeyPress-l>', flashb16g2)
#########################STRING 3################################
    def flashb1g3(event):
       b1g3.config(bg = 'green')
       root.after(175, lambda: b1g3.config(bg = '#a0eb38'))
       g31()
    root.bind('<KeyPress-q>', flashb1g3)
    def flashb3g3(event):
       b3g3.config(bg = 'green')
       root.after(175, lambda: b3g3.config(bg = '#a0eb38'))
       g33()
    root.bind('<KeyPress-w>', flashb3g3)
    def flashb4g3(event):
       b4g3.config(bg = 'green')
       root.after(175, lambda: b4g3.config(bg = '#a0eb38'))
       g34()
    root.bind('<KeyPress-e>', flashb4g3)
    def flashb6g3(event):
       b6g3.config(bg = 'green')
       root.after(175, lambda: b6g3.config(bg = '#a0eb38'))
       g36()
    root.bind('<KeyPress-r>', flashb6g3)
    def flashb8g3(event):
       b8g3.config(bg = 'green')
       root.after(175, lambda: b8g3.config(bg = '#a0eb38'))
       g38()
    root.bind('<KeyPress-t>', flashb8g3)
    def flashb10g3(event):
       b10g3.config(bg = 'green')
       root.after(175, lambda: b10g3.config(bg = '#a0eb38'))
       g310()
    root.bind('<KeyPress-y>', flashb10g3)
    def flashb11g3(event):
       b11g3.config(bg = 'green')
       root.after(175, lambda: b11g3.config(bg = '#a0eb38'))
       g311()
    root.bind('<KeyPress-u>', flashb11g3)
    def flashb13g3(event):
       b13g3.config(bg = 'green')
       root.after(175, lambda: b13g3.config(bg = '#a0eb38'))
       g313()
    root.bind('<KeyPress-i>', flashb13g3)
    def flashb15g3(event):
       b15g3.config(bg = 'green')
       root.after(175, lambda: b15g3.config(bg = '#a0eb38'))
       g315()
    root.bind('<KeyPress-o>', flashb15g3)
    def flashb16g3(event):
       b16g3.config(bg = 'green')
       root.after(175, lambda: b16g3.config(bg = '#a0eb38'))
       g316()
    root.bind('<KeyPress-p>', flashb16g3)
#########################STRING 4################################
    def flashb1g4(event):
       b1g4.config(bg = 'green')
       root.after(175, lambda: b1g4.config(bg = '#a0eb38'))
       g41()
    root.bind('<KeyPress-1>', flashb1g4)
    def flashb3g4(event):
       b3g4.config(bg = 'green')
       root.after(175, lambda: b3g4.config(bg = '#a0eb38'))
       g43()
    root.bind('<KeyPress-2>', flashb3g4)
    def flashb4g4(event):
       b4g4.config(bg = 'green')
       root.after(175, lambda: b4g4.config(bg = '#a0eb38'))
       g44()
    root.bind('<KeyPress-3>', flashb4g4)
    def flashb6g4(event):
       b6g4.config(bg = 'green')
       root.after(175, lambda: b6g4.config(bg = '#a0eb38'))
       g46()
    root.bind('<KeyPress-4>', flashb6g4)
    def flashb8g4(event):
       b8g4.config(bg = 'green')
       root.after(175, lambda: b8g4.config(bg = '#a0eb38'))
       g48()
    root.bind('<KeyPress-5>', flashb8g4)
    def flashb9g4(event):
       b9g4.config(bg = 'green')
       root.after(175, lambda: b9g4.config(bg = '#a0eb38'))
       g49()
    root.bind('<KeyPress-6>', flashb9g4)
    def flashb11g4(event):
       b11g4.config(bg = 'green')
       root.after(175, lambda: b11g4.config(bg = '#a0eb38'))
       g411()
    root.bind('<KeyPress-7>', flashb11g4)
    def flashb13g4(event):
       b13g4.config(bg = 'green')
       root.after(175, lambda: b13g4.config(bg = '#a0eb38'))
       g413()
    root.bind('<KeyPress-8>', flashb13g4)
    def flashb15g4(event):
       b15g4.config(bg = 'green')
       root.after(175, lambda: b15g4.config(bg = '#a0eb38'))
       g415()
    root.bind('<KeyPress-9>', flashb15g4)
    def flashb16g4(event):
       b16g4.config(bg = 'green')
       root.after(175, lambda: b16g4.config(bg = '#a0eb38'))
       g416()
    root.bind('<KeyPress-0>', flashb16g4)
    b1g1.configure(background='#a0eb38')
    b2g1.configure(background='#a0eb38')
    b4g1.configure(background='#a0eb38')
    b6g1.configure(background='#a0eb38')
    b7g1.configure(background='#a0eb38')
    b9g1.configure(background='#a0eb38')
    b11g1.configure(background='#a0eb38')
    b13g1.configure(background='#a0eb38')
    b14g1.configure(background='#a0eb38')
    b16g1.configure(background='#a0eb38')
############################STRING 2 ################################
    b2g2.configure(background='#a0eb38')
    b4g2.configure(background='#a0eb38')
    b6g2.configure(background='#a0eb38')
    b7g2.configure(background='#a0eb38')
    b9g2.configure(background='#a0eb38')
    b11g2.configure(background='#a0eb38')
    b12g2.configure(background='#a0eb38')
    b14g2.configure(background='#a0eb38')
    b16g2.configure(background='#a0eb38')
#########################STRING 3################################
    b1g3.configure(background='#a0eb38')
    b3g3.configure(background='#a0eb38')
    b4g3.configure(background='#a0eb38')
    b6g3.configure(background='#a0eb38')
    b8g3.configure(background='#a0eb38')
    b10g3.configure(background='#a0eb38')
    b11g3.configure(background='#a0eb38')
    b13g3.configure(background='#a0eb38')
    b15g3.configure(background='#a0eb38')
    b16g3.configure(background='#a0eb38')
#########################STRING 4################################
    b1g4.configure(background='#a0eb38')
    b3g4.configure(background='#a0eb38')
    b4g4.configure(background='#a0eb38')
    b6g4.configure(background='#a0eb38')
    b8g4.configure(background='#a0eb38')
    b9g4.configure(background='#a0eb38')
    b11g4.configure(background='#a0eb38')
    b13g4.configure(background='#a0eb38')
    b15g4.configure(background='#a0eb38')
    b16g4.configure(background='#a0eb38')
def a_sharp_major_a0eb38():
    b_a_sharp_h.place_forget()
    b_a_sharp.place(x=1000,y=50,width=80)
    resetflash()

    b1g1.configure(background=orig_color)
    b2g1.configure(background=orig_color)
    b4g1.configure(background=orig_color)
    b6g1.configure(background=orig_color)
    b7g1.configure(background=orig_color)
    b9g1.configure(background=orig_color)
    b11g1.configure(background=orig_color)
    b13g1.configure(background=orig_color)
    b14g1.configure(background=orig_color)
    b16g1.configure(background=orig_color)
############################STRING 2 ################################
    b2g2.configure(background=orig_color)
    b4g2.configure(background=orig_color)
    b6g2.configure(background=orig_color)
    b7g2.configure(background=orig_color)
    b9g2.configure(background=orig_color)
    b11g2.configure(background=orig_color)
    b12g2.configure(background=orig_color)
    b14g2.configure(background=orig_color)
    b16g2.configure(background=orig_color)
#########################STRING 3################################
    b1g3.configure(background=orig_color)
    b3g3.configure(background=orig_color)
    b4g3.configure(background=orig_color)
    b6g3.configure(background=orig_color)
    b8g3.configure(background=orig_color)
    b10g3.configure(background=orig_color)
    b11g3.configure(background=orig_color)
    b13g3.configure(background=orig_color)
    b15g3.configure(background=orig_color)
    b16g3.configure(background=orig_color)
#########################STRING 4################################
    b1g4.configure(background=orig_color)
    b3g4.configure(background=orig_color)
    b4g4.configure(background=orig_color)
    b6g4.configure(background=orig_color)
    b8g4.configure(background=orig_color)
    b9g4.configure(background=orig_color)
    b11g4.configure(background=orig_color)
    b13g4.configure(background=orig_color)
    b15g4.configure(background=orig_color)
    b16g4.configure(background=orig_color)

def b_major_show():
    b_b.place_forget()
    b_b_h.place(x=1100,y=50,width=80)
    def flashb0g0(event):
       stopchannels()
       chordmute()
    root.bind('<KeyPress-space>', flashb0g0)
    
    def flashb2g1(event):
       b2g1.config(bg = 'green')
       root.after(175, lambda: b2g1.config(bg = '#e3bcbd'))
       g12()
    root.bind('<KeyPress-z>', flashb2g1)
    def flashb3g1(event):
       b3g1.config(bg = 'green')
       root.after(175, lambda: b3g1.config(bg = '#e3bcbd'))
       g13()
    root.bind('<KeyPress-x>', flashb3g1)
    def flashb5g1(event):
       b5g1.config(bg = 'green')
       root.after(175, lambda: b5g1.config(bg = '#e3bcbd'))
       g15()
    root.bind('<KeyPress-c>', flashb5g1)
    def flashb7g1(event):
       b7g1.config(bg = 'green')
       root.after(175, lambda: b7g1.config(bg = '#e3bcbd'))
       g17()
    root.bind('<KeyPress-v>', flashb7g1)
    def flashb8g1(event):
       b8g1.config(bg = 'green')
       root.after(175, lambda: b8g1.config(bg = '#e3bcbd'))
       g18()
    root.bind('<KeyPress-b>', flashb8g1)
    def flashb10g1(event):
       b10g1.config(bg = 'green')
       root.after(175, lambda: b10g1.config(bg = '#e3bcbd'))
       g110()
    root.bind('<KeyPress-n>', flashb10g1)
    def flashb12g1(event):
       b12g1.config(bg = 'green')
       root.after(175, lambda: b12g1.config(bg = '#e3bcbd'))
       g112()
    root.bind('<KeyPress-m>', flashb12g1)
    def flashb14g1(event):
       b14g1.config(bg = 'green')
       root.after(175, lambda: b14g1.config(bg = '#e3bcbd'))
       g114()
    root.bind('<KeyPress-,>', flashb14g1)
    def flashb15g1(event):
       b15g1.config(bg = 'green')
       root.after(175, lambda: b15g1.config(bg = '#e3bcbd'))
       g115()
    root.bind('<KeyPress-.>', flashb15g1)
############################STRING 2 ################################
    def flashb1g2(event):
       b1g2.config(bg = 'green')
       root.after(175, lambda: b1g2.config(bg = '#e3bcbd'))
       g21()
    root.bind('<KeyPress-a>', flashb1g2)
    def flashb3g2(event):
       b3g2.config(bg = 'green')
       root.after(175, lambda: b3g2.config(bg = '#e3bcbd'))
       g23()
    root.bind('<KeyPress-s>', flashb3g2)
    def flashb5g2(event):
       b5g2.config(bg = 'green')
       root.after(175, lambda: b5g2.config(bg = '#e3bcbd'))
       g25()
    root.bind('<KeyPress-d>', flashb5g2)
    def flashb7g2(event):
       b7g2.config(bg = 'green')
       root.after(175, lambda: b7g2.config(bg = '#e3bcbd'))
       g27()
    root.bind('<KeyPress-f>', flashb7g2)
    def flashb8g2(event):
       b8g2.config(bg = 'green')
       root.after(175, lambda: b8g2.config(bg = '#e3bcbd'))
       g28()
    root.bind('<KeyPress-g>', flashb8g2)
    def flashb10g2(event):
       b10g2.config(bg = 'green')
       root.after(175, lambda: b10g2.config(bg = '#e3bcbd'))
       g210()
    root.bind('<KeyPress-h>', flashb10g2)
    def flashb12g2(event):
       b12g2.config(bg = 'green')
       root.after(175, lambda: b12g2.config(bg = '#e3bcbd'))
       g212()
    root.bind('<KeyPress-j>', flashb12g2)
    def flashb13g2(event):
       b13g2.config(bg = 'green')
       root.after(175, lambda: b13g2.config(bg = '#e3bcbd'))
       g213()
    root.bind('<KeyPress-k>', flashb13g2)
    def flashb15g2(event):
       b15g2.config(bg = 'green')
       root.after(175, lambda: b15g2.config(bg = '#e3bcbd'))
       g215()
    root.bind('<KeyPress-l>', flashb15g2)
#########################STRING 3################################
    def flashb2g3(event):
       b2g3.config(bg = 'green')
       root.after(175, lambda: b2g3.config(bg = '#e3bcbd'))
       g32()
    root.bind('<KeyPress-q>', flashb2g3)
    def flashb4g3(event):
       b4g3.config(bg = 'green')
       root.after(175, lambda: b4g3.config(bg = '#e3bcbd'))
       g34()
    root.bind('<KeyPress-w>', flashb4g3)
    def flashb5g3(event):
       b5g3.config(bg = 'green')
       root.after(175, lambda: b5g3.config(bg = '#e3bcbd'))
       g35()
    root.bind('<KeyPress-e>', flashb5g3)
    def flashb7g3(event):
       b7g3.config(bg = 'green')
       root.after(175, lambda: b7g3.config(bg = '#e3bcbd'))
       g37()
    root.bind('<KeyPress-r>', flashb7g3)
    def flashb9g3(event):
       b9g3.config(bg = 'green')
       root.after(175, lambda: b9g3.config(bg = '#e3bcbd'))
       g39()
    root.bind('<KeyPress-t>', flashb9g3)
    def flashb11g3(event):
       b11g3.config(bg = 'green')
       root.after(175, lambda: b11g3.config(bg = '#e3bcbd'))
       g311()
    root.bind('<KeyPress-y>', flashb11g3)
    def flashb12g3(event):
       b12g3.config(bg = 'green')
       root.after(175, lambda: b12g3.config(bg = '#e3bcbd'))
       g312()
    root.bind('<KeyPress-u>', flashb12g3)
    def flashb14g3(event):
       b14g3.config(bg = 'green')
       root.after(175, lambda: b14g3.config(bg = '#e3bcbd'))
       g314()
    root.bind('<KeyPress-i>', flashb14g3)
    def flashb16g3(event):
       b16g3.config(bg = 'green')
       root.after(175, lambda: b16g3.config(bg = '#e3bcbd'))
       g316()
    root.bind('<KeyPress-o>', flashb16g3)
#########################STRING 4################################
    def flashb2g4(event):
       b2g4.config(bg = 'green')
       root.after(175, lambda: b2g4.config(bg = '#e3bcbd'))
       g42()
    root.bind('<KeyPress-1>', flashb2g4)
    def flashb4g4(event):
       b4g4.config(bg = 'green')
       root.after(175, lambda: b4g4.config(bg = '#e3bcbd'))
       g44()
    root.bind('<KeyPress-2>', flashb4g4)
    def flashb5g4(event):
       b5g4.config(bg = 'green')
       root.after(175, lambda: b5g4.config(bg = '#e3bcbd'))
       g45()
    root.bind('<KeyPress-3>', flashb5g4)
    def flashb7g4(event):
       b7g4.config(bg = 'green')
       root.after(175, lambda: b7g4.config(bg = '#e3bcbd'))
       g47()
    root.bind('<KeyPress-4>', flashb7g4)
    def flashb9g4(event):
       b9g4.config(bg = 'green')
       root.after(175, lambda: b9g4.config(bg = '#e3bcbd'))
       g49()
    root.bind('<KeyPress-5>', flashb9g4)
    def flashb10g4(event):
       b10g4.config(bg = 'green')
       root.after(175, lambda: b10g4.config(bg = '#e3bcbd'))
       g410()
    root.bind('<KeyPress-6>', flashb10g4)
    def flashb12g4(event):
       b12g4.config(bg = 'green')
       root.after(175, lambda: b12g4.config(bg = '#e3bcbd'))
       g412()
    root.bind('<KeyPress-7>', flashb12g4)
    def flashb14g4(event):
       b14g4.config(bg = 'green')
       root.after(175, lambda: b14g4.config(bg = '#e3bcbd'))
       g414()
    root.bind('<KeyPress-8>', flashb14g4)
    def flashb16g4(event):
       b16g4.config(bg = 'green')
       root.after(175, lambda: b16g4.config(bg = '#e3bcbd'))
       g416()
    root.bind('<KeyPress-9>', flashb16g4)
    b2g1.configure(background='#e3bcbd')
    b3g1.configure(background='#e3bcbd')
    b5g1.configure(background='#e3bcbd')
    b7g1.configure(background='#e3bcbd')
    b8g1.configure(background='#e3bcbd')
    b10g1.configure(background='#e3bcbd')
    b12g1.configure(background='#e3bcbd')
    b14g1.configure(background='#e3bcbd')
    b15g1.configure(background='#e3bcbd')
############################STRING 2 ################################
    b1g2.configure(background='#e3bcbd')
    b3g2.configure(background='#e3bcbd')
    b5g2.configure(background='#e3bcbd')
    b7g2.configure(background='#e3bcbd')
    b8g2.configure(background='#e3bcbd')
    b10g2.configure(background='#e3bcbd')
    b12g2.configure(background='#e3bcbd')
    b13g2.configure(background='#e3bcbd')
    b15g2.configure(background='#e3bcbd')
#########################STRING 3################################
    b2g3.configure(background='#e3bcbd')
    b4g3.configure(background='#e3bcbd')
    b5g3.configure(background='#e3bcbd')
    b7g3.configure(background='#e3bcbd')
    b9g3.configure(background='#e3bcbd')
    b11g3.configure(background='#e3bcbd')
    b12g3.configure(background='#e3bcbd')
    b14g3.configure(background='#e3bcbd')
    b16g3.configure(background='#e3bcbd')
#########################STRING 4################################
    b2g4.configure(background='#e3bcbd')
    b4g4.configure(background='#e3bcbd')
    b5g4.configure(background='#e3bcbd')
    b7g4.configure(background='#e3bcbd')
    b9g4.configure(background='#e3bcbd')
    b10g4.configure(background='#e3bcbd')
    b12g4.configure(background='#e3bcbd')
    b14g4.configure(background='#e3bcbd')
    b16g4.configure(background='#e3bcbd')
def b_major_e3bcbd():
    b_b_h.place_forget()
    b_b.place(x=1100,y=50,width=80)
    resetflash()
    b2g1.configure(background=orig_color)
    b3g1.configure(background=orig_color)
    b5g1.configure(background=orig_color)
    b7g1.configure(background=orig_color)
    b8g1.configure(background=orig_color)
    b10g1.configure(background=orig_color)
    b12g1.configure(background=orig_color)
    b14g1.configure(background=orig_color)
    b15g1.configure(background=orig_color)
############################STRING 2 ################################
    b1g2.configure(background=orig_color)
    b3g2.configure(background=orig_color)
    b5g2.configure(background=orig_color)
    b7g2.configure(background=orig_color)
    b8g2.configure(background=orig_color)
    b10g2.configure(background=orig_color)
    b12g2.configure(background=orig_color)
    b13g2.configure(background=orig_color)
    b15g2.configure(background=orig_color)
#########################STRING 3################################
    b2g3.configure(background=orig_color)
    b4g3.configure(background=orig_color)
    b5g3.configure(background=orig_color)
    b7g3.configure(background=orig_color)
    b9g3.configure(background=orig_color)
    b11g3.configure(background=orig_color)
    b12g3.configure(background=orig_color)
    b14g3.configure(background=orig_color)
    b16g3.configure(background=orig_color)
#########################STRING 4################################
    b2g4.configure(background=orig_color)
    b4g4.configure(background=orig_color)
    b5g4.configure(background=orig_color)
    b7g4.configure(background=orig_color)
    b9g4.configure(background=orig_color)
    b10g4.configure(background=orig_color)
    b12g4.configure(background=orig_color)
    b14g4.configure(background=orig_color)
    b16g4.configure(background=orig_color)

    ## Major Show and Hide Buttons###
b_c_h=Button(frame_major,text='C/Am',command=c_major_yellow,pady=10,background='yellow')
b_c_h.place(x=0,y=50,width=80)
b_c=Button(frame_major,text='C/Am',command=c_major_show,pady=10)
b_c.place(x=0,y=50,width=80)

b_c_sharp_h=Button(frame_major,text='C#/A#m',command=c_sharp_major_orange,pady=10,background='orange')
b_c_sharp_h.place(x=100,y=50,width=80)
b_c_sharp=Button(frame_major,text='C#/A#m',command=c_sharp_major_show,pady=10)
b_c_sharp.place(x=100,y=50,width=80)

b_d_h=Button(frame_major,text='D/Bm',command=d_major_e64040,pady=10,background='#944187')
b_d_h.place(x=200,y=50,width=80)
b_d=Button(frame_major,text='D/Bm',command=d_major_show,pady=10)
b_d.place(x=200,y=50,width=80)

b_d_sharp_h=Button(frame_major,text='D#/Cm',command=d_sharp_major_6fedd0,pady=10,background='#6fedd0')
b_d_sharp_h.place(x=300,y=50,width=80)
b_d_sharp=Button(frame_major,text='D#/Cm',command=d_sharp_major_show,pady=10)
b_d_sharp.place(x=300,y=50,width=80)

b_e_h=Button(frame_major,text='E/C#m',command=e_major_e39ad8,pady=10,background='#e39ad8')
b_e_h.place(x=400,y=50,width=80)
b_e=Button(frame_major,text='E/C#m',command=e_major_show,pady=10)
b_e.place(x=400,y=50,width=80)

b_f_h=Button(frame_major,text='F/Dm',command=f_major_ffc830,pady=10,background='#ffc830')
b_f_h.place(x=500,y=50,width=80)
b_f=Button(frame_major,text='F/Dm',command=f_major_show,pady=10)
b_f.place(x=500,y=50,width=80)

b_f_sharp_h=Button(frame_major,text='F#/D#m',command=f_sharp_major_f7929a,pady=10,background='#f7929a')
b_f_sharp_h.place(x=600,y=50,width=80)
b_f_sharp=Button(frame_major,text='F#/D#m',command=f_sharp_major_show,pady=10)
b_f_sharp.place(x=600,y=50,width=80)

b_g_h=Button(frame_major,text='G/Em',command=g_major_a8edaf,pady=10,background='#a8edaf')
b_g_h.place(x=700,y=50,width=80)
b_g=Button(frame_major,text='G/Em',command=g_major_show,pady=10)
b_g.place(x=700,y=50,width=80)

b_g_sharp_h=Button(frame_major,text='G#/Fm',command=g_sharp_major_d9a49a,pady=10,background='#d9a49a')
b_g_sharp_h.place(x=800,y=50,width=80)
b_g_sharp=Button(frame_major,text='G#/Fm',command=g_sharp_major_show,pady=10)
b_g_sharp.place(x=800,y=50,width=80)

b_a_h=Button(frame_major,text='A/F#m',command=a_major_e6d375,pady=10,background='#e6d375')
b_a_h.place(x=900,y=50,width=80)
b_a=Button(frame_major,text='A/F#m',command=a_major_show,pady=10)
b_a.place(x=900,y=50,width=80)

b_a_sharp_h=Button(frame_major,text='A#/Gm',command=a_sharp_major_a0eb38,pady=10,background='#a0eb38')
b_a_sharp_h.place(x=1000,y=50,width=80)
b_a_sharp=Button(frame_major,text='A#/Gm',command=a_sharp_major_show,pady=10)
b_a_sharp.place(x=1000,y=50,width=80)

b_b_h=Button(frame_major,text='B/G#m',command=b_major_e3bcbd,pady=10,background='#e3bcbd')
b_b_h.place(x=1100,y=50,width=80)
b_b=Button(frame_major,text='B/G#m',command=b_major_show,pady=10)
b_b.place(x=1100,y=50,width=80)

##############  GUITAR NOTES FRAME   ######
guitar_frame=Frame(c,background='#b53b35')
guitar_frame.place(x=0,y=270,width=1355,height=400)
l_guitar_main=Label(guitar_frame,text='Notes On the Ukulele',font=30)
l_guitar_main.place(x=600,y=0)
######## FRET LABELS##############
l_fret0=Label(guitar_frame,text='o',font=10)
l_fret0.place(x=120,y=30,width=20,height=30)

l_fret1=Label(guitar_frame,text='1',font=10)
l_fret1.place(x=150,y=30,width=45,height=30)

l_fret2=Label(guitar_frame,text='2',font=10)
l_fret2.place(x=207,y=30,width=45,height=30)

l_fret3=Label(guitar_frame,text='3',font=10)
l_fret3.place(x=264,y=30,width=45,height=30)

l_fret4=Label(guitar_frame,text='4',font=10)
l_fret4.place(x=321,y=30,width=45,height=30)

l_fret5=Label(guitar_frame,text='5',font=10)
l_fret5.place(x=378,y=30,width=45,height=30)

l_fret6=Label(guitar_frame,text='6',font=10)
l_fret6.place(x=435,y=30,width=45,height=30)

l_fret7=Label(guitar_frame,text='7',font=10)
l_fret7.place(x=492,y=30,width=45,height=30)

l_fret8=Label(guitar_frame,text='8',font=10)
l_fret8.place(x=549,y=30,width=45,height=30)

l_fret9=Label(guitar_frame,text='9',font=10)
l_fret9.place(x=606,y=30,width=45,height=30)

l_fret10=Label(guitar_frame,text='10',font=10)
l_fret10.place(x=663,y=30,width=45,height=30)

l_fret11=Label(guitar_frame,text='11',font=10)
l_fret11.place(x=720,y=30,width=45,height=30)

l_fret12=Label(guitar_frame,text='12',font=10)
l_fret12.place(x=777,y=30,width=45,height=30)

l_fret13=Label(guitar_frame,text='13',font=10)
l_fret13.place(x=834,y=30,width=45,height=30)

l_fret14=Label(guitar_frame,text='14',font=10)
l_fret14.place(x=891,y=30,width=45,height=30)

l_fret15=Label(guitar_frame,text='15',font=10)
l_fret15.place(x=948,y=30,width=45,height=30)
     #####   LABELS FOR STRINGS
l_guitar_string6=Label(guitar_frame,text='String 4:G',font=26)
l_guitar_string6.place(x=0,y=70,height=40,width=110)

l_guitar_string5=Label(guitar_frame,text='String 3:C',font=26)
l_guitar_string5.place(x=0,y=120,height=40,width=110)

l_guitar_string4=Label(guitar_frame,text='String 2:E',font=26)
l_guitar_string4.place(x=0,y=170,height=40,width=110)

l_guitar_string3=Label(guitar_frame,text='String 1:A',font=26)
l_guitar_string3.place(x=0,y=220,height=40,width=110)

############################stopchannels
def stopchannels():
    mixer.Channel(0).stop()
    mixer.Channel(1).stop()
    mixer.Channel(2).stop()
    mixer.Channel(3).stop()
    mixer.Channel(4).stop()
    mixer.Channel(5).stop()
    mixer.Channel(6).stop()
    mixer.Channel(7).stop()
    mixer.Channel(8).stop()
    mixer.Channel(9).stop()
    mixer.Channel(10).stop()
    mixer.Channel(11).stop()
    mixer.Channel(12).stop()
    mixer.Channel(13).stop()
    mixer.Channel(14).stop()
    mixer.Channel(15).stop()
    mixer.Channel(16).stop()
    mixer.Channel(17).stop()
    mixer.Channel(18).stop()
    mixer.Channel(19).stop()
    mixer.Channel(20).stop()
    mixer.Channel(21).stop()
    mixer.Channel(22).stop()
    mixer.Channel(23).stop()
    mixer.Channel(24).stop()
    mixer.Channel(25).stop()
    mixer.Channel(26).stop()
    mixer.Channel(27).stop()
    mixer.Channel(28).stop()
    mixer.Channel(29).stop()
    mixer.Channel(30).stop()
    mixer.Channel(31).stop()
    mixer.Channel(32).stop()
    mixer.Channel(33).stop()
    mixer.Channel(34).stop()
    mixer.Channel(35).stop()
    mixer.Channel(36).stop()
    mixer.Channel(37).stop()
    mixer.Channel(38).stop()
    mixer.Channel(39).stop()
    mixer.Channel(40).stop()
    mixer.Channel(41).stop()
    mixer.Channel(42).stop()
    mixer.Channel(43).stop()
    mixer.Channel(44).stop()
    mixer.Channel(45).stop()
    mixer.Channel(46).stop()
    mixer.Channel(47).stop()
    mixer.Channel(48).stop()
    mixer.Channel(49).stop()
    mixer.Channel(50).stop()
    mixer.Channel(51).stop()
    mixer.Channel(52).stop()
    mixer.Channel(53).stop()
    mixer.Channel(54).stop()
    mixer.Channel(55).stop()
    mixer.Channel(56).stop()
    mixer.Channel(57).stop()
    mixer.Channel(58).stop()
    mixer.Channel(59).stop()
    mixer.Channel(60).stop()
    mixer.Channel(61).stop()
    mixer.Channel(62).stop()
    mixer.Channel(63).stop()

######################FUNCTIONS FOR STRING 4
#################string 4 functions
def g41():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(0).play(mixer.Sound('Audio/G0.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(0).play(mixer.Sound('Audio/G0.wav'))
def g42():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(1).play(mixer.Sound('Audio/G1.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(1).play(mixer.Sound('Audio/G1.wav'))
def g43():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(2).play(mixer.Sound('Audio/G2.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(2).play(mixer.Sound('Audio/G2.wav'))
def g44():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(3).play(mixer.Sound('Audio/G3.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(3).play(mixer.Sound('Audio/G3.wav'))
def g45():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(4).play(mixer.Sound('Audio/G4.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(4).play(mixer.Sound('Audio/G4.wav'))
def g46():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(5).play(mixer.Sound('Audio/G5.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(5).play(mixer.Sound('Audio/G5.wav'))
def g47():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(6).play(mixer.Sound('Audio/G6.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(6).play(mixer.Sound('Audio/G6.wav'))
def g48():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(7).play(mixer.Sound('Audio/G7.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(7).play(mixer.Sound('Audio/G7.wav'))
def g49():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(8).play(mixer.Sound('Audio/G8.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(8).play(mixer.Sound('Audio/G8.wav'))
def g410():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(9).play(mixer.Sound('Audio/G9.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(9).play(mixer.Sound('Audio/G9.wav'))
def g411():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(10).play(mixer.Sound('Audio/G10.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(10).play(mixer.Sound('Audio/G10.wav'))
def g412():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(11).play(mixer.Sound('Audio/G11.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(11).play(mixer.Sound('Audio/G11.wav'))
def g413():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(12).play(mixer.Sound('Audio/G12.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(12).play(mixer.Sound('Audio/G12.wav'))
def g414():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(13).play(mixer.Sound('Audio/G13.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(13).play(mixer.Sound('Audio/G13.wav'))
def g415():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(14).play(mixer.Sound('Audio/G14.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(14).play(mixer.Sound('Audio/G14.wav'))
def g416():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(15).play(mixer.Sound('Audio/G15.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(15).play(mixer.Sound('Audio/G15.wav'))
#################string 3 functions
def g31():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(16).play(mixer.Sound('Audio/C0.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(16).play(mixer.Sound('Audio/C0.wav'))
def g32():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(17).play(mixer.Sound('Audio/C1.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(17).play(mixer.Sound('Audio/C1.wav'))
def g33():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(18).play(mixer.Sound('Audio/C2.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(18).play(mixer.Sound('Audio/C2.wav'))
def g34():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(19).play(mixer.Sound('Audio/C3.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(19).play(mixer.Sound('Audio/C3.wav'))
def g35():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(20).play(mixer.Sound('Audio/C4.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(20).play(mixer.Sound('Audio/C4.wav'))
def g36():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(21).play(mixer.Sound('Audio/C5.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(21).play(mixer.Sound('Audio/C5.wav'))
def g37():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(22).play(mixer.Sound('Audio/C6.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(22).play(mixer.Sound('Audio/C6.wav'))
def g38():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(23).play(mixer.Sound('Audio/C7.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(23).play(mixer.Sound('Audio/C7.wav'))
def g39():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(24).play(mixer.Sound('Audio/C8.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(24).play(mixer.Sound('Audio/C8.wav'))
def g310():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(25).play(mixer.Sound('Audio/C9.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(25).play(mixer.Sound('Audio/C9.wav'))
def g311():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(26).play(mixer.Sound('Audio/C10.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(26).play(mixer.Sound('Audio/C10.wav'))
def g312():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(27).play(mixer.Sound('Audio/C11.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(27).play(mixer.Sound('Audio/C11.wav'))
def g313():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(28).play(mixer.Sound('Audio/C12.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(28).play(mixer.Sound('Audio/C12.wav'))
def g314():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(29).play(mixer.Sound('Audio/C13.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(29).play(mixer.Sound('Audio/C13.wav'))
def g315():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(30).play(mixer.Sound('Audio/C14.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(30).play(mixer.Sound('Audio/C14.wav'))
def g316():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(31).play(mixer.Sound('Audio/C15.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(31).play(mixer.Sound('Audio/C15.wav'))
#################string 2 functions
#################string 2 functions
def g21():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(32).play(mixer.Sound('Audio/E0.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(32).play(mixer.Sound('Audio/E0.wav'))
def g22():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(33).play(mixer.Sound('Audio/E1.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(33).play(mixer.Sound('Audio/E1.wav'))
def g23():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(34).play(mixer.Sound('Audio/E2.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(34).play(mixer.Sound('Audio/E2.wav'))
def g24():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(35).play(mixer.Sound('Audio/E3.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(35).play(mixer.Sound('Audio/E3.wav'))
def g25():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(36).play(mixer.Sound('Audio/E4.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(36).play(mixer.Sound('Audio/E4.wav'))
def g26():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(37).play(mixer.Sound('Audio/E5.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(37).play(mixer.Sound('Audio/E5.wav'))
def g27():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(38).play(mixer.Sound('Audio/E6.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(38).play(mixer.Sound('Audio/E6.wav'))
def g28():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(39).play(mixer.Sound('Audio/E7.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(39).play(mixer.Sound('Audio/E7.wav'))
def g29():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(40).play(mixer.Sound('Audio/E8.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(40).play(mixer.Sound('Audio/E8.wav'))
def g210():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(41).play(mixer.Sound('Audio/E9.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(41).play(mixer.Sound('Audio/E9.wav'))
def g211():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(42).play(mixer.Sound('Audio/E10.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(42).play(mixer.Sound('Audio/E10.wav'))
def g212():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(43).play(mixer.Sound('Audio/E11.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(43).play(mixer.Sound('Audio/E11.wav'))
def g213():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(44).play(mixer.Sound('Audio/E12.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(44).play(mixer.Sound('Audio/E12.wav'))
def g214():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(45).play(mixer.Sound('Audio/E13.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(45).play(mixer.Sound('Audio/E13.wav'))
def g215():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(46).play(mixer.Sound('Audio/E14.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(46).play(mixer.Sound('Audio/E14.wav'))
def g216():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(47).play(mixer.Sound('Audio/E15.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(47).play(mixer.Sound('Audio/E15.wav'))
#################string 1  functions
#################string 1  functions
def g11():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(48).play(mixer.Sound('Audio/A0.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(48).play(mixer.Sound('Audio/A0.wav'))
def g12():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(49).play(mixer.Sound('Audio/A1.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(49).play(mixer.Sound('Audio/A1.wav'))
def g13():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(50).play(mixer.Sound('Audio/A2.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(50).play(mixer.Sound('Audio/A2.wav'))
def g14():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(51).play(mixer.Sound('Audio/A3.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(51).play(mixer.Sound('Audio/A3.wav'))
def g15():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(52).play(mixer.Sound('Audio/A4.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(52).play(mixer.Sound('Audio/A4.wav'))
def g16():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(53).play(mixer.Sound('Audio/A5.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(53).play(mixer.Sound('Audio/A5.wav'))
def g17():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(54).play(mixer.Sound('Audio/A6.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(54).play(mixer.Sound('Audio/A6.wav'))
def g18():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(55).play(mixer.Sound('Audio/A7.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(55).play(mixer.Sound('Audio/A7.wav'))
def g19():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(56).play(mixer.Sound('Audio/A8.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(56).play(mixer.Sound('Audio/A8.wav'))
def g110():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(57).play(mixer.Sound('Audio/A9.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(57).play(mixer.Sound('Audio/A9.wav'))
def g111():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(58).play(mixer.Sound('Audio/A10.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(58).play(mixer.Sound('Audio/A10.wav'))
def g112():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(59).play(mixer.Sound('Audio/A11.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(59).play(mixer.Sound('Audio/A11.wav'))
def g113():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(60).play(mixer.Sound('Audio/A12.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(60).play(mixer.Sound('Audio/A12.wav'))
def g114():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(61).play(mixer.Sound('Audio/A13.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(61).play(mixer.Sound('Audio/A13.wav'))
def g115():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(62).play(mixer.Sound('Audio/A14.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(62).play(mixer.Sound('Audio/A14.wav'))
def g116():
    if(flag_for_guitar==0):
        stopchannels()
        mixer.Channel(63).play(mixer.Sound('Audio/A15.wav'))
    elif(flag_for_guitar==1):
        mixer.Channel(63).play(mixer.Sound('Audio/A15.wav'))
########    GUITAR BUTTONS string 4  ######
###################STRING 4 BUTTONS#############
b1g4=Button(guitar_frame,text='G',command=g41)
b1g4.place(x=120,y=70,height=40,width=20)
b2g4=Button(guitar_frame,text='G#/Ab',command=g42)
b2g4.place(x=150,y=70,height=40,width=45)
b3g4=Button(guitar_frame,text='A',command=g43)
b3g4.place(x=207,y=70,height=40,width=45)
b4g4=Button(guitar_frame,text='A#/Bb',command=g44)
b4g4.place(x=263,y=70,height=40,width=45)
b5g4=Button(guitar_frame,text='B',command=g45)
b5g4.place(x=321,y=70,height=40,width=45)
b6g4=Button(guitar_frame,text='C',command=g46)
b6g4.place(x=378,y=70,height=40,width=45)
b7g4=Button(guitar_frame,text='C#/Db',command=g47)
b7g4.place(x=434,y=70,height=40,width=45)
b8g4=Button(guitar_frame,text='D',command=g48)
b8g4.place(x=492,y=70,height=40,width=45)
b9g4=Button(guitar_frame,text='D#/Eb',command=g49)
b9g4.place(x=549,y=70,height=40,width=45)
b10g4=Button(guitar_frame,text='E',command=g410)
b10g4.place(x=606,y=70,height=40,width=45)
b11g4=Button(guitar_frame,text='F',command=g411)
b11g4.place(x=663,y=70,height=40,width=45)
b12g4=Button(guitar_frame,text='F#/Gb',command=g412)
b12g4.place(x=720,y=70,height=40,width=45)
b13g4=Button(guitar_frame,text='G',command=g413)
b13g4.place(x=777,y=70,height=40,width=45)
b14g4=Button(guitar_frame,text='G#/Ab',command=g414)
b14g4.place(x=833,y=70,height=40,width=45)
b15g4=Button(guitar_frame,text='A',command=g415)
b15g4.place(x=891,y=70,height=40,width=45)
b16g4=Button(guitar_frame,text='A#/Bb',command=g416)
b16g4.place(x=948,y=70,height=40,width=45)
########    GUITAR BUTTONS string 3 ######
###################STRING 3 BUTTONS#############
b1g3=Button(guitar_frame,text='C',command=g31)
b1g3.place(x=120,y=120,height=40,width=20)
b2g3=Button(guitar_frame,text='C#/Db',command=g32)
b2g3.place(x=150,y=120,height=40,width=45)
b3g3=Button(guitar_frame,text='D',command=g33)
b3g3.place(x=207,y=120,height=40,width=45)
b4g3=Button(guitar_frame,text='D#/Eb',command=g34)
b4g3.place(x=263,y=120,height=40,width=45)
b5g3=Button(guitar_frame,text='E',command=g35)
b5g3.place(x=321,y=120,height=40,width=45)
b6g3=Button(guitar_frame,text='F',command=g36)
b6g3.place(x=378,y=120,height=40,width=45)
b7g3=Button(guitar_frame,text='F#/Gb',command=g37)
b7g3.place(x=434,y=120,height=40,width=45)
b8g3=Button(guitar_frame,text='G',command=g38)
b8g3.place(x=492,y=120,height=40,width=45)
b9g3=Button(guitar_frame,text='G#/Ab',command=g39)
b9g3.place(x=549,y=120,height=40,width=45)
b10g3=Button(guitar_frame,text='A',command=g310)
b10g3.place(x=606,y=120,height=40,width=45)
b11g3=Button(guitar_frame,text='A#/Bb',command=g311)
b11g3.place(x=663,y=120,height=40,width=45)
b12g3=Button(guitar_frame,text='B',command=g312)
b12g3.place(x=720,y=120,height=40,width=45)
b13g3=Button(guitar_frame,text='C',command=g313)
b13g3.place(x=777,y=120,height=40,width=45)
b14g3=Button(guitar_frame,text='C#/Db',command=g314)
b14g3.place(x=833,y=120,height=40,width=45)
b15g3=Button(guitar_frame,text='D',command=g315)
b15g3.place(x=891,y=120,height=40,width=45)
b16g3=Button(guitar_frame,text='D#/Eb',command=g316)
b16g3.place(x=948,y=120,height=40,width=45)
###################STRING 2 BUTTONS#############
b1g2=Button(guitar_frame,text='E',command=g21)
b1g2.place(x=120,y=170,height=40,width=20)
b2g2=Button(guitar_frame,text='F',command=g22)
b2g2.place(x=150,y=170,height=40,width=45)
b3g2=Button(guitar_frame,text='F#/Gb',command=g23)
b3g2.place(x=207,y=170,height=40,width=45)
b4g2=Button(guitar_frame,text='G',command=g24)
b4g2.place(x=263,y=170,height=40,width=45)
b5g2=Button(guitar_frame,text='G#/Ab',command=g25)
b5g2.place(x=321,y=170,height=40,width=45)
b6g2=Button(guitar_frame,text='A',command=g26)
b6g2.place(x=378,y=170,height=40,width=45)
b7g2=Button(guitar_frame,text='A#/Bb',command=g27)
b7g2.place(x=434,y=170,height=40,width=45)
b8g2=Button(guitar_frame,text='B',command=g28)
b8g2.place(x=492,y=170,height=40,width=45)
b9g2=Button(guitar_frame,text='C',command=g29)
b9g2.place(x=549,y=170,height=40,width=45)
b10g2=Button(guitar_frame,text='C#/Db',command=g210)
b10g2.place(x=606,y=170,height=40,width=45)
b11g2=Button(guitar_frame,text='D',command=g211)
b11g2.place(x=663,y=170,height=40,width=45)
b12g2=Button(guitar_frame,text='D#/Eb',command=g212)
b12g2.place(x=720,y=170,height=40,width=45)
b13g2=Button(guitar_frame,text='E',command=g213)
b13g2.place(x=777,y=170,height=40,width=45)
b14g2=Button(guitar_frame,text='F',command=g214)
b14g2.place(x=833,y=170,height=40,width=45)
b15g2=Button(guitar_frame,text='F#/Gb',command=g215)
b15g2.place(x=891,y=170,height=40,width=45)
b16g2=Button(guitar_frame,text='G',command=g216)
b16g2.place(x=948,y=170,height=40,width=45)
###################STRING 1 BUTTONS#############
b1g1=Button(guitar_frame,text='A',command=g11)
b1g1.place(x=120,y=220,height=40,width=20)
b2g1=Button(guitar_frame,text='A#/Bb',command=g12)
b2g1.place(x=150,y=220,height=40,width=45)
b3g1=Button(guitar_frame,text='B',command=g13)
b3g1.place(x=207,y=220,height=40,width=45)
b4g1=Button(guitar_frame,text='C',command=g14)
b4g1.place(x=263,y=220,height=40,width=45)
b5g1=Button(guitar_frame,text='C#/Db',command=g15)
b5g1.place(x=321,y=220,height=40,width=45)
b6g1=Button(guitar_frame,text='D',command=g16)
b6g1.place(x=378,y=220,height=40,width=45)
b7g1=Button(guitar_frame,text='D#/Eb',command=g17)
b7g1.place(x=434,y=220,height=40,width=45)
b8g1=Button(guitar_frame,text='E',command=g18)
b8g1.place(x=492,y=220,height=40,width=45)
b9g1=Button(guitar_frame,text='F',command=g19)
b9g1.place(x=549,y=220,height=40,width=45)
b10g1=Button(guitar_frame,text='F#/Gb',command=g110)
b10g1.place(x=606,y=220,height=40,width=45)
b11g1=Button(guitar_frame,text='G',command=g111)
b11g1.place(x=663,y=220,height=40,width=45)
b12g1=Button(guitar_frame,text='G#/Ab',command=g112)
b12g1.place(x=720,y=220,height=40,width=45)
b13g1=Button(guitar_frame,text='A',command=g113)
b13g1.place(x=777,y=220,height=40,width=45)
b14g1=Button(guitar_frame,text='A#/Bb',command=g114)
b14g1.place(x=833,y=220,height=40,width=45)
b15g1=Button(guitar_frame,text='B',command=g115)
b15g1.place(x=891,y=220,height=40,width=45)
b16g1=Button(guitar_frame,text='C',command=g116)
b16g1.place(x=948,y=220,height=40,width=45)
################################################
guitarmode=Label(frame_chord,text='composer active',bg='#b53b35')
guitarmode.place(x=1200,y=10,height=80,width=105)
#########################functions for flags FOR PLAYING STYLE#######
flag_for_guitar=0
def deactivatesinglemode():
    btn_for_single_mode.config(bg='green')
    btn_for_piano_mode.config(bg=orig_color)
def deactivatepianomode():
    btn_for_single_mode.config(bg=orig_color)
    btn_for_piano_mode.config(bg='green')
def singlemode():
    global flag_for_guitar
    flag_for_guitar=0
    guitarmode.config(text='composer active')
    deactivatepianomode()
def pianomode():
    global flag_for_guitar
    flag_for_guitar=1
    guitarmode.config(text='piano mode active')
    deactivatesinglemode()
#########################flags FOR PLAYING STYLE#######
btn_for_single_mode=Button(frame_chord,text='piano mode',command=pianomode)
btn_for_single_mode.place(x=1100,y=50,height=40,width=85)
btn_for_piano_mode=Button(frame_chord,text='composer',command=singlemode)
btn_for_piano_mode.place(x=1100,y=5,height=40,width=85)
input()
