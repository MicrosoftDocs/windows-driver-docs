---
title: Splitting IPsec Frames
description: Splitting IPsec Frames
ms.assetid: 2d6841f2-6eb6-4c59-80fb-5c777fa2bf56
keywords:
- Ethernet frame splitting WDK networking , IPsec frames
- IPsec frame splitting WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Splitting IPsec Frames

\[The IPsec Task Offload feature is deprecated and should not be used.\]




A NIC can split IPsec frames at the [beginning of the upper-layer-protocol header](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md), the [beginning of the TCP payload](splitting-frames-at-the-tcp-payload.md), or the [beginning of the UDP payload](splitting-frames-at-the-udp-payload.md). The NIC should treat the IPsec information the same as an IPv4 option or IPv6 extension header.

The NIC might not be able to split the frame if the resulting header buffer has a greater length than the maximum header size. For more information about the maximum header size, see [Allocating the Header Buffer](allocating-the-header-buffer.md).

 

 





