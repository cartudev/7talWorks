# ----------------------------------------------------------
# Author: Cartu
# ----------------------------------------------------------

# ----------------------------------------------
# Define Addon info
# ----------------------------------------------
bl_info = {
    "name": "7tals",
    "author": "Cartu",
    "location": "View3D > Add Mesh / Sidebar > Create Tab",
    "version": (0, 0, 2),
    "blender": (3, 5, 0),
    "description": "Generador de paneleria y sistema de aluminio",
    "doc_url": "{BLENDER_MANUAL_URL}/addons/add_mesh/archimesh.html",
    "category": "Add Mesh"
    }


import bpy
import os
import math

from bpy.types import PropertyGroup, Panel, Object, Operator, SpaceView3D
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




# Register
bpy.utils.register_class(baseprops)



Object.STW = bpy.props.PointerProperty(type=baseprops)


#Propiedades generador Paneleria

def items_tipo(self, context):
        return[
            ('addcolumnas', 'columnas', 'The zeroth item'),
            ('addplacas', 'placas', 'The first item'),
            ('addcenefas', 'cenefas', 'The second item'),
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
            ('propplc600', 'placa 600 x 2417', 'The zeroth item'),
            ('propplc455', 'placa 472 x 2417', 'The first item'),
            ('propplc310', 'placa 327 x 2417', 'The second item'),
            ('propplc207_5', 'placa 225 x 2417', 'The third item'),
            ('propplc950x2150', 'placa 967 x 2067', 'The zeroth item'),
            ('propplc950sf', 'placa 967 x 2417 simple faz', 'The zeroth item')
        ]

    if bpy.data.scenes['Scene'].agregar_tipo == 'addcenefas' :
        return[
            ('propcen1x455', 'cenefa 472 x 252', 'cenefa 0.5 m'),
            ('propcen1x950', 'cenefa 967 x 252', 'cenefa 1 m'),
            ('propcen1x1445', 'cenefa 1462 x 252', 'cenefa 1.5 m'),
            ('propcen1x1940', 'cenefa 1957 x 252', 'cenefa  2 m'),
            ('propcen1x2435', 'cenefa 2452 x 252', 'cenefa 2.5 m'),
            ('propcen1x2930', 'cenefa 2947 x 252', 'cenefa 3 m'),
            ('propcen1x3425', 'cenefa 3425 x 252', 'cenefa 3.5 m'),
            ('propcen1x3920', 'cenefa 3920 x 252', 'cenefa 4 m'),
            ('propcen1x4415', 'cenefa 4415 x 252', 'cenefa 4.5 m'),
            ('propcen1x4910', 'cenefa 4910 x 252', 'cenefa 5 m'),
            ('propcen2x455', 'cenefa 472 x 404', 'cenefa 0.5 m grande'),
            ('propcen2x950', 'cenefa 967 x 404', 'cenefa 1 m grande'),
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


def update_tipo(self, context):
    print("Prop1 changed to", context.scene.agregar_tipo)

def update_direccion(self, context):
    print("Prop1 changed to", context.scene.agregar_direccion)

def update_propiedad(self, context):
    print("Prop1 changed to", context.scene.agregar_propiedad)


#funciones a utilizar

def contexto():
    tipo = bpy.context.active_object.STW.tipo
    ancho = bpy.context.active_object.STW.ancho
    if tipo == 'pl' or tipo == 'v':
        return round((ancho-.017)/2, 6)
    else:
        return round(ancho/2, 6)

def direccionx():
    return math.sin(bpy.context.scene.agregar_direccion)

def direcciony():
    return math.cos(bpy.context.scene.agregar_direccions)






class View3DPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "7talWorks"

    @classmethod
    def poll(cls, context):
        return (context.object is not None)


# ------------------------------------------------------------------
# Inicio del panel
# ------------------------------------------------------------------


class PanelProps(View3DPanel, bpy.types.Panel):
    bl_idname = "VIEWD_7TW_Props"
    bl_label = "Propiedades de Objeto"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "7talWorks"


# ------------------------------------------------------------------
# Panel  de propiedades del objeto
# ------------------------------------------------------------------


    def draw(self, context):
        STW = context.object.STW
        layout = self.layout
        layout.prop(STW, "mat7tw", text="Objeto sistema",  icon='CHECKMARK')
        if STW.mat7tw:
            layout.use_property_split = True
            layout.use_property_decorate = False  # No animation.
            row = layout.row()
            split = layout.split()
            col = layout.column()
            subcol = col.column(align=True)
            # First column
            subcol.prop(STW, "nombre", text="Name")
            layout.prop(STW, "tipo", text="Tipo")
            layout.prop(STW, "detallesmaterial", text="Detalles del Material")
            if  bpy.context.object.STW.detallesmaterial != 'ND':
                layout.prop(STW, "descripciondetalles", text="Descripcion Detalles")
            layout.prop(STW, "anidado", text="Material Anidado")
            if bpy.context.object.STW.anidado:
                layout.prop(STW, "nombreanidado", text="Nombre del Anidado")
            layout.prop(STW, "ancho", text="ancho")
            layout.prop(STW, "alto", text="alto")
            layout.prop(context.scene, "agregarireccion", text="direccion")


# ------------------------------------------------------------------
# Panel generador de paneleria
# ------------------------------------------------------------------


class PanelAdd(View3DPanel, bpy.types.Panel):
    bl_label = "Generador Paneleria"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "7talWorks"



    def draw(self, context):
        layout = self.layout

        scene = context.scene
#        stw = scene.stw
        # Create a simple row.
        split = layout.split()

        # First column

        col = split.column()
        col.label(text="Agregar Tipo:")
        col.prop(scene, "agregar_tipo", text='',)

        # Second column, aligned
        col = split.column(align=True)
        col.label(text="Propiedad:")
        col.prop(scene, "agregar_propiedad", text='')

        row = layout.row()
        row.prop(scene, "agregar_direccion", text='Dirección',expand=True)

        if bpy.context.scene.agregar_tipo == 'addestanterias':
            row = layout.row(align=True)
            row.prop(scene, "pospos",icon='BLANK1', text="Posicion +90°")
            row.prop(scene, "posneg", icon='BLANK1', text="Posicion -90°")

        if  scene.agregar_tipo == 'addcolumnas': pass
        elif scene.agregar_tipo == 'addestanterias':
            row = layout.row(align=True)
            row.prop(scene, "cantidad", text='Cantidad',expand=True)
        else:
            row = layout.row(align=True)
            row.prop(scene, "cantidad", text='Cantidad',expand=True)
            row.prop(scene, "colend",icon='BLANK1')

        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.generar")




def register():

    bpy.types.Scene.cantidad = bpy.props.IntProperty(name='Cant', description="cantidad de objetos", default=1,min=1, max=15)
    bpy.types.Scene.agregar_tipo = bpy.props.EnumProperty(name='Tipo', items=items_tipo, update=update_tipo)
    bpy.types.Scene.agregar_propiedad = bpy.props.EnumProperty(name='Propiedad', items=items_propiedad, update=update_propiedad)
    bpy.types.Scene.colend = bpy.props.BoolProperty(name="columna al final", description="agregar columna al final", default = True)
    bpy.types.Scene.pospos = bpy.props.BoolProperty(name="Posicion positiva", description="Ubicar en posicion positiva", default = False)
    bpy.types.Scene.posneg = bpy.props.BoolProperty(name="Posicion negativa", description="Ubicar en posicion negativa", default = False)


    bpy.utils.register_class(PanelProps)
    bpy.utils.register_class(PanelAdd)
    bpy.types.Scene.agregar_direccion = bpy.props.FloatProperty(name='Direccion', subtype = 'ANGLE', step = 100 )



def unregister():
    bpy.types.Scene.agregar_direccion
    bpy.utils.unregister_class(PanelAdd)
    bpy.utils.unregister_class(PanelProps)

    bpy.types.Scene.posneg
    bpy.types.Scene.pospos
    bpy.types.Scene.colend
    bpy.types.Scene.agregar_propiedad
    bpy.types.Scene.agregar_tipo
    bpy.types.Scene.cantidad
