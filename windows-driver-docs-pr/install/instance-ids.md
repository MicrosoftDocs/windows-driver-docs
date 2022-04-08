---
title: Instance ID
description: An instance ID is a device identification string that distinguishes a device from other devices of the same type on a computer.
ms.date: 04/08/2022
---

# Instance ID

An *instance ID* is a string reported by a device's *enumerator* (its [bus driver](../kernel/bus-drivers.md)) and distinguishes a device from other devices of the same type on a computer. An *instance ID* contains serial number information, if supported by the underlying bus, or some kind of location information. The string cannot contain any "\\" characters or any other character disallowed in a response to a [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md) request; otherwise, the generic format of the string is bus-specific. The number of characters of an *instance ID*, excluding a NULL-terminator, must be less than `MAX_DEVICE_ID_LEN`. In addition, the *instance ID* is another input into the creation of the [device instance ID](device-instance-ids.md), along with a [device ID](device-ids.md), and the maximum possible length of a device instance ID is `MAX_DEVICE_ID_LEN`. This requires that the length of the *instance ID* be enough less than `MAX_DEVICE_ID_LEN` that the device instance ID can be created as a string with length less than `MAX_DEVICE_ID_LEN`.

The **UniqueID** member of the [**DEVICE_CAPABILITIES**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_capabilities) structure for a device indicates if a bus-supplied *instance ID* is unique across the system, as follows:

- If **UniqueID** is **FALSE**, the bus-supplied *instance ID* for a device is unique only to the device's bus. The Plug and Play (PnP) manager modifies the bus-supplied *instance ID*, and combines it with the corresponding device ID, to create a device instance ID that is unique in the system.

- If **UniqueID** is **TRUE**, the device instance ID, formed from the bus-supplied device ID and *instance ID*, uniquely identifies a device in the system.

An *instance ID* is persistent across system restarts.

The PnP manager queries this string from the device's bus driver using an [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md) request with the **Parameters.QueryId.IdType** field set to **BusQueryInstanceID**.
