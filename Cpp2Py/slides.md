---
customTheme : "flatiron"
---

## Interfacing C++ and Python

[Cpp2Py - github.com/TRIQS/cpp2py](https://github.com/TRIQS/cpp2py)


### Cpp2Py Setup

```bash
# Clone the repository
git clone https://github.com/TRIQS/cpp2py cpp2py.src

# Build and install
mkdir cpp2py.build && cd cpp2py.build
cmake ../cpp2py.src -DCMAKE_INSTALL_PREFIX=path_to_install
make install

# Load installation into environment
source path_to_install/share/cpp2pyvars.sh
```


### An Example --- `simple.hpp`
```cpp
#include <vector>

/// A Simple class
class myclass {

  int a = 35, b = 3, c = 5;

  public:
  myclass() = default;

  /// Return a vector with all members
  std::vector<int> list_of_members() const { return {a, b, c}; }
};
```

Just run c++2py on the source file
```bash
$ c++2py simple.hpp
Welcome to C++2py
Parsing the C++ file (may take a few seconds) ...
... done.

Analysing dependencies
Wrapping classes:
    myclass
Generating simple_desc.py
```


### The descriptor file --- `simple_desc.py`

```python
# Generated automatically using the command :
# c++2py simple.cpp --target_file_only
from cpp2py.wrap_generator import *

# The module
module = module_(full_name = "simple", doc = r"", app_name = "simple")

# Add here all includes
module.add_include("simple.cpp")

# Add here anything to add in the C++ code at the start, e.g. namespace using
module.add_preamble("""
#include <cpp2py/converters/vector.hpp>

""")

# The class myclass
c = class_(
        py_type = "Myclass",  # name of the python class
        c_type = "myclass",   # name of the C++ class
        doc = r"""A Simple class""",   # doc of the C++ class
        hdf5 = False,
)

c.add_constructor("""()""", doc = r"""""")

c.add_method("""std::vector<int> list_of_members ()""",
             doc = r"""Return a vector with all members""")

module.add_class(c)

module.generate_code()
```


### Compile the module

```bash
# Generate the wrapper code from the desc file
python simple_desc.py simple_wrap.hxx

# Compile the wrapper code into a module
$ g++ -shared -o simple.so -lcpp2py -lpython2.7
```


### Import and use

```python
from simple import Myclass
print Myclass().get_sum()

----- Output ------
42
```


### Some useful options (c.f. `c++2py --help`)

* `--target_file_only` --- No recursion into includes
* `-N mynamespace` --- Filter by Namespace
* `-I somedir` --- Add include directories
* `--cxxflags "flags"` --- Add compile flags
* `-C pytriqs` --- Include converters for TRIQS objects
* `-r my_desc.py` --- Regenerate a file


## Real-World Examples

* [app4triqs Skeleton --- github.com/triqs/app4triqs](https://github.com/triqs/app4triqs)
* [TRIQS CTHyb --- triqs.github.io/cthyb](https://triqs.github.io/cthyb/2.1.x/guide/aim.html)