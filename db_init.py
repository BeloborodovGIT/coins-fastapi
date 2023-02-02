from coins_fastapi.database import *

def start_base() -> None:
    Base.metadata.create_all(bind=engine)

def generate_references() -> None:
    session = get_session()

    refs = [
        Countries(name='Country'),
        Currencies(name='Currency'),
        Mints(name='Mint'),
        TypesOfCoins(name='Type')
    ]

    session.add_all(refs)
    session.commit()

if __name__ == '__main__':
    start_base()
    generate_references()
