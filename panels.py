import bpy
import math



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


class STW_PT_PanelProps(View3DPanel, bpy.types.Panel):
    bl_label = "Propiedades de Objetos"
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
"""         if STW.mat7tw:
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
            layout.prop(STW, "alto", text="alto") """
#            layout.prop(context.scene, "agregardireccion", text="direccion")



class STW_PT_PanelPropsSet(bpy.types.Panel):
    bl_parent_id = "STW_PT_PanelProps"
    bl_category = "7talWorks"
    bl_label = "Setear Propiedades del Objeto"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'




    def draw(self, context):
        STW = context.object.STW
        layout = self.layout
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





class STW_PT_PanelCounter(bpy.types.Panel):
    bl_parent_id = "STW_PT_PanelProps"
    bl_category = "7talWorks"
    bl_label = "Contador de Material"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'


    def draw(self, context):
        scene = bpy.context.scene
        layout = self.layout
        split = layout.split()



        scene = context.scene

        col = layout.column()
        col.prop(scene, "pdfPath", text="")
        
        col = layout.column()

        col.prop(scene, "pdfFile", text="")

        col = layout.column()
        col.operator("object.count")




# ------------------------------------------------------------------
# Panel generador de paneleria
# ------------------------------------------------------------------


class STW_PT_PanelBuild(View3DPanel, bpy.types.Panel):
    bl_label = "Construir"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "7talWorks"



    def draw(self, context):
        layout = self.layout

        scene = bpy.context.scene
#        stw = scene.stw
        # Create a simple row.
        pass


class STW_PT_PanelBuildStructure(bpy.types.Panel):
    bl_parent_id = "STW_PT_PanelBuild"
    bl_category = "7talWorks"
    bl_label = "Construir paneleria"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'


    def draw(self, context):
        layout = self.layout

        scene = bpy.context.scene
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

        row = layout.row(align=True)
        row.prop(scene, "angulos",icon='BLANK1',expand=True)
        
        row = layout.row(align=True)

        row.prop(scene, "agregar_direccion", text='Dirección',expand=True)
        if bpy.context.scene.angulos == '0':
            row.label(text="angulo final " +  f'{math.degrees(scene.agregar_direccion % (math.pi*2)):.1f}' + " º")
        elif bpy.context.scene.angulos == '90':
            row.label(text="angulo final " +  f'{math.degrees((scene.agregar_direccion + math.pi/2) % (math.pi*2)):.1f}' + " º")
        elif bpy.context.scene.angulos == '180':
            row.label(text="angulo final " +  f'{math.degrees((scene.agregar_direccion + math.pi) % (math.pi*2)):.1f}' + " º")
        elif bpy.context.scene.angulos == '270':
            row.label(text="angulo final " +  f'{math.degrees((scene.agregar_direccion + math.pi*1.5) % (math.pi*2)):.1f}' + " º")
        if  scene.agregar_tipo == 'addperfil':
            row.prop(scene, "altura", text='altura del elemento',expand=True)

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
        if  scene.agregar_tipo == 'addperfil':
            row = layout.row(align=True)
            row.prop(scene, "finalAltura",icon='BLANK1',expand=True)


        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.test")
