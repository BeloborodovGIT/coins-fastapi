from ..database import session_factory

class DatabaseService:

    def __init__(self, session=None, **kwargs) -> None:
        if session is None:
            self.session = session_factory(**kwargs)
        else:
            self.session = session

    def __getattr__(self, attr):
        return getattr(self.session, attr)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()
