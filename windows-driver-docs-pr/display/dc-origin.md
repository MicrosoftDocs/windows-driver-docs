---
title: DC Origin
description: DC Origin
ms.assetid: 7e997f6b-fec4-4aa4-b0ed-0d02cb3f844d
keywords:
- DC origin WDK GDI
- surface negotiation WDK GDI , DC origin
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DC Origin


## <span id="ddk_dc_origin_gg"></span><span id="DDK_DC_ORIGIN_GG"></span>


Application programs are required to keep their graphics within an array of 2²⁷ by 2²⁷ pixels. The device space has additional size at the graphics DDI level because Window Manager may offset the application's coordinate system by one signed 27-bit coordinate, the *DC origin*. The DC origin is not visible to the driver, and the driver identifies the graphics coordinates only after the offset is applied.

 

 





