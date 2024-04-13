---
title: How Container IDs are Generated
description: How container IDs are generated
ms.date: 09/19/2022
---

# How container IDs are generated

Starting with Windows 7, the Plug and Play (PnP) manager generates a container ID for a device node (*devnode*) through one of three mechanisms:

- A [bus driver](../kernel/bus-drivers.md) provides a container ID.

    When assigning a container ID to a devnode, the PnP manager first checks whether the bus driver of the devnode can provide a container ID. Bus drivers provide a container ID through an [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md) request with the **Parameters.QueryId.IdType** field set to **BusQueryContainerID**.

    If a bus driver wants to provide a container ID, it can either obtain a genuine container ID that was embedded in the physical device hardware, or use a bus-specific unique ID from the device hardware to generate a container ID. Some examples of bus-specific unique IDs are a device's serial number or a media access control (MAC) address in the device's firmware.

    > [!NOTE]
    > The independent hardware vendor (IHV) is responsible for the uniqueness of the container ID reported by the bus driver.

    For more information, see [Container IDs Generated from a Bus-Specific Unique ID](container-ids-generated-from-a-bus-specific-unique-id.md).

- The PnP manager generates a container ID through the removable device capability.

    If a bus driver cannot provide a container ID for a devnode that it is enumerating, the PnP manager uses the removable device capability to generate a container ID for all devnodes enumerated for the device. The bus driver reports this device capability in response to an [**IRP_MN_QUERY_CAPABILITIES**](../kernel/irp-mn-query-capabilities.md) request.

    For more information, see [Container IDs Generated from the Removable Device Capability](container-ids-generated-from-the-removable-device-capability.md).

- The PnP manager generates a container ID through an override of the removable device capability.

    > [!NOTE]
    > In Windows 10, DPWS devices will always generate a container ID for the device using this method.

    Although the override mechanism does not change the value of the removable device capability, it forces the PnP manager to use the override setting and not the value of the removable device capability when generating container IDs for devices.

    For example, if an override of the removable device capability specifies the device is removable, the PnP manager generates a container ID for all devnodes enumerated for the device. This action is performed regardless of whether the device reported itself as removable or not.

    An IHV can populate the registry with keys that override the removable device capability reported by the device. This override mechanism is useful for legacy devices that either do not support the removable device capability or report it incorrectly.

    For more information, see [Container IDs Generated from a Removable Device Capability Override](container-ids-generated-from-a-removable-device-capability-override.md).

In addition to these methods, the system uses ACPI BIOS object settings to specify device container groupings. For more information, see [Using ACPI for Device Container Grouping](using-acpi-for-device-container-grouping.md).
