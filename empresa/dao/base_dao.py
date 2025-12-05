'''
  *** BaseDAO ***
  Classe abstrata base para DAOs (Data Access Objects)
  Operações CRUD genéricas
'''

from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from supabase import Client

# TypeVar - tornar a classe genérica
T = TypeVar('T')

class BaseDAO(ABC, Generic[T]):

    def __init__(self, client: Client, table_name: str):
        self._client = client
        self._table_name = table_name

    @abstractmethod
    def to_model(self, data: dict) -> T:
        pass

    @abstractmethod
    def to_dict(self, model: T) -> dict:
        pass

### CREATE
    def create(self, model: T) -> Optional[T]:
        try:
            data = self.to_dict(model)
            response = self._client.table(self._table_name).insert(data).execute()
            if response.data:
                return self.to_model(response.data[0])
            return None
        except Exception as e:
            print(f"Erro ao criar registro: {e}")
            return None

### READ
    def read(self, pk: str, value: T) -> Optional[T]:
        try:
            response = self._client.table(self._table_name).select('*').eq(pk, value).execute()
            if response.data:
                return self.to_model(response.data[0])
            return None
        except Exception as e:
            print(f'Erro ao buscar registro: {e}')
            return None

### READ ALL
    def read_all(self) -> List[T]:
        try:
            response = self._client.table(self._table_name).select('*').execute()
            if response.data:
                return [self.to_model(item) for item in response.data]
            return None
        except Exception as e:
            print(f'Erro ao buscar todos os registros: {e}')
            return None

### UPDATE
    def update(self, pk: str, value: T, model: T) -> Optional[T]:
        try:
            data = self.to_dict(model)
            response = self._client.table(self._table_name).update(data).eq(pk, value).execute()
            if response.data:
                return self.to_model(response.data[0])
            return None
        except Exception as e:
            print(f'Erro ao atualizar registro: {e}')
            return None