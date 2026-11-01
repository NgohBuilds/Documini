from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text

# Create a python table => DocumentModel defines a mapped table of the real table
class Base(DeclarativeBase):
    pass

class DocumentModel(Base):

    __tablename__ = "documents"

    id : Mapped[int] = mapped_column(primary_key=True)

    title : Mapped[str] = mapped_column(
        String(255), nullable=False
    )

    category : Mapped[str] =  mapped_column(
        String(100),
        nullable=False
    )

    description : Mapped[str | None] = mapped_column(
        Text,
        nullable=True 
    )
