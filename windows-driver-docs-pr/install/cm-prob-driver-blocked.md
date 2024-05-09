---
title: CM_PROB_DRIVER_BLOCKED
description: CM_PROB_DRIVER_BLOCKED
keywords:
- CM_PROB_DRIVER_BLOCKED
ms.date: 03/03/2023
---

# Code 48 - CM_PROB_DRIVER_BLOCKED

This Device Manager error message indicates that the system will not load the driver because it is listed in the Windows Driver Protection database supplied by Windows Update.

If the device is being used for [Enhanced Sign-in Security](/windows-hardware/design/device-experiences/windows-hello-enhanced-sign-in-security), the system has detected that the installed driver is incompatible with Enhanced Sign-in Security requirements and therefore prevented the device from starting.

## Error Code

48

### Display Message

"The software for this device has been blocked from starting because it is known to have problems with Windows. Contact the hardware vendor for a new driver. (Code 48)"

### Recommended Resolution

Obtain a new driver from the hardware vendor.
