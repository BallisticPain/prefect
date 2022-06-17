from uuid import uuid4

import pytest

from prefect.orion import schemas


class TestBlockDocumentCreate:
    async def test_anonymous_block_document_cant_have_name_provided(self):
        with pytest.raises(
            ValueError,
            match="(Names cannot be provided for anonymous block documents.)",
        ):
            schemas.actions.BlockDocumentCreate(
                block_schema_id=uuid4(),
                block_type_id=uuid4(),
                is_anonymous=True,
                name="test",
            )