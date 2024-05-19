#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
import MySQLdb
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage():
    __engine = None
    __session = None
    hbnb_env = os.environ.get("HBNB_ENV")
    mysql_user = os.environ.get("HBNB_MYSQL_USER")
    mysql_pwd = os.environ.get("HBNB_MYSQL_PWD")
    mysql_host = os.environ.get("HBNB_MYSQL_HOST")
    mysql_db = os.environ.get("HBNB_MYSQL_DB")

    def __init__(self):
        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(self.mysql_user,
                                                      self.mysql_pwd,
                                                      self.mysql_host,
                                                      self.mysql_db)
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        if self.hbnb_env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """

        classes = {'State': State, 'City': City,
                   'User': User, 'Place': Place,
                   'Review': Review, 'Amenity': Amenity}
        result = {}
        if cls and cls in classes:
            cls = classes[cls]
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj
        else:
            for cls, class_obj in classes.items():
                objects = self.__session.query(class_obj).all()
                for obj in objects:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """
        add the object to the current
        database session (self.__session)
        """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """
        commit all changes of the
        current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy)
        (WARNING: all classes who inherit from Base must be imported before
        calling Base.metadata.create_all(engine)
        """
        from models.state import State
        from models.city import City
        Base.metadata.create_all(bind=self.__engine)
        ssion = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ssion)
        self.__session = Session

    @property
    def _FileStorage__objects(self):
        """
        Returns a dictionary of all objects
        in the format of _FileStorage__objects
        """
        return self.all()

    def close(self):
        """permanently removes a scoped_session from registry thus removing
        all connections and returning them to their pool
        """
        self.__session.remove()
