---
title: CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD
description: CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD
keywords:
- CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD
ms.date: 03/03/2023
---

# Code 38 - CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD

This Device Manager error message indicates that the driver could not be loaded because a previous instance is still loaded.

## Error Code

38

### Display Message

"Windows cannot load the device driver for this hardware because a previous instance of the device driver is still in memory. (Code 38)"

### Recommended Resolution

A previous driver instance can still be loaded due to an incorrect reference count or a race between load and unload operations. Additionally, this message can appear if a driver is referenced by multiple [**INF AddService directives**](inf-addservice-directive.md) in one or more INF files.

Select **Restart Computer**, which will restart the computer.
