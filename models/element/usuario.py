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
