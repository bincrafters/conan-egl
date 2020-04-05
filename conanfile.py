from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration
import os


class EglConan(ConanFile):
    name = "egl"
    # version = "virtual"
    description = "Virtual package for EGL"
    topics = ("conan", "opengl", "gl", "glu", "utility")
    url = "https://github.com/bincrafters/conan-egl"
    homepage = "https://www.khronos.org/egl"
    license = "None"  # TODO: Relax hooks about license attribute for virtual packages? How?

    # TODO: Add check if system_libs are installed if provider=system?
    # TODO: Write a test_package
    # TODO: Should this depend on our OpenGL ES packages? If yes, what version(s)?

    settings = {"os"}
    options = {
        # Leave this so it can be potentially extended in the future
        # and for consistency with other virtual packages
        "provider": ["system"],
    }
    default_options = {
        "provider": "system",
    }

    def configure(self):
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration("This package only supports Linux right now. Contributions welcome!")

    def system_requirements(self):
        if self.options.provider == "system":
            # Note: If you want to disable installation on your system
            # set CONAN_SYSREQUIRES_MODE to disabled
            if self.settings.os == "Linux" and tools.os_info.is_linux:
                if tools.os_info.with_apt or tools.os_info.with_yum:
                    installer = tools.SystemPackageTool()
                    packages = []
                    packages_apt = ["libegl1-mesa-dev"]
                    packages_yum = ["mesa-libEGL-devel"]

                    if tools.os_info.with_apt:
                        packages = packages_apt
                    elif tools.os_info.with_yum:
                        packages = packages_yum
                    for package in packages:
                        installer.install(package)
           
    def package_info(self):
        if self.options.provider == "system":
            if self.settings.os == "Linux":
                self.cpp_info.system_libs.append("EGL")
