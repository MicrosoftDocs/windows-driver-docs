---
title: Splitting Fragmented IP Frames
description: Splitting Fragmented IP Frames
ms.assetid: faee7ec8-a49e-4107-a83f-d97391d69b43
keywords:
- Ethernet frame splitting WDK networking , fragmented IP frames
- fragmented IP frames WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Splitting Fragmented IP Frames





If a fragmented IP frame contains the upper-layer-protocol header, a NIC must split the frame at the [beginning of upper-layer-protocol header](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md) or must not split the frame. That is, the NIC must not split fragmented IP frames at the beginning of the TCP or UDP payload.

If a fragmented IPv4 frame does not contain the upper-layer-protocol header, the NIC must split the frame at the beginning of the UDP or TCP payload or must not split the frame.

If a fragmented IPv6 frame does not contain the upper-layer-protocol header, the NIC must not split the frame.

For more information about splitting frames at the beginning of the upper-layer-protocol header, see [Splitting Frames at the Beginning of the Upper-Layer-Protocol Headers](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md).

 

 





