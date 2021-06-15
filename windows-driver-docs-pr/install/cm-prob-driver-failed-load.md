---
title: CM_PROB_DRIVER_FAILED_LOAD
description: CM_PROB_DRIVER_FAILED_LOAD
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

## For driver developers

Some of the more common reasons for this error include the following:

- A driver file that links with another binary file that is not present on the system

- A driver file that links with an operating system provided API and the driver file is being loaded on a version of the operating system that does not support that API.

- The system has [Hypervisor-Protected Code Integrity](/windows-hardware/test/hlk/testref/driver-compatibility-with-device-guard) enabled and the driver is not compatible with that feature.

- A failure to load a driver file or one of its dependencies due to the file being corrupted or a file I/O problem