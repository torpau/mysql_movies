import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = sa.create_engine(
    'mysql+mysqlconnector://root:s3cr37@127.0.0.1:6033/test_db'
)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class Testing(Base):
    __tablename__='testing_it'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    country = sa.Column(sa.String(50), nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.country}'


def main():
    #Base.metadata.create_all(engine)

    #testing_obj = Testing(name='Eva', country='Norge')
    #session.add(testing_obj)
    #session.commit()
    #print(testing_obj)

    #testing_obj = session.query(Testing).all()
    #for obj in testing_obj:
    #    print(obj)

    testing_obj = session.query(Testing).filter(Testing.id==2).first()
    print(testing_obj)


if __name__ == '__main__':
    main()
