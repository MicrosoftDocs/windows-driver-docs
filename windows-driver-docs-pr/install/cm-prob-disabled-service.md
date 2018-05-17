---
title: CM_PROB_DISABLED_SERVICE
description: CM_PROB_DISABLED_SERVICE
ms.assetid: b2447b01-c25d-4761-bc96-291d508feb15
keywords:
- CM_PROB_DISABLED_SERVICE
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CM_PROB_DISABLED_SERVICE

This function is reserved for system use.


## <a href="" id="ddk-cm-prob-disabled-service-dg"></a>


The driver has been disabled.

### Error Code

32

### Display Message (Windows 2000 and later versions of Windows)

"A driver (service) for this device has been disabled. An alternate driver may be providing this functionality. (Code 32)"

### Recommended Resolution (Windows 2000 and later versions of Windows)

The start type for this service is set to Disabled in the registry. If the driver really is required, change the start type.

 

 





