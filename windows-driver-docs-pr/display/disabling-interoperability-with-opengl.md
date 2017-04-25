---
title: Disabling Interoperability with OpenGL
description: Disabling Interoperability with OpenGL
ms.assetid: 2b684cda-2137-4395-b2ee-beee8614e4c1
keywords:
- INF files WDK display , interoperability
- interoperability WDK display
- OpenGL WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Disabling Interoperability with OpenGL


To ensure that no Microsoft Direct3D display drivers are exposed to possible interoperability issues with OpenGL installable client drivers (ICDs), you must set the following entry in an add-registry section of the INF:

```
[Xxx_SoftwareDeviceSettings]
...
HKR,, CapabilityOverride,    %REG_DWORD%, 0x8
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Disabling%20Interoperability%20with%20OpenGL%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




