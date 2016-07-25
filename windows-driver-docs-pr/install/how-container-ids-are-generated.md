---
title: How Container IDs are Generated
description: How Container IDs are Generated
ms.assetid: baa3c045-05ee-4012-97a3-c6e575c897be
---

# How Container IDs are Generated


Starting with Windows 7, the Plug and Play (PnP) manager generates a container ID for a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) through one of three mechanisms:

-   A bus driver provides a container ID.

    When assigning a container ID to a devnode, the PnP manager first checks whether the bus driver of the devnode can provide a container ID. Bus drivers provide a container ID through an [**IRP\_MN\_QUERY\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679) request with the **Parameters.QueryId.IdType** field set to **BusQueryContainerID**.

    A bus driver can either obtain a genuine container ID that was embedded in the physical device hardware, or use a bus-specific unique ID from the device hardware to generate a container ID. Some examples of bus-specific unique IDs are a device's serial number or a media access control (MAC) address in the device's firmware.

    **Note**  The independent hardware vendor (IHV) is responsible for the uniqueness of the container ID reported by the bus driver.

     

    For more information, see [Container IDs Generated from a Bus-Specific Unique ID](container-ids-generated-from-a-bus-specific-unique-id.md).

-   The PnP manager generates a container ID through the removable device capability.

    If a bus driver cannot provide a container ID for a devnode that it is enumerating, the PnP manager uses the removable device capability to generate a container ID for all devnodes enumerated for the device. The bus driver reports this device capability in response to an [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) request.

    For more information, see [Container IDs Generated from the Removable Device Capability](container-ids-generated-from-the-removable-device-capability.md).

-   The PnP manager generates a container ID through an override of the removable device capability.

    **Note**  In Windows 10, DPWS devices will always generate a container ID for the device using this method.

     

    Although the override mechanism does not change the value of the removable device capability, it forces the PnP manager to use the override setting and not the value of the removable device capability when generating container IDs for devices.

    For example, if an override of the removable device capability specifies the device is removable, the PnP manager generates a container ID for all devnodes enumerated for the device. This action is performed regardless of whether the device reported itself as removable or not.

    An IHV can populate the registry with keys that override the removable device capability reported by the device. This override mechanism is useful for legacy devices that either do not support the removable device capability or report it incorrectly.

    For more information, see [Container IDs Generated from a Removable Device Capability Override](container-ids-generated-from-a-removable-device-capability-override.md).

In addition to these methods, the system uses ACPI BIOS object settings to specify device container groupings. For more information, see [Using ACPI for Device Container Grouping](using-acpi-for-device-container-grouping.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20How%20Container%20IDs%20are%20Generated%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




