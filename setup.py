from distutils.core import setup, Extension

module1 = Extension('_tkinter',
                    libraries=['tcl9.0', 'tcl9tk9.0'],
                    sources=['_tkinter.c'],
                    include_dirs=['/app/include/', '/usr/include/python3.13/internal/'])

setup(
    name='tkinter-standalone',
    version='3.13',
    description='Tkinter packaged as an external package for flatpak.',
    ext_modules=[module1],
    packages=["tkinter"]
)
