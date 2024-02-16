# Welcome to the AirBnB clone project! <sub>The  Console</sub>

This is the first step towards building the first full web application: the AirBnB clone.
![AirBnB](image.png)

#### Resources provided by ALX:

* [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
* [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
* [packages concept page]()
* [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
* [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
* [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
* [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
* [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
* [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
* [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)

## Learning Objectives

### General

* How to create a Python package
* How to create a command interpreter in Python using the <code>cmd</code> module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage <code>datetime</code>
* What is an <code>UUID</code>
* What is <code>*args</code> and how to use it
* What is <code>**kwargs</code> and how to use it
* How to handle named arguments in a function

```
./console.py
(hbnb)
(hbnb)
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help all
 Prints all string representation of all instances.
(hbnb) help destroy
 Deletes an instance & save the change into the JSON file.
(hbnb) create User
acc18e68-0c86-47f3-8b25-4a83322db9a6
(hbnb)
(hbnb)
(hbnb) show User acc18e68-0c86-47f3-8b25-4a83322db9a6
[User] (acc18e68-0c86-47f3-8b25-4a83322db9a6) {'id': 'acc18e68-0c86-47f3-8b25-4a83322db9a6', 'created_at': datetime.datetime(2024, 2, 12, 22, 41, 4, 868042),
 'updated_at': datetime.datetime(2024, 2, 12, 22, 41, 4, 868071)}
(hbnb)
(hbnb)
(hbnb) all User
["[User] (acc18e68-0c86-47f3-8b25-4a83322db9a6) {'id': 'acc18e68-0c86-47f3-8b25-4a83322db9a6', 'created_at': datetime.datetime(2024, 2, 12, 22, 41, 4, 868042),
 'updated_at': datetime.datetime(2024, 2, 12, 22, 41, 4, 868071)}"]
(hbnb) destroy User acc18e68-0c86-47f3-8b25-4a83322db9a6
(hbnb) destroy User 4199194d-a858-4d1b-9b00-d425db78ed71
(hbnb)
(hbnb) all User
[]
(hbnb)
(hbnb) quit
```
