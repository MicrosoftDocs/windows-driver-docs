---
title: Device Instance ID
description: A device instance ID is a system-supplied device identification string that uniquely identifies a device in the system.
ms.assetid: 578973f4-463f-4707-8dc3-dff27b3d3052
ms.date: 04/20/2017
ms.localizationpriority: High
---

# Device Instance ID


A device instance ID is a system-supplied device identification string that uniquely identifies a device in the system. The Plug and Play (PnP) manager assigns a device instance ID to each device node (*devnode*) in a system's [device tree](https://docs.microsoft.com/windows-hardware/drivers/kernel/device-tree).




The format of this string consists of an [instance ID](instance-ids.md) concatenated to a [device ID](device-ids.md), as follows:

`<device-ID>\<instance-specific-ID>`

The number of characters of a device instance ID, excluding a NULL-terminator, must be less than MAX_DEVICE_ID_LEN. This constraint applies to the sum of the lengths of all the fields and "\\" field separator between the *device ID* and *instance-specific-ID* fields.

A device instance ID is persistent across system restarts.

The following is an example of an instance ID ("1&08") concatenated to a device ID for a PCI device:

`PCI\VEN_1000&DEV_0001&SUBSYS_00000000&REV_02\1&08`

 

 





