---
title: Resetting a Virtual Function
description: Resetting a Virtual Function
ms.assetid: 4B7A4E02-6383-45FB-9F75-D17C047C40D0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Resetting a Virtual Function


An overlying driver issues an object identifier (OID) set request of [OID\_SRIOV\_RESET\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451889) to reset a specified PCI Express (PCIe) Virtual Function (VF). The VF is a hardware component of a network adapter that supports single root I/O virtualization. Overlying drivers issue this OID set request to the miniport driver of the PCI Express (PCIe) Physical Function (PF).

For example, the virtualization stack runs in the management operating system of the Hyper-V parent partition. Before the stack detaches a VF from a Hyper-V child partition, it requests a Function Level Reset (FLR) on the VF. Because the FLR is a privileged operation, it can be performed only by the PF miniport driver that also runs in the management operating system. To request an FLR of a specified VF, the virtualization stack issues the [OID\_SRIOV\_RESET\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451889)request to the PF miniport driver.

Before it issues this OID set request, the overlying driver must initialize an [**NDIS\_SRIOV\_RESET\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451682) structure. The driver must set the **VFId** member to the identifier of the VF to be reset.

When it handles this OID request, the PF miniport driver must follow these guidelines:

-   The PF miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_RESET\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451682) structure, has resources that have been previously allocated. The PF miniport driver allocates resources for a VF during an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814). If resources for the specified VF have not been allocated, the driver must fail the OID request.

-   The reset operation must only affect the specified VF. The operation must not affect other VFs or the PF on the same network adapter.

 

 





