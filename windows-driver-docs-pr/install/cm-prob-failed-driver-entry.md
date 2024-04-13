---
title: CM_PROB_FAILED_DRIVER_ENTRY
description: CM_PROB_FAILED_DRIVER_ENTRY
keywords:
- CM_PROB_FAILED_DRIVER_ENTRY
ms.date: 03/03/2023
---

# Code 37 - CM_PROB_FAILED_DRIVER_ENTRY

This Device Manager error message indicates that the driver returned failure from its **DriverEntry** routine.

## Error Code

37

### Display Message

"Windows cannot initialize the device driver for this hardware. (Code 37)"

### Recommended Resolution

Reinstall or obtain a new driver.

**Note**  If the **DriverEntry** routine returns STATUS_INSUFFICIENT_RESOURCES, Device Manager reports the [CM_PROB_OUT_OF_MEMORY](cm-prob-out-of-memory.md) error code.
