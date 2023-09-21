## HBNB - The Console
This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

### Repository Contents by Project Task

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/Githu77/AirBnB_clone_v2/blob/master/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/Githu77/AirBnB_clone_v2/tree/master/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/Githu77/AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/Githu77/AirBnB_clone_v2/blob/master/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/Githu77/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/Githu77/AirBnB_clone_v2/blob/master/models/__init__.py) [/models/base_model.py](https://github.com/Githu77/AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/Githu77/AirBnB_clone_v2/blob/master/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
...
