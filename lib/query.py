from sqlalchemy.orm import sessionmaker
from models import Base, Audition, Role, engine
from seed import session

#Audition.role returns an instance of role associated with this audition.
audition = session.query(Audition).first()
print(audition.role.character_name)

#Audition.call_back() will change the the hired attribute to True.



#Role.auditions returns all of the auditions associated with this role.
role1 = session.query(Role).first()
print(role1.auditions)

#Role.actors returns a list of names from the actors associated with this role.
role2 = session.query(Role).first()
print(role2.actors)

#Role.locations returns a list of locations from the auditions associated with this role.
role3 = session.query(Role).first()
print(role3.locations)
  
#Role.lead() returns the first instance of the audition that was hired for this role or returns a string 'no actor has been hired for this role'.
role4 = session.query(Role).first()  
print(role4.lead())  

#Role.understudy() returns the second instance of the audition that was hired for this role or returns a string 'no actor has been hired for understudy for this role'.
role = session.query(Role).first()
print(role.understudy())  
