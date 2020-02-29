---
title: CM_PROB_FAILED_DRIVER_ENTRY
description: CM_PROB_FAILED_DRIVER_ENTRY
ms.assetid: e1345892-69db-4135-be5b-1d182a2a1d66
keywords:
- CM_PROB_FAILED_DRIVER_ENTRY
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code 37 - CM_PROB_FAILED_DRIVER_ENTRY

This function is reserved for system use.
The driver returned failure from its **DriverEntry** routine.

## Error Code

37

### Display Message

"Windows cannot initialize the device driver for this hardware. (Code 37)"

### Recommended Resolution

Reinstall or obtain a new driver.

**Note**  If the **DriverEntry** routine returns STATUS_INSUFFICIENT_RESOURCES, Device Manager reports the [CM_PROB_OUT_OF_MEMORY](cm-prob-out-of-memory.md) error code.
