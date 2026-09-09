### RPM external pluto-decayer 20260908
# Local review candidate; source publication is not yet approved.
%define source_base file:///mnt/vdb/Codes/cmssw_improve_gen/build/source-bundles
Source: %{source_base}/generator-integrations-%{realversion}.tar.gz
Requires: pythia8 root cmake

%prep
%setup -q -n generator-integrations-%{realversion}

%build
export PYTHIA8_ROOT ROOT_ROOT
bash packaging/build.sh %{i} pluto

%install
test -f %{i}/lib/libCMSPluto.so
test -f %{i}/lib/libPluto_rdict.pcm
test -f %{i}/etc/scram.d/pluto-decayer.xml
test ! -e %{i}/lib/libCMSPanScales.so
test ! -e %{i}/lib/libCMSDire.so
