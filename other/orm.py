import sqlalchemy as sa
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base=declarative_base()

pymysql.install_as_MySQLdb()
engine=sa.create_engine("mysql://root:123456@localhost/test",
                                                      echo=True)
Session=sessionmaker(bind=engine)

session=Session()

class RelationShip(Base):
    __tablename__="relationship"

    user_id=sa.Column(sa.BigInteger,sa.ForeignKey("user.id"),primary_key=True)
    msg_id=sa.Column(sa.BigInteger,sa.ForeignKey("msg.id"),primary_key=True)

    data=sa.Column("data",sa.String(20))


class User(Base):
    __tablename__="user"

    id=sa.Column("id",sa.BigInteger,primary_key=True)
    name=sa.Column("name",sa.String(20))

    msg_relation=sa.orm.relationship(RelationShip,
                                     backref=sa.orm.backref('user_relation',lazy="joined"),lazy="select")

    def __init__(self,rawdata=None,**kwargs):
        super().__init__(**kwargs)

    def _handle_data(self):
        pass

class Msg(Base):
    __tablename__="msg"

    id=sa.Column("id",sa.BigInteger,primary_key=True)
    content=sa.Column("content",sa.String(200))
    user_id=sa.Column(sa.BigInteger,sa.ForeignKey("user.id"))
    user=sa.orm.relationship(User,back_populates="msg")
    user_relation=sa.orm.relationship(RelationShip,
                                     backref=sa.orm.backref('msg_relation',lazy="joined"),lazy="select")


User.msg=sa.orm.relationship(Msg,lazy="dynamic")


def test_add():
    user=User(id=12345678901,name="jdfi")
    print(user.id)
    session.add(user)
    print(session.new)
    print(session.dirty)
    session.commit()


def test_query():
    user_query=session.query(User).filter(User.name == None ).all()
    for user in user_query:
        all=user.msg.all()
        for i in all:
            print(i.id,i.content)
        # print(i.msg[0].user.id)


def test_create_schame():
    User.__table__.create(engine,checkfirst=True)
    Msg.__table__.create(engine,checkfirst=True)
    RelationShip.__table__.create(engine,checkfirst=True)


def test_relationship():

    #one to many
    def one_to_many():
        user1=User()
        user1.msg.append(Msg(content="hello world"))
        user1.msg.append(Msg(content="hello world"))
        user1.msg.append(Msg(content="hello world"))
        session.add(user1)
        session.commit()
        print(user1.msg)

    #many to many
    def many_to_many():
        user=session.query(User).first()
        l=map(lambda x:x.msg_relation,user.msg_relation)
        for i in l:
            print(i.id,i.content)




    many_to_many()
def test_insert_data():
    for i in range(1,10):
        for j in range(127,132):
            t=RelationShip(user_id=i,msg_id=j)
            session.add(t)
    session.commit()

def test():
    # test_relationship()
    pass
    # test_create_schame()
    test_query()
    # test_insert_data()


if __name__=="__main__":
    test()