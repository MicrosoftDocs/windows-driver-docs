---
title: Reporting Packet Coalescing Capabilities
description: Reporting Packet Coalescing Capabilities
ms.assetid: 6118F648-87FE-4B9E-9535-1602F4FF79D2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Packet Coalescing Capabilities


Miniport drivers register the following capabilities with NDIS during network adapter initialization:

-   The packet coalescing capabilities that the network adapter supports.

-   The packet coalescing capabilities that are currently enabled on the network adapter.

-   The packet coalescing receive filtering capabilities that are currently enabled on the network adapter.

**Note**  A miniport driver's support for packet coalescing can be enabled or disabled through the **\*PacketCoalescing** INF keyword setting. This setting is displayed in the **Advanced** property page for the network adapter. For more information about the packet coalescing INF file setting, see [Standardized INF Keywords for Packet Coalescing](standardized-inf-keywords-for-packet-coalescing.md).



The miniport driver reports the packet coalescing and filtering capabilities of the underlying network adapter through an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure. If the **\*PacketCoalescing** keyword setting in the registry has a value of one, packet coalescing is enabled and the miniport driver initializes the **NDIS\_RECEIVE\_FILTER\_CAPABILITIES** structure in the following way:

1.  The miniport driver initializes the **Header** member. The driver sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_DEFAULT.

    If the driver supports packet coalescing, it sets the **Revision** member of **Header** to the NDIS\_RECEIVE\_FILTER\_CAPABILITIES\_REVISION\_2 and the **Size** member to NDIS\_SIZEOF\_RECEIVE\_FILTER\_CAPABILITIES\_REVISION\_2.

2.  The miniport driver sets the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_SUPPORTED\_ON\_DEFAULT\_QUEUE flag in the **SupportedQueueProperties** member.

    If this flag is set, the network adapter must support the filtering of received multicast packets in hardware. This filtering is based on the multicast addresses that NDIS offloaded to the network adapter by sending it [OID\_802\_3\_MULTICAST\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569073) OID set requests.

    **Note**  Protocol drivers can also change the contents of the multicast address list by sending [OID\_802\_3\_ADD\_MULTICAST\_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569068) and [OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569070) requests. NDIS combines these requests into [OID\_802\_3\_MULTICAST\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569073) OID set requests.




**Note**  The adapter is required to reject any incoming multicast packet whose destination media access control (MAC) address does not match any of the multicast addresses specified by these OID set requests.




3.  The miniport driver sets the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag in the **EnabledFilterTypes** member.

    **Note**  If the driver sets this flag, it must also set the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_SUPPORTED\_ON\_DEFAULT\_QUEUE flag in the **SupportedQueueProperties** member. Otherwise, NDIS will fail the call to [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) by returning NDIS\_STATUS\_BAD\_CHARACTERISTICS.



4.  If the miniport driver sets the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the driver must support all receive filter test criteria. The driver advertises this support by setting the following flags in the **SupportedFilterTests** member:

    -   NDIS\_RECEIVE\_FILTER\_TEST\_HEADER\_FIELD\_EQUAL\_SUPPORTED

    -   NDIS\_RECEIVE\_FILTER\_TEST\_HEADER\_FIELD\_MASK\_EQUAL\_SUPPORTED

    -   NDIS\_RECEIVE\_FILTER\_TEST\_HEADER\_FIELD\_NOT\_EQUAL\_SUPPORTED

    **Note**  If the miniport driver does not set the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the driver must set the **SupportedFilterTests** member to zero.



5.  If the miniport driver sets the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the miniport driver must support the filtering of data within various fields of the media access control (MAC), IP version 4 (IPv4), and IP version 6 (IPv6) headers. The driver advertises this support by setting the following flags in the **SupportedHeaders** member:

    -   NDIS\_RECEIVE\_FILTER\_MAC\_HEADER\_SUPPORTED

    -   NDIS\_RECEIVE\_FILTER\_ARP\_HEADER\_SUPPORTED

    -   NDIS\_RECEIVE\_FILTER\_IPV4\_HEADER\_SUPPORTED

    -   NDIS\_RECEIVE\_FILTER\_IPV6\_HEADER\_SUPPORTED

    -   NDIS\_RECEIVE\_FILTER\_UDP\_HEADER\_SUPPORTED

    **Note**  If the miniport driver does not set the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the driver must set the **SupportedHeaders** member to zero.



6.  If the miniport driver sets the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the miniport driver must support the filtering of data within the media access control (MAC) header of the received packet. The driver advertises this support by setting the following flags in the **SupportedMacHeaderFields** member:

    -   NDIS\_RECEIVE\_FILTER\_MAC\_HEADER\_DEST\_ADDR\_SUPPORTED

    -   NDIS\_RECEIVE\_FILTER\_MAC\_HEADER\_PROTOCOL\_SUPPORTED

    -   NDIS\_RECEIVE\_FILTER\_MAC\_HEADER\_PACKET\_TYPE\_SUPPORTED

    **Note**  If the miniport driver does not set the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the driver must set the **SupportedMacHeaderFields** member to zero.



7.  If the miniport driver sets the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the miniport driver must support the filtering of data within the header of a received Address Resolution Protocol (ARP) packet. The driver advertises this support by setting the following flags in the **SupportedARPHeaderFields** member:

    -   NDIS\_RECEIVE\_FILTER\_ARP\_HEADER\_OPERATION\_SUPPORTED

    -   NDIS\_RECEIVE\_FILTER\_ARP\_HEADER\_SPA\_SUPPORTED

    -   NDIS\_RECEIVE\_FILTER\_ARP\_HEADER\_TPA\_SUPPORTED

    **Note**  If the miniport driver does not set the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the driver must set the **SupportedARPHeaderFields** member to zero.



8.  If the miniport driver sets the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the miniport driver must support the filtering of data within the Open Systems Interconnection (OSI) layer 3 (L3) header of a received IP version 4 (IPv4) packet. The driver advertises this support by setting the following flags in the **SupportedIPv4HeaderFields** member:

    -   NDIS\_RECEIVE\_FILTER\_IPV4\_HEADER\_PROTOCOL\_SUPPORTED

    **Note**  If the miniport driver does not set the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the driver must set the **SupportedIPv4HeaderFields** member to zero.



9.  If the miniport driver sets the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the miniport driver must support the filtering of data within the L3 header of a received IP version 6 (IPv6) packet. The driver advertises this support by setting the following flags in the **SupportedIPv6HeaderFields** member:

    -   NDIS\_RECEIVE\_FILTER\_IPV6\_HEADER\_PROTOCOL\_SUPPORTED

    **Note**  If the miniport driver does not set the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the driver must set the **SupportedIPv6HeaderFields** member to zero.



10. If the miniport driver sets the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the miniport driver must support the filtering of data within the OSI layer 4 (L4) header of a received User Datagram Protocol (UDP) packet. The driver advertises this support by setting the following flags in the **SupportedIUdpHeaderFields** member:

    -   NDIS\_RECEIVE\_FILTER\_UDP\_HEADER\_DEST\_PORT\_SUPPORTED

    **Note**  If the received UDP packet contains IPv4 options or IPv6 extension headers, the network adapter can handle the packet as if it failed the UDP filter test. In this way, the adapter can automatically drop the received packet.




**Note**  If the miniport driver does not set the NDIS\_RECEIVE\_FILTER\_PACKET\_COALESCING\_FILTERS\_ENABLED flag, the driver must set the **SupportedIUdpHeaderFields** member to zero.




11. The miniport driver must report the maximum number of tests on packet header fields that can be specified for a single packet coalescing filter. The driver specifies this value in the **MaxFieldTestsPerPacketCoalescingFilter** member.

    **Note**  Network adapters that support packet coalescing must support five or more packet header fields that can be specified for a single packet coalescing filter. If the adapter does not support packet coalescing, the miniport driver must set this value to zero.



12. The miniport driver must report the maximum number of packet coalescing filters that are supported by the network adapter. The driver specifies this value in the **MaxPacketCoalescingFilters** member.

    **Note**  Network adapters that support packet coalescing must support ten or more packet coalescing filters. If the adapter does not support packet coalescing, the miniport driver must set this value to zero.



When NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the driver reports the packet coalescing and filtering capabilities of the underlying network adapter by following these steps:

-   The miniport driver initializes an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

    If the **\*PacketCoalescing** keyword setting in the registry has a value of one, the miniport driver sets the **HardwareReceiveFilterCapabilities** member to a pointer to the previously initialized [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure.

    If the **\*PacketCoalescing** keyword setting in the registry has a value of zero, the miniport driver does not advertise support for packet coalescing. It must set the **HardwareReceiveFilterCapabilities** member to NULL.

-   The driver calls [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) and sets the *MiniportAttributes* parameter to a pointer to the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

The method that is used by miniport drivers to report the packet coalescing and filtering capabilities of the underlying network adapter is based on the NDIS 6.20 method for reporting power management capabilities. For more information about this method, see [Reporting Power Management Capabilities](reporting-power-management-capabilities.md).

For more information about the adapter initialization process, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).
