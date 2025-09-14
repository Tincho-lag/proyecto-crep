# usuario.py
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Usuario:
    id: int
    nombre: str
    email: Optional[str]
    estado: bool
    descripcion: str
    materia: str
    promedio : str
    carrera : str

    def to_dict(self) -> dict:
        return asdict(self)
    
#biblioteca_sistema 

#├── models/a
#│   ├── element
#│   ├────── elemento.py          # Clase base para materiales (TU ENFOQUE INICIAL)
#│   ├────── utilidades.py           # Herencias de libros
#│   ├────── usuario.py            # resolver como hacerlo

#├── date/

#├── repositories/
#│   ├── __init__.py
#│   └── material_repository.py

#├── clases/                
#│   └── interfas.py
