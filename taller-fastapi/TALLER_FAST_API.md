# Taller FastAPI

## Información de la práctica

La implementación completa de esta práctica, incluyendo el código fuente, el archivo de almacenamiento y las evidencias de funcionamiento, se encuentra en el siguiente repositorio de GitHub:

**Repositorio:** [LauraVargas22/Fast_Api](https://github.com/LauraVargas22/Fast_Api)

## 1. ¿Qué es una API REST y cuáles son sus métodos principales?

Una **API REST** (Representational State Transfer) es una interfaz que permite la comunicación entre aplicaciones mediante el protocolo HTTP. En este tipo de API, la información se organiza en **recursos**, los cuales se identifican mediante URL. Por ejemplo, en esta práctica el recurso principal son las tareas y se accede a él mediante la ruta `/tareas`.

Las API REST generalmente intercambian información en formato JSON y utilizan los métodos HTTP para indicar la operación que se desea realizar sobre un recurso.

### Métodos principales

| Método | Función | Ejemplo en la práctica |
| --- | --- | --- |
| `GET` | Consultar uno o varios recursos sin modificarlos. | `GET /tareas` obtiene todas las tareas. |
| `POST` | Crear un nuevo recurso. | `POST /tareas` registra una tarea. |
| `PUT` | Reemplazar o actualizar completamente un recurso existente. | `PUT /tareas/1` actualiza la tarea con id 1. |
| `PATCH` | Actualizar parcialmente un recurso. | Podría utilizarse para cambiar únicamente el estado de una tarea. |
| `DELETE` | Eliminar un recurso. | `DELETE /tareas/1` elimina la tarea con id 1. |

Cada operación produce una respuesta con un código de estado HTTP. Algunos ejemplos son:

- `200 OK`: la consulta o actualización se realizó correctamente.
- `201 Created`: el recurso fue creado correctamente.
- `204 No Content`: el recurso fue eliminado y no hay contenido que retornar.
- `404 Not Found`: el recurso solicitado no existe.
- `422 Unprocessable Entity`: los datos enviados no cumplen con la estructura esperada.

REST favorece una comunicación uniforme y desacoplada: el cliente solicita o modifica recursos sin necesitar conocer cómo están implementados internamente en el servidor.

## 2. ¿Qué ventaja tiene usar modelos Pydantic para validación?

Pydantic permite definir la estructura y los tipos de los datos que recibe y devuelve una aplicación FastAPI. En esta práctica se utiliza un modelo similar al siguiente:

```python
from typing import Optional
from pydantic import BaseModel


class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False
```

Sus principales ventajas son:

- **Validación automática:** comprueba que cada campo tenga el tipo indicado antes de ejecutar la lógica del endpoint.
- **Reducción de errores:** impide que se almacenen fácilmente datos con una estructura inválida o con campos obligatorios ausentes.
- **Conversión de datos:** cuando es posible y seguro, convierte los valores recibidos al tipo declarado.
- **Mensajes de error claros:** FastAPI devuelve automáticamente una respuesta detallada cuando los datos no son válidos.
- **Documentación automática:** los modelos se incorporan a los esquemas de Swagger UI y muestran al usuario qué datos debe enviar.
- **Código más legible:** la estructura de los recursos queda definida explícitamente en clases reutilizables.

Por ejemplo, si se intenta crear una tarea sin el campo obligatorio `titulo`, FastAPI rechazará la solicitud antes de llamar a la función que guarda la tarea y responderá normalmente con el código `422`.

## 3. ¿Qué limitaciones tiene el almacenamiento en un archivo JSON frente a una base de datos?

Un archivo JSON es apropiado para ejercicios, prototipos o aplicaciones con pocos datos porque es sencillo de leer y no requiere instalar un servidor de base de datos. Sin embargo, presenta varias limitaciones:

- **Problemas de concurrencia:** dos solicitudes podrían intentar escribir el archivo al mismo tiempo y provocar pérdida o corrupción de información.
- **Bajo rendimiento:** para consultar o modificar una tarea, la aplicación debe cargar el archivo completo en memoria y volver a escribirlo.
- **Escalabilidad limitada:** el tiempo y la memoria necesarios aumentan a medida que crece la cantidad de registros.
- **Consultas básicas:** no proporciona un lenguaje de consulta, índices, relaciones, agrupaciones ni filtros eficientes como una base de datos.
- **Falta de transacciones:** no garantiza que un conjunto de operaciones se complete totalmente o se revierta en caso de error.
- **Menor integridad:** restricciones como identificadores únicos, claves foráneas o reglas entre entidades deben programarse manualmente.
- **Seguridad limitada:** no incluye por sí mismo usuarios, roles, permisos ni control de acceso a los datos.
- **Copias de seguridad y recuperación manuales:** recuperar versiones anteriores requiere implementar una estrategia adicional.
- **Uso distribuido complejo:** varias instancias de la API no pueden compartir de manera segura un archivo local como fuente central de datos.

Una base de datos, por el contrario, está diseñada para administrar grandes cantidades de información, atender accesos simultáneos, ejecutar consultas eficientes y conservar la consistencia de los datos.

## Conclusiones

FastAPI facilita la construcción de servicios REST gracias a su integración con los métodos HTTP, la documentación automática y la validación mediante Pydantic. El almacenamiento en JSON permitió desarrollar y comprobar rápidamente las operaciones CRUD de esta práctica, pero una aplicación destinada a producción debería utilizar una base de datos como PostgreSQL, MySQL o SQLite, dependiendo de sus necesidades de concurrencia, volumen y despliegue.
