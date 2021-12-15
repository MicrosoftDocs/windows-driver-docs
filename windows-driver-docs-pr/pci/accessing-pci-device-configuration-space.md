---
title: Accessing PCI Device Configuration Space
description: Accessing PCI Device Configuration Space
keywords:
- PCI configuration space WDK buses
- configuration space WDK buses
- IRP_MN_READ_CONFIG
- IRP_MN_WRITE_CONFIG
ms.date: 09/13/2021
---

# Accessing PCI Device Configuration Space


Some operations on a peripheral component interconnect (PCI) device are reserved for the device's function driver. Such operations include, for example, accessing the device-specific configuration space of a bus and programming a direct memory access (DMA) controller. Microsoft provides system support for accessing the configuration space of PCI devices by two methods:

-   The [**BUS\_INTERFACE\_STANDARD**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_bus_interface_standard) bus interface

-   The configuration I/O request packets (IRPs), [**IRP\_MN\_READ\_CONFIG**](../kernel/irp-mn-read-config.md) and [**IRP\_MN\_WRITE\_CONFIG**](../kernel/irp-mn-write-config.md)

>[!NOTE]
>Starting with Windows 10, 2004, if a device has a Secure Devices (SDEV) ACPI table and Virtualization-based security enabled, restrictions are placed on unsupported methods for accessing PCI device configuration space. If a driver or process attempts to read or manipulate PCI device configuration space using a method that is not listed above, the access will be blocked and will result in a system bug check.

The Windows XP and Windows Server 2003 and later operating systems have exclusive control over the configuration space header, as defined by the *PCI Local Bus* specification, as well as all of the capabilities in the capabilities linked list. Drivers must not attempt to modify these registers.

However, drivers can write to the configuration space that does not belong to the header or the capabilities list that is vendor-defined, using the IRP\_MN\_WRITE\_CONFIG request or the **SetBusData** method of BUS\_INTERFACE\_STANDARD. Drivers can also read a device's capabilities, using the IRP\_MN\_READ\_CONFIG request or the **GetBusData** method of BUS\_INTERFACE\_STANDARD. To use IRP\_MN\_READ\_CONFIG or IRP\_MN\_WRITE\_CONFIG, drivers must be running at PASSIVE\_LEVEL. For a list of capabilities and the corresponding structures that drivers can query for, see the [PCI Structures](/windows-hardware/drivers/ddi/_pci/#structures) section.

Drivers can read from the extended PCI device configuration space (that is, more than 256 bytes of configuration data) using the IRP\_MN\_READ\_CONFIG request or the **GetBusData** method of BUS\_INTERFACE\_STANDARD. Likewise, drivers can write to the extended PCI device configuration space using the IRP\_MN\_WRITE\_CONFIG request or the **SetBusData** method of BUS\_INTERFACE\_STANDARD. If a device does not have an extended configuration space or the platform does not define a path for an extended configuration space on a device, the read requests will return 0xFFFF and the write requests will have no effect. To determine if the operation succeeded, drivers can examine the number of bytes read or written.

PCI Express and PCI-X mode 2 support an extended PCI device configuration space of greater than 256 bytes. Drivers can read and write to this configuration space, but only with the appropriate hardware and BIOS support. Within the ACPI BIOS, the root bus must have a PNP ID of either PNP0A08 or PNP0A03. For root buses with PNP ID of PNP0A03, the \_DSM method with function 4 should indicate that the current mode is PCI-X mode 2. All the bridges and devices should either be PCI express or operate in PCI-X mode 2.

In addition, the system should support memory-mapped configuration space accesses. This is by defining an MCFG table in the system BIOS/firmware. Windows Vista and Windows Server 2008 and later operating systems automatically support memory-mapped configuration space accesses.

