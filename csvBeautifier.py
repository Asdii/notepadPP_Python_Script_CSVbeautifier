import os
import csv
from Npp import editor, notepad

#Conteo de archivos temporales
rutaArchTemp = "C:/test"
file_count = sum(len(files) for _, _, files in os.walk(rutaArchTemp))
if file_count > 2:
    notepad.messageBox("Su directorio de archivos temporales esta demasiado llena.\nSe recomienda limpiarla antes de continuar." + "\n\nRuta de archivos actual: " + rutaArchTemp, "Advertencia", MESSAGEBOXFLAGS.ICONEXCLAMATION)

#Obtencion de palabra mas grande en toda la columna
texto = editor.getText()
csvTemp = csv.reader(texto.splitlines(), delimiter=';')
csv_reader = list(csvTemp)
listaPalMasG = []
for columnId in range(0, len(list(csv_reader)[0])):
    tamMasGrande = 0
    for row in list(csv_reader):
        if len(str(row[columnId])) > tamMasGrande:
            tamMasGrande = len(str(row[columnId]))
    listaPalMasG.append([columnId, tamMasGrande])

#Adicion de espacios en blanco usando la informacion anterior
filas = []
columnas = []
for fila in list(csv_reader):
    index = 0
    for columna in fila:
        columnas.append(columna.ljust(int(listaPalMasG[index][1])))
        index += 1
    filas.append(columnas)
    columnas = []

#Abrir CSV ordenado en Notepad++
pathCSVord = rutaArchTemp+"/"+notepad.getCurrentFilename().split("\\")[-1]+"_ordenado"
with open(pathCSVord, 'w') as tempCsv:
    tempCsv = csv.writer(tempCsv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    tempCsv.writerows(list(filas))
notepad.open(pathCSVord)