---
title: CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD
description: CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD
ms.assetid: c7639fd7-738f-4115-9abc-0bafca097b9e
keywords:
- CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD

This function is reserved for system use.


## <a href="" id="ddk-cm-prob-driver-failed-prior-unload-dg"></a>


The driver could not be loaded because a previous instance is still loaded.

### Error Code

38

### Display Message (Windows XP and later versions of Windows)

"Windows cannot load the device driver for this hardware because a previous instance of the device driver is still in memory. (Code 38)"

### Recommended Resolution (Windows XP and later versions of Windows)

A previous driver instance can still be loaded due to an incorrect reference count or a race between load and unload operations. Additionally, this message can appear if a driver is referenced by multiple [**INF AddService directives**](inf-addservice-directive.md) in one or more INF files.

Select **Restart Computer**, which will restart the computer.

 

 





