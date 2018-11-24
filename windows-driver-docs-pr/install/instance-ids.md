---
title: Instance ID
description: An instance ID is a device identification string that distinguishes a device from other devices of the same type on a computer.
ms.assetid: 093063a6-1855-4e36-9465-1eedaa3cd0f9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Instance ID


An instance ID is a device identification string that distinguishes a device from other devices of the same type on a computer. An instance ID contains serial number information, if supported by the underlying bus, or some kind of location information. The string cannot contain any "\\" characters; otherwise, the generic format of the string is bus-specific.




The number of characters of an instance ID, excluding a NULL-terminator, must be less than MAX_DEVICE_ID_LEN. In addition, when an instance ID is concatenated to a [device ID](device-ids.md) to create a device instance ID, the lengths of the device ID and the instance ID are further constrained by the maximum possible length of a device instance ID.

The **UniqueID** member of the [**DEVICE_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure for a device indicates if a bus-supplied instance ID is unique across the system, as follows:

-   If **UniqueID** is **FALSE**, the bus-supplied instance ID for a device is unique only to the device's bus. The Plug and Play (PnP) manager modifies the bus-supplied instance ID, and combines it with the corresponding device ID, to create a device instance ID that is unique in the system.

-   If **UniqueID** is **TRUE**, the device instance ID, formed from the bus-supplied device ID and instance ID, uniquely identifies a device in the system.

An instance ID is persistent across system restarts.

To obtain the bus-supplied instance ID for a device, use an [**IRP_MN_QUERY_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679) request and set the **Parameters.QueryId.IdType** member to **BusQueryInstanceID**.

 

 





