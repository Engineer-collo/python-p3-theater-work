from sqlalchemy import ForeignKey,Boolean, Column, Integer, String, MetaData,create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__ = "Auditions"

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(String())
    hired = Column(Boolean, default=False)
    #relationship
    role_id =Column(Integer(), ForeignKey("roles.id"))
    role = relationship("Role", back_populates="auditions")

    #
    def call_back(self, session):
        self.hired = True
        session.commit()

    def __repr__(self):
        return f"Audition id: {self.id} {self.actor}, {self.location}, {self.phone}" 
        
    

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())
    #relatioship
    auditions = relationship("Audition", back_populates="role")
    
    @property
    def actors(self):
        return [audition.actor for audition in self.auditions]


    @property
    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self):
        for audition in self.auditions:
            if audition.hired: 
                return audition  
        return "no actor has been hired for this role"  

    def understudy(self):
        hired_auditions = []  

        for audition in self.auditions:
            if audition.hired:
                hired_auditions.append(audition)  
        
        if len(hired_auditions) == 2:  
            return hired_auditions[1]  

        return "no actor has been hired for understudy for this role"  

        


    def __repr__(self):
        return f"{self.character_name}"

engine = create_engine("sqlite:///theatre_work.db")
Base.metadata.create_all(engine)


