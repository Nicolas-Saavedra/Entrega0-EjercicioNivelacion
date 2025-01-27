import type { Category } from "./category"

export type Task = {
        id: number,
        texto_tarea: string,
        fecha_creacion: string,
        fecha_tentativa_finalizacion: string,
        estado: string,
        id_Usuario: number,
        id_Categoria: number
        categoria: Category
}
