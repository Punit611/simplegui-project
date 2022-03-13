#------------------------------#
#--------pong game-------------#
#------------------------------#
import simplegui
import random
radius=8
pad1_len=80
pad2_len=80
t=2
pad_key=0
lives1=5
lives2=5
pos=[20,20]
pad1_pos=[150,5]
pad2_pos=[150,597]
vel=[1,2]
pad2_t=0
pad2_t=0
pad_vel=3
def time():
    global pad1_t
    global pad2_t
    global t
    t+=0.01
    pad1_t+=0.5
    pad2_t+=0.5
def draw(canvas):
    global vel
    global t
    global lives1
    global lives2
    global pos
    global pad1_pos
    global pad2_pos
    canvas.draw_circle(pos,radius,5,'white','red')
    canvas.draw_text('first lives = '+str(lives1),[250,20],12,'white')
    canvas.draw_text('second lives ='+str(lives2),[250,40],12,'white')
    canvas.draw_line([pad1_pos[0]-pad1_len//2,pad1_pos[1]],[pad1_pos[0]+pad1_len//2,pad1_pos[1]],9,'blue')
    canvas.draw_line([pad2_pos[0]-pad2_len//2,pad2_pos[1]],[pad2_pos[0]+pad2_len//2,pad2_pos[1]],9,'green')
    pos[0]=pos[0]+t*vel[0]
    if pos[0]+radius>500 and vel[0]>0:
        vel[0]=-vel[0]
    elif pos[0]<radius and vel[0]<0:
        vel[0]=-vel[0]
    pos[1]=pos[1]+t*vel[1]
    if pos[1]+radius>600 and vel[1]>0 and pos[0]+radius//2>=pad2_pos[0]-pad2_len//2 and pos[0]-radius//2<=pad2_pos[0]+pad1_len//2:
        vel[1]=-vel[1]
    elif pos[1]+radius>600 and vel[1]>0 and (pos[0]+radius//2<pad2_pos[0]-pad2_len//2 or pos[0]-radius//2>=pad2_pos[0]+pad1_len//2):
        pos=[250,250]
        lives2-=1
        t=2
        vel[0]=random.randrange(-3,4,2)
        vel[1]=random.randrange(-3,4,2)
    if pos[1]<radius and vel[1]<0 and pos[0]+radius//2>=pad1_pos[0]-pad1_len//2 and pos[0]-radius//2<=pad1_pos[0]+pad1_len//2:
        vel[1]=-vel[1]
    elif pos[1]<radius and vel[1]<0 and (pos[0]+radius//2<=pad1_pos[0]-pad1_len//2 or pos[0]-radius//2>=pad1_pos[0]+pad1_len//2):
        pos =[250,300]
        lives1-=1
        t=2
        vel[0]=random.randrange(-3,4,2)
        vel[1]=random.randrange(-3,4,2)
    if pad_key==1 and pad1_pos[0]>pad1_len//2:
        pad1_pos[0]-=pad1_t*pad_vel
    elif pad_key==2 and pad1_pos[0]<500-pad1_len//2:
        pad1_pos[0]+=pad1_t*pad_vel
    elif pad_key==3 and pad2_pos[0]>pad2_len//2:
        pad2_pos[0]-=pad2_t*pad_vel
    elif pad_key==4 and pad2_pos[0]<500-pad2_len//2:
        pad2_pos[0]+=pad2_t*pad_vel
        
def keydown(key):
    timer.start()
    global pad1_t
    global pad2_t
    global pad_key
    pad1_t=0
    pad2_t=0
    if key==simplegui.KEY_MAP['left']:
        pad_key=1
    elif key==simplegui.KEY_MAP['right']:
        pad_key=2
    elif key==simplegui.KEY_MAP['a']:
        pad_key=3
    elif key==simplegui.KEY_MAP['d']:
        pad_key=4
def keyup(key):
    global pad_key
    pad_key=0
    timer.stop()
f=simplegui.create_frame('pong',500,600)
f.set_draw_handler(draw)
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
timer=simplegui.create_timer(10,time)
#t=simplegui.create_timer(1000,time_ball)
f.start()
#t.start()
