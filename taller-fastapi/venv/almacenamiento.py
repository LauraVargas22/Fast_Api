# almacenamiento.py
import json
from pathlib import Path
ARCHIVO = Path("tareas.json")
def cargar_tareas() -> list[dict]:
 """Carga las tareas desde el archivo JSON."""
 if not ARCHIVO.exists():
    return []
 with open(ARCHIVO, "r", encoding="utf-8") as f:
    return json.load(f)
def guardar_tareas(tareas: list[dict]) -> None:
 """Guarda la lista de tareas en el archivo JSON."""
 with open(ARCHIVO, "w", encoding="utf-8") as f:
    json.dump(tareas, f, ensure_ascii=False, indent=2)
def siguiente_id(tareas: list[dict]) -> int:
 """Retorna el siguiente id disponible."""
 if not tareas:
    return 1
 return max(t["id"] for t in tareas) + 1
