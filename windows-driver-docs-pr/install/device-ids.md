---
title: Device ID String
description: A device ID is a string reported by a device's enumerator. A device has only one device ID. A device ID has the same format as a hardware ID.
ms.date: 04/08/2022
---

# Device ID string

A device ID is a string reported by a device's *enumerator* (its [bus driver](../kernel/bus-drivers.md)). A device has only one device ID. A device ID has the same format as a [hardware ID](hardware-ids.md).

The Plug and Play (PnP) manager uses the device ID as one of the inputs into the creation of the [device instance ID](device-instance-ids.md). The PnP manager queries this string from the device's bus driver using an [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md) request with the **Parameters.QueryId.IdType** field set to **BusQueryDeviceID**.
