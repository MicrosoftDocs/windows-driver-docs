---
title: Splitting IPv6 Frames
description: Splitting IPv6 Frames
ms.assetid: fe18ccfb-29d0-4b57-9308-a9d4a9c6777a
keywords:
- Ethernet frame splitting WDK networking , IPv6 frames
- IPv6 frames WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Splitting IPv6 Frames





To support header-data split, a NIC must support splitting IPv6 Ethernet frames without any IPv6 extension headers. The NIC must be able to split such frames at the beginning of upper-layer-protocol header.

Support for IPv6 Ethernet frames with IPv6 extension headers is optional. A NIC can support some IPv6 options and not support others. The NIC must not split IPv6 frames that contain IPv6 extension headers that is does not support. The header portion of a split frame must contain the entire IPv6 header and all of the IPv6 extension headers that are present.

The NIC can also support header-data split for fragmented IPv6 frames. For more information about fragmented IPv4 frames, see [Splitting Fragmented IP Frames](splitting-fragmented-ip-frames.md).

**Note**  Supporting an IPv4 option, an IPv6 extension header or a TCP option, for the purposes of header-data requirements, implies the ability of the NIC to recognize the element, determine its length, include it in the header MDL and locate its end and the beginning of the next element in the frame.

 

If the header-data split provider splits an IPv6 frame, the indicated [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures must have the NDIS\_NBL\_FLAGS\_IS\_IPV6 flag set in the **NblFlags** member. For complete information about setting header-data split flags in the NET\_BUFFER\_LIST structure, see [Setting NET\_BUFFER\_LIST Information](setting-net-buffer-list-information.md).

Additional Ethernet frame characteristics determine how to split IPv6 frames. If the frame is fragmented, see [Splitting Fragmented IP Frames](splitting-fragmented-ip-frames.md). If the frame contains TCP information, see [Splitting Frames at the TCP Payload](splitting-frames-at-the-tcp-payload.md). If the frame contains UDP information, see [Splitting Frames at the UDP Payload](splitting-frames-at-the-udp-payload.md). For all other cases, see [Splitting Frames Other Than TCP and UDP](splitting-frames-other-than-tcp-and-udp.md).

 

 





