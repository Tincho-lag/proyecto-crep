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

#├── models/
#│   ├── __init__.py
#│   ├── element.py          # Clase base para materiales (TU ENFOQUE INICIAL)
#│   ├── libro.py           # Herencias de libros
#│   ├── usuario.py         # Para después
#│   └── prestamo.py        # Para después

#├── services/
#│   ├── __init__.py
#│   └── biblioteca_service.py
#├── repositories/
#│   ├── __init__.py
#│   └── material_repository.py

#├── data/                  # Archivos JSON/CSV temporales
#│   ├── libros.json
#│   └── materiales.json

#├── utils/
#│   ├── __init__.py
#│   └── helpers.py
#└── main.py