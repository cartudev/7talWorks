
import bpy


def testImport():
    try:
        from fpdf import FPDF
    except ModuleNotFoundError:

        import subprocess
        import sys
        import bpy
        from pathlib import Path
        import ensurepip
        
        ensurepip.bootstrap()
        pybin = Path(sys.executable)
#        subprocess.check_call([pybin, '-m', 'pip', 'list'])

        subprocess.check_call([pybin, '-m', 'ensurepip'])
        subprocess.check_call([pybin, '-m', 'pip', 'install', '--upgrade', 'pip'])
        
        subprocess.check_call([pybin, '-m', 'pip', 'install', 'git+https://github.com/PyFPDF/fpdf2.git@master'])
        
        print('FINISHED')

        
    try:
        from fpdf import FPDF
    except ImportError:
        print('no se pudo instalar el modulo fpdf')



references = {
    'ND': "No definido",
    'pl': "Placa",
    'pe': "Perfil",
    'c': "Columna",
    'cm': "Media Columna",
    'ca': "Columna Angular",
    'al': "Alfombra",
    'v': "Vidrio",
    'e': "Estante",
    'ev': "Estante Vidrio"
}

detalles = {
    'ND': "No definido", 
    'sf': "Placa simple faz", 
    'l': "Placa laminada", 
    'df': "placa doble faz", 
    'sfc': "Simple faz color", 
    'dfc': "Doble faz color", 
    'lps': "Placa laminada con ploteo simple", 
    'lpd': "Placa laminada con ploteo doble", 
    'mp': "Material pintado", 
    'me': "Material empatillado",
}


def objectsOrder():

    objectsCount = {
    "tipo" : {
        }
    
    }

    allObjects = bpy.data.objects

    for obj in allObjects:
        if references[obj.STW.tipo] not in objectsCount['tipo']:
            objectsCount['tipo'][references[obj.STW.tipo]] = {}
        if obj.STW.nombre not in objectsCount['tipo'][references[obj.STW.tipo]]:
            object = objectsCount['tipo'][references[obj.STW.tipo]]
            object[obj.STW.nombre] = {'nombre': obj.STW.nombre, 'cantidad': 1}
            if not obj.STW.detallesmaterial == 'ND':
                object[obj.STW.nombre]['detallesMaterial'] = detalles[obj.STW.detallesmaterial] + ' ' + obj.STW.descripciondetalles
            else:
                object[obj.STW.nombre]['detallesMaterial'] = ''
            object[obj.STW.nombre]['materialAnidado']  = obj.STW.nombreanidado
            if obj.STW.tipo == 'c' or obj.STW.tipo == 'cm' or obj.STW.tipo == 'ca':
                object[obj.STW.nombre]['medida'] = f"{int(round(obj.STW.alto, 3)*1000)}mm"
            elif obj.STW.tipo == 'pl' or obj.STW.tipo == 'al' or obj.STW.tipo == 'v' or obj.STW.tipo == 'e' or obj.STW.tipo == 'ev':
                object[obj.STW.nombre]['medida'] = f"{int(round(obj.STW.ancho, 3)*1000)}mm x {int(round(obj.STW.alto, 3)*1000)}mm"
            elif obj.STW.tipo == 'pe':
                if round(obj.STW.ancho, 2) == 0.04 or round(obj.STW.ancho, 2) == 0.05:
                    object[obj.STW.nombre]['medida'] = f"{int(round(obj.STW.alto, 3)*1000)}mm"
                else:
                    object[obj.STW.nombre]['medida'] = f"{int(round(obj.STW.ancho, 3)*1000)}mm"
                
                
                
        else:
            objectsCount['tipo'][references[obj.STW.tipo]][obj.STW.nombre]['cantidad'] += 1
        
        
    TABLE_DATA = [    
        ["TIPO MATERIAL", "MEDIDA", "DET. MATERIAL", "CANTIDAD","MATERIAL PARA"],
    ]
    for tipo in objectsCount['tipo']:
        for nombres in objectsCount['tipo'][tipo]:
            if objectsCount['tipo'][tipo][nombres]['nombre'] == '':
                pass
            else: 
                TABLE_DATA.append([tipo, objectsCount['tipo'][tipo][nombres]['medida'], objectsCount['tipo'][tipo][nombres]['detallesMaterial'] , str(objectsCount['tipo'][tipo][nombres]['cantidad']),objectsCount['tipo'][tipo][nombres]['materialAnidado']])
    pdfLaunch(TABLE_DATA)

    

def pdfLaunch(data):


    from fpdf import FPDF
    from fpdf.fonts import FontFace

    class PDF(FPDF):
        def footer(self):
            # Position cursor at 1.5 cm from bottom:
            self.set_y(-10)
            # Setting font: helvetica italic 8
            self.set_text_color(200,50,50)
            self.set_font("helvetica", "I", 8)
            # Printing page number:
            self.cell(0, 1, f"Pagina {self.page_no()}/{{nb}}", align="R")




    pdf = PDF()


    textColorHd = (255, 255, 255)
    bgColorHd = (42, 54, 82)
    headings_style = FontFace(emphasis="ITALICS", color=textColorHd, fill_color=bgColorHd)

    rowGrey = (225,227,240)

    pdf.add_page()
    pdf.set_font("Helvetica", size=11)
    with pdf.table(headings_style=headings_style, cell_fill_color=rowGrey, cell_fill_mode="ROWS") as table:
        for data_row in data:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    if bpy.context.scene.pdfFile.endswith('.pdf'):
        print(bpy.path.abspath(bpy.context.scene.pdfPath))
        print(bpy.context.scene.pdfPath)
        pdf.output(bpy.path.abspath(bpy.context.scene.pdfPath) + bpy.context.scene.pdfFile)
    else:
        pdf.output(bpy.path.abspath(bpy.context.scene.pdfPath) + bpy.context.scene.pdfFile + '.pdf')



testImport()
