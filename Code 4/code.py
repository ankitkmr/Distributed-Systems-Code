try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
import time

#Global Variables
WIDTH = 720
HEIGHT = 470
BALL_RADIUS = 10

ball1_pos = [40,40]
ball1_color = 'Red'

ball2_pos = [205,430]
ball2_color = 'Red'

ball3_pos = [680,40]
ball3_color = 'Blue'

ball4_pos = [515,430]
ball4_color = 'Blue'

REQUEST_STATE = [0,0,0,0]
LEFT = [1,2]
RIGHT =[3,4]
last = 0
LOCK = False
CROSS = 0

#Helper Functions
def move(ball, ball_pos):
    global CROSS, LOCK, ball1_color, ball2_color,ball3_color,ball4_color

    if CROSS == ball and (ball_pos[1] == 235 and ball_pos[0]<=515 and ball_pos[0]>=205):
        if ball in LEFT: 
            if ball_pos[0]>=205 and ball_pos[0]<=510 and ball_pos[1] ==235 :
                ball_pos[0]+=5

            elif ball_pos==[515,235]:
                LEFT.remove(ball)
                RIGHT.append(ball)

                if ball == 1:
                    ball1_color = 'Blue'
                elif ball == 2:
                    ball2_color = 'Blue'
                elif ball == 3:
                    ball3_color = 'Blue'
                else:
                    ball4_color = 'Blue'

                CROSS = 0            
                LOCK= False
                print "Lock Released"

        elif ball in RIGHT:
            if ball_pos[0]>=210 and ball_pos[0]<=515 and ball_pos[1] ==235:
                ball_pos[0]-=5

            elif ball_pos==[205,235]:
                RIGHT.remove(ball)
                LEFT.append(ball)

                if ball == 1:
                    ball1_color = 'Red'
                elif ball == 2:
                    ball2_color = 'Red'
                elif ball == 3:
                    ball3_color = 'Red'
                else:
                    ball4_color = 'Red'

                CROSS = 0
                LOCK= False
                print "Lock Released"
    else:
        #Handling up
        if ball_pos[1] == 40:
            #Handling Left Side Movement
            if ball_pos[0]>=45 and ball_pos[0]<=205:
                ball_pos[0]-=5
            elif ball_pos[0]==40:
                ball_pos[1]+=5
            #Handling Right Side Movement
            elif ball_pos[0]>=515 and ball_pos[0]<=675:
                ball_pos[0]+=5
            elif ball_pos[0]==680:
                ball_pos[1]+=5
        
        #Handling Down
        elif ball_pos[1] == 430:
            if ball_pos[0]>=40 and ball_pos[0]<=200:
                ball_pos[0]+=5
            elif ball_pos[0]==205:
                ball_pos[1]-=5
            elif ball_pos[0]>=520 and ball_pos[0]<=680:
                ball_pos[0]-=5
            elif ball_pos[0]==515:
                ball_pos[1]-=5

        #Handling Left verticals
        elif ball_pos[0] == 40 and (ball_pos[1]>=40 and ball_pos[1]<=425):
            ball_pos[1]+=5
        elif ball_pos[0] == 205 and (ball_pos[1]<=430 and ball_pos[1]>=45):
            ball_pos[1]-=5

        #Handling Right Verticals
        elif ball_pos[0] == 515 and (ball_pos[1]>=45 and ball_pos[1]<430):
            ball_pos[1]-=5
        elif ball_pos[0] == 680 and (ball_pos[1]<=430 and ball_pos[1]>=45):
            ball_pos[1]+=5

    
# Handler for timer
def movement1():
    if 1 in LEFT:
        move(1, ball1_pos)
    if 2 in LEFT:
        move(2, ball2_pos)
    if 3 in LEFT:
        move(3, ball3_pos)
    if 4 in LEFT:
        move(4, ball4_pos)

        
def movement2():
    if 1 in RIGHT:
        move(1, ball1_pos)
    if 2 in RIGHT:
        move(2, ball2_pos)
    if 3 in RIGHT:
        move(3, ball3_pos)
    if 4 in RIGHT:
        move(4, ball4_pos)
        
               
def flip(ball):
    global LOCK, CROSS
    print REQUEST_STATE
    if LOCK == False:
        LOCK = True

        CROSS = ball
        print "Process",ball,"granted Access."
         
        
def decide(arg = 'Timer'):
    global last, LOCK
    
    if arg == 'Handler' and LOCK == 'True':
        print 'Mutex Lock'
        
    elif REQUEST_STATE != [0,0,0,0] and arg == 'Timer' and LOCK == False:
        for j in xrange(1,5):
            if REQUEST_STATE[(last+j)%4] !=0:
                last = (last+j)%4
                break

        if REQUEST_STATE[last]>0:  
            flip(last+1)                   
            REQUEST_STATE[last]-=1

    
def keyHandler(key):
    global REQUEST_STATE
    dict_key = {49:1,50:2,51:3,52:4}
    
    print 'Requesting Access for Process', dict_key[key]
    REQUEST_STATE[dict_key[key]-1]=REQUEST_STATE[dict_key[key]-1]+1    
    
    print "New State:", REQUEST_STATE
    decide(arg = 'Handler')
    
    

# Handler to draw on canvas
def draw_handler(canvas):
    canvas.draw_polyline([(10, 10), (235, 10), 
                          (235, 210),(485,210),
                          (485,10),(710,10),
                         (710,460),(485,460),
                          (485,260),(235,260),
                         (235,460),(10,460),
                          (10,10)], 5, 'White')
    
    canvas.draw_polyline([(70,70),(175,70),
                          (175,400),(70,400),
                          (70,70)], 5, 'White')
    
    canvas.draw_polyline([(545,70),(650,70),
                          (650,400),(545,400),
                         (545,70)], 5, 'White')
    
    canvas.draw_circle(ball1_pos, BALL_RADIUS, 2, 'White', ball1_color)
    canvas.draw_text('1', [ball1_pos[0]-5,ball1_pos[1]+5], 20, 'White', 'monospace' )
    canvas.draw_circle(ball2_pos, BALL_RADIUS, 2, 'White', ball2_color)
    canvas.draw_text('2', [ball2_pos[0]-5,ball2_pos[1]+5], 20, 'White', 'monospace' )
    canvas.draw_circle(ball3_pos, BALL_RADIUS, 2, 'White', ball3_color)
    canvas.draw_text('3', [ball3_pos[0]-5,ball3_pos[1]+5], 20, 'White', 'monospace' )
    canvas.draw_circle(ball4_pos, BALL_RADIUS, 2, 'White', ball4_color)
    canvas.draw_text('4', [ball4_pos[0]-5,ball4_pos[1]+5], 20, 'White', 'monospace' )
        

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame('Mutex', WIDTH, HEIGHT)
timer1 = simplegui.create_timer(20, movement1)
timer2 = simplegui.create_timer(35, movement2)
timer3 = simplegui.create_timer(10, decide)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keyHandler)

# Start the frame animation
timer1.start()
timer2.start()
timer3.start()
frame.start()
