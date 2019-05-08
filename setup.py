import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(
     name='GortzTools',
     version='0.1',
     scripts=['GortzTools'] ,
     author="Adrian Gortzak",
     author_email="addegor95@gmail.com",
     description="Tools for storing json data into mysql database",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Adddrian/GortzTools",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
