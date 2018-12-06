---
title: Returning Completion Status of an Initiate Offload Operation
description: Returning Completion Status of an Initiate Offload Operation
ms.assetid: 8405d881-6a0d-4c4e-85db-a8cada8f6e11
keywords:
- state offloading process WDK TCP chimney offload , completion status
- offloading state process WDK TCP chimney offload , completion status
- completion status of initiate operation WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning Completion Status of an Initiate Offload Operation


\[The TCP chimney offload feature is deprecated and should not be used.\]




Before calling [**NdisMInitiateOffloadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563604), the offload target must write a completion status to the **Status** member of each [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure in the state tree. The offload target can write one of the following NDIS\_STATUS values:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The offload target successfully offloaded the following:

-   The offload state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure.

-   The offload state that is associated with all of the immediately dependent NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structures. An *immediately dependent structure* is a structure that is referenced by the pointer in the **DependentBlockList** member or a structure that is linked directly or indirectly to such a structure through a next block link.

<a href="" id="ndis-status-offload-partial-success"></a>NDIS\_STATUS\_OFFLOAD\_PARTIAL\_SUCCESS  
The offload target successfully offloaded the offload state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure. However, the offload target failed to offload the offload state that is associated with one or more of the immediately dependent NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structures.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The offload target failed to offload the state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure. The cause of the failure cannot be categorized.

<a href="" id="ndis-status-resources"></a>NDIS\_STATUS\_RESOURCES  
The offload target failed to offload the state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure because the offload target could not allocate sufficient host memory.

<a href="" id="ndis-status-offload-tcp-entries"></a>NDIS\_STATUS\_OFFLOAD\_TCP\_ENTRIES  
The offload target failed to offload the state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure because the offload target could not allocate a TCP connection state object.

<a href="" id="ndis-status-offload-path-entries"></a>NDIS\_STATUS\_OFFLOAD\_PATH\_ENTRIES  
The offload target failed to offload the state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure because the offload target could not allocate a path state object.

<a href="" id="ndis-status-offload-neighbor-entries"></a>NDIS\_STATUS\_OFFLOAD\_NEIGHBOR\_ENTRIES  
The offload target failed to offload the state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure because the offload target could not allocate a neighbor state object.

<a href="" id="ndis-status-offload-hw-address-entries"></a>NDIS\_STATUS\_OFFLOAD\_HW\_ADDRESS\_ENTRIES  
The offload target failed to offload the state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure because the host stack specified a non-NULL value in the **DlSourceAddress** member of the [**NEIGHBOR\_OFFLOAD\_STATE\_CONST**](https://msdn.microsoft.com/library/windows/hardware/ff568324) structure, and the offload target either does not support configurable source medium access control (MAC) addresses or cannot accept additional source MAC addresses.

<a href="" id="ndis-status-offload-ip-address-entries"></a>NDIS\_STATUS\_OFFLOAD\_IP\_ADDRESS\_ENTRIES  
The offload target failed to offload the state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure because the offload target could not allocate a data structure for the source IP address that is referenced by the pointer in the **SourceAddress** member of the [**PATH\_OFFLOAD\_STATE\_CONST**](https://msdn.microsoft.com/library/windows/hardware/ff569984) structure.

<a href="" id="ndis-status-offload-tcp-xmit-buffer"></a>NDIS\_STATUS\_OFFLOAD\_TCP\_XMIT\_BUFFER  
The offload target failed to offload the state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure because the offload target could not allocate enough TCP transmit buffers.

<a href="" id="ndis-status-offload-tcp-rcv-buffer"></a>NDIS\_STATUS\_OFFLOAD\_TCP\_RCV\_BUFFER  
The offload target failed to offload the state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure because the offload target could not allocate enough TCP receive buffers.

<a href="" id="ndis-status-offload-tcp-rcv-window"></a>NDIS\_STATUS\_OFFLOAD\_TCP\_RCV\_WINDOW  
The offload target failed to offload the state that is associated with the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure because the **InitialRcvWnd** member that is specified in the [**TCP\_OFFLOAD\_STATE\_CACHED**](https://msdn.microsoft.com/library/windows/hardware/ff570937) structure is larger than the offload target can support.

<a href="" id="ndis-status-offload-vlan-entries"></a>NDIS\_STATUS\_OFFLOAD\_VLAN\_ENTRIES  
The offload target has run out of resources to track additional VLAN identifiers.

<a href="" id="ndis-status-offload-vlan-mismatch"></a>NDIS\_STATUS\_OFFLOAD\_VLAN\_MISMATCH  
The **VlanId** member of the NEIGHBOR\_OFFLOAD\_STATE\_CONST structure is nonzero and does not match one of the interface VLAN identifiers.

<a href="" id="ndis-status-offload-path-mtu"></a>NDIS\_STATUS\_OFFLOAD\_PATH\_MTU  
The path maximum transmission unit (MTU) for the TCP connection is larger than what the offload target supports.

<a href="" id="ndis-status-offload-connection-rejected"></a>NDIS\_STATUS\_OFFLOAD\_CONNECTION\_REJECTED  
The offload target failed to offload the connection because the offload target determined this connection is not a good candidate for offload.

 

 





