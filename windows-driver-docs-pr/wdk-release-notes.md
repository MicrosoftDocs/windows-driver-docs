---
title: Windows Drivers Kit (WDK) release notes
description: Highlights features in new WDK releases
ms.date: 11/04/2024
---

# Windows Driver Kits Release Notes
The following are features and bug fix in Windows 11 24H2 WDK update

## Version 10.0.26100.2161
*Released November 4th, 2024*.

### Kasan
New! The Kernel Address Sanitizer is a bug-detection technology supported on Windows Drivers that allows to detect several classes of illegal memory accesses. For more information [Kasan](./devtest/kasan.md)

### Azure File Sync reparse tag defination updated

### WDK MSI Update
The WDK VSIX is included as part of Visual Studio individual component. We have removed the WDK VSIX component which ships with WDK MSI. At the end of WDK installation, the custom action message to launch VSIX installer has been replaced with a simple message telling the user to install VSIX from VS as individual component. 

## Version 10.0.26100.1882
*Released October 14th, 2024*.

### Audio Headers
Added AudioAggregation.h and AudioSensors.h for enabling SoundWire Device Class for Audio (SDCA) speaker aggregation and ultrasound support.

### EWDK VS Build Tools
The Visual Studio Build tools in EWDK have been updated to version 17.10.5.

## Version 10.0.26100.1591
*Released September 18th, 2024*.

### WDK VSIX installation

The WDK VSIX has been added as a Visual Studio individual component starting with the VS 17.11 release. For more information, see the [Windows Drivers Kits download page](download-the-wdk.md).

![screenshot of visual studio wdk individual component selected](images/vs-wdk-selection.png)

### Static Tools Logo - Creating a Driver Verification Log

To create a Driver Verification Log (DVL) for the Static Tools Logo Test, see the [Creating a Driver Verification Log](./develop/creating-a-driver-verification-log.md) article.

Navigating to **Extensions > Drivers > Create Driver Verification Log** in Visual Studio will now trigger the redirection message below.

![screenshot of visual studio notification for codeql dvl generation](images/codeql-redirection.png)

### Static Tools Logo - Placement requirement for CodeQL Sarif file

The process of generating DVL for CodeQL previously required placing the SARIF file in the same directory as the VCXProj file for the driver project. Recognizing the inconvenience this posed for developers, we have eliminated this requirement. Now users can generate the DVL and save it in any location of their choice by using this command:

```cmd
C:\Program Files (x86)\Windows Kits\10\Tools\dvl\dvl.exe" /manualCreate `<driverName>` `<driverArchitecture>` /`<path to sarif file>`'\
```

![screenshot of sarif placement updated](images/sarif-placement-update.png)

### UMDF WiFiCX drivers

To support UMDF WiFiCX drivers, we have added UMDF public header and library support. These changes ensure that WiFiCX drivers leverage the [advantages of writing UMDF drivers](./wdf/advantages-of-writing-umdf-drivers.md). The following updates have been made:

- Created a new UMDF version of WifiCxTlvGenParse.lib.

- Created UMDF equivalents of KMDF's dot11wificxintf.h, dot11wificxtypes.hpp, and WifiCxTlvGenParse.lib.

### Bug fixes for Device Fundamentals and WDTF test framework

Bugs associated with DevFund tests were fixed, this change improves the WDK bring up experience.


