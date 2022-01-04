---
title: MSI-X Resource Filtering
description: MSI-X Resource Filtering
keywords:
- MSI-X WDK networking , resource-requirements filter function
- message-signaled interrupts WDK networking , resource-requirements filter function
- MSIs WDK networking , resource-requirements filter function
- resource-requirements filter function WDK net
ms.date: 04/20/2017
---

# MSI-X Resource Filtering





Miniport drivers must register a resource-requirements filter function if they support MSI-X and will change the interrupt affinity for each MSI-X message or will remove message interrupt resources.

NDIS calls the [*MiniportFilterResourceRequirements*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp) function after NDIS receives the [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](../kernel/irp-mn-filter-resource-requirements.md) I/O request packet (IRP) for a network interface card (NIC). NDIS calls *MiniportFilterResourceRequirements* after the underlying function drivers in the device stack have completed the IRP.

NDIS will call *MiniportFilterResourceRequirements* after the [*MiniportAddDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device) function returns NDIS\_STATUS\_SUCCESS. NDIS may call *MiniportFilterResourceRequirements* again at any time before calling [*MiniportRemoveDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_remove_device). NDIS may call *MiniportFilterResourceRequirements* while the miniport is running. While the miniport may modify the resource list as described below, the miniport should not immediately attempt to use the new resources. NDIS will eventually halt and re-initialize the miniport with the new resources; only then should the miniport attempt to use the new resources.

[**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](../kernel/irp-mn-filter-resource-requirements.md) provides a resource list as an [**IO\_RESOURCE\_REQUIREMENTS\_LIST**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_resource_requirements_list) structure at **Irp-&gt;IoStatus.Information**. The resources in the list are described by [**IO\_RESOURCE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_resource_descriptor) structures.

A miniport driver can modify the interrupt affinity policy for each resource of type **CmResourceTypeInterrupt** that describes an MSI-X message. If an affinity policy requests targeting for a specific set of processors, the miniport driver also sets a [**KAFFINITY**](../kernel/interrupt-affinity-and-priority.md#about-kaffinity) mask at **Interrupt.TargetedProcessors** in the IO\_RESOURCE\_DESCRIPTOR structure.

A miniport driver can remove all resources of type **CmResourceTypeInterrupt** that are message interrupt resources. The driver can then register for line-based interrupts in the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. If the miniport driver does not remove these message interrupt resources, the operating system will fail if the driver tries to register line-based interrupts in *MiniportInitializeEx*.

An NDIS 6.1 or later miniport driver can add message interrupt resources to the resources list. For example on a computer with eight CPUs, if the NIC can generate four MSI-X messages and if the operating system enables the four message interrupts, the operating system initializes four message table entries in the device's MSI-X configuration space and puts four message interrupt resources in the resources list. In this case, because the miniport driver requires more message interrupt resources, it can allocate four more message interrupt resources to the resources list and set the affinity of each MSI-X message to a CPU. If the operating system can provide more message interrupt resources, the miniport adapter receives eight message interrupt resources when it is started. In this case, the messages have numbers from 0 through 7.

Each message interrupt resource in the list is assigned a message number later that corresponds to the order it shows in the list. For example, the first message interrupt resources in the list is assigned to message 0, the second one is assigned to message 1, and so on.

To assign an MSI-X table entry to a CPU at run time, the miniport driver can call the [**NdisMConfigMSIXTableEntry**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismconfigmsixtableentry) function, which maps a table entry to an MSI-X message that already has the affinity set to the CPU. For more information about configuration operations for MSI-X table entries, see [Changing the CPU Affinity of MSI-X Table Entries](changing-the-cpu-affinity-of-msi-x-table-entries.md).

To allocate memory for a new resource-requirements list, use the [**NdisAllocateMemoryWithTagPriority**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatememorywithtagpriority) function. You can free the memory for the old resources-requirement list with the [**NdisFreeMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreememory) function.

Miniport drivers should not modify other resources, such as **CmResourceTypeMemory** and **CmResourceTypePort** resources. Miniport drivers should avoid adding a new resource to the resource list. However, NDIS 6.1 and later miniport drivers can add more message interrupt resources. If the miniport driver adds more message interrupt resources, it must not remove them from the [*MiniportStartDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp) function.

For more information about adding and removing resources, see [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](../kernel/irp-mn-filter-resource-requirements.md).
