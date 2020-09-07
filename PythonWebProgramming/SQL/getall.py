
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:root@localhost:5432")
db = scoped_session(sessionmaker(bind=engine))

def main():
	animee = db.execute("SELECT * FROM ANIME").fetchall()
	for anime in animee:
		print(f"{anime.name}, genre: {anime.genre}")


if __name__ == "__main__":
	main()