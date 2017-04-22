---
title: CM_PROB_DRIVER_FAILED_LOAD
description: CM_PROB_DRIVER_FAILED_LOAD
ms.assetid: 84d88db9-338b-4318-ba05-696521c96dd6
keywords:
- CM_PROB_DRIVER_FAILED_LOAD
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CM_PROB_DRIVER_FAILED_LOAD


## <a href="" id="ddk-cm-prob-driver-failed-load-dg"></a>


The driver could not be loaded.

### Error Code

39

### Display Message (Windows XP and later versions of Windows)

"Windows cannot load the device driver for this hardware. The driver may be corrupted or missing. (Code 39)"

### Recommended Resolution (Windows XP and later versions of Windows)

Reinstall or obtain a new driver.

Reasons for this error include the following:

-   A driver file that is not present, a binary file that is corrupted, a file I/O problem, or a driver that references an entry point in another binary that could not be loaded.

-   Starting with Windows Vista, the driver does not comply with [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md).

 

 





