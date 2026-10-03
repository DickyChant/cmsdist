### RPM external hepmc3 3.3.1
## INCLUDE cpp-standard
Source: https://gitlab.cern.ch/hepmc/HepMC3/-/archive/%{realversion}/HepMC3-%{realversion}.tar.gz
# no HepMC:: compatibility typedefs in the rootIO dictionary: they clash with HepMC2's HepMC::FourVector
Patch0: hepmc3-3.3.1-rootio-dict

BuildRequires: cmake gmake
Requires: zlib bz2lib xz zstd root

%define drop_files %i/share/doc

%prep
%setup -q -n HepMC3-%{realversion}
%patch0 -p1

%build
rm -rf ../build
mkdir ../build
cd ../build

cmake ../HepMC3-%{realversion} \
  -DCMAKE_INSTALL_PREFIX="%i" \
  -DCMAKE_BUILD_TYPE=%{cmake_build_type} \
  -DCMAKE_CXX_STANDARD=%{cms_cxx_standard} \
  -DHEPMC3_CXX_STANDARD=%{cms_cxx_standard} \
  -DHEPMC3_ENABLE_ROOTIO="ON" \
  -DHEPMC3_ENABLE_TEST="ON" \
  -DHEPMC3_TEST_THREADS="ON" \
  -DHEPMC3_TEST_HEPMC2="OFF" \
  -DHEPMC3_TEST_VALGRIND="OFF" \
  -DHEPMC3_TEST_ZLIB="ON" \
  -DHEPMC3_TEST_LZMA="ON" \
  -DHEPMC3_TEST_BZIP2="ON" \
  -DHEPMC3_TEST_ZSTD="ON" \
  -DHEPMC3_ENABLE_PYTHON="OFF" \
  -DHEPMC3_BUILD_STATIC_LIBS="OFF" \
  -DHEPMC3_BUILD_DOCS="OFF" \
  -DHEPMC3_INSTALL_INTERFACES="ON" \
  -DCMAKE_PREFIX_PATH="%{cmake_prefix_path}" \
  -L

make %{makeprocesses} VERBOSE=1

%install
cd ../build
make install VERBOSE=1
# libHepMC3rootIO is loaded on demand by HepMC3::deduce_reader, so its rootmap is not needed;
# CMSSW dictionaries already declare the HepMC3 data classes, and a second rootmap would make
# ROOT warn about them at the start of every job
rm -f %i/lib*/libHepMC3rootIO.rootmap
