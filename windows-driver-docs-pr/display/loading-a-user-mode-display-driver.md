---
title: Loading a User-Mode Display Driver
description: Loading a User-Mode Display Driver
ms.assetid: bfebe590-bcde-40cf-9074-8d0f63e0562d
keywords:
- INF files WDK display , user-mode driver loading
- user-mode display drivers WDK Windows Vista , loading
- loading drivers WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Loading a User-Mode Display Driver


You must set the following entry in an add-registry section of the INF file so that the user-mode display driver's DLL name is added to the registry during driver installation and so that the Microsoft Direct3D runtime can subsequently load the DLL:

```
[Xxx_SoftwareDeviceSettings]
...
HKR,, UserModeDriverName,    %REG_MULTI_SZ%, Xxx.dll
```

The INF file must contain information to direct the operating system to copy the user-mode display driver into the system's %systemroot%\\system32 directory. For more information, see [**INF CopyFiles Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) and [**INF DestinationDirs Section**](https://msdn.microsoft.com/library/windows/hardware/ff547383).

The Direct3D runtime obtains the user-mode display driver's DLL name from the registry in order to load the user-mode display driver in the runtime's process space.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Loading%20a%20User-Mode%20Display%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




