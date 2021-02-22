---
title: Device ID
description: A device ID is a string reported by a device’s enumerator. A device has only one device ID. A device ID has the same format as a hardware ID.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device ID


A device ID is a string reported by a device’s *enumerator*. A device has only one device ID. A device ID has the same format as a [hardware ID](hardware-ids.md).




The Plug and Play (PnP) manager uses the device ID to create a subkey for a device under the registry key for the device's enumerator.

To obtain a device ID, use an [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md) request and set the **Parameters.QueryId.IdType** field to **BusQueryDeviceID**.

 

