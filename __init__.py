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
    "version": (0, 1, 0),
    "blender": (3, 5, 0),
    "description": "Generador de paneleria y sistema de aluminio",
    "doc_url": "",
    "category": "Add Mesh"
    }


import bpy
import os
import math
import asyncio
from .properties import *
from .panels import *
from .pdfMod import *

from bpy.types import Panel, Object, Operator, SpaceView3D
from bpy.props import IntProperty, CollectionProperty, FloatVectorProperty, BoolProperty, StringProperty, \
                      FloatProperty, EnumProperty



try:
    bpy.utils.register_class(baseprops)
except ValueError:
    pass




Object.STW = bpy.props.PointerProperty(type=baseprops)


#Propiedades generador Paneleria

async def linkObj(obj, type):
    directory = os.path.dirname(os.path.realpath(__file__))
    print(obj)
    print(obj + ' ' + type + ' ' + directory)

    bpy.ops.wm.append(
        filename= obj,
        directory= directory + '/base.blend/'+ type +'/',
        filepath= directory + '/base.blend/'+ type +'/'+ obj,
        autoselect=True,
        link=False, 
        do_reuse_local_id=True,
        instance_object_data=False)
        

class objectCount(bpy.types.Operator):
    bl_idname = "object.count"        # Unique identifier for buttons and menu items to reference.
    bl_label = "count objects and export in a pdf"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.
    def execute(self, context):
        objectsOrder()
        return {'FINISHED'}

def object_func(self, context):
    self.layout.operator(objectCount.bl_idname, text="pdf counter Operator")




class test(bpy.types.Operator):
    bl_idname = "object.test"        # Unique identifier for buttons and menu items to reference.
    bl_label = "just a test"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.
    async def act(self):        # execute() is called when running the operator.

#        lastLocation = bpy.context.selected_objects[0].location
#       lastLocation = ((location.x) + (contexto()*direccionx()) ,(location.y) + (contexto()*direcciony()) ,0)
        loop = asyncio.get_event_loop()


        if bpy.context.scene.agregar_propiedad.startswith("propcol"):
            await addcol()

        if bpy.context.scene.agregar_propiedad.startswith("propplc"):
            for i in range((bpy.context.scene.cantidad)-1):
                await addper()
                await addplc()
                await addper()
                await addcol()
            await addper()
            await addplc()
            await addper()
            if bpy.context.scene.colend == True:
                await addcol()
            else:
                pass
        if bpy.context.scene.agregar_propiedad.startswith("propcen"):
            for i in range((bpy.context.scene.cantidad)-1):
                await addper()
                await addplc()
                await addper()
                await addcol()
            await addper()
            await addplc()
            await addper()
            if bpy.context.scene.colend == True:
                await addcol()
            else:
                pass

        if bpy.context.scene.agregar_propiedad.startswith("proppfl"):
            for i in range((bpy.context.scene.cantidad)-1):
                await addper()
            await addper()


        

        

    def execute(self, context):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.act())
        return {'FINISHED'}





def update_tipo(self, context):
    print("Prop1 changed to", context.scene.agregar_tipo)

def update_direccion(self, context):
    print("Prop1 changed to", context.scene.agregar_direccion)

def update_propiedad(self, context):
    print("Prop1 changed to", context.scene.agregar_propiedad)



def menu_func(self, context):
    self.layout.operator(test.bl_idname)

#funciones a utilizar

def contexto():
    tipo = bpy.context.selected_objects[0].STW.tipo
    ancho = bpy.context.selected_objects[0].STW.ancho
    mat7tw = bpy.context.selected_objects[0].STW.mat7tw
    if not mat7tw :
        return 0
    if tipo == 'pl' or tipo == 'v':
        return round((ancho-.017)/2, 6)
    else:
        return round(ancho/2, 6)

def altura():
    alto = bpy.context.selected_objects[0].STW.alto
    tipo = bpy.context.selected_objects[0].STW.tipo
    if bpy.context.scene.agregar_tipo == 'addperfil':
        if bpy.context.scene.finalAltura == 'alturaBase':
            return round(alto/2+bpy.context.scene.altura, 6)
        elif bpy.context.scene.finalAltura == 'alturaFinal':
            return round(-alto/2+bpy.context.scene.altura, 6)



    elif tipo == 'pl' or tipo == 'v':
        return round((alto-.017 )/2, 6)
    else:
        return round(alto/2, 6)

def direccion(eje, object):
    mat7tw = bpy.context.selected_objects[0].STW.mat7tw

    if not mat7tw :
        return 0
    rotation = 1
    if object == 'last':
        rotation = dirrot()
        if eje == 'x':
            return math.cos(rotation)
        if eje == 'y':
            return math.sin(rotation)
    else: 
        rotation = bpy.context.selected_objects[0].rotation_euler[2]
        if eje == 'x':
            return math.cos(rotation)
        if eje == 'y':
            return math.sin(rotation)



def dirrot():
    if bpy.context.scene.angulos == '0':
        return bpy.context.scene.agregar_direccion
    elif bpy.context.scene.angulos == '90':
        return (bpy.context.scene.agregar_direccion + math.pi/2)
    elif bpy.context.scene.angulos == '180':
        return (bpy.context.scene.agregar_direccion + math.pi)
    elif bpy.context.scene.angulos == '270':
        return (bpy.context.scene.agregar_direccion + math.pi*1.5)

async def addcol():
    direccionXVar = direccion('x', 'last')
    direccionYVar = direccion('y', 'last')
    obj = bpy.context.selected_objects[0]

    if  bpy.context.selected_objects[0].STW.mat7tw:
        lastloc = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar),0)
    else:
        lastloc = (obj.location.x , obj.location.y ,0)
    await linkObj(obj3(), 'Object')
    obj = bpy.context.selected_objects[0]
    obj.location = lastloc
    obj.location = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar), altura())
    obj.rotation_euler[2] = dirrot()

async def addper():
    direccionXVar = direccion('x', 'last')
    direccionYVar = direccion('y', 'last')
    obj = bpy.context.selected_objects[0]
    agpr = bpy.context.scene.agregar_propiedad


    tipo = obj.STW.tipo
    if tipo == 'pl' or tipo == 'v':
        if agpr == 'propcen1x3425' or agpr == 'propcen2x3425' or agpr == 'propcen2x4415' :
            lastloc = (obj.location.x-((.455/2)*direccionXVar),obj.location.y-((.455/2)*direccionYVar), obj.location.z+altura())
        else:
            lastloc = (obj.location.x , obj.location.y , obj.location.z+altura())
    else:
        lastloc = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar),0)

    await linkObj(obj2(), 'Object')
    obj = bpy.context.selected_objects[0]
    obj.location = lastloc
    if bpy.context.scene.agregar_tipo == 'addperfil':
        obj.location = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar), altura())


    elif tipo == 'c':
        if agpr.startswith("propcen1"):
            obj.location = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar), altura()+2.165)
        elif agpr.startswith("propcen2"):  
            obj.location = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar), altura()+2.348)
        else:
            obj.location = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar), altura())
    elif tipo == 'pl' or tipo == 'v':
        obj.location = (obj.location.x , obj.location.y , obj.location.z+altura())
    obj.rotation_euler[2] = dirrot()

async def addplc():
    obj = bpy.context.selected_objects[0]
    objselected = obj
    lastloc = (obj.location.x , obj.location.y , obj.location.z+altura())
    await linkObj(obj1(), 'Object')

    bpy.context.selectable_objects[-1].select_set(True)
    obj = bpy.context.selected_objects[0]
    obj.location = lastloc
    obj.location = (obj.location.x , obj.location.y , obj.location.z+altura())
    obj.rotation_euler[2] = dirrot()
    if objselected.STW.ancho > 2.947:
        await addfit()
    
async def addfit():
    agpr = bpy.context.scene.agregar_propiedad
    direccionXVar = direccion('x', 'last')
    direccionYVar = direccion('y', 'last')
    obj = bpy.context.selected_objects[0]
    objselected = obj
    if agpr == 'propcen1x3425' or agpr == 'propcen2x3425' or agpr == 'propcen2x4415' :
        obj.location = (obj.location.x+((.455/2)*direccionXVar),obj.location.y+((.455/2)*direccionYVar), obj.location.z)
    if  agpr == 'propcen1x3425' or  agpr == 'propcen2x3425' :
        pass
    else:
        lastloc = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar), obj.location.z)
        await linkObj(obj4(), 'Object')
        bpy.context.selectable_objects[-1].select_set(True)
        obj = bpy.context.selected_objects[0]
        obj.location = lastloc
        lastloc = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar), obj.location.z)
        obj.location = lastloc
        lastloc = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar), obj.location.z)
        await linkObj(obj5('a'), 'Object')
        bpy.context.selectable_objects[-1].select_set(True)
        obj = bpy.context.selected_objects[0]
        obj.location = lastloc
        lastloc = (obj.location.x+(contexto()*direccionXVar),obj.location.y+(contexto()*direccionYVar), obj.location.z)
        obj.location = lastloc
    

    bpy.ops.object.select_all(action='DESELECT')
    objselected.select_set(True)
    obj = bpy.context.selected_objects[0]
    lastloc = (obj.location.x-(contexto()*direccionXVar),obj.location.y-(-contexto()*direccionYVar), obj.location.z)
    await linkObj(obj4(), 'Object')
    bpy.context.selectable_objects[-1].select_set(True)
    obj = bpy.context.selected_objects[0]
    obj.location = lastloc
    lastloc = (obj.location.x-(contexto()*direccionXVar),obj.location.y-(contexto()*direccionYVar), obj.location.z)
    obj.location = lastloc
    lastloc = (obj.location.x-(contexto()*direccionXVar),obj.location.y-(contexto()*direccionYVar), obj.location.z)
    await linkObj(obj5('b'), 'Object')
    bpy.context.selectable_objects[-1].select_set(True)
    obj = bpy.context.selected_objects[0]
    obj.location = lastloc
    lastloc = (obj.location.x-(contexto()*direccionXVar),obj.location.y-(contexto()*direccionYVar), obj.location.z)
    obj.location = lastloc
    bpy.ops.object.select_all(action='DESELECT')
    objselected.select_set(True)




def register():


    bpy.utils.register_class(test)
    bpy.types.VIEW3D_MT_object.append(menu_func)

    bpy.utils.register_class(objectCount)
    bpy.types.VIEW3D_MT_object.append(object_func)


    bpy.types.Scene.pdfPath = bpy.props.StringProperty(name='pdfpath', description="ubicación del archivo de conteo", maxlen=255, subtype='DIR_PATH')
    bpy.types.Scene.pdfFile = bpy.props.StringProperty(name='pdffile', description="ubicación del archivo de conteo", maxlen=40, default= 'conteo.pdf')

    

    bpy.types.Scene.cantidad = bpy.props.IntProperty(name='Cantidad', description="cantidad de objetos", default=1,min=1, max=15)
    bpy.types.Scene.agregar_tipo = bpy.props.EnumProperty(name='Tipo', items=items_tipo, update=update_tipo)
    bpy.types.Scene.agregar_propiedad = bpy.props.EnumProperty(name='Propiedad', items=items_propiedad, update=update_propiedad)
    bpy.types.Scene.colend = bpy.props.BoolProperty(name="columna al final", description="agregar columna al final", default = True)
    
    bpy.types.Scene.finalAltura = bpy.props.EnumProperty(name='altura final', items=finalAltura)
    bpy.types.Scene.angulos = bpy.props.EnumProperty(name='angulos', items=angulos, default = 0)

    bpy.types.Scene.pospos = bpy.props.BoolProperty(name="Posicion positiva", description="Ubicar en posicion positiva", default = False)
    bpy.types.Scene.posneg = bpy.props.BoolProperty(name="Posicion negativa", description="Ubicar en posicion negativa", default = False)
    bpy.utils.register_class(STW_PT_PanelProps)
    bpy.utils.register_class(STW_PT_PanelBuild)
    bpy.utils.register_class(STW_PT_PanelPropsSet)
    bpy.utils.register_class(STW_PT_PanelCounter)
    bpy.utils.register_class(STW_PT_PanelBuildStructure)
    bpy.types.Scene.agregar_direccion = bpy.props.FloatProperty(name='Direccion', subtype = 'ANGLE', step = 100 )
    bpy.types.Scene.altura = bpy.props.FloatProperty(name='altura', description="altura a colocar", default=0 ,min=0, max=4, step = 1)


def unregister():
    bpy.utils.unregister_class(objectCount)

    bpy.utils.unregister_class(test)


    bpy.types.Scene.agregar_direccion
    bpy.utils.unregister_class(STW_PT_PanelBuildStructure)
    bpy.utils.unregister_class(STW_PT_PanelCounter)
    bpy.utils.unregister_class(STW_PT_PanelPropsSet)
    bpy.utils.unregister_class(STW_PT_PanelBuild)
    bpy.utils.unregister_class(STW_PT_PanelProps)


    bpy.types.Scene.posneg
    bpy.types.Scene.pospos
    bpy.types.Scene.colend

    bpy.types.Scene.finalAltura
    bpy.types.Scene.altura
    bpy.types.Scene.angulos

    bpy.types.Scene.agregar_propiedad
    bpy.types.Scene.agregar_tipo
    bpy.types.Scene.cantidad


    bpy.types.Scene.pdfFile
    bpy.types.Scene.pdfPath


if __name__ == "__main__":
    register()