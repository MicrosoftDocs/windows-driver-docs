---
title: Splitting IPv4 Frames
description: Splitting IPv4 Frames
ms.assetid: 1906dc31-7969-49da-adc4-8a174923d9d5
keywords:
- Ethernet frame splitting WDK networking , IPv4 frames
- IPv4 frames WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Splitting IPv4 Frames





To support header-data split, a NIC must support splitting IPv4 Ethernet frames that have no IPv4 options. The NIC must be able to split such frames at the [beginning of upper-layer-protocol header](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md).

Support for IPv4 Ethernet frames with IPv4 options is optional. The NIC can support some IPv4 options and not the others. The NIC must not split IPv4 frames that contain IPv4 options that it does not recognize. The header portion of a split frame must contain the entire IPv4 header and all of the IPv4 options that are present.

The NIC can also support header-data split for fragmented IPv4 frames. For more information about fragmented IPv4 frames, see [Splitting Fragmented IP Frames](splitting-fragmented-ip-frames.md).

**Note**  Supporting an IPv4 option, an IPv6 extension header or a TCP option, for the purposes of header-data requirements, implies the ability of the NIC to recognize the element, determine its length, include it in the header MDL and locate its end and the beginning of the next element in the frame.

 

If the header-data split provider splits an IPv4 frame, the indicated [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures must have the NDIS\_NBL\_FLAGS\_IS\_IPV4 flag set in the **NblFlags** member. For complete information about setting header-data split flags in the NET\_BUFFER\_LIST structure, see [Setting NET\_BUFFER\_LIST Information](setting-net-buffer-list-information.md).

Additional Ethernet frame characteristics determine how to split IPv4 frames. If the IP frame is fragmented, see [Splitting Fragmented IP Frames](splitting-fragmented-ip-frames.md). If the frame contains TCP information, see [Splitting Frames at the TCP Payload](splitting-frames-at-the-tcp-payload.md). If the frame contains UDP information, see [Splitting Frames at the UDP Payload](splitting-frames-at-the-udp-payload.md). For all other cases, see [Splitting Frames Other Than TCP and UDP](splitting-frames-other-than-tcp-and-udp.md).

 

 





