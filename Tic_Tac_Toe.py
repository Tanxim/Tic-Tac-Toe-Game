from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from time import *

def reset():
	restart()
	wpl1.config(text="0 win")
	dr1.config(text="0 draw")
	wpl2.config(text="0 win")

def restart():
	global turn,matrix
	matrix=[[""]*3 for i in range(3)]
	turn=0
	#sleep(2)
	turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",fg=col[fig[turn&1]])
	playagain.config(text="Restart !")
	btn1.config(text=" ")
	btn2.config(text=" ")
	btn3.config(text=" ")
	btn4.config(text=" ")
	btn5.config(text=" ")
	btn6.config(text=" ")
	btn7.config(text=" ")
	btn8.config(text=" ")
	btn9.config(text=" ")

def showwin():
	global turn
	flg=False
	win_index=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
	for i,j,k in win_index:
		if matrix[i//3][i%3] and matrix[i//3][i%3]==matrix[j//3][j%3]==matrix[k//3][k%3]:
			turn-=1
			turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1} won the match",fg=col[fig[turn&1]])
			playagain.config(text="Play Again?")
			break

def showdraw():
	turnlbl.config(text="The match is draw :')")
	playagain.config(text="Play Again?")

def bt1():
	global turn
	if not matrix[0][0]:
		sleep(.15)
		mat=matrix[0][0]=fig[turn&1]
		turn+=1
		btn1.config(text=mat,fg=col[mat],activeforeground=col[mat])
		turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",fg=col[fig[turn&1]])
		showwin()
		if turn==9:showdraw()
		
def bt2():
	global turn
	if not matrix[0][1]:
		sleep(.15)
		mat=matrix[0][1]=fig[turn&1]
		turn+=1
		btn2.config(text=mat,fg=col[mat],activeforeground=col[mat])
		turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",fg=col[fig[turn&1]])
		showwin()
		if turn==9:showdraw()

def bt3():
	global turn
	if not matrix[0][2]:
		sleep(.15)
		mat=matrix[0][2]=fig[turn&1]
		turn+=1
		btn3.config(text=mat,fg=col[mat],activeforeground=col[mat])
		turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",fg=col[fig[turn&1]])
		showwin()
		if turn==9:showdraw()

def bt4():
	global turn
	if not matrix[1][0]:
		sleep(.15)
		mat=matrix[1][0]=fig[turn&1]
		turn+=1
		btn4.config(text=mat,fg=col[mat],activeforeground=col[mat])
		turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",fg=col[fig[turn&1]])
		showwin()
		if turn==9:showdraw()
		
def bt5():
	global turn
	if not matrix[1][1]:
		sleep(.15)
		mat=matrix[1][1]=fig[turn&1]
		turn+=1
		btn5.config(text=mat,fg=col[mat],activeforeground=col[mat])
		turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",fg=col[fig[turn&1]])
		showwin()
		if turn==9:showdraw()

def bt6():
	global turn
	if not matrix[1][2]:
		sleep(.15)
		mat=matrix[1][2]=fig[turn&1]
		turn+=1
		btn6.config(text=mat,fg=col[mat],activeforeground=col[mat])
		turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",fg=col[fig[turn&1]])
		showwin()
		if turn==9:showdraw()

def bt7():
	global turn
	if not matrix[2][0]:
		sleep(.15)
		mat=matrix[2][0]=fig[turn&1]
		turn+=1
		btn7.config(text=mat,fg=col[mat],activeforeground=col[mat])
		turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",fg=col[fig[turn&1]])
		showwin()
		if turn==9:showdraw()
		
def bt8():
	global turn
	if not matrix[2][1]:
		sleep(.15)
		mat=matrix[2][1]=fig[turn&1]
		turn+=1
		btn8.config(text=mat,fg=col[mat],activeforeground=col[mat])
		turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",fg=col[fig[turn&1]])
		showwin()
		if turn==9:showdraw()

def bt9():
	global turn
	if not matrix[2][2]:
		sleep(.15)
		mat=matrix[2][2]=fig[turn&1]
		turn+=1
		btn9.config(text=mat,fg=col[mat],activeforeground=col[mat])
		turnlbl.config(text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",fg=col[fig[turn&1]])
		showwin()
		if turn==9:showdraw()

window=Tk()
window.title("Welcome Shanto")
window.configure(bg="black")
#window.geometry("50x50")

turn=0
col={"o":"hot pink","×":"cyan"}
fig=["o","×"]
matrix=[[""]*3 for i in range(3)]

fonts=[("calibri",10,"bold"),("calibri",40)]

headf=Frame(window,bg="black")
headf.grid(row=0,column=0,padx=15)

rset_btn=Button(headf,text="Reset",font=fonts[0],bg="black",fg="lime",activebackground='black',activeforeground="lime",command=reset)
rset_btn.config(highlightthickness=2,highlightbackground="lime")
rset_btn.grid(row=0,column=0)

lbl=Label(headf,text="",bg="black")
lbl.grid(row=0,column=1,padx=150)

quit_btn=Button(headf,text=" Quit !",font=fonts[0],bg="black",fg="red",activebackground="black",activeforeground="red",command=window.destroy)
quit_btn.config(highlightthickness=2,highlightbackground="red")
quit_btn.grid(row=0,column=2)

turnlbl=Label(window,text=f"({fig[turn&1]}) Player {(turn&1)+1}'s turn",font=("Arial",9),bg="black",fg="hot pink")
turnlbl.grid(row=1,pady=150)

mainf=Frame(window,bg="lime")
mainf.grid(row=2,column=0,pady=0)

pixel=PhotoImage(width=1,height=1)

btn1=Button(mainf,text=" ",font=fonts[1],image=pixel,compound="bottom",bg="black",activebackground="black",height=110,width=75,command=bt1)
btn1.config(highlightthickness=2,highlightbackground="lime")
btn1.grid(row=1,column=1,padx=0,pady=0)

btn2=Button(mainf,text=" ",font=fonts[1],image=pixel,compound="bottom",bg="black",activebackground="black",height=110,width=75,command=bt2)
btn2.config(highlightthickness=2,highlightbackground="lime")
btn2.grid(row=1,column=2,padx=0,pady=0)

btn3=Button(mainf,text=" ",font=fonts[1],image=pixel,compound="bottom",bg="black",activebackground="black",height=110,width=75,command=bt3)
btn3.config(highlightthickness=2,highlightbackground="lime")
btn3.grid(row=1,column=3,padx=0,pady=0)

btn4=Button(mainf,text=" ",font=fonts[1],image=pixel,compound="bottom",bg="black",activebackground="black",height=110,width=75,command=bt4)
btn4.config(highlightthickness=2,highlightbackground="lime")
btn4.grid(row=2,column=1,padx=0,pady=0)

btn5=Button(mainf,text=" ",font=fonts[1],image=pixel,compound="bottom",bg="black",activebackground="black",height=110,width=75,command=bt5)
btn5.config(highlightthickness=2,highlightbackground="lime")
btn5.grid(row=2,column=2,padx=0,pady=0)

btn6=Button(mainf,text=" ",font=fonts[1],image=pixel,compound="bottom",bg="black",activebackground="black",height=110,width=75,command=bt6)
btn6.config(highlightthickness=2,highlightbackground="lime")
btn6.grid(row=2,column=3,padx=0,pady=0)

btn7=Button(mainf,text=" ",font=fonts[1],image=pixel,compound="bottom",bg="black",activebackground="black",height=110,width=75,command=bt7)
btn7.config(highlightthickness=2,highlightbackground="lime")
btn7.grid(row=3,column=1,padx=0,pady=0)

btn8=Button(mainf,text=" ",font=fonts[1],image=pixel,compound="bottom",bg="black",activebackground="black",height=110,width=75,command=bt8)
btn8.config(highlightthickness=2,highlightbackground="lime")
btn8.grid(row=3,column=2,padx=0,pady=0)

btn9=Button(mainf,text=" ",font=fonts[1],image=pixel,compound="bottom",bg="black",activebackground="black",height=110,width=75,command=bt9)
btn9.config(highlightthickness=2,highlightbackground="lime")
btn9.grid(row=3,column=3,padx=0,pady=0)

playagain=Button(window,text="Restart !",font=("Arial",10),image=pixel,compound="center",bg="black",fg="lime",activebackground="black",activeforeground="lime",highlightthickness=2,highlightbackground="lime",height=30,width=200,command=restart)
playagain.grid(row=3,column=0,pady=80)

endf=Frame(window,bg="black")
endf.grid(row=4,column=0,padx=50,pady=60)

win1=0
win2=0
dr=0
pl1=Label(endf,text="×",font=("Arial",30),bg="black",fg="cyan")
pl1.grid(row=0,column=0)
wpl1=Label(endf,text=f"{win1} win",font=("Arial",10),bg="black",fg="cyan")
wpl1.grid(row=1,column=0)

draw=Label(endf,text="=",font=("Arial",30),bg="black",fg="yellow")
draw.grid(row=0,column=1,padx=140)
dr1=Label(endf,text=f"{dr} draw",font=("Arial",10),bg="black",fg="yellow")
dr1.grid(row=1,column=1)

pl2=Label(endf,text="o",font=("Arial",30),bg="black",fg="hot pink")
pl2.grid(row=0,column=2)
wpl2=Label(endf,text=f"{win2} win",font=("Arial",10),bg="black",fg="hot pink")
wpl2.grid(row=1,column=2)

window.mainloop()