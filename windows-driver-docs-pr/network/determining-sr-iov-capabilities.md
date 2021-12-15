---
title: Determining SR-IOV Capabilities
description: Determining SR-IOV Capabilities
ms.date: 04/20/2017
---

# Determining SR-IOV Capabilities


This topic describes how NDIS and overlying drivers determine the single root I/O virtualization (SR-IOV) capabilities of a network adapter. This topic contains the following information:

[Reporting SR-IOV Capabilities during *MiniportInitializeEx*](#reporting-sr-iov-capabilities-during-miniportinitializeex)

[Querying SR-IOV Capabilities by Overlying Drivers](#querying-sr-iov-capabilities-by-overlying-drivers)

## Reporting SR-IOV Capabilities during *MiniportInitializeEx*


When NDIS calls the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, the driver provides the following SR-IOV capabilities:

-   The complete set of SR-IOV hardware capabilities that the network adapter can support.

-   The SR-IOV capabilities that are currently enabled on the network adapter.

-   Whether the miniport driver is managing the PCI Express (PCIe) Physical Function (PF) or Virtual Function (VF) on the network adapter.

The miniport driver reports the SR-IOV hardware capabilities of the underlying network adapter through an [**NDIS\_SRIOV\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_capabilities) structure that is initialized in the following way:

1. The miniport driver initializes the **Header** member. The driver sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_DEFAULT.

   Starting with NDIS 6.30, the miniport driver sets the **Revision** member of **Header** to NDIS\_SRIOV\_CAPABILITIES \_REVISION\_1 and the **Size** member to NDIS\_SIZEOF\_SRIOV\_CAPABILITIES\_REVISION\_1.

2. The miniport driver sets the appropriate flags in the **SriovCapabilities** member to report SR-IOV capabilities.

   If the network adapter supports SR-IOV, the miniport driver for the PCI Express (PCIe) Physical Function of the adapter must set the following flags:

   -   NDIS\_SRIOV\_CAPS\_SRIOV\_SUPPORTED

   -   NDIS\_SRIOV\_CAPS\_PF\_MINIPORT

   > [!NOTE]
   > The miniport driver for a PCIe Virtual Function (VF) of the network adapter must set both the NDIS\_SRIOV\_CAPS\_VF\_MINIPORT flag and the NDIS\_SRIOV\_CAPS\_SRIOV\_SUPPORTED flag.    

When NDIS calls the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, the driver registers the SR-IOV capabilities of the network adapter by following these steps:

1.  The miniport driver initializes an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_hardware_assist_attributes) structure.

    The miniport driver sets the **HardwareSriovCapabilities** member to a pointer to the previously initialized [**NDIS\_SRIOV\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_capabilities) structure.

    If the registry setting for the **\*SRIOV** INF keyword has a value of one, the SR-IOV capabilities are currently enabled on the network adapter. The miniport driver sets the **CurrentSriovCapabilities** members to a pointer to the same [**NDIS\_SRIOV\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_capabilities) structure.

    If the registry setting for the **\*SRIOV** INF keyword has a value of zero, the SR-IOV capabilities are currently disabled on the network adapter. The miniport driver must set the **CurrentSriovCapabilities** member to NULL.

    For more information about the **\*SRIOV** INF keyword, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

2.  The driver calls [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) and sets the *MiniportAttributes* parameter to a pointer to the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_hardware_assist_attributes) structure.

For more information about the adapter initialization process, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

## Querying SR-IOV Capabilities by Overlying Drivers


NDIS passes the network adapter's currently enabled SR-IOV capabilities to overlying drivers that bind to the network adapter in the following way:

-   When NDIS calls an overlying filter driver's [*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach) function, NDIS passes the network adapter's SR-IOV capabilities through the *AttachParameters* parameter. This parameter contains a pointer to an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters) structure. The **SriovCapabilities** member of this structure contains a pointer to an [**NDIS\_SRIOV\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_capabilities) structure.

-   When NDIS calls an overlying protocol driver's [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function, NDIS passes the network adapter's SR-IOV capabilities through the *BindParameters* parameter. This parameter contains a pointer to an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters) structure. The **SriovCapabilities** member of this structure contains a pointer to an [**NDIS\_SRIOV\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_capabilities) structure.

NDIS also returns the [**NDIS\_SRIOV\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_capabilities) structure when it handles object identifier (OID) query requests of [OID\_SRIOV\_HARDWARE\_CAPABILITIES](./oid-sriov-hardware-capabilities.md) and [OID\_SRIOV\_CURRENT\_CAPABILITIES](./oid-sriov-current-capabilities.md) that are issued by overlying protocol or filter drivers.

 

