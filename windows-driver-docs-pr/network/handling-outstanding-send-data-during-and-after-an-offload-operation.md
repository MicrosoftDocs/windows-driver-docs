---
title: Handling outstanding send data during and after offload operation
description: Handling Outstanding Send Data During and After an Offload Operation
ms.assetid: 5dc8bf17-c4f5-4626-b879-4cd83b0243c0
keywords:
- state offloading process WDK TCP chimney offload , outstanding send data
- offloading state process WDK TCP chimney offload , outstanding send data
- outstanding send data WDK TCP chimney offload
- send data outstanding WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Outstanding Send Data During and After an Offload Operation


\[The TCP chimney offload feature is deprecated and should not be used.\]




When the host stack initiates the offload of a TCP connection, there might be outstanding send data on the connection. This data can include:

-   Data that the host stack has sent but that has not yet been acknowledged by the remote host.

-   Data that the host stack has not yet sent.

When offloading a TCP connection when there is outstanding send data on the connection, the host stack specifies a pointer in the **NetBufferListChain** member of the [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure that immediately precedes the delegated TCP state for that TCP connection. **NetBufferListChain** points to a NET\_BUFFER\_LIST structure that can be stand-alone or the first structure in a linked list of NET\_BUFFER\_LIST structures. Each NET\_BUFFER\_LIST structure in the linked list describes one [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure. The memory descriptor lists (MDLs) that are associated with the NET\_BUFFER structures in the list contain the send data.

The [**TCP\_OFFLOAD\_STATE\_DELEGATED**](https://msdn.microsoft.com/library/windows/hardware/ff570939) structure that is offloaded for the connection contains a pointer in the **SendDataHead** member and a pointer in the **SendDataTail** member. Each of these pointers points to a single NET\_BUFFER\_LIST structure in the linked list that is referenced by **NetBufferListChain** :

-   The pointer in **SendDataHead** points to the first NET\_BUFFER\_LIST structure whose NET\_BUFFER structure has send data associated with it.

-   The pointer in **SendDataTail** points to the last NET\_BUFFER\_LIST structure whose NET\_BUFFER structure has send data associated with it.

Note that the offload target does not have to copy the send data into its own buffers. The offload target can transmit the send data directly from the buffers that are supplied by the host stack.

In the TCP delegated state (the TCP\_OFFLOAD\_STATE\_DELEGATED structure) for the connection that is being offloaded, the host stack also specifies the following members that are related to send data. For more information, see [Send Data That Contains Data to Be Retransmitted](send-data-that-contains-data-to-be-retransmitted.md).

<a href="" id="snduna"></a>**SndUna**  
The sequence number for the first byte of unacknowledged data (see SND.UNA in RFC 793).

<a href="" id="sndnxt"></a>**SndNxt**  
The sequence number for the next byte to send on the connection (see SND.NEXT in RFC 793).

<a href="" id="sndmax"></a>**SndMax**  
The maximum sequence number that has been sent on the connection.

 

 





