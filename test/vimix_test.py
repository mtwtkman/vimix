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
    def setUp(self):
        self.project = 'hoge'
        self.project_dir = 'vim-hoge'
        self.autoload_path, self.doc_path, self.plugin_path = \
                {d: os.path.join(os.path.dirname(__file__), self.project_dir, d) for d in ['autoload', 'doc', 'plugin']}

    def test_vimix(self):
        """ run vimix function """

        vimix(self.project)
        self.assertTrue(os.path.exists(os.path.join(self.project_dir, self.autoload_path)))
        self.assertTrue(os.path.exists(os.path.join(self.project_dir, self.doc_path)))
        self.assertTrue(os.path.exists(os.path.join(self.project_dir, self.plugin_path)))

        self.assertTrue(os.path.isfile(os.path.join(self.project_dir, self.autoload_path, '{}.vim'.format(self.project))))
        self.assertTrue(os.path.isfile(os.path.join(self.project_dir, self.doc_path, '{}.txt'.format(self.project))))
        self.assertTrue(os.path.isfile(os.path.join(self.project_dir, self.plugin_path, '{}.vim'.format(self.project))))

        shutil.rmtree(self.project_dir)

if __name__ == '__main__':
    unittest.main(verbosity=2)
