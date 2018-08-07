from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.orm import *

#Base = declarative_base()
engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add(name, topic, rating):
	"""
	Add a student to the database, given
	their name, year, and whether they have
	finished the lab.
	"""
	knowledge_object = Knowledge(
	name=name,
	topic=topic,
	rating=rating)
	session.add(knowledge_object)
	session.commit()


def query_all_articles():

	knowledge = session.query(Knowledge).all()
	return knowledge

def query_article_by_topic(topic):
	
	return session.query(Knowledge).filter_by(topic = topic).all()

def query_article_by_rating(rating):
	
	return session.query(Knowledge).filter_by(rating = rating).all()

def query_article_by_name(name):

	return session.query(Knowledge).filter_by(name = name).all()

def delete_article_by_topic(topic):

	session.query(Knowledge).filter_by(topic = topic).delete()
	session.commit()

def delete_article_by_rating(rating):

	session.query(Knowledge).filter_by(rating = rating).delete()
	session.commit()

def delete_article_by_name(name):
	
	session.query(Knowledge).filter_by(name = name).delete()
	session.commit()

def delete_all_articles():
	
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(name, new_rating):
	
	knowledge_object = session.query(Knowledge).filter_by(name = name).first()
	knowledge_object.rating = new_rating
	session.commit()

def delete_low(threshold):
	
	l = query_all_articles()
	for i in l:
		if i.rating < threshold:
			delete_article_by_rating(i.rating)
	session.commit()

def delete_duplicates():

	l = query_all_articles()
	
	names = []
	
	for i in l:
	
		names.append(i.name)
	
	names = set(names)
	names = list(names)
	temp = []
	for i in names:
		
		l = query_article_by_name(i)
		temp.append(l[0])
	
	delete_all_articles()

	for i in temp:
		add(i.name, i.topic, i.rating)
		#for j in range(len(l)-1):

			#delete_article_by_name(i)
	session.commit()

a = Knowledge()
#add("ayy", "weather", 17)
#add("aby", "weather", 8)
#add("acy", "weather", 11)
#add("ady", "weather", 9)
##print(a.__repr__())
#delete_article_by_topic("weather")
#delete_all_articles()
#edit_article_rating("ayy", 17)
#delete_low(7)
delete_duplicates()
print(query_all_articles())
#print(query_article_by_topic("ayy"))