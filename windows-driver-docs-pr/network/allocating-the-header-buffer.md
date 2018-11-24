---
title: Allocating the Header Buffer
description: Allocating the Header Buffer
ms.assetid: 7a6e87ce-a0b8-45ce-961e-f09d5ca919cb
keywords:
- header-data split WDK , buffer allocation
- maximum header size WDK header-data split
- buffer allocations WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating the Header Buffer





NDIS specifies the maximum header size that a miniport driver should allocate in the **MaxHeaderSize** member of the [**NDIS\_HD\_SPLIT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565694) structure. For more information about setting header-data split attributes, see [Initializing a Header-Data Split Provider](initializing-a-header-data-split-provider.md).

When a NIC splits the header and data in a received Ethernet frame, the size of the header portion of the indicated Ethernet frame must not exceed the **MaxHeaderSize** value.

If an IP header contains IPv4 options, IPsec headers, or IPv6 extension headers, and if the header exceeds the **MaxHeaderSize** value, the NIC must not split the frame.

If a header that includes the UDP header, TCP header, or TCP options exceeds the **MaxHeaderSize** value, the NIC must either split the frame at the [beginning of the upper-layer-protocol header](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md) or must not split the frame.

 

 





