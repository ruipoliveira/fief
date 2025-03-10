import uuid
from typing import Optional

from sqlalchemy import select

from fief.models import Client
from fief.repositories.base import BaseRepository, UUIDRepositoryMixin


class ClientRepository(BaseRepository[Client], UUIDRepositoryMixin[Client]):
    model = Client

    async def get_by_client_id(self, client_id: str) -> Optional[Client]:
        statement = select(Client).where(Client.client_id == client_id)
        return await self.get_one_or_none(statement)

    async def get_by_client_id_and_tenant(
        self, client_id: str, tenant: uuid.UUID
    ) -> Optional[Client]:
        statement = select(Client).where(
            Client.client_id == client_id, Client.tenant_id == tenant
        )
        return await self.get_one_or_none(statement)

    async def get_by_client_id_and_secret(
        self, client_id: str, client_secret: str
    ) -> Optional[Client]:
        statement = select(Client).where(
            Client.client_id == client_id, Client.client_secret == client_secret
        )
        return await self.get_one_or_none(statement)
