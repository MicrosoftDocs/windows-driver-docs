---
title: CM_PROB_DUPLICATE_DEVICE
description: CM_PROB_DUPLICATE_DEVICE
ms.assetid: db0f6c98-d314-4882-ac8e-c73254f41c98
keywords:
- CM_PROB_DUPLICATE_DEVICE
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CM_PROB_DUPLICATE_DEVICE


## <a href="" id="ddk-cm-prob-duplicate-device-dg"></a>


A duplicate device was detected.

### Error Code

42

### Display Message (Windows XP and later versions of Windows)

"Windows cannot load the device driver for this hardware because there is a duplicate device already running in the system. (Code 42)"

### Recommended Resolution (Windows XP and later versions of Windows)

This error is reported when one of the following occurs:

-   A device with a serial number is discovered in a new location in the computer before the operating system notices that the device is missing from the old location. This typically happens when a device is moved, either very quickly or when the computer is in a standby or hibernate state, to a different location.

    In this case, you can resolve the problem by restarting the computer.

-   A bus driver incorrectly creates two identically named children on the bus. This is caused by multiple devices on the bus that report the same serial number. This can also be caused by a bus driver that incorrectly reports the same hardware identifiers for two or more devices.

    In this case, you should contact [Microsoft support](http://support.microsoft.com/) for more assistance with this problem.

 

 





