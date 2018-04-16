#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os

class LibnameConan(ConanFile):
    name = "wink"
    version = "20180415"
    commit_id = "c29b1168044bf18e198816a64b03020462291300"
    url = "https://github.com/bincrafters/conan-libname"
    author = "Bincrafters <bincrafters@gmail.com>"
    description = "A fast template signal library, for C++, using the Fastest Possible C++ Delegates."
    no_copy_source = True

    # Indicates License type of the packaged library
    license = "MIT"

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/miguelmartin75/Wink-Signals"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.commit_id))
        extracted_dir = self.name + "-" + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def package(self):
        include_folder = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="license", src=self.source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)


    def package_id(self):
        self.info.header_only()
