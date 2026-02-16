from sqlmodel import create_engine, Session

engine = create_engine("sqlite:///./database.db")


def db_session():
    with Session(engine) as session:
        yield session
