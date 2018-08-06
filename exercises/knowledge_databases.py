from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///data.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add(self, k_id, topic, name, rating):
	"""
	Add a student to the database, given
	their name, year, and whether they have
	finished the lab.
	"""
	student_object = Student(
	name=name,
	year=year,
	finished_lab=finished_lab)
	session.add(student_object)
	session.commit()


def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass

a = Knowledge()
a.add(1, "weather", "Rainbow", 9)
print(__repr__(a))