from conans import ConanFile, tools
import os

required_conan_version = ">=1.33.0"


class VcglibConan(ConanFile):
    name = "vcglib"
    description = "Library for manipulation, processing, cleaning, simplifying triangle meshes."
    license = "GPL-3.0-only"
    topics = ("conan", "vcglib", "mesh")
    homepage = "https://github.com/cnr-isti-vclab/vcglib"
    url = "https://github.com/conan-io/conan-center-index"

    exports_sources = "patches/**"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def requirements(self):
        self.requires("eigen/3.3.9")

    def package_id(self):
        self.info.header_only()

    def source(self):
        tools.get(**self.conan_data["sources"][self.version],
                  destination=self._source_subfolder, strip_root=True)

    def build(self):
        for patch in self.conan_data.get("patches", {}).get(self.version, []):
            tools.patch(**patch)

    def package(self):
        self.copy("LICENSE.txt", dst="licenses", src=self._source_subfolder)
        self.copy("*", dst=os.path.join("include", "vcg"), src=os.path.join(self._source_subfolder, "vcg"))
        self.copy("*", dst=os.path.join("include", "wrap"), src=os.path.join(self._source_subfolder, "wrap"))
        self.copy("*", dst=os.path.join("include", "img"), src=os.path.join(self._source_subfolder, "img"))
