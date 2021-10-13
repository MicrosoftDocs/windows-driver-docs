---
title: CM_PROB_FAILED_ADD
description: CM_PROB_FAILED_ADD
keywords:
- CM_PROB_FAILED_ADD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code 31 - CM_PROB_FAILED_ADD

This Device Manager error message indicates that the [function driver](../kernel/function-drivers.md) for the device returned an error from its [AddDevice routine](../kernel/writing-an-adddevice-routine.md).

## Error Code

31

### Display Message

"This device is not working properly because Windows cannot load the drivers required for this device. (Code 31)"

### Recommended Resolution

Update the device driver.

## For driver developers

The [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md) property on the device should indicate the failure code returned by the function driver.

If the function driver is a WDF driver, this problem code may be the result of the driver returning an error from its [*EVT_WDF_DRIVER_DEVICE_ADD*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function.