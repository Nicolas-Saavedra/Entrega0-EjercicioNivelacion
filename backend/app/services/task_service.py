from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, task_create: TaskCreate) -> Task:
    db_task = Task(
        texto_tarea=task_create.texto_tarea,
        fecha_creacion=task_create.fecha_creacion,
        fecha_tentativa_finalizacion=task_create.fecha_tentativa_finalizacion,
        estado=task_create.estado,
        id_Usuario=task_create.id_Usuario,
        id_Categoria=task_create.id_Categoria,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task: Task, task_update: TaskUpdate) -> Task:
    task.texto_tarea = task_update.texto_tarea or task.texto_tarea
    task.estado = task_update.estado or task.estado
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task: Task) -> None:
    task.delete()
    db.commit()
