# -*- coding:utf-8 -*-

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

# ----------------------------------------------------------
# Author: Stephen Leger (s-leger)
#
# ----------------------------------------------------------

bl_info = {
    'name': 'Innovastructure',
    'description': 'Architectural objects',
    'author': 'cartu',
    'license': 'GPL',
    'deps': '',
    'version': (0, 0, 8),
    'blender': (2, 80, 0),
    'location': 'View3D > Tools > Create > IES',
    'warning': '',
    'wiki_url': 'https://github.com/s-leger/archipack/wiki',
    'tracker_url': 'https://github.com/s-leger/archipack/issues',
    'link': 'https://github.com/s-leger/archipack',
    'support': 'COMMUNITY',
    'category': 'Add Mesh'
    }
from innova_structure import pdf creator
import os



# noinspection PyUnresolvedReferences
import bpy
from bpy.props import IntProperty
import math

def items_tipo(self, context):
    if 0 == 0:
        return[
            ('addcolumnas', 'columnas', 'The zeroth item'),    
            ('addplacas', 'placas', 'The first item'),    
            ('addcenefas', 'cenefas', 'The second item'),    
            ('addestanterias', 'estanterias', 'The third item')
        ]
    
def items_direccion(self, context):

        return[
            ('dirxa', '+X', 'Direccion 0 grados'),    
            ('dirxb', '-X', 'Direccion 180 grados'),    
            ('dirya', '+Y', 'Direccion 90 grados'),    
            ('diryb', '-Y', 'Direccion 270 grados'),
            ('dirxaya', '+X+Y', 'Direccion 45 grados'),    
            ('dirxbya', '-X+Y', 'Direccion 135 grados'),    
            ('dirxayb', '+X-Y', 'Direccion 225 grados'),    
            ('dirxbyb', '-X-Y', 'Direccion 315 grados')
        ]
    
def items_propiedad(self, context):
    if bpy.data.scenes['Scene'].agregar_tipo == 'addcolumnas' :
        return[
            ('propcol2500', 'columnas 2500', 'The zeroth item'),    
            ('propcol2835', 'columnas 2835', 'The first item'),    
            ('propcol3200', 'columnas 3200', 'The second item'),    
            ('propcol335', 'columnas 335', 'The third item')
        ]
    
    if bpy.data.scenes['Scene'].agregar_tipo == 'addplacas' :
        return[
            ('propplc950', 'placa 967 x 2417', 'The zeroth item'),    
            ('propplc455', 'placa 472 x 2417', 'The first item'),    
            ('propplc310', 'placa 327 x 2417', 'The second item'),    
            ('propplc207_5', 'placa 225 x 2417', 'The third item')
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
            ('propcen2x4415', 'cenefa 4415 x 404', 'cenefa 4.5 m grande'),
            ('propcen2x4910', 'cenefa 4910 x 404', 'cenefa 5 m grande'), 
        ]
    
    if bpy.data.scenes['Scene'].agregar_tipo == 'addestanterias' :
        return[
    ('noseaun', 'falta programar no molestar', 'Falta la programacion')    
        ]
def update_tipo(self, context):
    print("Prop1 changed to", context.scene.agregar_tipo)

def update_direccion(self, context):
    print("Prop1 changed to", context.scene.agregar_direccion)
    
def update_propiedad(self, context):
    print("Prop1 changed to", context.scene.agregar_propiedad)

def contexto():
    if bpy.context.active_object.name.startswith("placa 950"): 
        return .475

    if bpy.context.active_object.name.startswith("columna"): 
        return .02
    
    if bpy.context.active_object.name.startswith("placa 455"): 
        return .2275
    
    if bpy.context.active_object.name.startswith("placa 310"): 
        return .155

    if bpy.context.active_object.name.startswith("placa 207_5"): 
        return .10375

    if bpy.context.active_object.name.startswith("cenefa 455"): 
        return .2275
    
    if bpy.context.active_object.name.startswith("cenefa 950"): 
        return .475

    if bpy.context.active_object.name.startswith("cenefa 1445"): 
        return .7225
    
    if bpy.context.active_object.name.startswith("cenefa 1940"): 
        return .970
    
    if bpy.context.active_object.name.startswith("cenefa 2435"): 
        return 1.2175

    if bpy.context.active_object.name.startswith("cenefa 2930"): 
        return 1.465
    
    if bpy.context.active_object.name.startswith("cenefa 3425"): 
        return 1.7125
    
    if bpy.context.active_object.name.startswith("cenefa 3920"): 
        return 1.96

    if bpy.context.active_object.name.startswith("cenefa 4415"): 
        return 2.2075
    
    if bpy.context.active_object.name.startswith("cenefa 4910"): 
        return 2.455
    
    
def direccionx():
    if bpy.context.scene.agregar_direccion == 'dirxa':
        return 1
    if bpy.context.scene.agregar_direccion == 'dirxb':
        return -1   
    if bpy.context.scene.agregar_direccion == 'dirya':
        return 0
    if bpy.context.scene.agregar_direccion == 'diryb':
        return 0
    if bpy.context.scene.agregar_direccion == 'dirxaya':
        return (math.sqrt(2)/2)*1
    if bpy.context.scene.agregar_direccion == 'dirxbya':
        return (math.sqrt(2)/2)*-1
    if bpy.context.scene.agregar_direccion == 'dirxayb':
        return (math.sqrt(2)/2)*1
    if bpy.context.scene.agregar_direccion == 'dirxbyb':
        return (math.sqrt(2)/2)*-1
    else:pass
    
def direcciony():
    if bpy.context.scene.agregar_direccion == 'dirxa':
        return 0
    if bpy.context.scene.agregar_direccion == 'dirxb':
        return 0   
    if bpy.context.scene.agregar_direccion == 'dirya':
        return 1
    if bpy.context.scene.agregar_direccion == 'diryb':
        return -1
    if bpy.context.scene.agregar_direccion == 'dirxaya':
        return (math.sqrt(2)/2)*1
    if bpy.context.scene.agregar_direccion == 'dirxbya':
        return (math.sqrt(2)/2)*1
    if bpy.context.scene.agregar_direccion == 'dirxayb':
        return (math.sqrt(2)/2)*-1
    if bpy.context.scene.agregar_direccion == 'dirxbyb':
        return (math.sqrt(2)/2)*-1
    else:pass
    
def dirrot():
    if bpy.context.scene.agregar_direccion == 'dirxa':
        return 0
    if bpy.context.scene.agregar_direccion == 'dirxb':
        return 0 
    if bpy.context.scene.agregar_direccion == 'dirya':
        return math.pi*0.5
    if bpy.context.scene.agregar_direccion == 'diryb':
        return math.pi*0.5
    if bpy.context.scene.agregar_direccion == 'dirxaya':
        return math.pi*0.25
    if bpy.context.scene.agregar_direccion == 'dirxbya':
        return math.pi*0.75
    if bpy.context.scene.agregar_direccion == 'dirxayb':
        return math.pi*0.75
    if bpy.context.scene.agregar_direccion == 'dirxbyb':
        return math.pi*0.25
    else:pass
    
    

    

    
def obj1():
    agpr = bpy.context.scene.agregar_propiedad
    if agpr == 'propcol2500':
        return 'columna 2500'
    if agpr == 'propcol2835':
        return 'columna 2835'
    if agpr == 'propcol335':
        return 'columna 335'
    if agpr == 'propcol3200':
        return 'columna 3200'
    if agpr == 'propplc950':
        return 'placa 950'
    if agpr == 'propplc455':
        return 'placa 455'
    if agpr == 'propplc310':
        return 'placa 310'
    if agpr == 'propplc207_5':
        return 'placa 207_5'
    if agpr == 'propcen1x455':
        return 'cenefa 455*335'
    if agpr == 'propcen1x950':
        return 'cenefa 950*335'
    if agpr == 'propcen1x1445':
        return 'cenefa 1445*335'
    if agpr == 'propcen1x1940':
        return 'cenefa 1940*335'
    if agpr == 'propcen1x2435':
        return 'cenefa 2435*335'
    if agpr == 'propcen1x2930':
        return 'cenefa 2930*335'
    if agpr == 'propcen1x3425':
        return 'cenefa 3425*335'
    if agpr == 'propcen1x3920':
        return 'cenefa 3920*335'
    if agpr == 'propcen1x4415':
        return 'cenefa 4415*335'
    if agpr == 'propcen1x4910':
        return 'cenefa 4415*335'
    if agpr == 'propcen2x455':
        return 'cenefa 455*487_5'
    if agpr == 'propcen2x950':
        return 'cenefa 950*487_5'
    if agpr == 'propcen2x1445':
        return 'cenefa 1445*487_5'
    if agpr == 'propcen2x1940':
        return 'cenefa 1940*487_5'
    if agpr == 'propcen2x2435':
        return 'cenefa 2435*487_5'
    if agpr == 'propcen2x2930':
        return 'cenefa 2930*487_5'
    if agpr == 'propcen2x3425':
        return 'cenefa 3425*487_5'
    if agpr == 'propcen2x3920':
        return 'cenefa 3920*487_5'
    if agpr == 'propcen2x4415':
        return 'cenefa 4415*487_5'
    if agpr == 'propcen2x4910':
        return 'cenefa 4910*487_5'
    else:
        return 'placa 950'
    
def obj2():
    agpr = bpy.context.scene.agregar_propiedad
    if agpr.startswith("propplc"):
        return "columna 2500"
    if agpr.startswith("propcen1x"):
        return "columna 2500"
    if agpr.startswith("propcen2x"):
        return "columna 2835"
    


    
class generador(bpy.types.Operator):
    """Tooltip"""
    bl_label = "generar"
    bl_idname = "object.generar"
        



    def execute(self, context):
        if bpy.context.scene.agregar_propiedad.startswith("propcol"):
                bpy.ops.object.collection_instance_add(
                    collection=obj1(), 
                    view_align=False, 
                    location=((bpy.context.active_object.location.x) + (contexto()*direccionx()) ,(bpy.context.active_object.location.y) + (contexto()*direcciony()) ,0), 
                    rotation=(0, 0, 0+dirrot()))  
                bpy.context.active_object.location=((bpy.context.active_object.location.x) + (contexto()*direccionx()) ,(bpy.context.active_object.location.y)+ (contexto()*direcciony()) ,0)    
        
        
        else:
            dada = bpy.context.active_object.name.startswith
            if dada('columna 2500') or dada("columna 335") or dada("columna 3200") and bpy.context.scene.agregar_propiedad.startswith("propcen2x"):
                copiarpos = bpy.context.active_object.location.copy()
                bpy.ops.object.delete()
                bpy.ops.object.collection_instance_add(
                    collection=obj2(), 
                    view_align=False, 
                    location=copiarpos,
                    rotation=(0, 0, 0))
                
            for i in range(bpy.context.scene.cantidad):
                if bpy.context.active_object.name.startswith('placa') or bpy.context.active_object.name.startswith("*335", (bpy.context.active_object.name.find("*335")),30 ) or bpy.context.active_object.name.startswith("*487_5", (bpy.context.active_object.name.find("*487_5")),30 ): 
                    bpy.ops.object.collection_instance_add(
                        collection=obj2(), 
                        view_align=False, 
                        location=((bpy.context.active_object.location.x) + (contexto()*direccionx()) ,(bpy.context.active_object.location.y)+ (contexto()*direcciony()) ,0),
                        rotation=(0, 0, 0))
                    bpy.context.active_object.location=((bpy.context.active_object.location.x) + (contexto()*direccionx()) ,(bpy.context.active_object.location.y) + (contexto()*direcciony()) ,0)    

                else:
                    pass



                bpy.ops.object.collection_instance_add(
                    collection=obj1(), 
                    view_align=False, 
                    location=((bpy.context.active_object.location.x) + (contexto()*direccionx()) ,(bpy.context.active_object.location.y) + (contexto()*direcciony()) ,0), 
                    rotation=(0, 0, 0+dirrot()))  
                bpy.context.active_object.location=((bpy.context.active_object.location.x) + (contexto()*direccionx()) ,(bpy.context.active_object.location.y)+ (contexto()*direcciony()) ,0)    

                bpy.ops.object.collection_instance_add(
                    collection=obj2(), 
                    view_align=False, 
                    location=((bpy.context.active_object.location.x) + (contexto()*direccionx()) ,(bpy.context.active_object.location.y)+(contexto()*direcciony()),0), 
                    rotation=(0, 0, 0))

                bpy.context.active_object.location=((bpy.context.active_object.location.x) + (contexto()*direccionx()),(bpy.context.active_object.location.y)+ (contexto()*direcciony()) ,0)    
        if bpy.context.scene.colend == False:
            bpy.ops.object.delete()
        else: pass
            
        return {"FINISHED"}



    

class PanelIES(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "INNOVA Structure"
    bl_idname = "innova_structure"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

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
        
        layout.label(text="Direccion")
        row = layout.row()
        row.prop(scene, "agregar_direccion", text='1',expand=True)
        if  bpy.context.scene.agregar_propiedad.startswith("propcol"): pass
        else:
            row = layout.row(align=True)
            row.prop(scene, "cantidad", text='Cantidad',expand=True)
            row.prop(scene, "colend",text='columna al final')


        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.generar")



        
def register():
    bpy.types.Scene.cantidad = bpy.props.IntProperty(name='Cant', description="cantidad de objetos", default=1,min=1, max=15)
    bpy.utils.register_class(generador)
    bpy.types.Scene.agregar_tipo = bpy.props.EnumProperty(name='Tipo', items=items_tipo, update=update_tipo)
    bpy.types.Scene.agregar_propiedad = bpy.props.EnumProperty(name='Propiedad', items=items_propiedad, update=update_propiedad)
    bpy.types.Scene.agregar_direccion = bpy.props.EnumProperty(name='Direccion', items=items_direccion, update=update_direccion)
    bpy.types.Scene.colend = bpy.props.BoolProperty(name="colfinal", description="agregar columna al final", default = True)
    bpy.utils.register_class(PanelIES)

def unregister():
    bpy.utils.unregister_class(PanelIES)
    bpy.types.Scene.agregar_direccion
    bpy.types.Scene.agregar_propiedad
    bpy.types.Scene.agregar_tipo
    bpy.utils.unregister_class(generador)
    bpy.types.Scene.cantidad

    
if __name__ == '__main__':
    register()


