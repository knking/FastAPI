
from sqlalchemy import create_engine
DATABASE_URL="sqlite:///./mydb.db"

engine = create_engine(DATABASE_URL, echo=True)
