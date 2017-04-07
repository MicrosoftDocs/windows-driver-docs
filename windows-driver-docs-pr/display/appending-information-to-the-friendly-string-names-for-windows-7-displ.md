---
title: Append Information to the Friendly String Names for Windows 7 Display Drivers
description: Appending Information to the Friendly String Names for Windows 7 Display Drivers
ms.assetid: 8c65f3d9-6f4c-49e9-a9b2-2689d83a181c
---

# Appending Information to the Friendly String Names for Windows 7 Display Drivers


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

A graphics adapter's friendly name is a localizable string name that is required in the INF for every Windows 7 in-box display driver. The section on [Appending Information to the Friendly String Names of Graphics Adapters](appending-information-to-the-friendly-string-names-of-graphics-adapter.md) describes the information that you must append for the Windows Display Driver Model (WDDM) and the [Windows 2000 Display Driver Model](windows-2000-display-driver-model-design-guide.md). For the WDDM optimized for Windows 7, you must append "(Microsoft Corporation - WDDM v1.1)":

```
New Driver Model Foo Device Name (Microsoft Corporation - WDDM v1.1)
```

The text appended to the graphics adapter's friendly name specifies the WDDM version that the driver uses.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Appending%20Information%20to%20the%20Friendly%20String%20Names%20for%20Windows%207%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




