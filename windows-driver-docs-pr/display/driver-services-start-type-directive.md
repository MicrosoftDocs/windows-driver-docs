---
title: Driver\services start type directive
description: The "driver\services" start type directive is a service installation setting requirement for all display drivers. Windows Display Driver Model (WDDM) drivers are Plug and Play (PnP) and therefore must be demand started, where StartType=3.
ms.assetid: 1B34DC18-EA81-44DB-B60A-D05B685E9321
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver\\services start type directive


The *driver\\services* start type directive is a service installation setting requirement for all display drivers. Windows Display Driver Model (WDDM) drivers are Plug and Play (PnP) and therefore must be demand started, where *StartType* =3.

For example:

``` syntax
; Service Installation Section
;

[R200_Service_Inst]
ServiceType    = 1                  ; SERVICE_KERNEL_DRIVER
StartType      = 3                  ; SERVICE_DEMAND_START
ErrorControl   = 0                  ; SERVICE_ERROR_IGNORE
LoadOrderGroup = Video
ServiceBinary  = %12%\r200.sys
```

 

 





