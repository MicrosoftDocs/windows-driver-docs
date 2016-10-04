---
title: Building BDA Drivers
author: windows-driver-content
description: Building BDA Drivers
MS-HAID:
- 'bdabuild\_204783a0-9b51-4a0a-ac71-6b3e314476fb.xml'
- 'stream.building\_bda\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2272fa18-5102-443e-8728-f256444ab044
keywords: ["Broadcast Driver Architecture WDK AVStream , building drivers", "BDA WDK AVStream , building drivers", "building drivers WDK , BDA", "Build utility WDK , BDA", "macros WDK BDA"]
---

# Building BDA Drivers


## <a href="" id="ddk-building-bda-drivers-ksg"></a>


**Note**  Beginning with Windows 8, the WDK build environment no longer uses Build.exe. See [WDK and Visual Studio build environment](https://msdn.microsoft.com/library/windows/hardware/hh454286). The following discussion applies only if you build your driver using the WDK Windows 7 version or earlier.

 

You can use the Microsoft Windows Driver Kit (WDK) to build your Broadcast Driver Architecture (BDA) driver. To build a BDA driver, open a WDK build environment window, change to the appropriate BDA driver's source code subdirectory of the WDK's main source directory, and use the **build** command. The **build** command gets instructions on how to build the BDA driver from the *Sources* file that resides in the BDA driver's source code subdirectory.

For more information about the Build utility, the WDK's build environments, the macros and environment variables which control the Build utility, and the files that are required to build your BDA driver, see "Using the Build Utility" and "Build Utility Reference" in the Windows 7 WDK documentation (build 7600).

The following list contains the macro names to use in a BDA *Sources* file and discusses how to use them to build your BDA driver:

<a href="" id="--------targetname-------"></a> TARGETNAME   
Set to the BDA driver's name so that when the WDK builds the driver it is built with this name. The following code provides an example:

```
TARGETNAME=BDAsampl  # WDK builds the driver as BDAsampl.sys
```

<a href="" id="--------targetpath-------"></a> TARGETPATH   
Set the destination directory for the built driver. Note that depending on whether your build environment is "free" or "checked", you can use the BUILD\_ALT\_DIR variable to append "fre" or "chk" to the \\obj subdirectory that the build command creates under the directory containing the *Sources* file. The following code provides an example:

```
TARGETPATH=obj$(BUILD_ALT_DIR) # built driver in \objfre or \objchk
```

<a href="" id="--------targettype-------"></a> TARGETTYPE   
Set the type of file to build as a driver (as opposed to, for example, a program or DLL) as shown in the following code:

```
TARGETTYPE=DRIVER  # WDK builds the driver as *.sys
```

<a href="" id="--------targetlibs-------"></a> TARGETLIBS   
Point to the library files to which the BDA driver's sample source must link. A BDA driver must at least link to the libraries shown in the following code example:

```
TARGETLIBS=..\..\..\..\lib\ks.lib \
           ..\..\..\..\lib\ksguid.lib \
           ..\..\..\..\lib\BdaSup.lib
```

<a href="" id="--------includes---"></a> INCLUDES   
Point to a list of paths to search for the header files that the BDA driver's sample source requires in order to compile. The following code provides an example:

```
INCLUDES=..\..\..\..\inc; \
    $(DDK_INC_PATH)\wdm; 
```

<a href="" id="--------sources-------"></a> SOURCES   
Point to a list of source files that must be compiled to build the driver. The files must reside in the directory in which the *Sources* file resides. The following code provides an example:

```
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

```
DRIVERTYPE=WDM
```

<a href="" id="--------use-mapsym-------"></a> USE\_MAPSYM   
Generate *.sym* symbol files, in addition to the *.pdb* symbol files. These files map names to addresses. Setting this macro is required to debug on Windows 98/Me platforms. Set this macro as shown in the following example:

```
USE_MAPSYM=1
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Building%20BDA%20Drivers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


