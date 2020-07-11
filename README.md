# AirBnb_clone - Console

### Description
AirBnb_Clone console is a Command interpreter that will manage AirBnB Objects for a full-scale clone of the
AirBnB website.

## Usage

### Interactive Mode

$ ./console.py
(hbnb) help

Documented Commands (type help <topic>)

========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

### Non-Interactive Mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
 
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
 
========================================
EOF  help  quit
(hbnb) 
$
