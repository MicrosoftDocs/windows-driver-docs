---
title: Determining Receive Filtering Capabilities
description: Determining Receive Filtering Capabilities
ms.assetid: 11EE5987-A2DE-4388-86D0-77285453E80A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining Receive Filtering Capabilities


This topic describes how NDIS and overlying drivers determine the receive filtering capabilities of a network adapter that supports single root I/O virtualization (SR-IOV). This topic contains the following information:

[Reporting Receive Filtering Capabilities during *MiniportInitializeEx*](#report)

[Querying Receive Filtering Capabilities by Overlying Drivers](#query)

**Note**  Only the miniport driver for the PCI Express (PCIe) Physical Function (PF) of an SR-IOV network adapter can report receive filtering capabilities. Miniport drivers for PCIe Virtual Functions (VFs) must not report the receive filtering capabilities of the SR-IOV adapter.

 

## Reporting Receive Filtering Capabilities during *MiniportInitializeEx*


When NDIS calls the PF miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the driver provides the following receive filtering capabilities:

-   The complete hardware receive filtering capabilities that the network adapter can support.

-   The receive filtering capabilities for the interfaces that are currently enabled on the network adapter.

The miniport driver reports the complete hardware receive filtering capabilities of the underlying network adapter through an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure that is initialized in the following way:

1.  The miniport driver initializes the **Header** member. The driver sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_DEFAULT.

    Starting with NDIS 6.30, the miniport driver sets the **Revision** member of **Header** to NDIS\_RECEIVE\_FILTER\_CAPABILITIES\_REVISION\_2 and the **Size** member to NDIS\_SIZEOF\_RECEIVE\_FILTER\_CAPABILITIES\_REVISION\_2.

2.  The miniport driver sets the other members of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure to the range of values for the receive filtering capabilities of the SR-IOV network adapter. For example, the miniport driver sets the appropriate flags in the **SupportedFilterTests** to specify filter test operations that the miniport driver supports.

3.  Besides SR-IOV, receive filtering is also used in the following interfaces:

    -   [NDIS Packet Coalescing](ndis-packet-coalescing.md). For more information about how to use receive filters in this interface, see [Managing Packet Coalescing Receive Filters](managing-packet-coalescing-receive-filters.md).

    -   [Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq--in-ndis-6-20.md). For more information about how to use receive filters in this interface, see [Setting and Clearing VMQ Filters](setting-and-clearing-vmq-filters.md).

    If the miniport driver supports any of these interfaces, it must also set the members of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure to the range of receive filtering capability values that are specific to the interface. For example, if the driver supports NDIS packet coalescing and SR-IOV, it must set the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_SUPPORTED\_ON\_DEFAULT\_QUEUE flag in the **SupportedQueueProperties** member.

The miniport driver reports the currently-enabled receive filtering capabilities of the underlying network adapter through an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure that is initialized in the following way:

1.  The miniport driver initializes the **Header** member. The driver sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_DEFAULT.

    Starting with NDIS 6.30, the miniport driver sets the **Revision** member of **Header** to NDIS\_RECEIVE\_FILTER\_CAPABILITIES\_REVISION\_2 and the **Size** member to NDIS\_SIZEOF\_RECEIVE\_FILTER\_CAPABILITIES\_REVISION\_2.

2.  The miniport driver sets the other members of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure to the range of values for the receive filtering capabilities of the interfaces that are currently enabled. For example, if NDIS packet coalescing is enabled, the driver must only set the members that are specific to this technology.

    Interfaces that use receive filtering are enabled or disabled through standardized INF keywords. For more information on how NDIS packet coalescing is enabled, see [Standardized INF Keywords for Packet Coalescing](standardized-inf-keywords-for-packet-coalescing.md). For more information on how SR-IOV and VMQ are enabled, see [Handling SR-IOV, VMQ, and RSS Standardized INF Keywords](handling-sr-iov--vmq--and-rss-standardized-inf-keywords.md).

When NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the driver registers the receive filtering capabilities of the network adapter by following these steps:

1.  The miniport driver initializes an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

    The miniport driver sets the **HardwareReceiveFilterCapabilities** member to the address of an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure. This structure was previously-initialized with the complete hardware receive filtering capabilities of the network adapter.

2.  If the VMQ, SR-IOV, and NDIS packet coalescing are all currently disabled on the network adapter, the miniport driver sets the **CurrentReceiveFilterCapabilities** member to NULL.

3.  If either VMQ, SR-IOV, or NDIS packet coalescing are currently enabled on the network adapter, the miniport driver must do the following:

    -   The miniport driver must initialize another [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure with the current receive filtering capabilities for the interfaces that are currently enabled on the network adapter.

        If the SR-IOV interface is enabled, there are situations in which the miniport driver must set the members of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure to the same or different values. This is because the SR-IOV interface provides a similar queuing mechanism to VMQ, but uses virtual ports (VPorts) instead of VM receive queues.

        For example, the miniport driver must set the NDIS\_RECEIVE\_FILTER\_VMQ\_FILTERS\_ENABLED flag in the **EnabledFilterTypes** member if either the VMQ or SR-IOV interface is enabled. However, the miniport driver must set the **NumQueues** member to zero if the SR-IOV interface is enabled and a nonzero value if the VMQ interface is enabled.

    -   The miniport driver sets the **CurrentReceiveFilterCapabilities** member to the address of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure that contains the current receive filtering capabilities for the currently-enabled interface.

4.  If either VMQ, SR-IOV, or NDIS packet coalescing are currently enabled on the network adapter, the miniport driver sets the **HardwareReceiveFilterCapabilities** member to the address of an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure. This structure was previously-initialized with the currently-enabled receive filtering capabilities of the network adapter.

5.  The driver calls [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) and sets the *MiniportAttributes* parameter to a pointer to the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

For more information about the adapter initialization process, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

## Querying Receive Filtering Capabilities by Overlying Drivers


NDIS passes the network adapter's currently-enabled receive filtering capabilities to overlying drivers that bind to the network adapter in the following way:

-   When NDIS calls an overlying filter driver's [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function, NDIS passes the network adapter's NIC switch capabilities through the *AttachParameters* parameter. This parameter contains a pointer to an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure. The **ReceiveFilterCapabilities** member of this structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure.

-   When NDIS calls an overlying protocol driver's [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function, NDIS passes the network adapter's NIC switch capabilities through the *BindParameters* parameter. This parameter contains a pointer to an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure. The **ReceiveFilterCapabilities** member of this structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure.

NDIS also returns the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure when it handles object identifier (OID) query requests of [OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569786) and [OID\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569791) that are issued by overlying protocol or filter drivers.

 

 





