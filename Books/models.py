from Database.database import base
from sqlalchemy.orm import Mapped, mapped_column

class Book(base):
    __tablename__ = "books"

    id:Mapped[int] = mapped_column(primary_key=True,index=True,autoincrement='auto')
    title:Mapped[str] = mapped_column(nullable=False)
    author:Mapped[str] = mapped_column(nullable=False)
    description:Mapped[str | None] = mapped_column(nullable=True)