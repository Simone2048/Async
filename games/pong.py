#OLED_WIDTH = 128
#OLED_HEIGHT = 64

xVel=2
yVel=1
player_score = 0
ai_score = 0
paddle_length = 16

x,y = 64,32 #Center Of Screen
plY = 32
aiY = y
ball = None

player_paddle_speed = yVel+1
def run(canvas, read_btns):
    global ball, x, y, xVel, yVel, player_score, ai_score, paddle_length, plY, aiY, player_paddle_speed
    if ball == None:
        ball = canvas.import_bit_map('sprites/ball.json')
        print("Imported Ball Sprite")
        
    up, down, left, right, action = read_btns
    canvas.clear()
    canvas.draw_bit_map(ball,x,y)
    
    aiY =  max(int(paddle_length/2), min(y, 64-int(paddle_length/2)))
    
    if down:
        plY += player_paddle_speed
    if up:
        plY -= player_paddle_speed
    plY =  max(int(paddle_length/2), min(plY, 64-int(paddle_length/2)))
    
    draw_paddle(canvas,aiY,paddle_length,"ai")
    draw_paddle(canvas,plY,paddle_length,"player")
    x+=xVel
    if x <= 1:
        if plY-int(paddle_length/2) <= y <= plY+int(paddle_length/2):
            xVel = -xVel
        else:
            ai_score += 1
            x = 64
            y = 32
    if x >= 122:
        if aiY-int(paddle_length/2) <= y <= aiY+int(paddle_length/2):
            xVel = -xVel
        else:
            player_score += 1
            x=64
            y = 32
    
    draw_scores(canvas,player_score,ai_score)
    y+=yVel
    if y <= 0:
        yVel = -yVel
    if y >= 59:
        yVel = -yVel
    canvas.show()
    
def draw_paddle(canvas,y,length,side):
    x = 0 if side == "player" else 127
    canvas.vline(x,y-int(length/2),length)
def draw_scores(canvas,playerScore,aiScore):
    canvas.text(str(player_score),48,0)
    canvas.text(str(ai_score),80,0)