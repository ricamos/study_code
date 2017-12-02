import time
import webbrowser

# Passo 3 - Repetir pocesso do inicio

total_breaks = 1
break_ount = 0
time_to_break = 5 #Seconds

print ("This program started  on " + time.ctime())
while break_ount < total_breaks:
    # Passo 1 - Contar o tempo
    time.sleep(time_to_break)

    # Passo 2 - Abrir um video de alerta
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")

    break_ount += 1

print ("This program finished on " + time.ctime())