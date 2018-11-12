---
title: Adding User-Mode Display Driver Names to the Registry
description: Adding User-Mode Display Driver Names to the Registry
ms.assetid: 52f98ce5-4458-4058-9134-f57e4b56377f
keywords:
- INF files WDK display , user-mode driver names
- user-mode display drivers WDK Windows Vista , names added to registry
- registry WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding User-Mode Display Driver Names to the Registry


You must set the following entry in an add-registry section of the INF file so that the names of user-mode display drivers are added to the registry during driver installation:

```inf
[Xxx_SoftwareDeviceSettings]
...
HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, UserModeDriverName1, UserModeDriverName2, UserModeDriverNameWow1, UserModeDriverNameWow2
```

For example, for x86 computers:

```inf
[Xxx_SoftwareDeviceSettings]
...
HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, r200umd 
```

For example, for x64 computers:

```inf
[Xxx_SoftwareDeviceSettings]
...
HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, r200umd, r200umdva, r200umd64, r200umd64va
```

Microsoft Windows Hardware Quality Labs (WHQL) test programs use the list of user-mode display driver names to validate that the driver binaries remain unchanged over a test run. Other applications might also use the list of user-mode display driver names, typically through [Implementing WMI](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI), as the list of files that the applications determine are part of the [driver package](https://msdn.microsoft.com/library/windows/hardware/ff539954).

 

 





