#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_do_create_no_params(self):
        """ Test 'create' command with no parameters """
        console = HBNBCommand()
        console.onecmd("create BaseModel")
        self.assertTrue(len(storage.all("BaseModel")) != 0)
    
    def test_do_create_with_string_param(self):
        """ Test 'create' command with a string parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel name="John_Doe"')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == "John Doe" for obj in objects.values()))

    def test_do_create_with_integer_param(self):
        """ Test 'create' command with an integer parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel age=30')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.age == 30 for obj in objects.values()))

    def test_do_create_with_float_param(self):
        """ Test 'create' command with a float parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel score=99.5')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.score == 99.5 for obj in objects.values()))

    def test_do_create_with_invalid_param(self):
        """ Test 'create' command with an invalid parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel invalid_param')
        objects = storage.all("BaseModel")
        self.assertFalse(any('invalid_param' in obj.to_dict() for obj in objects.values()))

    def test_do_create_with_float_param(self):
        """ Test 'create' command with a float parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel score=99.5')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.score == 99.5 for obj in objects.values()))

    def test_do_create_with_invalid_param(self):
        """ Test 'create' command with an invalid parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel invalid_param')
        objects = storage.all("BaseModel")
        self.assertFalse(any('invalid_param' in obj.to_dict() for obj in objects.values()))\

    def test_do_create_multiple_params(self):
        """ Test 'create' command with multiple parameters """
        console = HBNBCommand()
        console.onecmd('create BaseModel name="John_Doe" age=30 score=99.5')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == "John Doe" and obj.age == 30 and obj.score == 99.5 for obj in objects.values()))

    def test_do_create_with_escaped_string(self):
        """ Test 'create' command with a string containing an escaped quote """
        console = HBNBCommand()
        console.onecmd('create BaseModel name="John_\\"Doe\\"_Smith"')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == 'John "Doe" Smith' for obj in objects.values()))

    def test_do_create_with_nonexistent_class(self):
        """ Test 'create' command with a nonexistent class """
        console = HBNBCommand()
        console.onecmd('create NonexistentClass')
        self.assertTrue(len(storage.all("NonexistentClass")) == 0)

    def test_do_create_with_special_chars(self):
        """ Test 'create' command with a string containing special characters """
        console = HBNBCommand()
        console.onecmd('create BaseModel name="John_@#%_Doe"')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == 'John @#% Doe' for obj in objects.values()))

    def test_do_create_with_empty_string(self):
        """ Test 'create' command with an empty string parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel name=""')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == '' for obj in objects.values()))

    def test_do_create_with_spaces_in_string(self):
        """ Test 'create' command with a string containing spaces """
        console = HBNBCommand()
        console.onecmd('create BaseModel name="John_ _Doe"')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.name == 'John  Doe' for obj in objects.values()))

    def test_do_create_with_negative_integer(self):
        """ Test 'create' command with a negative integer parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel age=-30')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.age == -30 for obj in objects.values()))

    def test_do_create_with_zero_integer(self):
        """ Test 'create' command with a zero integer parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel age=0')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.age == 0 for obj in objects.values()))

    def test_do_create_with_large_integer(self):
        """ Test 'create' command with a large integer parameter """
        console = HBNBCommand()
        console.onecmd('create BaseModel age=1000000')
        objects = storage.all("BaseModel")
        self.assertTrue(any(obj.age == 1000000 for obj in objects.values()))
