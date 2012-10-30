'''
  Created on 29/10/2012.

  Setup script for islandora_file_system_summarizer.

  @author
    William Panting
'''
import os, py2exe
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'islandora_file_system_summarizer',
      version = '0.1',
      description = 'Will populate Islandora file system summaries.',
      author = 'William Panting',
      author_email = 'will@discoverygarden.ca',
      license = "GPL",
      console = {'islandora_file_system_summarizer.py'},
      long_description = read('README'),
      install_requires = ['distutils','py2exe'])
