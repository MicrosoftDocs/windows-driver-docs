---
title: CM_PROB_DEVICE_NOT_THERE
description: CM_PROB_DEVICE_NOT_THERE
ms.assetid: 843afcc0-30ca-42f8-8c9b-3c4a56ec019d
keywords:
- CM_PROB_DEVICE_NOT_THERE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code 24 - CM_PROB_DEVICE_NOT_THERE

This function is reserved for system use.

The device does not seem to be present.

## Error Code

24

### Display Message

"This device is not present, is not working properly, or does not have all its drivers installed. (Code 24)"

### Recommended Resolution

The problem could be bad hardware, or a new driver might be needed. Devices stay in this state if they have been prepared for removal. This error code can be set if a driver's **DriverEntry** routine detects a device but the **DriverEntry** routine later fails.

**Note**  For Windows XP and later versions of Windows, **DriverEntry** problems have separate error codes.
