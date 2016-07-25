---
title: Container IDs Generated from a Bus-Specific Unique ID
description: Container IDs Generated from a Bus-Specific Unique ID
ms.assetid: 06bd4f06-51f2-4983-9ddc-bff27eaa367e
---

# Container IDs Generated from a Bus-Specific Unique ID


The preferred way to generate a container ID for a device is based on a bus-specific unique ID. This is the most precise and reliable method for generating container IDs.

The Plug and Play (PnP) manager uses this method if the following are true:

-   The device contains a bus-specific unique ID.

-   The bus driver for the device recognizes this unique ID as present and well formatted.

-   The bus driver can reliably hash the unique ID into a globally unique identifier ([*GUID*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-guid)), and returns this GUID in response to the [**IRP\_MN\_QUERY\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679) function code when the **Parameters.QueryId.IdType** member of the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure is set to **BusQueryContainerID**.

Windows 7 and later versions of Windows provide inbox drivers for several of the most common bus types. This includes USB, Bluetooth, and PnP-X. For these bus types, the device is only required to include a bus-specific unique ID. The supplied Windows bus driver will then read the unique ID from the device and create a container ID.

The following topics describe how the inbox bus drivers generate container IDs for certain bus types:

[Container IDs for USB Devices](container-ids-for-usb-devices.md)

[Container IDs for Bluetooth Devices](container-ids-for-bluetooth-devices.md)

[Container IDs for PnP-X Devices](container-ids-for-pnp-x-devices.md)

[Container IDs for 1394 Devices](container-ids-for-1394-devices.md)

[Container IDs for eSATA Devices](container-ids-for-esata-devices.md)

[Container IDs for PCI Express Devices](container-ids-for-pci-express-devices.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Container%20IDs%20Generated%20from%20a%20Bus-Specific%20Unique%20ID%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




