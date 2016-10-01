import win32com.client
import time

shell = win32com.client.Dispatch("WScript.Shell")
shell.appActivate("Tibia")

#PARAMETROS
#HOTKEYS
hkMagia  = "F1" #MAGIA
hkComida = "F2" #COMIDA

#TEMPO
tpMagia  = 2    #MAGIA (EM SEGUNDOS)
tpMexer  = 1800 #MEXER (EM SEGUNDOS)
tpComida = 300  #COMIDA (EM SEGUNDOS)

#Variaveis auxiliares
auxTempoComida = 0
auxTempoMexer  = 0
auxPosicao     = 0

while True:
    shell.SendKeys("{"+hkMagia+"}")
    print ("Soltando magia")
    
    if auxTempoComida >= tpComida :
        shell.SendKeys("{"+hkComida+"}")
        print ("Comendo a comida")
        auxTempoComida = 0

    if auxTempoMexer >= tpMexer :
        print ("Se movimentando")
        if (auxPosicao % 2) == 0 :
            shell.SendKeys("^{UP}")
        else :
            shell.SendKeys("^{RIGHT}")        
        auxTempoMexer = 0
        auxPosicao = auxPosicao + 1
        
    time.sleep(tpMagia)
    
    auxTempoComida = auxTempoComida + tpMagia
    auxTempoMexer  = auxTempoMexer + tpMagia
