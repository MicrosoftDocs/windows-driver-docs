---
title: Setting the Start Type Value
description: Setting the Start Type Value
ms.assetid: dcc38a36-4755-472b-94c8-dfed892460ee
keywords:
- INF files WDK display , start type values
- start type values WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Start Type Value


You should set display drivers that are written to the Windows Display Driver Model (WDDM) to start to run on demand on Windows Vista and later, rather than during operating-system initialization, as was the case with display drivers that ran on operating systems prior to Windows Vista. This change is due to manifest and image-based-install functionality that was not present on operating systems prior to Windows Vista. You should set the value for the **StartType** entry to SERVICE\_DEMAND\_START (3) rather than SERVICE\_SYSTEM\_START (1).

The following example shows a service-install section with the value for the **StartType** entry set to SERVICE\_DEMAND\_START to indicate that the display miniport driver is started on demand:

```inf
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

 

 





