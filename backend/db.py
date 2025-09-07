from sqlmodel import SQLModel, create_engine, Field, Session
engine = create_engine("sqlite:///./app.db", echo=False)

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    amount_cents: int
    currency: str = "GBP"
    timestamp: str
    merchant: str | None = None
    note: str | None = None

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
