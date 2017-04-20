---
title: Setting the Start Type Value
description: Setting the Start Type Value
ms.assetid: dcc38a36-4755-472b-94c8-dfed892460ee
keywords:
- INF files WDK display , start type values
- start type values WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting the Start Type Value


You should set display drivers that are written to the Windows Display Driver Model (WDDM) to start to run on demand on Windows Vista and later, rather than during operating-system initialization, as was the case with display drivers that ran on operating systems prior to Windows Vista. This change is due to manifest and image-based-install functionality that was not present on operating systems prior to Windows Vista. You should set the value for the **StartType** entry to SERVICE\_DEMAND\_START (3) rather than SERVICE\_SYSTEM\_START (1).

The following example shows a service-install section with the value for the **StartType** entry set to SERVICE\_DEMAND\_START to indicate that the display miniport driver is started on demand:

```
;
; Service Installation Section
;

[R200_Service_Inst]
ServiceType    = 1        ; SERVICE_KERNEL_DRIVER
StartType      = 3        ; SERVICE_DEMAND_START
ErrorControl   = 0        ; SERVICE_ERROR_IGNORE
LoadOrderGroup = Video
ServiceBinary  = %12%\r200.sys
```

For more information about service-install sections that are associated with the **AddService** directive, see [**INF AddService Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20the%20Start%20Type%20Value%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




