import datetime
import time
import sys 
from tabulate import tabulate
import pandas as pd
import sqlite3 as sql
from sqlite3 import Error
import csv
from openpyxl import Workbook


try:
    with sql.connect("Evidencia_3.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Pacientes (clave INTEGER PRIMARY KEY, apellidoPaterno TEXT NOT NULL, apellidoMaterno TEXT, nombres TEXT NOT NULL, fechaNacimiento timestamp NOT NULL, sexoPaciente TEXT NOT NULL);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Citas (folio INTEGER PRIMARY KEY AUTOINCREMENT, clave_paciente INTEGER, fechaCita timestamp NOT NULL, turno TEXT NOT NULL, edad INTEGER, peso REAL, estatura REAL, horaLlegada timestamp , presionArterial TEXT, diagnostico TEXT, FOREIGN KEY (clave_paciente) REFERENCES tb_Pacientes(clave));")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

def menu_Principal():
    print()
    print('---------------------- CONSULTORIO ----------------------')
    print('---------------------- MENU PRINCIPAL ----------------------')
    print('1. Registro de pacientes')
    print('2. Citas')
    print('3. Consultas y reportes')
    print('4. Salir del sistema')

clave_paciente = None 

while True:
    while True:
        menu_Principal()
        tupla_opciones = (1, 2, 3, 4)
        opcion_menuPrincipal_str = input('Selecciona la opcion a realizar: ')
        if opcion_menuPrincipal_str.isdigit():
            opcion_menuPrincipal = int(opcion_menuPrincipal_str)
            if opcion_menuPrincipal in tupla_opciones:
                print('Se registro correctamente')
                print()
                print()
                break
            else:
                print('Error. Seleccionar una opcion valida del menu. Intente de neuvo.')
                print()
        else:
            print('Error. Seleccionar el numero de la opcion. Intente de nuevo')
            print()

    if opcion_menuPrincipal == 1:
        print()    
        print('----------------- REGISTRO DE PACIENTE -----------------')
        while True:
            try:
                primer_apellido_paciente = input('Proporciona tu apellido Paterno: ').strip().upper()
                if primer_apellido_paciente == '':
                    raise ValueError('Error. El dato no puede ser omitido.')
                elif not primer_apellido_paciente.replace(' ', '').isalpha():
                    raise ValueError(f'El dato ingresado "{primer_apellido_paciente}" no contiene únicamente letras o espacios.')
                else:
                    print('El dato ingresado se registró correctamente.')
                    print()
                    break
            except ValueError as error:
                print(error)
        while True:
            segundo_apellido_paciente = input('Proporciona tu apellido Materno (o presiona Enter para omitir): ').strip().upper()
            if segundo_apellido_paciente == '':
                segundo_apellido_paciente = 'N/A'
                print('El dato se ha omitido.')
                break  
            elif not segundo_apellido_paciente.replace(' ', '').isalpha():
                print(f'El dato ingresado "{segundo_apellido_paciente}" no contiene únicamente letras.')
            else:
                print('El dato ingresado se registró correctamente.')
                break
        while True:
            print()
            nombres_paciente = input('Proporciona tus nombres: ').strip().upper()
            
            if nombres_paciente == '':
                print('Error: El dato no puede ser omitido.')
            elif not nombres_paciente.replace(' ', '').isalpha():
                print(f'El dato ingresado "{nombres_paciente}" no contiene únicamente letras.')
            else:
                print('El dato ingresado se registró correctamente.')
                print()
                break
        while True:
            fecha_nacimiento_paciente_str = input('Ingrese su fecha de nacimiento en el formato mm/dd/aaaa: ')
            
            if fecha_nacimiento_paciente_str == '':
                print('Error. La fecha de nacimiento no puede ser omitida.')
            else:
                try:
                    fecha_nacimiento_paciente = datetime.datetime.strptime(fecha_nacimiento_paciente_str, '%m/%d/%Y').date()
                    fecha_actual = datetime.date.today()
                    
                    if fecha_nacimiento_paciente >= fecha_actual:
                        print('Error. La fecha de nacimiento no es valida.')
                    else:
                        print('El dato ingresado se registró correctamente.')
                        print()
                        break
                except ValueError:
                    print('Error: El formato de fecha ingresado no es válido. Por favor, ingrese la fecha en el formato mm/dd/aaaa.')
        while True:
            sexo_paciente = str(input('Ingrese su sexo (H, M o N): ')).upper()
            if sexo_paciente.isalpha():
                if sexo_paciente == 'H' or sexo_paciente == 'M' or sexo_paciente == 'N':
                    if sexo_paciente == 'H':
                        sexo_paciente_final = 'HOMBRE'
                    elif sexo_paciente == 'M':
                        sexo_paciente_final = 'MUJER'
                    elif sexo_paciente == 'N' or '':
                        sexo_paciente_final = 'NO CONTESTO'
                    print('El dato ingresado se registró correctamente.')
                    break
                    
                else:
                    print('ERROR. Ingrese una opcion valida (H, M o N)')
            else:
                print(f'ERROR. El valor ingresado {sexo_paciente} no es valido. Intente de nuevo')        
        try:
            with sql.connect("Evidencia_3.db") as conn:
                mi_cursor = conn.cursor()
                datos = primer_apellido_paciente, segundo_apellido_paciente, nombres_paciente, fecha_nacimiento_paciente, sexo_paciente_final
                mi_cursor.execute('INSERT INTO Pacientes (apellidoPaterno, apellidoMaterno, nombres, fechaNacimiento, sexoPaciente) VALUES (?,?,?,?,?)', datos)
                mi_cursor.execute('SELECT last_insert_rowid()') 
                clave_paciente = mi_cursor.fetchone()[0] 
        except sql.Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            conn.close()
        print('El paciente se ha registrado correctamente.')
        print()
        print('Datelles del paciente:')
        print(f'Clave: {clave_paciente}')
        print(f'Apellido Paterno: {primer_apellido_paciente}')
        print(f'Apellido Materno: {segundo_apellido_paciente}')
        print(f'Nombres: {nombres_paciente}')
        print(f'Fecha de nacimiento: {fecha_nacimiento_paciente}')
        print(f'Sexo del paciente: {sexo_paciente_final}')
        print()
    if opcion_menuPrincipal == 2:
        while True:
            print()
            print('----------------- MENU DE CITAS -----------------')
            print('1. Programacion de citas')
            print('2. Realizacion de citas programadas')
            print('3. Cancelacion de citas')
            print('4. Salir del submenu')
            while True:
                try:
                    tupla_citas = (1, 2, 3, 4)
                    opcion_submenuCitas = int(input('Selecciona la opcion del menu. Solo el numero: '))
                    if opcion_submenuCitas in tupla_citas:
                        print('Opcion valida')
                        break
                    else:
                        print('ERROR. Selecciona una opcion valida del menu. Intenta de nuevo')
                except ValueError:
                    print('ERROR. El valor ingresado no es numerico. Intenta de nuevo')
            if opcion_submenuCitas == 1:
                print('----------------- PROGRAMACION DE CITAS -----------------\n')
                claves_in_list = []
                print('------------------------- CLAVES DISPONIBLES ------------------------- ')
                try:
                    with sql.connect("Evidencia_3.db") as conn:
                        mi_cursor = conn.cursor()
                        mi_cursor.execute('SELECT clave, apellidoPaterno, apellidoMaterno, nombres FROM Pacientes')
                        claves_disponibles = mi_cursor.fetchall()
                        print(f'{"Clave":<10} {"Apellido Paterno":<20} {"Apellido Materno":<20} {"Nombres":<20}')
                        print('-' * 70)
                        for clave, apellidoPaterno, apellidoMaterno, nombres in claves_disponibles:
                            print(f'{clave:<10} {apellidoPaterno:<20} {apellidoMaterno:<20} {nombres:<20}\n')
                            claves_in_list.append(clave)
                except sql.Error as e:
                    print(e)
                except:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                    conn.close()
                while True:
                    try:
                        clave_seleccionada = int(input('Ingrese la clave a registrar: '))
                        if clave_seleccionada in claves_in_list:
                            break
                        else:
                            print('ERROR. Selecciona una clave existente')
                    except ValueError:
                        print('ERROR. La clave debe ser numerica. Intente de nuevo.')
                    except:
                        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                dias_habiles = datetime.timedelta(days=60)
                fecha_actual_cita = datetime.date.today()
                while True:
                    fecha_cita_str = input('Fecha de la cita (En el siguiente formato (mm/dd/aaaa)): ')
                    if fecha_cita_str == '':
                        print('El dato de fecha no puede ser omitido.')
                        continue
                    try:
                        fecha_cita = datetime.datetime.strptime(fecha_cita_str, '%m/%d/%Y').date()
                        if fecha_cita <= fecha_actual_cita:
                            print('La fecha no es válida. Debe ser posterior al día actual.')
                            continue
                        if fecha_cita > fecha_actual_cita + dias_habiles:
                            print('La fecha no puede ser mayor a 60 días.')
                            continue
                        if fecha_cita.weekday() == 6:
                            recorrer_cita_opcion = input('La fecha de la cita cae en domingo. ¿Desea recorrer la cita un dia antes, día Sabado? (SI/NO): ').upper()
                            if recorrer_cita_opcion == 'SI':
                                fecha_cita = fecha_cita - datetime.timedelta(days=1)
                            else:
                                continue
                        print('La fecha de la cita es válida:', fecha_cita)
                        print()
                        break
                    except ValueError:
                        print('Error: El formato de fecha ingresado no es válido. Por favor, ingrese la fecha en el formato mm/dd/aaaa.')

                while True:
                    tupla_turno = {1, 2, 3}
                    print('Turno #1. Mañana')
                    print('Turno #2. Mediodía')
                    print('Turno #3. Tarde')
                    print()
                    turno_cita_str = input('Favor elegir el turno de la cita. (Solo el numero.): ')
                    if turno_cita_str == '':
                        print('El valor no puede omitirse')
                    if turno_cita_str.isdigit():
                        turno_cita = int(turno_cita_str)
                        if turno_cita in tupla_turno:
                            if turno_cita == 1:
                                turno_str = 'Mañana'
                            elif turno_cita == 2:
                                turno_str = 'Mediodía'
                            else:
                                turno_str = 'Tarde'
                            print(f'El turno de la cita es de {turno_str}.')
                            break
                        else:
                            print('Error. Intente de nuevo. ')

                try:
                    with sql.connect("Evidencia_3.db") as conn:
                        mi_cursor = conn.cursor()
                        datos = (clave_seleccionada,fecha_cita, turno_str)
                        mi_cursor.execute('INSERT INTO Citas (clave_paciente, fechaCita, turno) VALUES (?,?,?)' , datos)
                except sql.Error as e:
                    print(f'ERROR. Base de datos {e}')
                except:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                    conn.close()    
                try:
                    with sql.connect('Evidencia_3.db') as conn:
                        mi_cursor = conn.cursor()
                        mi_cursor.execute('SELECT folio, clave_paciente, fechaCita, edad, turno FROM Citas WHERE clave_paciente = ? AND fechaCita = ? AND turno = ?', (clave_seleccionada, fecha_cita, turno_str))
                        datos_cita = mi_cursor.fetchone()
                        if datos_cita:
                            folio, clave_paciente, fechaCita, edad, turno = datos_cita
                            mi_cursor.execute('SELECT apellidoPaterno, apellidoMaterno, nombres, fechaNacimiento FROM Pacientes WHERE clave = ?', (clave_paciente,))
                            detalles_paciente = mi_cursor.fetchone()
                            apellido_paterno, apellido_materno, nombres, fecha_nacimiento = detalles_paciente
                            print('La cita se ha registrado correctamente.')
                            print()
                            print('Detalles de la cita:')
                            print(f'Clave del Paciente: {clave_paciente}')
                            print(f'Folio de la cita: {folio}')
                            print(f'Apellido Paterno: {apellido_paterno}')
                            print(f'Apellido Materno: {apellido_materno}')
                            print(f'Nombres: {nombres}')
                            print(f'Fecha de Nacimiento: {fecha_nacimiento}')
                            print(f'Fecha de Cita: {fechaCita}')
                            print(f'Turno de Cita: {turno}')
                            print()
                        else:
                            print('No se encontraron datos para la cita recién registrada.')
                except sql.Error as e:
                    print(f'ERROR. Base de datos {e}')
                except:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                    conn.close()
            if opcion_submenuCitas == 2:
                folios_in_list = []
                try:
                    with sql.connect('Evidencia_3.db') as conn:
                        mi_cursor = conn.cursor()
                        mi_cursor.execute('SELECT folio FROM Citas')
                        folios_disponibles = mi_cursor.fetchall()  # Cambio aquí
                        print('Folios disponibles:')
                        for folio in folios_disponibles:
                            print(f'\t-{folio[0]}-')  # Accedemos al primer elemento de la tupla
                            folios_in_list.append(folio[0])
                except sql.Error as e:
                    print(f'ERROR. En la Base de datos: {e}')
                except:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                finally:
                    conn.close()

                hora_actual = datetime.datetime.now()
                hora_actual_str = hora_actual.strftime("%H:%M:%S")
                while True:
                    try:
                        folio_seleccionado = int(input('Ingrese el folio del paciente: '))
                        if folio_seleccionado in folios_in_list:
                            break
                        else:
                            print('ERROR. Elige un folio existente')
                    except ValueError:
                        print('ERROR. El folio debe ser numerico. Intente de nuevo.')
                    except:
                        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

                while True:
                    try:
                        peso_paciente = float(input('Ingrese el peso en kilogramos del paciente: '))
                        if peso_paciente <= 0:
                            print('Error: El peso debe ser un valor numérico positivo.')
                        else:
                            print(f'Peso registrado correctamente: {peso_paciente} ')
                            print()
                            break
                    except ValueError:
                        print('Error: Por favor, ingrese un valor numérico válido para el peso.')
                    

                while True:
                    try:
                        estatura_paciente = float(input('Ingrese la estatura en centímetros del paciente: '))
                        if estatura_paciente <= 0:
                            print('Error: La estatura debe ser un valor numérico positivo.')
                        else:
                            print('Estatura registrada correctamente:', estatura_paciente)
                            print()
                            break
                    except ValueError:
                        print('Error: Por favor, ingrese un valor numérico válido para la estatura.') 
                    break

                while True:
                    sistolica_str = input('Ingrese el valor de la sistolica: ')
                    if sistolica_str == '':
                        print('ERROR. El valor no se puede omitir. Intente de nuevo.')
                    else:
                        if sistolica_str.isdigit():
                            print(f'El valor de la sistolica regirstrado correctamente: {sistolica_str} \n')
                            break
                        else:
                            print('ERROR. Ingrese un valor numerico. Intente de nuevo.')

                while True:
                    asistolica_str = input('Ingresa el valor de la diastolica: ')
                    if asistolica_str == '':
                        print('ERROR. El valor no se puede omitir. Intente de nuevo')
                    else:
                        if asistolica_str.isdigit():
                            print(f'Valor de las diastolica registrado correctamente: {asistolica_str} \n')
                            break
                        else:
                            print('ERROR. Imgrese un valor numerico. Intente de nuevo')
                presion_arterial = f'{sistolica_str.zfill(3)}/{asistolica_str.zfill(3)}'
                
                while True:
                    print('El diagnostico no puede excederse de los 200 caracteres')
                    diagnostico = input('Diagnostico: ')
                    if len(diagnostico) == 0:
                        print('ERROR. El diagnostico no puede omitirse. Intente de nuevo.')
                        continue
      