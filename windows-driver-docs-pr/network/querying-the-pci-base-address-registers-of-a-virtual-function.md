---
title: Querying the PCI Base Address Registers of a Virtual Function
description: Querying the PCI Base Address Registers of a Virtual Function
ms.assetid: 99C2BF61-E87E-4C3B-BE7E-C16B5318EC1A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying the PCI Base Address Registers of a Virtual Function

**Note** This method can only be used by overlying drivers that run in the management operating system of the Hyper-V parent partition.

The PCI bus driver, which runs in the management operating system of the Hyper-V parent partition, queries the memory or I/O address space requirements of each PCI Base Address Register (BAR) of the network adapter. The PCI bus driver performs this query when it first detects the adapter on the bus.

Through this PCI BAR query, the PCI bus driver determines the following:

-   Whether a PCI BAR is supported by the network adapter.

-   If a BAR is supported, how much memory or I/O address space is required for the BAR.

The PCI driver performs this PCI BAR query in following way:

1.  The PCI driver first writes all ones to a BAR.

2.  The PCI driver then reads the BAR to determine the required memory or address space that is required by the BAR. A value of zero indicates that the BAR is not supported by the network adapter.

The virtual PCI (VPCI) bus driver runs in the guest operating system of a Hyper-V child partition. When a PCI Express (PCIe) Virtual Function (VF) is attached to the child partition, the VPCI bus driver exposes a virtual network adapter for the VF (*VF network adapter*). Before it does this, the VPCI bus driver must perform a PCI BAR query to determine the required memory or address space that is required by the VF network adapter.

Because access to the PCI configuration space is a privileged operation, it can only be performed by components that run in the management operating system of a Hyper-V parent partition. When the VPCI bus driver queries the PCI BARs, NDIS issues an object identifier (OID) query request of [OID\_SRIOV\_PROBED\_BARS](https://msdn.microsoft.com/library/windows/hardware/hh451870) to the PF miniport driver. The results returned by this OID query request are forwarded to the VPCI bus driver so that it can determine how much memory address space would be needed by the VF network adapter.

**Note**  OID requests of OID\_SRIOV\_BAR\_RESOURCES can only be issued by NDIS. The OID request must not be issued by overlying drivers, such as protocol or filter drivers.

 

The OID\_SRIOV\_PROBED\_BARS query request contains an [**NDIS\_SRIOV\_PROBED\_BARS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451679) structure. When the PF miniport driver handles this OID, the driver must return the PCI BAR values within the array referenced by the **BaseRegisterValuesOffset** member of the **NDIS\_SRIOV\_PROBED\_BARS\_INFO** structure. For each offset within the array, the PF miniport driver must set the array element to the ULONG value of the BAR at the same offset within the physical network adapter's PCI configuration space.

Each BAR value returned by the driver must be the same value that would follow a PCI BAR query as performed by the PCI driver that runs in the management operating system. The PF miniport driver can call [**NdisMQueryProbedBars**](https://msdn.microsoft.com/library/windows/hardware/hh451520) to determine this information.

For more information about the base address registers of a PCI device, see the *PCI Local Bus Specification*.

 

 





