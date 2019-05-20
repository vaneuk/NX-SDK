### Spec file auto-generated by rpm_gen.py...

%define APP_NAME pbwMonitor

%define APP_DESC RPM package for custom application

%define APP_TARGET /NX-SDK/examples/python/pbwMonitor

%define NXSDK_ROOT /NX-SDK

%define RELEASE_VERSION 1.0.0

%define APP_SOURCE /NX-SDK/examples/python

%define APP_VERSION 1.0

#####################################################################
########### Do not update beyond this point.#########################
#####################################################################
%define TARGET_DIR    /isan/bin/nxsdk
%define CURR_DIR      %(pwd)

Summary: Custom Application
Name: %{APP_NAME}
Version: %{APP_VERSION}
Release: %{RELEASE_VERSION}
Group: Development/Tools
License: Propreitary
URL: None


##Source: %{APP_SOURCE}
BuildRoot: %{NXSDK_ROOT}
 
%description
%{APP_DESC}
 
%prep
 
%build
### If needed you can make the application here as well.
#cd $NXSDK_ROOT
#%make clean
#%make all
#cd $CURR_DIR
 
%install
rm -rf "$RPM_BUILD_ROOT/%{TARGET_DIR}"
mkdir -p "$RPM_BUILD_ROOT/%{TARGET_DIR}"
cp -R %{APP_TARGET} "$RPM_BUILD_ROOT/%{TARGET_DIR}"
 
%clean
rm -rf "$RPM_BUILD_ROOT/%{TARGET_DIR}"
 
%files
%{TARGET_DIR}
 
%changelog
