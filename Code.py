#Entrevista práctica: programa recibe hora númerica, muestra hora en texto
#AUTOR: Alver Alcides Carrillo Romero
#Fecha: 20/07/2021

#Esta funcion determina si la hora ingresada es de la mañana(am) o de la tarde(pm)
#Y retorna el valor en texto para ir formando la cadena de texto.
def horario(hora):
    if hora == "am":
        tiempo="mañana"
        return tiempo
    elif hora == "pm":
        tiempo = "Tarde"
        return tiempo
#Esta Función tiene como objetivo definir en que unidad de los minutos esta la hora que se ingresó
#Y retorna el valor en texto
def minutos10(min):
    if int(min)==1:
        return " Y uno"
    elif int(min)==2:
        return " y Dos"
    elif int(min)==3:
        return " y Tres"
    elif int(min)==4:
        return " y Cuatro"
    elif int(min)==5:
        return " y Cinco"
    elif int(min)==6:
        return " y Seis"
    elif int(min)==7:
        return " y Siete"
    elif int(min)==8:
        return " y Ocho"
    elif int(min)==9:
        return " y Nueve"
#Esta Función verifica en que decena se encuentran los minutos y devuelve el valor para que 
#Coincida con la unidad de los minutos, retornando el valor en texto.
def minutos(min):
    if int(min) < 10:
        return minutos10(min) 
    elif min == "10":
        return "y Diez"
    elif min == "11":
        return "y Once"
    elif min == "12":
        return "y Doce"
    elif min == "13":
        return "y Trece"
    elif min == "14":
        return "y Catorce"
    elif min == "15":
        return "y Cuarto"
    elif int(min) > 15 and int(min)<20:
        return "y Diez" + minutos10(min[-1:])
    elif min[:1]=="2":
        if min[-1:] =="0":
            return "Y Veinte"
        return "y Veinte" + minutos10(min[-1:])
    elif min[:1]=="3":
        if min[-1:] =="0":
            return "Y media"
        return "y Treinta" + minutos10(min[-1:])
    elif min[:1]=="4":
        if min[-1:] =="0":
            return "Y Cuarenta"
        return "y Cuarenta" + minutos10(min[-1:])
    elif min[:1]=="5":
        if min[-1:] =="0":
            return "Y Cincuenta"
        return "y Cincuenta" + minutos10(min[-1:])
def horas(hora):
    if int(hora)==1:
        return " La Una "
    elif int(hora)==2:
        return " Las Dos "
    elif int(hora)==3:
        return " Las Tres "
    elif int(hora)==4:
        return " Las Cuatro "
    elif int(hora)==5:
        return " Las Cinco "
    elif int(hora)==6:
        return " Las Seis "
    elif int(hora)==7:
        return " Las Siete "
    elif int(hora)==8:
        return " Las Ocho "
    elif int(hora)==9:
        return " Las Nueve "
    elif int(hora)==10:
        return " Las Diez "
    elif int(hora)==11:
        return " Las Once "
    elif int(hora)==12:
        return " Las Doce "
     
#Este es el procedimiento principal, en donde se recibe la hora, se hacen validaciones,
# se llaman las funciones y se concatenan los valores.
hora = input()
if hora.__len__() == 6 or hora.__len__() == 7  :    #valida la longitud correcta de la hora
    if hora[-2:] == "am" or hora[-2:] == "pm":      #valida que se indique si es am ó pm
        if int(hora[-4:-2]) < 60:                   #valida que los minutos esten dados en la cantidad correcta
            if int(hora[-7:-5]) < 13:               #valida que las horas esten dadas en la cantidad correcta
                if hora[-7:-5]=="12" and hora[-4:-2]=="00" and hora[-2:]=="pm": #valida si es medio dia
                    print("Es Medio Dia")
                elif hora[-7:-5]=="12" and hora[-4:-2]=="00" and hora[-2:]=="am":           #valida si es medianoche
                    print("Es Media Noche")
                elif hora[-4:-2]=="00":                                                     #valida si las horas son en punto
                    print("Son"+ horas(hora[-7:-5])+" "+ "En Punto" + " de la " + horario(hora[-2:]))
                elif int(hora[-7:-5])>5 and int(hora[-7:-5]) < 12 and hora[-2:]=="pm":      #valida si es en la noche o tarde
                        print("Son"+ horas(hora[-7:-5])+" "+ minutos(hora[-4:-2]) + " de la " + "Noche")
                else:
                    print("Son"+ horas(hora[-7:-5])+" "+ minutos(hora[-4:-2]) + " de la " + horario(hora[-2:]))
            else:
                print("Ingrese horas validas entre 0 y 12")
        else:
            print("Ingrese minutos validos menores a 60 y mayores a 0")
    else:
        print("Ingrese si la hora es 'am' ó 'pm', por ejemplo: 10:07am ó 3:57pm ")
else : 
    print("Ingrese una hora en el formato de 12 Hrs, por ejemplo: 10:07am ó 3:57pm ")


