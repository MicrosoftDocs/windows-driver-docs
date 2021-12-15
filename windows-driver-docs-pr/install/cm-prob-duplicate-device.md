---
title: CM_PROB_DUPLICATE_DEVICE
description: CM_PROB_DUPLICATE_DEVICE
keywords:
- CM_PROB_DUPLICATE_DEVICE
ms.date: 04/20/2017
---

# Code 42 - CM_PROB_DUPLICATE_DEVICE

This Device Manager error message indicates that a duplicate device was detected.

## Error Code

42

### Display Message

"Windows cannot load the device driver for this hardware because there is a duplicate device already running in the system. (Code 42)"

### Recommended Resolution

This error is reported when one of the following occurs:

- A device with a serial number is discovered in a new location in the computer before the operating system notices that the device is missing from the old location. This typically happens when a device is moved, either very quickly or when the computer is in a standby or hibernate state, to a different location.

    In this case, you can resolve the problem by restarting the computer.

- A bus driver incorrectly creates two identically named children on the bus. This is caused by multiple devices on the bus that report the same serial number. This can also be caused by a bus driver that incorrectly reports the same hardware identifiers for two or more devices.

    In this case, you should contact [Microsoft support](https://support.microsoft.com/en-us) for more assistance with this problem.
