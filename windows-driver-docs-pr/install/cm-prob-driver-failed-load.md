---
title: CM_PROB_DRIVER_FAILED_LOAD
description: CM_PROB_DRIVER_FAILED_LOAD
ms.assetid: 84d88db9-338b-4318-ba05-696521c96dd6
keywords:
- CM_PROB_DRIVER_FAILED_LOAD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code 39 - CM_PROB_DRIVER_FAILED_LOAD

This Device Manager error message indicates that the driver could not be loaded.

## Error Code

39

### Display Message

"Windows cannot load the device driver for this hardware. The driver may be corrupted or missing. (Code 39)"

### Recommended Resolution

Reinstall or obtain a new driver.

Reasons for this error include the following:

- A driver file that is not present, a binary file that is corrupted, a file I/O problem, or a driver that references an entry point in another binary that could not be loaded.

- The driver does not comply with [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md).

