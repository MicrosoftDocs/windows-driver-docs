---
title: Manufacturer Section in a Network INF File
description: How to create the manufacturer section of a network INF file.
ms.date: 04/12/2023
---

# Manufacturer Section in a Network INF File

The Manufacturer section in a network INF file is based on the generic [INF Manufacturer section](../install/inf-manufacturer-section.md).

Starting with Windows OS build version 25319, you can create a network driver package that can be executed from the [Driver Store](../develop/run-from-driver-store.md). An INF that is using 'run from Driver Store' means that the INF uses [**DIRID 13**](../install/using-dirids.md) to specify the location for [driver package](../install/driver-packages.md) files on install.

You can't install a driver package through the network configuration interfaces and use the driver store feature on older Windows versions. To successfully install the driver package in this scenario, you need to have a minimum OS build number of 25319.


To use DIRID 13, include the following section in the INF file:

```cpp
[Standard.NT$ARCH$.10.0...25319]
%NDISPROT_Desc%=Install, MS_NDISPROT
```

To use DIRID 12, include the following section in the INF file:

```cpp
[Standard.NT$ARCH$]
%NDISPROT_Desc%=Install_NC, MS_NDISPROT
```

To allow your driver to install using DIRID 12 or DIRID 13 depending on the OS build number that the driver is being installed on, include both sections in the INF file. 

The following example show a skeletal INF file with a variety of OS-specific INF Models sections:

```inf
[Manufacturer]
%ManufacturerName%=Standard,NT$ARCH$,NT$ARCH$.10.0...25319 

[Standard.NT$ARCH$.10.0...25319]
%NDISPROT_Desc%=Install, MS_NDISPROT

[Standard.NT$ARCH$]
%NDISPROT_Desc%=Install_NC, MS_NDISPROT

[Install]    ; OS build numbers 25319 and higher
AddReg=Inst_Ndi
Characteristics=0x0 ; 
CopyFiles=CpyFiles_Sys

[Install_NC]    ; OS build numbers lower than 25319
AddReg=Inst_Ndi
Characteristics=0x0 ; 
CopyFiles=CpyFiles_Sys_NC
```

