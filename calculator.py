import turtle
r,Clear,player=(turtle.Turtle() for i in range(3))
turtle.tracer(2)
r.up()
r.goto(-330,190)
r.hideturtle()
FONT=('Times New Roman',40,'bold')
wn=turtle.Screen()
wn.bgcolor('gold')
images=['seven_.gif','eight_.gif','nine_.gif','division_.gif',\
         'four_.gif','five_.gif','six_.gif','multiplication_.gif',\
         'one_.gif','two_.gif','three_.gif','subtraction_.gif',\
         'zero_.gif','decimal_.gif','addition_.gif','equal_.gif',\
         'calc_area2.gif']
digits=['7','8','9','/','4','5','6','*','1','2','3','-','0','.','+',' ','']
wn.addshape('clear_.gif')
Clear.shape('clear_.gif')
Clear.up()
Clear.goto(-300,-50)
number,t,a=([] for i in range (3))
for i in range (17):
        wn.addshape(images[i])
        t.append(turtle.Turtle())
        t[i].up()
        t[i].shape(images[i])
        a.append(0)
for m in range(16):
    m1=m//4
    m2=m%4
    t[m].goto(-300+150*m2,150-m1*50)
t[16].goto(-75,250)
wn.addshape('pixx_10.gif')
player.shape('pixx_10.gif')
player.up()
player.hideturtle()
player.goto(-300,-200)
player.showturtle()
playersposition=player.position()
q1=0
def h1(x,y):
    global q1
    if q1==1:
        r.clear()
        number.clear()
        q1=0
    FONT=('Times New Roman',40,'bold')
    player.goto(x,y)
    playerposition=player.position()
    for q in range(16):
        a[q]=abs(playerposition-t[q].position())
        if a[q]<30:
            number.append(digits[q])
    result_str = str("".join(number)) # Join the string values into one string
    r.write(result_str,font=FONT)
    if abs(playerposition-t[15].position())<30:
        try:
            estimation=round(eval(result_str ),5)
            r.clear()
            r.write(result_str+'='+str(estimation),font=FONT)
            q1=1
        except:
            r.clear()
            r.write('Error',font=FONT)
            q1=1
    if abs(playerposition-Clear.position())<30:
            r.clear()
            number.clear()
wn.onclick(h1)