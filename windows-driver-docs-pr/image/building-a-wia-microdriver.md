---
title: Building a WIA Microdriver
description: Building a WIA Microdriver
ms.date: 03/27/2023
---

# Building a WIA Microdriver

> [!IMPORTANT]
> This article contains information that applies to obsolete Windows operating systems.

The following header files and library files are required by all WIA microdrivers.

## Header Files

All WIA microdrivers must include the header files that are shown in the following table.

| Header File | Description |
|--|--|
| *wiamicro.h* | Defines the function prototypes and structures that the WIA microdriver requires. |

WIA microdrivers may require additional header files. The headers that are required depend on the device type and the functionality that is implemented. These requirements are noted in the reference section.

### Library Files

WIA uses the library files shown in the following table.

| Library File | Description |
|--|--|
| *wiaguid.lib* | Exports class identifiers (CLSIDs) and interface identifiers (IIDs). All WIA microdrivers require this library. |

In your build environment, the WDK *Include* and *Lib* directories should be the first directories in the search path. This ensures that you are using the most recent versions of the headers and library files.

If you wish to use logging with Visual C++ 6.0 when building a microdriver, turn on logging for *Wiafbdrv.dll* by using the *Wialogcfg.exe* program that came with the Windows Me Driver Development Kit (DDK). Also, check the INF file to make sure that the microdriver name is correct. In the INF, check the **DeviceData** section for MicroDriver="YOURNAME.DLL".
