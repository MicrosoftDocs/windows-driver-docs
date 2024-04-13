---
title: CM_PROB_FAILED_START
description: CM_PROB_FAILED_START
keywords:
- CM_PROB_FAILED_START
ms.date: 02/28/2020
---

# Code 10 - CM_PROB_FAILED_START

This Device Manager error message indicates that the device failed to start.

## Error Code

10

### Display Message

If the device's [hardware key](opening-a-device-s-hardware-key.md) contains a "FailReasonString" value, the value string is displayed as the error message. (A driver or enumerator supplies this registry string value.) If the hardware key does not contain a "FailReasonString" value, the following generic error message is displayed:

"This device cannot start. (Code 10)"

"Try upgrading the device drivers for this device."

### Recommended Resolution

Select **Update Driver**, which starts the Hardware Update wizard.

This error code is set when one of the drivers in the device's driver stack fails IRP_MN_START_DEVICE. If there are many drivers in the stack, it can be difficult to determine the one that failed.

See the [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md) property on the device for the failure code returned for the [start IRP](../kernel/irp-mn-start-device.md).

For additional information, see [Retrieving the Status and Problem Code for a Device Instance](retrieving-the-status-and-problem-code-for-a-device-instance.md).

## For driver developers

One of the drivers in the device stack failed the [start IRP](../kernel/irp-mn-start-device.md). The [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md) property on the device should indicate the failure code.

If one of the drivers in the device's driver stack is a UMDF driver and the [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md) property on the device is STATUS_DRIVER_PROCESS_TERMINATED, this information may be helpful for the owner of the driver to diagnose the problem:
* [Determining Why the Reflector Terminated the Host Process](../wdf/determining-why-the-reflector-terminated-the-host-process.md)
* [Troubleshooting UMDF 2.0 Driver Crashes](../wdf/debugging-umdf-2-0-drivers.md)

