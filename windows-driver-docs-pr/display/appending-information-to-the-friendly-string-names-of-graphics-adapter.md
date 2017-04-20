---
title: Appending Information to the Friendly String Names of Graphics Adapters
description: Appending Information to the Friendly String Names of Graphics Adapters
ms.assetid: 660104ba-b082-407b-afdc-3e02f4c3d087
keywords:
- INF files WDK display , friendly string names
- friendly string names WDK display
- graphics adapters string names WDK display
- appending to graphics adapters string names WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Appending Information to the Friendly String Names of Graphics Adapters


You must append information to the string names of graphics adapters. This information depends on the display driver model that the adapters' drivers are written to:

For the Windows 2000 Display Driver Model, you must append "(Microsoft Corporation)":

```
XDDM Foo Device Name (Microsoft Corporation)
```

For the Windows Display Driver Model (WDDM), you must append "(Microsoft Corporation - WDDM)":

```
New Driver Model Foo Device Name (Microsoft Corporation - WDDM)
```

For more information about the *Strings* section and the *%strkey%* tokens that are specified elsewhere in the INF, see [**INF Strings Section**](https://msdn.microsoft.com/library/windows/hardware/ff547485).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Appending%20Information%20to%20the%20Friendly%20String%20Names%20of%20Graphics%20Adapters%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




