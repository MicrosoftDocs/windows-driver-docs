---
title: Building BDA Drivers
description: Building BDA Drivers
ms.assetid: 2272fa18-5102-443e-8728-f256444ab044
keywords:
- Broadcast Driver Architecture WDK AVStream , building drivers
- BDA WDK AVStream , building drivers
- building drivers WDK , BDA
- Build utility WDK , BDA
- macros WDK BDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Building BDA Drivers





**Note**  Beginning with Windows 8, the WDK build environment no longer uses Build.exe. See [WDK and Visual Studio build environment](https://msdn.microsoft.com/library/windows/hardware/hh454286). The following discussion applies only if you build your driver using the WDK Windows 7 version or earlier.

 

You can use the Microsoft Windows Driver Kit (WDK) to build your Broadcast Driver Architecture (BDA) driver. To build a BDA driver, open a WDK build environment window, change to the appropriate BDA driver's source code subdirectory of the WDK's main source directory, and use the **build** command. The **build** command gets instructions on how to build the BDA driver from the *Sources* file that resides in the BDA driver's source code subdirectory.

For more information about the Build utility, the WDK's build environments, the macros and environment variables which control the Build utility, and the files that are required to build your BDA driver, see "Using the Build Utility" and "Build Utility Reference" in the Windows 7 WDK documentation (build 7600).

The following list contains the macro names to use in a BDA *Sources* file and discusses how to use them to build your BDA driver:

<a href="" id="--------targetname-------"></a> TARGETNAME   
Set to the BDA driver's name so that when the WDK builds the driver it is built with this name. The following code provides an example:

```make
TARGETNAME=BDAsampl  # WDK builds the driver as BDAsampl.sys
```

<a href="" id="--------targetpath-------"></a> TARGETPATH   
Set the destination directory for the built driver. Note that depending on whether your build environment is "free" or "checked", you can use the BUILD\_ALT\_DIR variable to append "fre" or "chk" to the \\obj subdirectory that the build command creates under the directory containing the *Sources* file. The following code provides an example:

```make
TARGETPATH=obj$(BUILD_ALT_DIR) # built driver in \objfre or \objchk
```

<a href="" id="--------targettype-------"></a> TARGETTYPE   
Set the type of file to build as a driver (as opposed to, for example, a program or DLL) as shown in the following code:

```make
TARGETTYPE=DRIVER  # WDK builds the driver as *.sys
```

<a href="" id="--------targetlibs-------"></a> TARGETLIBS   
Point to the library files to which the BDA driver's sample source must link. A BDA driver must at least link to the libraries shown in the following code example:

```make
TARGETLIBS=..\..\..\..\lib\ks.lib \
           ..\..\..\..\lib\ksguid.lib \
           ..\..\..\..\lib\BdaSup.lib
```

<a href="" id="--------includes---"></a> INCLUDES   
Point to a list of paths to search for the header files that the BDA driver's sample source requires in order to compile. The following code provides an example:

```make
INCLUDES=..\..\..\..\inc; \
    $(DDK_INC_PATH)\wdm; 
```

<a href="" id="--------sources-------"></a> SOURCES   
Point to a list of source files that must be compiled to build the driver. The files must reside in the directory in which the *Sources* file resides. The following code provides an example:

```make
SOURCES= \
    ObjDesc.cpp     \
    inpin.cpp     \
    outpin.cpp    \
    Filter.cpp      \
    Device.cpp      \
    bdaguid.c       \
    BDAsampl.rc
```

<a href="" id="--------drivertype-------"></a> DRIVERTYPE   
Set type of driver to WDM as shown in the following code:

```make
DRIVERTYPE=WDM
```

<a href="" id="--------use-mapsym-------"></a> USE\_MAPSYM   
Generate *.sym* symbol files, in addition to the *.pdb* symbol files. These files map names to addresses. Setting this macro is required to debug on Windows 98/Me platforms. Set this macro as shown in the following example:

```make
USE_MAPSYM=1
```
