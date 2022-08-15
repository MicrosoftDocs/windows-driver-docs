---
title: Container IDs Generated from a Bus-Specific Unique ID
description: Container IDs Generated from a Bus-Specific Unique ID
ms.date: 04/20/2017
---

# Container IDs Generated from a Bus-Specific Unique ID


The preferred way to generate a container ID for a device is based on a bus-specific unique ID. This is the most precise and reliable method for generating container IDs.

The Plug and Play (PnP) manager uses this method if the following are true:

-   The device contains a bus-specific unique ID.

-   The bus driver for the device recognizes this unique ID as present and well formatted.

-   The bus driver can reliably hash the unique ID into a globally unique identifier (*GUID*), and returns this GUID in response to the [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md) function code when the **Parameters.QueryId.IdType** member of the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) structure is set to **BusQueryContainerID**.

Windows 7 and later versions of Windows provide inbox drivers for several of the most common bus types. This includes USB, Bluetooth, and PnP-X. For these bus types, the device is only required to include a bus-specific unique ID. The supplied Windows bus driver will then read the unique ID from the device and create a container ID.

The following topics describe how the inbox bus drivers generate container IDs for certain bus types:

[Container IDs for USB Devices](./how-usb-devices-are-assigned-container-ids.md)

[Container IDs for Bluetooth Devices](container-ids-for-bluetooth-devices.md)

[Container IDs for PnP-X Devices](container-ids-for-pnp-x-devices.md)

[Container IDs for 1394 Devices](container-ids-for-1394-devices.md)

[Container IDs for eSATA Devices](container-ids-for-esata-devices.md)

[Container IDs for PCI Express Devices](container-ids-for-pci-express-devices.md)

