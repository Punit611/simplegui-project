import simplegui
import random
num=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
mou_pos=[0,0]
check=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
chk=[]
chk_in=[]
turn=0
random.shuffle(num)
def draw(canvas):
    global check
    global chk
    global chk_in
    for i in range(20):
        canvas.draw_line([i*40,50],[i*40,150],1,'white')
    canvas.draw_text('Turn '+str(turn),[370,35],32,'red')
    canvas.draw_line([0,50],[800,50],2,'white')
    for i in range(len(check)):
        if check[i]>-1:
            canvas.draw_text(str(check[i]),[i*40+15,100],32,'red')
    if len(chk)%2==0 and len(chk)>=2:
        if chk[len(chk)-1]!=chk[len(chk)-2]:
            chk.pop()
            chk.pop()
            check[chk_in[len(chk_in)-1]]=-1
            check[chk_in[len(chk_in)-2]]=-1
          
def click(pos):
    global mou_pos
    global turn
    global check
    global chk
    global chk_in
    turn+=1
    mou_pos=list(pos)
    a=mou_pos[0]//40
    if len(chk_in)==0:
        check[a]=num[a]
        chk.append(num[a])
        chk_in.append(a)
    elif a!=chk_in[len(chk_in)-1]:
        check[a]=num[a]
        chk.append(num[a])
        chk_in.append(a)

def restart():
    global num
    global check
    global chk
    global chk_in
    global turn
    check=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    chk=[]
    chk_in=[]
    turn=0
    random.shuffle(num)

f=simplegui.create_frame('memory game',800,150)
f.set_draw_handler(draw)
f.set_mouseclick_handler(click)
f.add_button('Restart',restart,150)
f.start()