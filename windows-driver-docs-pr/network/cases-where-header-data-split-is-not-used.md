---
title: Cases Where Header-Data Split Is Not Used
description: Cases Where Header-Data Split Is Not Used
ms.assetid: e5d3071e-a0d1-4a66-b8aa-6823e737f242
keywords:
- header-data split WDK , when not used
- Ethernet frame splitting WDK networking , when not used
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cases Where Header-Data Split Is Not Used





This topic provides an overview of the cases where a header-data split provider must not split Ethernet frames. For a listing of the minimum requirements that a provider must meet to support header-data split, see [Minimum Requirements for Supporting Header-Data Split](minimum-requirements-for-supporting-header-data-split.md).

**Note**  There are cases where a received frame can be split outside of the header-data split provider requirements. That is, the header-data split requirements only apply to header-data split providers. In these cases, never split Ethernet frames in the middle of the IP header, IPv4 options, IPsec headers, IPv6 extension headers, or upper-layer-protocol headers, unless the first MDL contains at least as many bytes as NDIS specified for lookahead size.

 

All Ethernet frames that are not split must follow the general NDIS rules and requirements. For example, the first MDL in the chain of MDLs in a received [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure must contain either the lookahead part of the frame or the entire Ethernet frame (whichever is smaller) in a virtually contiguous buffer. NDIS sets the size of lookahead with the [OID\_GEN\_CURRENT\_LOOKAHEAD](https://msdn.microsoft.com/library/windows/hardware/ff569574) OID.

Header-data split providers:

-   Do not split non-IP frames.

-   Do not split frames if they cannot be split in one of these locations: at the beginning of the upper-layer-protocol header, the beginning of the TCP payload, or the beginning of the UDP payload.

-   Do not split frames that would exceed the maximum configured header size unless the header can be split at the [beginning of the upper-layer-protocol header](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md). For more information about the maximum header size, see [Allocating the Header Buffer](allocating-the-header-buffer.md).

-   Do not split frames that contain IPv4 options that the NIC does not recognize.

-   Do not split frames that contain IPv6 extension headers that the NIC does not recognize.

-   Do not split frames that contain TCP options that the NIC does not recognize unless they can be split at the beginning of the TCP header.

 

 





