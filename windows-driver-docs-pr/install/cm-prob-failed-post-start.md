---
title: CM_PROB_FAILED_POST_START
description: CM_PROB_FAILED_POST_START
ms.assetid: 82d43c8b-d5de-4395-9ca0-34d2258b9772
keywords:
- CM_PROB_FAILED_POST_START
ms.date: 02/28/2020
ms.localizationpriority: medium
---

# Code 43 - CM_PROB_FAILED_POST_START

This function is reserved for system use.

A driver has reported a device failure.

## Error Code

43

### Display Message

"Windows has stopped this device because it has reported problems. (Code 43)"

### Recommended Resolution

Uninstall and reinstall the device.

One of the drivers controlling the device told the operating system the device failed in some manner in response to IRP_MN_QUERY_PNP_DEVICE_STATE.

## For driver developers

A driver [invalidated the device state](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinvalidatedevicestate) of the device and in the resulting query device state the device stack reported [PNP_DEVICE_FAILED](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-query-pnp-device-state).

If the driver is a WDF driver, the reporting of the device as failed may be indirectly caused by the WDF driver calling [**WdfDeviceSetFailed**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetfailed) or returning an error from a WDF callback. For more info, see [Reporting Device Failures](https://docs.microsoft.com/windows-hardware/drivers/wdf/reporting-device-failures).
