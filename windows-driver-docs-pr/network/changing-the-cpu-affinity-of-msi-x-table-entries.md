---
title: Changing the CPU Affinity of MSI-X Table Entries
description: Changing the CPU Affinity of MSI-X Table Entries
keywords:
- MSI-X WDK networking , MSI-X table entry CPU affinity
- message-signaled interrupts WDK networking , MSI-X table entry CPU affinity
- MSIs WDK networking , MSI-X table entry CPU affinity
- interrupts WDK networking , MSI-X table entry CPU affinity
- CPU af
ms.date: 04/20/2017
---

# Changing the CPU Affinity of MSI-X Table Entries





NDIS 6.1 and later miniport drivers that support MSI-X can call the [**NdisMConfigMSIXTableEntry**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismconfigmsixtableentry) function to mask, unmask, or map MSI-X table entries to device-assigned MSI-X messages. Miniport drivers that support RSS use **NdisMConfigMSIXTableEntry** to change the CPU affinity of MSI-X table entries at run time.

**NdisMConfigMSIXTableEntry** is a wrapper around the [GUID\_MSIX\_TABLE\_CONFIG\_INTERFACE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_pci_msix_table_config_interface) query. Miniport drivers can call **NdisMConfigMSIXTableEntry** after NDIS calls the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function and before the drivers return from the [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function.

A miniport driver that assigns an MSI-X table entry for each RSS queue and has fewer queues than the number of RSS processors can add additional MSI-X message resources in the [*MiniportFilterResourceRequirements*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp) function. For more information about how to modify assigned resources for a device, see [MSI-X Resource Filtering](msi-x-resource-filtering.md).

The miniport driver can set the CPU affinity of MSI-X interrupt resources so that the device has at least one MSI-X message for each RSS processor. Note that the PCI bus driver initially maps the *n* MSI-X table entries (where *n* is the number of MSI-X table entries that the NIC hardware reported to the bus) to the first *n* MSI-X messages in modified resources. After NDIS calls *MiniportInitializeEx*, when the miniport driver changes the target processor of a particular MSI-X table entry, the driver calls **NdisMConfigMSIXTableEntry** to map that table entry to an MSI-X message that already has the affinity set to the desired processor.

 

