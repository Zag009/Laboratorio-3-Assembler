import PySimpleGUI as sg

g.theme('DarkAmber')

###############################################
#Genera texto y botones para elejir opciones.
layout = [ 
    [sg.Text("Ingrese el valor en Binario o Hexadecimal"), sg.InputText()],
    [sg.Text("Elija una opción:")],
    [sg.Button("Binario - Hexadecimal"), sg.Button("Hexadecimal - Binario"),sg.Button("Cancelar")],
    [sg.Text('Resultado'), sg.Text('', key='Resultado')]]

###############################################
#Crea la ventana 
window = sg.Window("Conversor", layout,  margins = (30,30))

###############################################
#Procesa la decicion del usuario


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancelar": #Lee la decision del usuario para cerrar la ventanta
        break

    if event == "Binario - Hexadecimal":
        num = values[0]
        hex = 0
        mul = 1
        chk = 1
        Hnum = []
        i = 0
        respuesta = ""
        while num!=0:
            rem = int(num)%10
            hex = hex + (rem*mul)
            if chk%4 == 0:
                if hex<10:
                    hex = hex+48
                    val = chr(hex)
                    Hnum.insert(i,val)
                else:
                    hex = hex+55
                    val = chr(hex)
                    Hnum.insert(i,val)
                mul = 1
                hex = 0
                chk = 1
                i = i+1
            else:
                mul = mul*2
                chk = chk+1
            num = int(num)/10
        if chk!=1:
            hex = hex+48
            val = chr(hex)
            Hnum.insert(i,val)
        if chk == 1:
            i = i - 1
        if values [0] [-1] not in ("01"):
            sg.popup("El valor ingresado no es binario")
        i = i + 1
        
        for i in range(len(Hnum)):
            respuesta += str(Hnum[(len(Hnum)) - i - 1])
            
        window["Resultado"].update(respuesta)

    elif event == "Hexadecimal - Binario":
        Num = values[0]
        binnum = ""
        hex = len(Num)
        i = 0
        while i<hex:
            if Num[i] == '0':
                binnum = binnum + "0000"
            elif Num[i] == '1':
                binnum = binnum + "0001"
            elif Num[i] == '2':
                binnum = binnum + "0010"
            elif Num[i] == '3':
                binnum = binnum + "0011"
            elif Num[i] == '4':
                binnum = binnum + "0100"
            elif Num[i] == '5':
                binnum = binnum + "0101"
            elif Num[i] == '6':
                binnum = binnum + "0110"
            elif Num[i] == '7':
                binnum = binnum + "0111"
            elif Num[i] == '8':
                binnum = binnum + "1000"
            elif Num[i] == '9':
                binnum = binnum + "1001"
            elif Num[i] == 'a' or Num[i] == 'A':
                binnum = binnum + "1010"
            elif Num[i] == 'b' or Num[i] == 'B':
                binnum = binnum + "1011"
            elif Num[i] == 'c' or Num[i] == 'C':
                binnum = binnum + "1100"
            elif Num[i] == 'd' or Num[i] == 'D':
                binnum = binnum + "1101"
            elif Num[i] == 'e' or Num[i] == 'E':
                binnum = binnum + "1110"
            elif Num[i] == 'f' or Num[i] == 'F':
                binnum = binnum + "1111"
            i = i+1

        window["Resultado"].update(binnum)
    elif event == "Cancelar":
        break
    
        

###############################################
#Muestra los resultados


###############################################
#Cierra la ventana cuando el usuario lo decee
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancelar": #Lee la decision del usuario para cerrar la ventanta
        break


