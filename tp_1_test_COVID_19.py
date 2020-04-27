#   TITULOS
#----------------------------------------------------
print('\x1b[1;30m                                                                                                ')
print('                          +-----------------------------------------------------+                         ')
print('                          |       Bienvenido al TEST RÁPIDO de COVID-19         |                         ')
print('                          +-----------------------------------------------------+                         ')
print('\x1b[1;34m \nDebido a la creciente preocupación surgida por el COVID-19, hemos creado este test '
      'rápido para ayudarte                                                                                      ')
print('a ti y a tus seres queridos a detectar a tiempo cualquier síntoma o indicador de esta enfermedad,         ')
print('de manera que puedan recibir atención adecuada y pertinente.\n                                            ')
print('\x1b[1;30m                                                                                                ')
print('                                         INICIAR EL TEST:\n                                               ')
print('-' * 100)

print('\x1b[1;34m' + '¡¡¡¡PREPARADO PARA COMENZAR!!!')

# CARGA DE DATOS
#----------------------------------------------------
edad = int(input('Ingrese su edad :') )
temperatura = float(input('Ingrese la temperatura Corporal :'))
neumonia = int(input('Tiene Neumonia ya Evidenciada ? \x1b[1;31m (1 para SI o 2 para NO, y luego presione Enter)\n'))

#  PROCESOS
#----------------------------------------------------
casoSospechoso = ''
casoAutoctono =''
casoNoSospechosoMayor = ''
casoNoSospechoso = ''
cont=0
if neumonia == 1 :
     casoSospechoso = 'SOSPECHOSO'
else:
     if temperatura <=37:
        if edad >60 :
            casoNoSospechosoMayor = 'NO SOSPECHOSO ,Le recordamos que usted pertenece a un grupo de riesgo porque es mayor de 60 años'
        else:
            casoNoSospechoso = 'NO SOSPECHOSO ,cuidese y quedese en casa'
     else:
            input('Por favor presione la tecla INTRO ')
            print('\x1b[1;30m                                                                                                ')
            print('                          +-----------------------------------------------------+                         ')
            print('                          |                      SINTOMAS                       |                         ')
            print('                          +-----------------------------------------------------+                         ')

            print('\x1b[1;31m' +'1 para SI o 2 para  NO, y luego presione Enter\n')

            print('\x1b[1;30m-' * 100)
            T = int(input('Tiene tos :')) #TOS
            DG=int(input('Tiene Odinofagia(Dolor de garganta) :'))#DOLOR DE GARGANTA
            DR =int(input('Tiene Dificultad Respiratoria :')) #DIFICULTAD RESPIRATORIO
            if T==1 :
               cont+=1
            if DG ==1:
               cont+=1
            if DR ==1:
               cont+=1
            if cont >=1:
                 print('\x1b[1;30m-' * 100)
                 ps = int(input('Es Personal de Salud :'))
                 if ps == 1:
                     casoSospechoso='SOSPECHOSO'
                 else:

                     cc =int( input('Estuvo en contacto con casos confirmados en los ultimos 14 dias?:'))
                     ve= int(input('Viajo al Exterior en los ultimos 14 dias? :'))
                     ctc =int(input('Estuvo en alguna zonas nacionales con casos de transmision local confirmados en los ultimos 14 dias? :'))

                     if  cc == 1 or ve == 1 or ctc == 1:
                         if cont >= 2 and  ctc == 1 and ve == 2 and cc == 2: #CASO AUTOCTONO
                            casoAutoctono =' Y AUTOCTONO'
                            casoSospechoso='SOSPECHOSO'
                         else:
                              casoSospechoso='SOSPECHOSO'
                     else:
                         if edad >60 :
                            casoNoSospechosoMayor = 'NO SOSPECHOSO ,Le recordamos que usted pertenece a un grupo de riesgo porque es mayor de 60 años'
                         else:
                            casoNoSospechoso = 'NO SOSPECHOSO ,cuidese y quedese en casa'
            else:
                 if edad >60 :
                    casoNoSospechosoMayor = 'NO SOSPECHOSO ,Le recordamos que usted pertenece a un grupo de riesgo porque es mayor de 60 años'
                 else:
                    casoNoSospechoso = 'NO SOSPECHOSO ,cuidese y quedese en casa'

  #Impresión de resultados .
#----------------------------------------------------
print('\x1b[1;30m   \n RESULTADO ')
print('='*20)
print('\x1b[1;34m-' * 100)
print(' Ud es un caso :' ,casoNoSospechoso,casoNoSospechosoMayor,casoSospechoso,casoAutoctono )
print('-' * 100)
print()

print('\x1b[1;35mGRACIAS POR CONSULTAR!!!!---->>>>>QUEDATE EN CASA,CUIDANDOTE NOS CUIDAMOS TODOS !!!!!!\n')
print('\x1b[1;30m-' * 100)

opcion = input('Presione la tecla "1" para información sobre los programadores)\n')
if opcion == '1':
        print('\nPrograma (T.P.1) diseñado por los Alumnos:  \nDel Castillo - LN.:53067-1k12 \nFlores - LN.:56731-1k16 ')
        print('Cátedra de Algoritmos y Estructuras de Datos 2020 - UTN Córdoba')

