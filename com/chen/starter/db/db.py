from sqlalchemy import Column, String, create_engine
from sqlalchemy import Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return 'id=%s, name=%s, address=%s, age=%s' % (self.id, self.name, self.address, self.age)

    def __init__(self, id, name, address, age):
        self.id = id
        self.name = name
        self.address = address
        self.age = age

# 创建数据库连接引擎
engine = create_engine('mysql+pymysql://root:chen@localhost:3306/test')
session = sessionmaker()
session.configure(bind=engine)

# # 1s创建sesseion添加数据
# DBSession = sessionmaker(bind = engine)


# session = DBSession()
#
# user01 = User(2, 'liang', 'chengdu', 22)
# user02 = User(3, 'liang2', 'chengdu2', 23)
#
# session.add(user01)
# session.add(user02)
#
# session.commit()
# session.close()
# print('add ok')

# 查询数据库对象
session1 = session()
user = session1.query(User).filter(User.id > 1).all()

for i in range(len(user)):
    userModel = user[i]
    print(user[i])
    # print('%s, %s, %s, %s'% (userModel.id, userModel.name, userModel.address, userModel.age))

session1.close()
print('query ok')


