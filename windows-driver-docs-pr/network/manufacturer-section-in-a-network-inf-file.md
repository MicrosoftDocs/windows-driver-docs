---
title: Manufacturer Section in a Network INF File
description: How to create the manufacturer section of a network INF file.
ms.date: 04/17/2023
---

# Manufacturer Section in a Network INF File

The Manufacturer section in a network INF file is based on the generic [**INF Manufacturer section**](../install/inf-manufacturer-section.md).

Starting with Windows OS build version 25319, you can create a network driver package that can be executed from the [Driver Store](../develop/run-from-driver-store.md). An INF that is using 'run from Driver Store' means that the INF uses [**DIRID 13**](../install/using-dirids.md) to specify the location for [driver package](../install/driver-packages.md) files on install. 

You can't install a driver package through the network configuration interfaces and use the driver store feature on older Windows versions. To successfully install the driver package in this scenario, you need to have a minimum OS build number of 25319.

To use DIRID 13 for installation in newer builds, it's useful to create an INF Manufacturer section that includes multiple *models-section-name* entries that specify target operating system versions. Different [**INF _Models_ sections**](../install/inf-models-section.md) can be specified for different versions of the operating system. The *models-section-name* entries indicate operating system versions with which the INF **_Models_** sections are used.

The following example shows how to create an OS-specific INF Manufacturer section using two *models-section-name* entries. OS builds 25319 and later will use ``MyMfg.NT$ARCH$.10.0...25319``. All other builds will use ``MyMfg.NT$ARCH$``. This example uses build 25319 because it's the first build that allows for installation using DIRID 13. 

```inf
[Manufacturer]
%ManufacturerName%=Standard,NT$ARCH$,NT$ARCH$.10.0...25319 

[Standard.NT$ARCH$.10.0...25319]
%NDISPROT_Desc%=InstallA, MS_NDISPROT

[Standard.NT$ARCH$]
%NDISPROT_Desc%=InstallB, MS_NDISPROT

[InstallA]    ; OS build numbers 25319 and higher
AddReg=Inst_Ndi
Characteristics=0x0 ; 
CopyFiles=CpyFiles_Sys_A

[InstallB]    ; OS build numbers lower than 25319
AddReg=Inst_Ndi
Characteristics=0x0 ; 
CopyFiles=CpyFiles_Sys_B
```

For an example of how an OS-specific Manufacturer section can allow for installation using DIRID 13 for new builds and DIRID 12 for older builds, see the [Sample NDIS Protocol Driver](https://github.com/microsoft/Windows-driver-samples/blob/main/network/ndis/ndisprot/6x/sys/630/ndisprot630.inf).