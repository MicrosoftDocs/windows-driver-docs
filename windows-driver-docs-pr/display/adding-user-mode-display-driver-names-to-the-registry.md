---
title: Adding User-Mode Display Driver Names to the Registry
description: Adding User-Mode Display Driver Names to the Registry
ms.assetid: 52f98ce5-4458-4058-9134-f57e4b56377f
keywords:
- INF files WDK display , user-mode driver names
- user-mode display drivers WDK Windows Vista , names added to registry
- registry WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adding User-Mode Display Driver Names to the Registry


You must set the following entry in an add-registry section of the INF file so that the names of user-mode display drivers are added to the registry during driver installation:

```
[Xxx_SoftwareDeviceSettings]
...
HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, UserModeDriverName1, UserModeDriverName2, UserModeDriverNameWow1, UserModeDriverNameWow2
```

For example, for x86 computers:

```
[Xxx_SoftwareDeviceSettings]
...
HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, r200umd 
```

For example, for x64 computers:

```
[Xxx_SoftwareDeviceSettings]
...
HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, r200umd, r200umdva, r200umd64, r200umd64va
```

Microsoft Windows Hardware Quality Labs (WHQL) test programs use the list of user-mode display driver names to validate that the driver binaries remain unchanged over a test run. Other applications might also use the list of user-mode display driver names, typically through [Implementing WMI](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI), as the list of files that the applications determine are part of the [driver package](https://msdn.microsoft.com/library/windows/hardware/ff539954).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Adding%20User-Mode%20Display%20Driver%20Names%20to%20the%20Registry%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




