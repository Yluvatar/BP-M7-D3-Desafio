from .models import Tarea, SubTarea


def recupera_tareas_y_sub_tareas():
    Tarea.objects.filter(eliminada=True).update(eliminada=False)
    SubTarea.objects.filter(eliminada=True).update(eliminada=False)
    imprimir_en_pantalla()

def crear_tarea(descripcion):
    tarea = Tarea.objects.create(descripcion=descripcion)
    imprimir_en_pantalla()

def crear_subtarea(descripcion, tarea_id):
    subtarea = SubTarea.objects.create(descripcion=descripcion, tarea_id=Tarea.objects.get(id=tarea_id))
    imprimir_en_pantalla()

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.filter(id=tarea_id).update(eliminada=True)
    SubTarea.objects.filter(tarea_id=tarea_id).update(eliminada=True)
    imprimir_en_pantalla()

def elimina_subtarea(subtarea_id):
    subtarea = SubTarea.objects.filter(id=subtarea_id).update(eliminada=True)
    imprimir_en_pantalla()

def imprimir_en_pantalla():
    tareas = Tarea.objects.filter(eliminada=False).all()
    subtareas = SubTarea.objects.filter(eliminada=False).all()

    for tarea in tareas:
        print(f"[{tarea.id}] Tarea: {tarea.descripcion}")
        for subtarea in subtareas.filter(tarea_id=tarea.id):
            print(f".... [{subtarea.id}] Sub tarea: {subtarea.descripcion}")