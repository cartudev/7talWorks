import bpy
import math
from bpy.types import PropertyGroup
from bpy.props import IntProperty, CollectionProperty, FloatVectorProperty, BoolProperty, StringProperty, \
                      FloatProperty, EnumProperty


class baseprops(PropertyGroup):
    mat7tw: BoolProperty(name="Objeto 7tal Works",
                          description="Es un objeto del software?",
                          default=False)
    nombre: StringProperty(name="Nombre", maxlen=70,
                           description="Nombre, usar espacio para definir propiedades")
    ancho: FloatProperty(name="ancho")
    alto: FloatProperty(name="alto")
    tipo: EnumProperty(items=(('ND', "No definido", ""),
                                       ('pl', "Placa", ""),
                                       ('pe', "Perfil", ""),
                                       ('c', "Columna", ""),
                                       ('cm', "Media Columna", ""),
                                       ('ca', "Columna Angular", ""),
                                       ('al', "Alfombra", ""),
                                       ('v', "Vidrio", ""),
                                       ('e', "Estante", ""),
                                       ('ev', "Estante Vidrio", ""),),
                                name="Tipo de material",
                                description="Tipo de material")

    detallesmaterial: EnumProperty(items=(('ND', "No definido", ""),
                                        ('sf', "Placa simple faz", ""),
                                       ('l', "Placa laminada", ""),
                                       ('df', "placa doble faz", ""),
                                       ('sfc', "Simple faz color", ""),
                                       ('dfc', "Doble faz color", ""),
                                       ('lps', "Placa laminada con ploteo simple", ""),
                                       ('lpd', "Placa laminada con ploteo doble", ""),
                                       ('mp', "Material pintado", ""),
                                       ('me', "Material empatillado", ""),),
                                name="Detalles del material",
                                description="detalles del material")

    anidado: BoolProperty(name="Anidado",
                          description="Material anidado a otro material",
                          default=False)
    nombreanidado: StringProperty(name="Nombre del anidado", maxlen=70,
                           description="Nombre, de a que objeto esta anidado")

    descripciondetalles: StringProperty(name="Descripcion de detalles", maxlen=70,
                           description="Alguna descripcion de los detalles adicionales")


def items_tipo(self, context):
        return[
            ('addplacas', 'placas', 'The first item'),
            ('addcenefas', 'cenefas', 'The second item'),
            ('addcolumnas', 'columnas', 'The zeroth item'),
            ('addperfil', 'perfiles', 'The zeroth item'),
            ('addestanterias', 'estanterias', 'The third item'),
            ('addespeciales', 'especiales', 'The fourth item'),

        ]


def items_propiedad(self, context):
    if bpy.data.scenes['Scene'].agregar_tipo == 'addcolumnas' :
        return[
            ('propcol2500', 'columnas 2500', 'Columnas 2500'),
            ('propcol2835', 'columnas 2835', 'Columnas 2835'),
            ('propcol3200', 'columnas 3200', 'Columnas 3200'),
            ('propcol2150', 'columnas 2150', 'Columnas 2150'),
            ('propcol335', 'columnas 335', 'Columnas 335')
        ]

    if bpy.data.scenes['Scene'].agregar_tipo == 'addplacas' :
        return[
            ('propplc950', 'placa 967 x 2417', 'The zeroth item'),
            ('propplc455', 'placa 472 x 2417', 'The first item'),
            ('propplc310', 'placa 327 x 2417', 'The second item'),
            ('propplc600', 'placa 600 x 2417', 'The zeroth item'),
            ('propplc660', 'placa 660 x 2417', 'The zeroth item'),
            ('propplc207_5', 'placa 225 x 2417', 'The third item'),
            ('propplc950x2150', 'placa 967 x 2067', 'The zeroth item'),
            ('propplc950sf', 'placa 967 x 2417 simple faz', 'The zeroth item')
        ]

    if bpy.data.scenes['Scene'].agregar_tipo == 'addperfil' :
        return[
            ('proppfl950', 'perfil 950', 'The zeroth item'),
            ('proppfl455', 'perfil 455', 'The first item'),
            ('proppfl310', 'perfil 310', 'The second item'),
            ('proppfl600', 'perfil 600', 'The zeroth item'),
            ('proppfl660', 'perfil 660', 'The zeroth item'),
            ('proppfl207_5', 'perfil 207,5', 'The third item'),
        ]

    if bpy.data.scenes['Scene'].agregar_tipo == 'addcenefas' :
        return[
            ('propcen1x455', 'cenefa 472 x 252', 'cenefa 0.5 m'),
            ('propcen1x950', 'cenefa 967 x 252', 'cenefa 1 m'),
            ('propcen1x1240', 'cenefa 1257 x 252', 'cenefa 1.24 m'),
            ('propcen1x1445', 'cenefa 1462 x 252', 'cenefa 1.5 m'),
            ('propcen1x1940', 'cenefa 1957 x 252', 'cenefa  2 m'),
            ('propcen1x2435', 'cenefa 2452 x 252', 'cenefa 2.5 m'),
            ('propcen1x2930', 'cenefa 2947 x 252', 'cenefa 3 m'),
            ('propcen1x3425', 'cenefa 3425 x 252', 'cenefa 3.5 m'),
            ('propcen1x3920', 'cenefa 3920 x 252', 'cenefa 4 m'),
            ('propcen1x4210', 'cenefa 4210 x 252', 'cenefa 4.2   m'),
            ('propcen1x4415', 'cenefa 4415 x 252', 'cenefa 4.5 m'),
            ('propcen1x4910', 'cenefa 4910 x 252', 'cenefa 5 m'),
            ('propcen2x455', 'cenefa 472 x 404', 'cenefa 0.5 m grande'),
            ('propcen2x950', 'cenefa 967 x 404', 'cenefa 1 m grande'),
            ('propcen2x1240', 'cenefa 1257 x 404', 'cenefa 1.2 m grande'),
            ('propcen2x1445', 'cenefa 1462 x 404', 'cenefa 1.5 m grande'),
            ('propcen2x1940', 'cenefa 1957 x 404', 'cenefa  2 m grande'),
            ('propcen2x2435', 'cenefa 2452 x 404', 'cenefa 2.5 m grande'),
            ('propcen2x2930', 'cenefa 2947 x 404', 'cenefa 3 m grande'),
            ('propcen2x3425', 'cenefa 3425 x 404', 'cenefa 3.5 m grande'),
            ('propcen2x3920', 'cenefa 3920 x 404', 'cenefa 4 m grande'),
            ('propcen2x4210', 'cenefa 4210 x 404', 'cenefa 4.2 m grande'),
            ('propcen2x4415', 'cenefa 4415 x 404', 'cenefa 4.5 m grande'),
            ('propcen2x4910', 'cenefa 4910 x 404', 'cenefa 5 m grande'),
        ]

    if bpy.data.scenes['Scene'].agregar_tipo == 'addestanterias' :
        return[
    ('modulo2150exical', 'modulo exical 2150', 'modulo de pared 2150')
        ]

    if bpy.data.scenes['Scene'].agregar_tipo == 'addespeciales' :
        return[
            ('proppuerta950', 'puerta 950 x 2500', 'puerta'),
            ('propplcsw950', 'placa spacewall', 'placa spacewall 950 x 2500')

        ]
def finalAltura(self, context):
        return[
            ('alturaBase', 'altura Base', 'altura en la base del elemento'),
            ('alturaFinal', 'altura Final', 'altura en el final del elemento')
        ]

def angulos(self, context):
        return[
            ('0', '0', 'direccion final 0ª'),
            ('90', '+90', 'direccion final 90ª'),
            ('180', '+180', 'direccion final 180ª'),
            ('270', '+270', 'direccion final 270ª')
        ]



def obj1():
    agpr = bpy.context.scene.agregar_propiedad
    if agpr == 'propplc950':
        return 'placa 967x2417'
    if agpr == 'propplc950x2150':
        return 'placa 967x2067'
    if agpr == 'propplc950sf':
        return 'placa 967x2417 sf'
    if agpr == 'propplc660':
        return 'placa 677x2417'
    if agpr == 'propplc600':
        return 'placa 617x2417'
    if agpr == 'propplc455':
        return 'placa 472x2417'
    if agpr == 'propplc310':
        return 'placa 327x2417'
    if agpr == 'propplc207_5':
        return 'placa 225x2417'


    if agpr == 'propcen1x455':
        return 'placa 472x252'
    if agpr == 'propcen1x950':
        return 'placa 967x252'
    if agpr == 'propcen1x1445':
        return 'placa 1462x252'
    if agpr == 'propcen1x1240':
        return 'placa 1257x252'
    if agpr == 'propcen1x1940':
        return 'placa 1957x252'
    if agpr == 'propcen1x2435':
        return 'placa 2452x252'
    if agpr == 'propcen1x2930':
        return 'placa 2947x252'
    if agpr == 'propcen1x3425':
        return 'placa 2947x252'
    if agpr == 'propcen1x3920':
        return 'placa 2947x252'
    if agpr == 'propcen1x4210':
        return 'placa 2947x252'
    if agpr == 'propcen1x4415':
        return 'placa 2947x252'
    if agpr == 'propcen1x4910':
        return 'placa 2947x252'

    if agpr == 'propcen2x455':
        return 'placa 472x404'
    if agpr == 'propcen2x950':
        return 'placa 967x404'
    if agpr == 'propcen2x1240':
        return 'placa 1257x404'
    if agpr == 'propcen2x1445':
        return 'placa 1462x404'
    if agpr == 'propcen2x1940':
        return 'placa 1957x404'
    if agpr == 'propcen2x2435':
        return 'placa 2452x404'
    if agpr == 'propcen2x2930':
        return 'placa 2947x404'
    if agpr == 'propcen2x3425':
        return 'placa 2947x404'
    if agpr == 'propcen2x3920':
        return 'placa 2947x404'
    if agpr == 'propcen2x4210':
        return 'placa 2947x404'
    if agpr == 'propcen2x4415':
        return 'placa 2947x404'
    if agpr == 'propcen2x4910':
        return 'placa 2947x404'
    else:
        return 'placa 967x2417'
    
def obj3():
    agpr = bpy.context.scene.agregar_propiedad
    if agpr == 'propcol2500':
        return 'columna 2500'
    if agpr == 'propcol2150':
        return 'columna 2150'
    if agpr == 'propcol2835':
        return 'columna 2835'
    if agpr == 'propcol335' :
        return 'columna 335'
    if agpr == 'propcol3200':
        return 'columna 3200'
    
    if agpr.startswith("propplc") and agpr.endswith("x2150"):
        return "columna 2150"
    if agpr.startswith("propplc"):
        return "columna 2500"
    if agpr.startswith("propcen1x"):
        return "columna 2500"
    if agpr.startswith("propcen2x"):
        return "columna 2835"

def obj2():
    agpr = bpy.context.scene.agregar_propiedad
    if agpr == 'propplc950':
        return 'perfil 950'

    if agpr == 'propplc950x2150':
        return 'perfil 950'
    if agpr == 'propplc950sf':
        return 'perfil 950'


    if agpr == 'propplc660':
        return 'perfil 660'
    if agpr == 'propplc600':
        return 'perfil 600'
    if agpr == 'propplc455':
        return 'perfil 455'
    if agpr == 'propplc310':
        return 'perfil 310'
    if agpr == 'propplc207_5':
        return 'perfil 207_5'


    if agpr == 'proppfl950':
        return 'perfil 950'
    if agpr == 'proppfl455':
        return 'perfil 455'
    if agpr == 'proppfl310':
        return 'perfil 310'
    if agpr == 'proppfl600':
        return 'perfil 600'
    if agpr == 'proppfl660':
        return 'perfil 660'
    if agpr == 'proppfl207_5':
        return 'perfil 207_5'
    
    

    if agpr == 'propcen1x455':
        return 'perfil 455'
    if agpr == 'propcen1x950':
        return 'perfil 950'
    if agpr == 'propcen1x1240':
        return 'perfil 1240'
    if agpr == 'propcen1x1445':
        return 'perfil 1445'
    if agpr == 'propcen1x1940':
        return 'perfil 1940'
    if agpr == 'propcen1x2435':
        return 'perfil 2435'
    if agpr == 'propcen1x2930':
        return 'perfil 2930'
    if agpr == 'propcen1x3425':
        return 'perfil 3425'
    if agpr == 'propcen1x3920':
        return 'perfil 3920'
    if agpr == 'propcen1x4210':
        return 'perfil 4210'
    if agpr == 'propcen1x4415':
        return 'perfil 4415'
    if agpr == 'propcen1x4910':
        return 'perfil 4910'
   
    if agpr == 'propcen2x455':
        return 'perfil 455'
    if agpr == 'propcen2x950':
        return 'perfil 950'
    if agpr == 'propcen2x1240':
        return 'perfil 1240'
    if agpr == 'propcen2x1445':
        return 'perfil 1445'
    if agpr == 'propcen2x1940':
        return 'perfil 1940'
    if agpr == 'propcen2x2435':
        return 'perfil 2435'
    if agpr == 'propcen2x2930':
        return 'perfil 2930'
    if agpr == 'propcen2x3425':
        return 'perfil 3425'
    if agpr == 'propcen2x3920':
        return 'perfil 3920'
    if agpr == 'propcen2x4210':
        return 'perfil 4210'
    if agpr == 'propcen2x4415':
        return 'perfil 4415'
    if agpr == 'propcen2x4910':
        return 'perfil 4910'


def obj4():
    agpr = bpy.context.scene.agregar_propiedad
    if agpr.startswith("propcen1x"):
        return 'perfil 235'
    if agpr.startswith("propcen2x"):
        return 'perfil 387 l40'

def obj5(option):
    agpr = bpy.context.scene.agregar_propiedad
    if agpr == 'propcen1x3425':
        return 'placa 462x252'
    if agpr == 'propcen1x3920':
        return 'placa 462x252'
    if agpr == 'propcen1x4210':
        return 'placa 607x252'
    if agpr == 'propcen1x4415':
        return 'placa 710x252'
    if agpr == 'propcen1x4910':
        return 'placa 957x252'


    if agpr == 'propcen2x3425':
        return 'placa 472x404'
    if agpr == 'propcen2x3920':
        return 'placa 472x404'
    if agpr == 'propcen2x4210':
        return 'placa 617x404'
    if agpr == 'propcen2x4415':
        if option == 'b':
            return 'placa 967x404'
        else:
            return 'placa 472x404'
    if agpr == 'propcen2x4910':
        return 'placa 967x404'

