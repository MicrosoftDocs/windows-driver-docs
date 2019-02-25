---
title: Determining SR-IOV Capabilities
description: Determining SR-IOV Capabilities
ms.assetid: 61895987-2469-471E-BB29-FF1CDD2869DC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining SR-IOV Capabilities


This topic describes how NDIS and overlying drivers determine the single root I/O virtualization (SR-IOV) capabilities of a network adapter. This topic contains the following information:

[Reporting SR-IOV Capabilities during *MiniportInitializeEx*](#report)

[Querying SR-IOV Capabilities by Overlying Drivers](#query)

## Reporting SR-IOV Capabilities during *MiniportInitializeEx*


When NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the driver provides the following SR-IOV capabilities:

-   The complete set of SR-IOV hardware capabilities that the network adapter can support.

-   The SR-IOV capabilities that are currently enabled on the network adapter.

-   Whether the miniport driver is managing the PCI Express (PCIe) Physical Function (PF) or Virtual Function (VF) on the network adapter.

The miniport driver reports the SR-IOV hardware capabilities of the underlying network adapter through an [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure that is initialized in the following way:

1. The miniport driver initializes the **Header** member. The driver sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_DEFAULT.

   Starting with NDIS 6.30, the miniport driver sets the **Revision** member of **Header** to NDIS\_SRIOV\_CAPABILITIES \_REVISION\_1 and the **Size** member to NDIS\_SIZEOF\_SRIOV\_CAPABILITIES\_REVISION\_1.

2. The miniport driver sets the appropriate flags in the **SriovCapabilities** member to report SR-IOV capabilities.

   If the network adapter supports SR-IOV, the miniport driver for the PCI Express (PCIe) Physical Function of the adapter must set the following flags:

   -   NDIS\_SRIOV\_CAPS\_SRIOV\_SUPPORTED

   -   NDIS\_SRIOV\_CAPS\_PF\_MINIPORT

   > [!NOTE]
   > The miniport driver for a PCIe Virtual Function (VF) of the network adapter must set both the NDIS\_SRIOV\_CAPS\_VF\_MINIPORT flag and the NDIS\_SRIOV\_CAPS\_SRIOV\_SUPPORTED flag.    

When NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the driver registers the SR-IOV capabilities of the network adapter by following these steps:

1.  The miniport driver initializes an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

    The miniport driver sets the **HardwareSriovCapabilities** member to a pointer to the previously initialized [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure.

    If the registry setting for the **\*SRIOV** INF keyword has a value of one, the SR-IOV capabilities are currently enabled on the network adapter. The miniport driver sets the **CurrentSriovCapabilities** members to a pointer to the same [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure.

    If the registry setting for the **\*SRIOV** INF keyword has a value of zero, the SR-IOV capabilities are currently disabled on the network adapter. The miniport driver must set the **CurrentSriovCapabilities** member to NULL.

    For more information about the **\*SRIOV** INF keyword, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

2.  The driver calls [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) and sets the *MiniportAttributes* parameter to a pointer to the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

For more information about the adapter initialization process, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

## Querying SR-IOV Capabilities by Overlying Drivers


NDIS passes the network adapter's currently enabled SR-IOV capabilities to overlying drivers that bind to the network adapter in the following way:

-   When NDIS calls an overlying filter driver's [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function, NDIS passes the network adapter's SR-IOV capabilities through the *AttachParameters* parameter. This parameter contains a pointer to an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure. The **SriovCapabilities** member of this structure contains a pointer to an [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure.

-   When NDIS calls an overlying protocol driver's [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function, NDIS passes the network adapter's SR-IOV capabilities through the *BindParameters* parameter. This parameter contains a pointer to an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure. The **SriovCapabilities** member of this structure contains a pointer to an [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure.

NDIS also returns the [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure when it handles object identifier (OID) query requests of [OID\_SRIOV\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/hh451862) and [OID\_SRIOV\_CURRENT\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/hh451859) that are issued by overlying protocol or filter drivers.

 

 





