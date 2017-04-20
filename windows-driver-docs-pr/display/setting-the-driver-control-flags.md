---
title: Setting the Driver Control Flags
description: Setting the Driver Control Flags
ms.assetid: cca51b9c-ce37-4efb-ab42-8eb62b25eb21
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting the Driver Control Flags


The **ExcludeFromSelect** directive is required for all drivers, except for [mirror drivers](mirror-drivers.md), that are written to the Windows Display Driver Model (WDDM).

The following example shows how to add the **ExcludeFromSelect** directive to a **ControlFlags** section of the INF file:

```
[ControlFlags]
ExcludeFromSelect=*
```

For more information on driver control flags, see [**INF ControlFlags Section**](https://msdn.microsoft.com/library/windows/hardware/ff546342).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20the%20Driver%20Control%20Flags%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




