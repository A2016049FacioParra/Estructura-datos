import datetime
import time
import sys 
import csv
from tabulate import tabulate
import pandas as pd

pacientes = dict()
citas = dict()

clave_paciente = 1
folio_paciente = 100
pregunta_folio = None
citas_en_periodo = None

claves = pacientes.keys()
folios_citas = citas.keys()

try:
    with open('Pacientes.csv', 'r', newline='') as archivo_pacientes:
        lector_pacientes = csv.DictReader(archivo_pacientes)
        for row in lector_pacientes:
            clave = int(row['Clave'])
            fecha_nacimiento = datetime.datetime.strptime(row['Fecha de nacimiento'], '%Y-%m-%d').date()
            pacientes[clave] = {
                'PRIMER APELLIDO': row['Apellido Paterno'],
                'SEGUNDO APELLIDO': row['Apellido Materno'],
                'NOMBRES': row['Nombres'],
                'FECHA DE NACIMIENTO': fecha_nacimiento,
                'SEXO': row['Sexo']
            }
except FileNotFoundError:
    print("No se encontró el archivo 'Pacientes.csv'.")
except Exception as e:
    print(f"Error al leer el archivo 'Pacientes.csv': {e}")

try:
    with open('Citas.csv', 'r', newline='') as archivo_citas:
        lector_citas = csv.DictReader(archivo_citas)
        for row in lector_citas:
            folio = int(row['Folio'])
            fecha_nacimiento = datetime.datetime.strptime(row['Fecha de nacimiento'], '%m/%d/%Y').date()
            fecha_cita = datetime.datetime.strptime(row['Fecha de cita'], '%m/%d/%Y').date()
            citas[folio] = {
                'Clave del paciente': int(row['Clave del paciente']),
                'Apellido Paterno': row['Apellido Paterno'],
                'Apellido Materno': row['Apellido Materno'],
                'Nombres': row['Nombres'],
                'Fecha de Nacimiento': fecha_nacimiento,
                'Edad': int(row['Edad']),
                'Fecha de Cita': fecha_cita,
                'Turno de Cita': row['Turno de cita'],
                'Peso del Paciente': float(row['Peso del paciente']) if row['Peso del paciente'] else None,
                'Estatura del Paciente': float(row['Estatura del paciente']) if row['Estatura del paciente'] else None,
                'Hora de Llegada': row['Hora de llegada'],
                'Presion Arterial': row['Presion Arterial'],
                'Diagnostico': row['Diagnostico']
            }
except FileNotFoundError:
    print("No se encontró el archivo 'Citas.csv'.")
except Exception as e:
    print(f"Error al leer el archivo 'Citas.csv': {e}")




def menu_Principal():
    print()
    print('---------------------- CONSULTORIO ----------------------')
    print('---------------------- MENU PRINCIPAL ----------------------')
    print('1. Registro de pacientes')
    print('2. Citas')
    print('3. Consultas y reportes')
    print('4. Salir del sistema')

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
        
        if pacientes == dict():
            None
        else:    
            clave_paciente = max(pacientes) + 1
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
            
        pacientes[clave_paciente] = {
                                    'PRIMER APELLIDO': primer_apellido_paciente,
                                    'SEGUNDO APELLIDO': segundo_apellido_paciente,
                                    'NOMBRES': nombres_paciente,
                                    'FECHA DE NACIMIENTO': fecha_nacimiento_paciente,
                                    'SEXO': sexo_paciente_final
                                    }
        
        print('El paciente se ha registrado correctamente.')
        print()
        print('Datelles del paciente:')
        print(f'Clave: {clave_paciente}')
        print(f'Apellido Paterno: {pacientes[clave_paciente]["PRIMER APELLIDO"]}')
        print(f'Apellido Materno: {pacientes[clave_paciente]["SEGUNDO APELLIDO"]}')
        print(f'Nombres: {pacientes[clave_paciente]["NOMBRES"]}')
        print(f'Fecha de nacimiento: {pacientes[clave_paciente]["FECHA DE NACIMIENTO"]}')
        print(f'Sexo del paciente: {pacientes[clave_paciente]["SEXO"]}')
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
                if citas == dict():
                    None
                else:
                    folio_paciente = max(citas) + 1
                if pacientes == dict():
                    print()
                    print('<<ERROR. NO HAY PACIENTES REGISTRADOS.>>')
                    print()
                else:
                    print('----------------- PROGRAMACION DE CITAS -----------------')
                    print('-- Claves Disponibles --')
                    for clave in claves:  
                        print(f'    -{clave}-')
                    while True:
                        print()
                        preguntar_clave_str = input('Cual es la clave del paciente: ')
                        if preguntar_clave_str.isdigit():
                            preguntar_clave = int(preguntar_clave_str)
                            if preguntar_clave in claves:
                                print('Paciente encontrado')
                                print('Datos del paciente:')
                                print(f'Clave: {preguntar_clave}')
                                print(f'Apellido Paterno: {pacientes[preguntar_clave]["PRIMER APELLIDO"]}')
                                print(f'Apellido Materno: {pacientes[preguntar_clave]["SEGUNDO APELLIDO"]}')
                                print(f'Nombres: {pacientes[preguntar_clave]["NOMBRES"]}')
                                print(f'Fecha de nacimiento: {pacientes[preguntar_clave]["FECHA DE NACIMIENTO"]}')
                                print()
                                break
                            else:
                                print('Paciente no encontrado. Intente de nuevo')
                        else:
                            print('Por favor, ingrese un número válido para la clave del paciente.')
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
                    edad =  fecha_cita.year - fecha_nacimiento_paciente.year - ((fecha_cita.month, fecha_cita.day) < (fecha_nacimiento_paciente.month, fecha_nacimiento_paciente.day))


                    citas[folio_paciente] = {
                                            'Clave del paciente':preguntar_clave,
                                            'Apellido Paterno': pacientes[preguntar_clave]["PRIMER APELLIDO"],
                                            'Apellido Materno': pacientes[preguntar_clave]["SEGUNDO APELLIDO"],
                                            'Nombres': pacientes[preguntar_clave]["NOMBRES"],
                                            'Fecha de Nacimiento': pacientes[preguntar_clave]["FECHA DE NACIMIENTO"],
                                            'Edad': edad,
                                            'Fecha de Cita': fecha_cita,
                                            'Turno de Cita': turno_str
                                            }

                    print('La cita se ha registrada correctamente.')
                    print()
                    print('Detalles de la cita:')
                    print(f'Clave del Paciente: {preguntar_clave}')
                    print(f'Folio de la cita: {folio_paciente}')
                    print(f'Apellido Paterno: {citas[folio_paciente]["Apellido Paterno"]}')
                    print(f'Apellido Materno: {citas[folio_paciente]["Apellido Materno"]}')
                    print(f'Nombres: {citas[folio_paciente]["Nombres"]}')
                    print(f'Fecha de Nacimiento: {citas[folio_paciente]["Fecha de Nacimiento"]}')
                    print(f'Fecha de Cita: {citas[folio_paciente]["Fecha de Cita"]}')
                    print(f'Turno de Cita: {citas[folio_paciente]["Turno de Cita"]}')
                    print()
                    

            if opcion_submenuCitas == 2:
                if citas == dict():
                    print()
                    print('<<ERROR. NO HAY CITAS REGISTRADAS>>')
                    print()
                else:
                    print(f'Folios disponibles:')
                    for folio in folios_citas:
                        print(f'\t-{folio}- ')
                        print()
                    hora_actual = datetime.datetime.now()
                    hora_actual_str = hora_actual.strftime("%H:%M:%S")
                    while True:
                        pregunta_folio1 = input('Ingrese el folio del paciente: ')
                        if pregunta_folio1.isdigit():
                            pregunta_folio = int(pregunta_folio1)
                            if pregunta_folio in folios_citas:
                                print('Folio encontrado.')
                                break     
                            else:
                                print('ERROR. FOLIO NO ENCONTRADO. INTENTA DE NUEVO')
                                print()        
                        else:
                            print(f'ERROR. EL DATO -{pregunta_folio1}- NO ES UN NUMERO. INTENTA DE NUEVO  ')
                            print()

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

                        if len(diagnostico) > 200:
                            print('ERROR. El diagnostico ingresado excede del limite. Intente de nuevo.')
                            continue

                        print('Diagnostico valido')
                        break

                    citas[pregunta_folio].update({
                        'Peso del Paciente': peso_paciente,
                        'Estatura del Paciente': estatura_paciente,
                        'Hora de Llegada': hora_actual_str,
                        'Presion Arterial': presion_arterial,
                        'Diagnostico': diagnostico
                        })
                    
                    print('Datos de la cita:')
                    print(f'Folio de la cita: {pregunta_folio}')
                    print(f'Nombre del paciente: {citas[pregunta_folio]["Nombres"]}')
                    print(f'Apellido Paterno: {citas[pregunta_folio]["Apellido Paterno"]}')
                    print(f'Apellido Materno: {citas[pregunta_folio]["Apellido Materno"]}')
                    print(f'Peso del Paciente: {peso_paciente} kilogramos')
                    print(f'Estatura del Paciente: {estatura_paciente} centimetros')
                    print(f'Presion arterial del paciente: {presion_arterial} ')
                    print(f'Diagnostico: \n {diagnostico}')
                    print(f'Hora de Llegada: {hora_actual_str}')
                    print()
                    
            
            if opcion_submenuCitas == 3:
                while True:
                    while True:
                        print('----------------- CANCELACION DE CITAS -----------------')
                        print('1. Busqueda por fecha.')
                        print('2. Busqueda por paciente')
                        print('3. Salir')
                        try:
                            tupla_cancelacion = (1, 2, 3)
                            opcion_cancelacion = int(input('Selecciona la opcion del menu. Solo el numero: '))
                            if opcion_cancelacion in tupla_cancelacion:
                                print('Opcion valida')
                                break
                            else:
                                print('ERROR. Selecciona una opcion valida del menu. Intenta de nuevo')
                        except ValueError:
                            print('ERROR. El valor ingresado no es numerico. Intenta de nuevo')

                    if opcion_cancelacion == 1:
                        print('----------------- BUSQUEDA POR FECHA -----------------')
                        while True:
                            try:
                                busqueda_fecha_cancelacion_str = input('Ingrese la fecha de la cita a buscar, en el formato (mm/dd/yyyy): ')
                                busqueda_fecha_cancelacion = datetime.datetime.strptime(busqueda_fecha_cancelacion_str, '%m/%d/%Y').date()
                                break
                            except ValueError:
                                print('ERROR. El formato de la fecha no es el solicitado. Intente de nuevo')

                        citas_en_busqueda = [(folio, cita) for folio, cita in citas.items() if cita['Fecha de Cita'] == busqueda_fecha_cancelacion]
                        
                        if citas_en_busqueda:
                            print((f'Citas programadas para el {busqueda_fecha_cancelacion}'))
                            for folio, cita in citas_en_busqueda:
                                print(f'Folio del paciente: {folio}')
                                print(f'Nombre del paciente: {cita["Nombres"]}')
                                print(f'Apellido Paterno: {cita["Apellido Paterno"]}')
                                print(f'Apellido Materno: {cita["Apellido Materno"]}')
                                print(f'Turno de la cita: {cita["Turno de Cita"]} \n')
                        else:
                            print('No hay citas programadas para la fecha indicada.')
                        
                        while True:
                            folio_cancelar_str = input('Ingrese el folio a cancelar: ')
                            if folio_cancelar_str.isdigit():
                                folio_cancelar = int(folio_cancelar_str)
                                if folio_cancelar in citas:
                                    seguridad = input('¿Estás seguro de querer eliminar la cita (SI/NO): ').upper()
                                    if seguridad == 'SI':
                                        del citas[folio_cancelar]
                                        print('La cita ha sido eliminada exitosamente.')
                                        break
                                    else:
                                        print('Operación de eliminación de cita cancelada.')
                                        continue
                                else:
                                    print('El folio ingresado no corresponde a ninguna cita. Intente de nuevo.')
                            else:
                                print('ERROR. El valor ingresado no es numérico. Intenta de nuevo.')

                    if opcion_cancelacion == 2:
                        citas_pendientes = any(cita['Fecha de Cita'] >= datetime.date.today() for cita in citas.values())
                        if not citas_pendientes:
                            print('NO HAY CITAS PENDIENTES POR REALIZAR')
                        else:
                            print('---------------------- BUSQUEDA POR PACIENTE ----------------------')
                            print('Listado de los pacientes')
                            if citas:
                                for folio, datos in citas.items():
                                    if datos['Fecha de Cita'] > datetime.date.today():
                                        print(f'Folio del paciente: {folio}')
                                        print(f'Nombre del paciente: {datos.get("Nombres", "")}')
                                        print(f'Apellido Paterno: {datos.get("Apellido Paterno", "")}')
                                        print(f'Apellido Materno: {datos.get("Apellido Materno", "")} \n')
                            else:
                                print('No hay citas por realizar.')

                        while True:
                            try:
                                folio_cancelar = int(input('Ingrese el folio a eliminar: '))
                                if folio_cancelar in citas:
                                    print('Detalles de la cita a cancelar')
                                    cita_cancelada = citas[folio_cancelar]
                                    print(f'Fecha de la cita cancelada: {cita_cancelada.get("Fecha de Cita", "")}')
                                    print(f'Turno de la cita: {cita_cancelada.get("Turno de Cita", "")}')
                                    seguridad_2 = input('¿Estás seguro de querer eliminar la cita? (SI/NO): ').upper()
                                    if seguridad_2 == 'SI':
                                        citas.pop(folio_cancelar)
                                        print('La cita del paciente ha sido cancelada exitosamente')
                                        break
                                    elif seguridad_2 == 'NO':
                                        print('Operación de eliminación de cita cancelada')
                                        break
                                else:
                                    print('ERROR. El folio ingresado no corresponde a ninguna cita.')
                            except ValueError:
                                print('ERROR. El folio ingresado debe ser numérico. Intente de nuevo.')

                    if opcion_cancelacion == 3:
                        print('Saliendo del submenu')
                        break

            if opcion_submenuCitas == 4:
                print('Saliendo del submenu de citas')
                print()
                break

    if opcion_menuPrincipal == 3:
        while True:
            print()
            print('---------------------- MENU REPORTES Y CONSULTAS ----------------------')
            print('1. Reportes por citas.')
            print('2. Reportes de pacientes.')
            print('3. Salir del menu.')
            tupla_1 = (1, 2, 3)
            while True:
                opcion_menu4_1 = input('Selecciona la opcion. Solo el numero:  ')
                if opcion_menu4_1.isdigit():
                    opcion_menu_4 = int(opcion_menu4_1)
                    if opcion_menu_4 in tupla_1:
                        print('Se registro correctamente.')
                        print()
                        break
                    else:
                        print('ERROR. Selecciona una opcion valida en el menu.')
                else:
                    print(f'ERROR. El dato {opcion_menu4_1} no es numerico. Intenta de nuevo')

            if opcion_menu_4 == 1:
                while True:
                    print('---------------------- SUBMENU REPORTE DE CITAS ----------------------')
                    print('1. Reporte por periodo.')
                    print('2. Reporte de pacientes.')
                    print('3. Salir del menu')
                    while True:
                        opcion_1 = input('Selecciona la opcion del menu. Solo el numero:  ')
                        if opcion_1.isdigit():
                            opcion_submenu_1 = int(opcion_1)
                            if opcion_submenu_1 in tupla_1:
                                print('Se registro correctamente.')
                                break
                            else:
                                print('ERROR. Selecciona una opcion valida del menu')
                        else:
                            print(f'ERROR. El dato {opcion_1} no es numerio. Intenta de nuevo.')

                    if opcion_submenu_1 == 1:
                        
                        while True:
                            try:
                                fecha_inicial_str = input("Introduzca la fecha inicial (Valor de la fecha en el formato mm/dd/aaaa): ")
                                fecha_inicial = datetime.datetime.strptime(fecha_inicial_str, "%m/%d/%Y").date()
                                break
                            except ValueError:
                                print("El dato debe estar en el formato proporcionado")
                                continue

                        while True:
                            try:
                                fecha_fin_str = input("Introduzca la fecha final (Valor de la fecha en el formato mm/dd/aaaa): ")
                                fecha_fin = datetime.datetime.strptime(fecha_fin_str, "%m/%d/%Y").date()
                                if fecha_fin > fecha_inicial:
                                    break
                                else:
                                    print("La fecha inicial no debe ser mayor a la final. Intente de nuevo")
                            except ValueError:
                                print("El dato debe estar en el formato proporcionado")
                                continue
                        citas_en_periodo = []
                        for folio, cita in citas.items():
                            fecha_cita = cita["Fecha de Cita"]
                            if fecha_inicial <= fecha_cita <= fecha_fin:
                                citas_en_periodo.append((folio, cita))

                        if citas_en_periodo:
                            print("\nCitas programadas en el período seleccionado: \n")
                            headers = ["Folio", "Nombre", "Apellido Paterno", "Apellido Materno", "Fecha de Nacimiento", "Edad", "Fecha de Cita", "Turno", "Peso del Paciente", "Estatura del Paciente", "Presión Arterial"]
                            data = []
                            for folio, cita in citas_en_periodo:
                                nombre = cita['Nombres']
                                apellido_paterno = cita['Apellido Paterno']
                                apellido_materno = cita['Apellido Materno']
                                fecha_nacimiento = cita['Fecha de Nacimiento']
                                edad = cita['Edad']
                                fecha_cita = cita['Fecha de Cita']
                                turno = cita['Turno de Cita']
                                peso_paciente = cita['Peso del Paciente']
                                estatura_paciente = cita['Estatura del Paciente']
                                presion_arterial = cita['Presion Arterial']
                                data.append([folio, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, edad, fecha_cita, turno, peso_paciente, estatura_paciente, presion_arterial])
                            print(tabulate(data, headers=headers, tablefmt="grid"))
                            print()
                        else:
                            print("No hay citas programadas en el período seleccionado.")

                    if opcion_submenu_1 == 2:
                        print()
                        print('---------------------- PACIENTES CON CITA ----------------------')
                        print('Detalles de todas las citas:')
                        print(f'{"Folio del paciente":<20}{"Nombre del paciente":<30}{"Apellido Paterno":<20}{"Apellido Materno":<20}{"Fecha de Nacimiento":<20}{"Edad":<10}{"Peso del Paciente":<20}{"Estatura del Paciente":<25}{"Presión Arterial":<20}{"Hora de Llegada":<20}{"Turno de Cita":<15}')
                        print(f'{"-" * 20:<20}{"-" * 30:<30}{"-" * 20:<20}{"-" * 20:<20}{"-" * 20:<20}{"-" * 10:<10}{"-" * 20:<20}{"-" * 25:<25}{"-" * 20:<20}{"-" * 20:<20}{"-" * 15:<15}')

                        for folio, cita in citas.items():
                            nombre_paciente = cita["Nombres"]
                            apellido_paterno = cita["Apellido Paterno"]
                            apellido_materno = cita["Apellido Materno"]
                            fecha_nacimiento = cita["Fecha de Nacimiento"]
                            edad = cita["Edad"]
                            peso_paciente = cita.get("Peso del Paciente", "No especificado")
                            estatura_paciente = cita.get("Estatura del Paciente", "No especificada")
                            presion_arterial = cita.get("Presion Arterial", "No especificada")
                            hora_llegada = cita.get("Hora de Llegada", "No especificada")
                            turno_cita = cita["Turno de Cita"]

                            print(f'{folio:<20}'
                                f'{nombre_paciente:<30}'
                                f'{apellido_paterno:<20}'
                                f'{apellido_materno:<20}'
                                f'{fecha_nacimiento.strftime("%d/%m/%Y") if fecha_nacimiento is not None else "N/A":<20}'
                                f'{edad if edad is not None else "N/A":<10}'
                                f'{peso_paciente if peso_paciente is not None else "N/A":<20}'
                                f'{estatura_paciente if estatura_paciente is not None else "N/A":<25}'
                                f'{presion_arterial if presion_arterial is not None else "N/A":<20}'
                                f'{hora_llegada if hora_llegada is not None else "N/A":<20}'
                                f'{turno_cita if turno_cita is not None else "N/A":<15}')                            
                            print()

                    if opcion_submenu_1 == 3:
                        print('Saliendo del menu...')
                        break

            if opcion_menu_4 == 2:
                while True:
                    print('---------------------- SUBMENU REPORTE DE PACIENTES ----------------------')
                    print('1. Listado completo de los pacientes.')
                    print('2. Busqueda por clave del paciente')
                    print('3. Busqueda por apellidos y nombres')
                    print('4. Salir del menu')
                    tupla_2 = (1, 2, 3, 4)
                    while True:
                        opcion_2 = input('Selecciona la opcion del menu. Solo el numero:  ')
                        if opcion_2.isdigit():
                            opcion_submenu_2 = int(opcion_2)
                            if opcion_submenu_2 in tupla_2:
                                print('Se registro correctamente')
                                print()
                                break
                            else:
                                print('ERROR. Seleccciona una opcion valida en el menu.')
                        else:
                            print(f'ERROR. El dato ({opcion_2}) no es numerico. Intenta de nuevo.')

                    if opcion_submenu_2 == 1:
                        print('---------------------- LISTADO DE PACIENTES ----------------------')
                        print('Detalles de todos los pacientes:')
                        print()
                        print(f'{"Clave del Paciente":<20}{"Apellido Paterno":<20}{"Apellido Materno":<20}{"Nombres":<20}{"Fecha de Nacimiento":<20}')
                        print(f'{"-" * 20:<20}{"-" * 20:<20}{"-" * 20:<20}{"-" * 20:<20}{"-" * 20:<20}')

                        for clave, paciente in pacientes.items():
                            apellido_paterno = paciente["PRIMER APELLIDO"]
                            apellido_materno = paciente["SEGUNDO APELLIDO"]
                            nombres = paciente["NOMBRES"]
                            fecha_nacimiento = paciente["FECHA DE NACIMIENTO"].strftime("%Y-%m-%d")  
                            print(f'{clave:<20}{apellido_paterno:<20}{apellido_materno:<20}{nombres:<20}{fecha_nacimiento:<20}')
                            print()
                            print()

                    if opcion_submenu_2 == 2:
                        print()
                        print('---------------------- BUSQUEDA POR CLAVE ----------------------')
                        while True:
                            try:
                                clave_a_buscar = int(input('Ingrese la clave a buscar: '))
                                if clave_a_buscar in claves:
                                    paciente = pacientes[clave_a_buscar]
                                    print(f'Clave: {clave_a_buscar}')
                                    print(f'  Primer Apellido: {paciente["PRIMER APELLIDO"]}')
                                    print(f'  Segundo Apellido: {paciente["SEGUNDO APELLIDO"]}')
                                    print(f'  Nombres: {paciente["NOMBRES"]}')
                                    print(f'  Fecha de Nacimiento: {paciente["FECHA DE NACIMIENTO"]}')
                                    print()
                                    print()
                                    break
                                else:
                                    print('ERROR. No se enccontro la clave.')
                            except ValueError:
                                print('El dato ingresado no es numerico')
                                print()
                            except Exception:
                                print(f"Ocurrió un problema: {sys.exc_info()[0]}")
                                Excepcion = sys.exc_info()
                                for elemento in Excepcion:
                                    print(elemento)
                        while True:
                            pregunta_expediente_clinico = input('Desea consultar el expediente clinico (SI/NO):').upper()
                            if pregunta_expediente_clinico.isalpha():
                                print()
                                break
                            else:
                                print('ERROR. Ingresa solo "SI" o "NO". Intenta de nuevo.')

                        if pregunta_expediente_clinico == 'SI':
                            cita_encontrada = False
                            for folio_cita, valor in citas.items():
                                if valor['Clave del paciente'] == clave:
                                    print('Expediente Clínico:')
                                    print(f'  Turno de Cita: {valor["Turno de Cita"]}')
                                    print(f'  Peso del Paciente: {valor["Peso del Paciente"]} kilogramos.')
                                    print(f'  Estatura del Paciente: {valor["Estatura del Paciente"]} centimetros.')
                                    print(f'  Hora de Llegada: {valor["Hora de Llegada"]}')
                                    print(f'  Presión Arterial: {valor["Presion Arterial"]}')
                                    print(f'  Diagnóstico: \n\t{valor["Diagnostico"]}')
                                    print()
                                    print()
                                    cita_encontrada = True
                                    break
                            if not cita_encontrada:
                                print('No se encontró una cita para este paciente.')
                        else:
                            continue

                    if opcion_submenu_2 == 3:
                        print('---------------------- BUSQUEDA POR APELLIDO Y NOMBRES ----------------------')
                        while True:
                            nombres_busqueda = input('Ingrese los nombres del paciente: ')
                            if nombres_busqueda.strip().replace(' ', '').isalpha():
                                nombres_busqueda = nombres_busqueda.upper() 
                                break
                            else:
                                print('Error: Los nombres solo pueden contener letras. Por favor, inténtelo de nuevo.')

                        while True:
                            primer_apellido_busqueda = input('Ingrese el primer apellido del paciente: ')
                            if primer_apellido_busqueda.strip().replace(' ', '').isalpha():
                                primer_apellido_busqueda = primer_apellido_busqueda.upper()  
                                break
                            else:
                                print('Error: El primer apellido solo puede contener letras. Por favor, inténtelo de nuevo.')

                        pacientes_encontrados = []

                        for clave, datos in pacientes.items():
                            nombres_paciente = datos['NOMBRES']
                            primer_apellido_paciente = datos['PRIMER APELLIDO']  
                            if nombres_busqueda in nombres_paciente and primer_apellido_busqueda == primer_apellido_paciente:
                                pacientes_encontrados.append((clave, datos))

                        if pacientes_encontrados:
                            print()
                            print('Pacientes encontrados:')
                            for clave, datos in pacientes_encontrados:
                                print(f'Clave: {clave}')
                                print(f'Detalles del paciente:')
                                print(f'  Primer Apellido: {datos["PRIMER APELLIDO"]}')
                                print(f'  Segundo Apellido: {datos["SEGUNDO APELLIDO"]}')
                                print(f'  Nombres: {datos["NOMBRES"]}')
                                print(f'  Fecha de Nacimiento: {datos["FECHA DE NACIMIENTO"]}')
                                print()
                                print()
                        else:
                            print('\n <Paciente no encontrado> \n')
                        
                        while True:
                            pregunta_expediente_clinico = input('Desea consultar el expediente clinico (SI/NO):').upper()
                            if pregunta_expediente_clinico.isalpha():
                                print()
                                break
                            else:
                                print('ERROR. Ingresa solo "SI" o "NO". Intenta de nuevo.')  
                            
                        if pregunta_expediente_clinico == 'SI':
                            cita_encontrada_1 = False
                            for folio_cita, valor in citas.items():
                                if valor['Clave del paciente'] == clave:
                                    print('Expediente Clínico:')
                                    print(f'  Turno de Cita: {valor["Turno de Cita"]}')
                                    print(f'  Peso del Paciente: {valor["Peso del Paciente"]} kilogramos.')
                                    print(f'  Estatura del Paciente: {valor["Estatura del Paciente"]} centimetros.')
                                    print(f'  Hora de Llegada: {valor["Hora de Llegada"]}')
                                    print(f'  Presión Arterial: {valor["Presion Arterial"]}')
                                    print(f'  Diagnóstico: \n\t{valor["Diagnostico"]}')
                                    print()
                                    print()
                                    cita_encontrada = True
                            if not cita_encontrada_1:
                                print('No se encontró una cita para este paciente.')
                        else:
                            continue

                    if opcion_submenu_2 == 4:
                        print('Saliendo del menu...')
                        break


            if opcion_menu_4 == 3:
                print('Saliendo del menu...')
                print('\n')
                break

    if opcion_menuPrincipal == 4:
        print('Esta a punto de salir del sistema.')
        salir_Sistema = input('¿Está seguro que desea salir del sistema? (SI/NO): ').upper()
        if salir_Sistema == 'SI':
            print()
            print('Gracias por usar el sistema.')
            print('Vuelva pronto')
            print('Saliendo del sistema...')
            break
        elif salir_Sistema == 'NO':
            print('Volviendo al menú principal...')
            print()
        elif salir_Sistema == '':
            print('Error. No se puede omitir.')
        else:
            print('Por favor, responda con SI o NO.')
            continue

try:
    with open('Pacientes.csv', 'w', newline='') as archivo_1:
        grabador_1 = csv.writer(archivo_1)
        grabador_1.writerow(('Clave', 'Apellido Paterno', 'Apellido Materno', 'Nombres', 'Fecha de nacimiento', 'Sexo'))
        grabador_1.writerows([
            (clave, 
            datos['PRIMER APELLIDO'], 
            datos['SEGUNDO APELLIDO'], 
            datos['NOMBRES'],
            datos['FECHA DE NACIMIENTO'].strftime('%Y-%m-%d'), 
            datos['SEXO'])
            for clave, datos in pacientes.items()
        ])
except FileNotFoundError:
    print('ERROR. No se pudo preservar los datos del archivo Pacientes.csv')
except csv.Error as e:
    print(f"Error CSV: {e}")

try:
    with open('Citas.csv', 'w', newline='') as archivo_2:
        grabador_2 = csv.writer(archivo_2)
        grabador_2.writerow(('Folio','Clave del paciente', 'Apellido Paterno', 'Apellido Materno', 'Nombres', 'Fecha de nacimiento',
                            'Edad', 'Fecha de cita', 'Turno de cita', 'Peso del paciente', 'Estatura del paciente',
                            'Hora de llegada', 'Presion Arterial', 'Diagnostico'))
        grabador_2.writerows([
            (
                clave,
                datos['Clave del paciente'],
                datos.get('Apellido Paterno', ''),
                datos.get('Apellido Materno', ''),
                datos.get('Nombres', ''),
                datos['Fecha de Nacimiento'].strftime('%m/%d/%Y'),
                datos.get('Edad', ''),
                datos['Fecha de Cita'].strftime('%m/%d/%Y'),
                datos.get('Turno de Cita', ''),
                datos.get('Peso del Paciente', ''),
                datos.get('Estatura del Paciente', ''),
                datos.get('Hora de Llegada', ''),
                datos.get('Presion Arterial', ''),
                datos.get('Diagnostico', '')
            ) 
            for clave, datos in citas.items()
        ])
except FileNotFoundError:
    print('ERROR. No se pudo preservar los datos del archivo Citas.csv')
except csv.Error as e:
    print(f"Error CSV: {e}")