import math
a=int()
rad=a*math.pi/180
sin=math.sin(rad)
cos=math.sqrt(1-sin**2)
v=20
h=4
s=40
y=(s*sin/cos)-((9.8*s**2)/(2*v**2*cos**2))
for a in range(0,90):
   rad=a*math.pi/180
   sin=math.sin(rad)
   cos=math.sqrt(1-sin**2)
   y=(s*sin/cos)-((9.8*s**2)/(2*v**2*cos**2))
   if y<0:
      print(a, y)

   
#if y>=0:
  # if y<h:
   #   print("Попадание")
  # elif y>h:
  #    print("Перелет")
#else:
  # print("Недолет")
