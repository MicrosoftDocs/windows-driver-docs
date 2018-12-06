---
title: Device ID
description: A device ID is a string reported by a device’s enumerator. A device has only one device ID. A device ID has the same format as a hardware ID.
ms.assetid: a71b64bc-319e-4133-810b-7fd417cf0af8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device ID


A device ID is a string reported by a device’s [*enumerator*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-enumerator). A device has only one device ID. A device ID has the same format as a [hardware ID](hardware-ids.md).




The Plug and Play (PnP) manager uses the device ID to create a subkey for a device under the registry key for the device's enumerator.

To obtain a device ID, use an [**IRP_MN_QUERY_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679) request and set the **Parameters.QueryId.IdType** field to **BusQueryDeviceID**.

 

 





