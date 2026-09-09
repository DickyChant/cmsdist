### RPM external more-showers 20260908
# Local review candidate; source publication is not yet approved.
%define source_base file:///mnt/vdb/Codes/cmssw_improve_gen/build/source-bundles
Source: %{source_base}/generator-integrations-%{realversion}.tar.gz
Requires: pythia8 gsl OpenBLAS cmake

%prep
%setup -q -n generator-integrations-%{realversion}

%build
export PYTHIA8_ROOT GSL_ROOT OPENBLAS_ROOT
bash packaging/build.sh %{i} more-showers

%install
test -f %{i}/lib/libCMSPanScales.so
test -f %{i}/lib/libCMSDire.so
test -f %{i}/share/CMSDire/DireShowers.xml
test -f %{i}/etc/scram.d/more-showers.xml
test ! -e %{i}/lib/libCMSPluto.so
