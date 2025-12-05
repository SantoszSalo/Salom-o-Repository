from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Optional


@dataclass
class Departamento:

    _nome: str
    _data_ini: date
    _numero: int = None
    _cpf_gerente: str = None
    _created_at: datetime = datetime.now()
    _updated_at: datetime = datetime.now()

    # Departamento -> JSON (dict)
    def to_dict(self) -> dict:
        return asdict(self)

    # JSON (dict) -> Departamento
    @classmethod
    def from_dict(cls, data: dict) -> 'Departamento':
        return cls(
            data.get("nome"),
            data.get("data_ini"),
            data.get("numero"),
            data.get("cpf_gerente"),
            data.get("created_at"),
            data.get("updated_at")
        )

    def __str__(self) -> str:
        return (
            f"Numero='{self.numero}', "
            f"Nome='{self.nome}', "
            f"CPF Gerente='{self._cpf_gerente}', "
            f"Data Iniciação='{self._data_ini}', "
            f"created_at='{self._created_at}', "
            f"updated_at='{self._updated_at}'"
        )

    # --- Getters e Setters ---
    @property
    def numero(self) -> Optional[int]:
        return self._numero
    @numero.setter
    def numero(self, numero: int):
        self._numero = numero

    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def cpf_gerente(self) -> Optional[str]:
        return self._cpf_gerente
    @cpf_gerente.setter
    def cpf_gerente(self, cpf_gerente: str):
        self._cpf_gerente = cpf_gerente

    @property
    def data_ini(self) -> date:
        return self._data_ini
    @data_ini.setter
    def data_ini(self, data_ini: date):
        self._data_ini = data_ini

    @property
    def created_at(self) -> datetime:
        return self._created_at
    @created_at.setter
    def created_at(self, created_at: datetime):
        self._created_at = created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at
    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        self._updated_at = updated_at