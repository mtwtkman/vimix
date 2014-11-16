#!/usr/bin/env python

import unittest
import os
import sys
import shutil
from pathlib import Path

vimix_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(vimix_dir)

from vimix.vimix import vimix

class vimixTest(unittest.TestCase):

    def test_dirs_and_files_exists(self):
        ''' run vimix '''

        project = 'hoge'
        project_dir = 'vim-hoge'
        autoload_path, doc_path, plugin_path = \
                {d: os.path.join(os.path.dirname(__file__), project_dir, d) for d in ['autoload', 'doc', 'plugin']}
        vimix(project)

        self.assertTrue(os.path.exists(os.path.join(project_dir, autoload_path)))
        self.assertTrue(os.path.exists(os.path.join(project_dir, doc_path)))
        self.assertTrue(os.path.exists(os.path.join(project_dir, plugin_path)))

        self.assertTrue(os.path.isfile(os.path.join(project_dir, autoload_path, '{}.vim'.format(project))))
        self.assertTrue(os.path.isfile(os.path.join(project_dir, doc_path, '{}.txt'.format(project))))
        self.assertTrue(os.path.isfile(os.path.join(project_dir, plugin_path, '{}.vim'.format(project))))

        shutil.rmtree(project_dir)

if __name__ == '__main__':
    unittest.main(verbosity=2)
