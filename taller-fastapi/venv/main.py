from fastapi import FastAPI, HTTPException
from modelos import Tarea, TareaCreate
from typing import Optional
from almacenamiento import cargar_tareas, guardar_tareas, siguiente_id
app = FastAPI(
 title="API de Gestión de Tareas",
 description="Taller de Sistemas Distribuidos - UIS",
 version="1.0.0"
)

@app.get("/tareas", response_model=list[Tarea])
def listar_tareas(completada: Optional[bool] = None):
 """
 Retorna las tareas almacenadas.
 Si se proporciona el parámetro completada, filtra por estado.
 Ejemplo: GET /tareas?completada=true
 """
 tareas = cargar_tareas()
 if completada is not None:
    tareas = [t for t in tareas if t["completada"] == completada]
 return tareas

@app.post("/tareas", response_model=Tarea, status_code=201)
def crear_tarea(tarea: TareaCreate):
 """Crea una nueva tarea y la almacena."""
 tareas = cargar_tareas()
 nueva = tarea.model_dump()
 nueva["id"] = siguiente_id(tareas)
 tareas.append(nueva)
 guardar_tareas(tareas)
 return nueva

@app.put("/tareas/{tarea_id}", response_model=Tarea)
def actualizar_tarea(tarea_id: int, datos: TareaCreate):
 """Actualiza todos los campos de una tarea existente."""
 tareas = cargar_tareas()
 for i, t in enumerate(tareas):
    if t["id"] == tarea_id:
        tareas[i] = {**datos.model_dump(), "id": tarea_id}
 guardar_tareas(tareas)
 return tareas[i]
 raise HTTPException(status_code=404, detail="Tarea no encontrada")
@app.delete("/tareas/{tarea_id}", status_code=204)
def eliminar_tarea(tarea_id: int):
 """Elimina una tarea por su id."""
 tareas = cargar_tareas()
 tareas_filtradas = [t for t in tareas if t["id"] != tarea_id]
 if len(tareas_filtradas) == len(tareas):
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
 guardar_tareas(tareas_filtradas)

