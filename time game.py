import simplegui

upper=0
lower=0
count=0
tim='0/0'
star=0
stp=0
message='0:0.0'
def time():
    global count
    count+=1
    global tim
    global message
    message=str(count//600)+':'+str((count%600)//10)+'.'+str(count%10)
    tim =str(lower)+'/'+str(upper)
def draw(canvas):
    canvas.draw_text(tim,(260,30),24,'green')
    canvas.draw_text(message,(150,160),32,'red')

def start():
    timer.start()
    global star
    global stp
    if star==0:
        global upper
        star=1
        stp=0
        upper+=1
def stop():
    timer.stop()
    global lower
    global star
    global stp
    if stp==0:
        stp=1
        star=0
        if count%10==0:
            lower+=1
 
frame=simplegui.create_frame('time game',300,300)
frame.set_draw_handler(draw)
frame.add_button('start',start,150)
frame.add_button('stop',stop,150)
timer=simplegui.create_timer(100,time)
frame.start()