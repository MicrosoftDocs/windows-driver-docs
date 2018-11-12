---
title: Changing the CPU Affinity of MSI-X Table Entries
description: Changing the CPU Affinity of MSI-X Table Entries
ms.assetid: 46ce91ad-76eb-4d05-af9d-a295c665640a
keywords:
- MSI-X WDK networking , MSI-X table entry CPU affinity
- message-signaled interrupts WDK networking , MSI-X table entry CPU affinity
- MSIs WDK networking , MSI-X table entry CPU affinity
- interrupts WDK networking , MSI-X table entry CPU affinity
- CPU af
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Changing the CPU Affinity of MSI-X Table Entries





NDIS 6.1 and later miniport drivers that support MSI-X can call the [**NdisMConfigMSIXTableEntry**](https://msdn.microsoft.com/library/windows/hardware/ff563566) function to mask, unmask, or map MSI-X table entries to device-assigned MSI-X messages. Miniport drivers that support RSS use **NdisMConfigMSIXTableEntry** to change the CPU affinity of MSI-X table entries at run time.

**NdisMConfigMSIXTableEntry** is a wrapper around the [GUID\_MSIX\_TABLE\_CONFIG\_INTERFACE](https://msdn.microsoft.com/library/windows/hardware/ff546563) query. Miniport drivers can call **NdisMConfigMSIXTableEntry** after NDIS calls the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function and before the drivers return from the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function.

A miniport driver that assigns an MSI-X table entry for each RSS queue and has fewer queues than the number of RSS processors can add additional MSI-X message resources in the [*MiniportFilterResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff559384) function. For more information about how to modify assigned resources for a device, see [MSI-X Resource Filtering](msi-x-resource-filtering.md).

The miniport driver can set the CPU affinity of MSI-X interrupt resources so that the device has at least one MSI-X message for each RSS processor. Note that the PCI bus driver initially maps the *n* MSI-X table entries (where *n* is the number of MSI-X table entries that the NIC hardware reported to the bus) to the first *n* MSI-X messages in modified resources. After NDIS calls *MiniportInitializeEx*, when the miniport driver changes the target processor of a particular MSI-X table entry, the driver calls **NdisMConfigMSIXTableEntry** to map that table entry to an MSI-X message that already has the affinity set to the desired processor.

 

 





