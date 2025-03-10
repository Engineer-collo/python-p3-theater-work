from sqlalchemy.orm import sessionmaker
from models import Base, Audition, Role, engine

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    

    role1 = Role(character_name="Lead Actor")
    role2 = Role(character_name="Supporting Actor")
    role3 = Role(character_name="Director")
    role4 = Role(character_name="Co-ordinator")
    role5 = Role(character_name="Facilitator")


    session.add_all([role1, role2, role3, role4, role5])
    session.commit() 





    audition1 = Audition(actor="John Doe", location="Los Angeles", phone="123-456-7890", hired=True, role_id=role1.id)
    audition2 = Audition(actor="Jane Smith", location="New York", phone="987-654-3210", hired=False, role_id=role2.id)
    audition3 = Audition(actor="Leroy Sane", location="Kampala", phone="467-654-3210", hired=True, role_id=role3.id)
    audition4 = Audition(actor="Ann Kago", location="Dodoma", phone="908-654-3210", hired=False, role_id=role4.id)
    audition5 = Audition(actor="Irine maina", location="Nairobi", phone="684-654-3210", hired=False, role_id=role5.id)

    session.add_all([audition1, audition2, audition3, audition4, audition5])
    session.commit()  



