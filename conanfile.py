# conan-parse conanfile.py
from conans import ConanFile, CMake

class CParseConan(ConanFile):
    name = "CParser"
    version = "1.0"
    license = "MIT"
    exports = "CMakeLists.txt"
    generators = "cmake", "txt"
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        # this will create a cparse subfolder, take it into account
        self.run("git clone https://github.com/cparse/cparse.git")

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst=".", src="cparse")
        self.copy("*.cpp", dst=".", src="cparse")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["CParser"]
