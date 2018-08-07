from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
#from model import Base, Student

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	#def __init__(self, Base):
	__tablename__ = 'knowledge'
	k_id = Column(Integer, primary_key=True)
	name = Column(String)
	topic = Column(String)
	rating = Column(Integer)

	def is_rainbow(self):
		return self.topic == "weather" and self.name == "Rainbow" and self.rating == 9 and self.k_id == 1

	#def is_bad(self):
	#	return self.rating < 7

	
#add_student("Mayuri", 2, True)

	def __repr__(self):
		
		if self.is_rainbow():
			print("If you want to learn about weather, you should look at the Wikipedia article called rainbow.\nWe gave this article a rating of 9 out of 10!")
		
		#elif self.is_bad():
		#	print("Unfortunately, this article does not have a better rating. Maybe, this is an article that should be\nreplaced soon!.")

		return(("id: {}\narticle name: {}\n""article topic: {}\n""rating: {}\n").format(self.k_id, self.name, self.topic, self.rating))
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
