---
title: CM_PROB_NOT_CONFIGURED
description: CM_PROB_NOT_CONFIGURED
ms.assetid: 8bdc741c-6e1e-46ab-ab2d-fafe87bbd99f
keywords:
- CM_PROB_NOT_CONFIGURED
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CM_PROB_NOT_CONFIGURED

This function is reserved for system use.

There is a device on the system for which there is no **ConfigFlags** registry entry. This means no driver is installed. Typically this means an INF file could not be found.

## Error Code

1

### Display Message

"This device is not configured correctly. (Code 1)"

"To Update the drivers for this device, click Update Driver. If that doesn't work, see your hardware documentation for more information."

### Recommended Resolution

Select **Update Driver**, which starts the Hardware Update wizard.

## For driver developers

This error means that PnP has not attempted to install the device. This should be a transient problem code only appearing briefly when a device is first enumerated.

If this problem status occurs in conjunction with a [Bug Check 0x7B: INACCESSIBLE_BOOT_DEVICE](../debugger/bug-check-0x7b--inaccessible-boot-device.md) and the device is on the path to the boot disk, the system is missing a driver for a boot critical device.
