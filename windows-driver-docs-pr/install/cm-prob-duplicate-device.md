---
title: CM_PROB_DUPLICATE_DEVICE
description: CM_PROB_DUPLICATE_DEVICE
keywords:
- CM_PROB_DUPLICATE_DEVICE
ms.date: 09/10/2024
---

# Code 42 - CM_PROB_DUPLICATE_DEVICE

This Device Manager error message indicates that a duplicate device was detected.

## Error Code

42

### Display Message

"Windows cannot load the device driver for this hardware because there is a duplicate device already running in the system. (Code 42)"

### Recommended Resolution

Error code 42 is reported when one of the following occurs:

- A device with a serial number is discovered in a new location in the computer before the operating system notices that the device is missing from the old location. This situation typically happens when a device is moved, either quickly or when the computer is in a standby or hibernate state, to a different location.

    In this case, you can resolve the problem by restarting the computer.

- A bus driver incorrectly creates two identically named children on the bus. This situation occurs when multiple devices on the bus report the same serial number. A bus driver that incorrectly reports the same hardware identifiers for two or more devices can also cause this error.

    In this case, you should contact [Microsoft support](https://support.microsoft.com) for more assistance with this problem.
