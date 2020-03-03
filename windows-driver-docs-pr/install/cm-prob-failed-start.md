---
title: CM_PROB_FAILED_START
description: CM_PROB_FAILED_START
ms.assetid: a7759bcd-1806-4d7a-8ff0-3b03abcae08b
keywords:
- CM_PROB_FAILED_START
ms.date: 02/28/2020
ms.localizationpriority: medium
---

# Code 10 - CM_PROB_FAILED_START

This function is reserved for system use.

The device failed to start.

## Error Code

10

### Display Message

If the device's [hardware key](opening-a-device-s-hardware-key.md) contains a "FailReasonString" value, the value string is displayed as the error message. (A driver or enumerator supplies this registry string value.) If the hardware key does not contain a "FailReasonString" value, the following generic error message is displayed:

"This device cannot start. (Code 10)"

"Try upgrading the device drivers for this device."

### Recommended Resolution

Select **Update Driver**, which starts the Hardware Update wizard.

This error code is set when one of the drivers in the device's driver stack fails IRP_MN_START_DEVICE. If there are many drivers in the stack, it can be difficult to determine the one that failed.

See the [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md) property on the device for the failure code returned for the [start IRP](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-start-device).

For additional information, see [Retrieving the Status and Problem Code for a Device Instance](retrieving-the-status-and-problem-code-for-a-device-instance.md).

## For driver developers

One of the drivers in the device stack failed the [start IRP](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-start-device). The [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md) property on the device should indicate the failure code.
