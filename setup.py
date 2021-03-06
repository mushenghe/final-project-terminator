# Python setup file used for installing a python catkin package.
# See http://docs.ros.org/melodic/api/catkin/html/user_guide/setup_dot_py.html
# For catkin to use this we have called python_catkin_setup() in CMakeLists.txt
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['terminator'],
    package_dir={'': 'src'})

setup(**setup_args)
