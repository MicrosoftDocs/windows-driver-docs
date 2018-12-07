---
title: Setting NET_BUFFER_LIST Information
description: Setting NET_BUFFER_LIST Information
ms.assetid: 28f50ab4-043b-47bb-af70-e8c892288f21
keywords:
- NET_BUFFER_LIST
- header-data split WDK , NET_BUFFER_LIST
- flags WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting NET\_BUFFER\_LIST Information





A header-data split provider must set the header-data split flags in the **NblFlags** member of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures for receive indications. For split frames, a NIC must also provide the physical address of the data portion of the received frame in the **DataPhysicalAddress** member of each [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

**Note**  A miniport driver can set the **DataPhysicalAddress** member of the NET\_BUFFER structure, even if the NET\_BUFFER is not associated with a split frame. In this case, **DataPhysicalAddress** contains the physical address of the header MDL.

 

The header-data split provider combines the flags in the **NblFlags** member with a bitwise OR operation.

The header-data split provider can set the following flags even if it does not split a frame:

<a href="" id="ndis-nbl-flags-is-ipv4"></a>NDIS\_NBL\_FLAGS\_IS\_IPV4  
All of the frames in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) are IPv4 frames. If this flag is set, the NDIS\_NBL\_FLAGS\_IS\_IPV6 flag must not be set.

<a href="" id="ndis-nbl-flags-is-ipv6"></a>NDIS\_NBL\_FLAGS\_IS\_IPV6  
All of the frames in the NET\_BUFFER\_LIST are IPv6 frames. If this flag is set, the NDIS\_NBL\_FLAGS\_IS\_IPV4 flag must not be set.

<a href="" id="ndis-nbl-flags-is-tcp"></a>NDIS\_NBL\_FLAGS\_IS\_TCP  
All of the frames in the NET\_BUFFER\_LIST are TCP frames. If this flag is set, NDIS\_NBL\_FLAGS\_IS\_UDP must not be set. And either NDIS\_NBL\_FLAGS\_IS\_IPV4 or NDIS\_NBL\_FLAGS\_IS\_IPV6 must be set.

<a href="" id="ndis-nbl-flags-is-udp"></a>NDIS\_NBL\_FLAGS\_IS\_UDP  
All of the frames in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) are UDP frames. If this flag is set, NDIS\_NBL\_FLAGS\_IS\_TCP must not be set. And either NDIS\_NBL\_FLAGS\_IS\_IPV4 or NDIS\_NBL\_FLAGS\_IS\_IPV6 must be set.

Any NDIS driver can set the preceding flags for debugging, testing, or other purposes. If a driver sets these flags, the values must accurately describe the contents of the received frame. Setting these flags is recommended.

The header-data split provider can set the following header-data split flags:

<a href="" id="ndis-nbl-flags-hd-split"></a>NDIS\_NBL\_FLAGS\_HD\_SPLIT  
The header and data are split in all of the Ethernet frames that are associated with the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

<a href="" id="ndis-nbl-flags-split-at-upper-layer-protocol-header"></a>NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_HEADER  
All of the frames in the NET\_BUFFER\_LIST structure are split at the [beginning of the upper-layer-protocol header](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md). If this flag is set, either NDIS\_NBL\_FLAGS\_IS\_IPV4 or NDIS\_NBL\_FLAGS\_IS\_IPV6 must be set. Also, either NDIS\_NBL\_FLAGS\_IS\_TCP or NDIS\_NBL\_FLAGS\_IS\_UDP can be set. And NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_PAYLOAD must not be set.

<a href="" id="ndis-nbl-flags-split-at-upper-layer-protocol-payload"></a>NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_PAYLOAD  
All of the frames in a NET\_BUFFER\_LIST structure are split at the [beginning of the TCP payload](splitting-frames-at-the-tcp-payload.md) or [beginning of the UDP payload](splitting-frames-at-the-udp-payload.md). If this flag is set, either NDIS\_NBL\_FLAGS\_IS\_IPV4 or NDIS\_NBL\_FLAGS\_IS\_IPV6 must be set. Either NDIS\_NBL\_FLAGS\_IS\_TCP or NDIS\_NBL\_FLAGS\_IS\_UDP must be set. Also, NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_HEADER must not be set.

If the header-data split provider does not split a frame, the frame must be indicated with the following flags cleared in **NblFlags** :

-   NDIS\_NBL\_FLAGS\_HD\_SPLIT

-   NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_HEADER

-   NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_PAYLOAD

 

 





