---
title: Splitting frames at the upper-layer protocol header beginning
description: Splitting Frames at the Beginning of the Upper Layer-Protocol Headers
ms.assetid: 2559ac20-46dc-4116-9d12-b2cd634e501b
keywords:
- Ethernet frame splitting WDK networking , beginning of upper-layer protocol
- upper-layer protocols WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Splitting Frames at the Beginning of the Upper Layer-Protocol Headers





An *upper-layer protocol* is an IP transport protocol such as TCP, UDP, or ICMP.

**Note**  IPsec is not considered an upper-layer-protocol in the header-data split requirements. For more information about splitting IPsec frames, see [Splitting IPsec Frames](splitting-ipsec-frames.md).

 

If a NIC splits an Ethernet frame at the beginning of the upper-layer-protocol header, the indicated [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) must contain exactly two MDLs. The buffer that the first MDL describes must begin with the first byte of the Ethernet frame (MAC header) and the buffer that the second MDL describes must start with the first byte of the upper-layer-protocol header.

**Note**  The NIC can split TCP and UDP frames at the TCP or UDP payload. For more information, see [Splitting Frames at the TCP Payload](splitting-frames-at-the-tcp-payload.md) and [Splitting Frames at the UDP Payload](splitting-frames-at-the-udp-payload.md).

 

If the header-data split provider splits the frame at the beginning of the upper-layer-protocol header, the indicated [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures must have the NDIS\_NBL\_FLAGS\_SPLIT\_AT\_UPPER\_LAYER\_PROTOCOL\_HEADER flag set in the **NblFlags** member. For more information about setting header-data split NET\_BUFFER\_LIST flags, see [Setting NET\_BUFFER\_LIST Information](setting-net-buffer-list-information.md).

The NIC must not split a frame if the resulting header buffer has a greater length than the maximum header size. For more information about splitting frames when the maximum header size is exceeded, see [Allocating the Header Buffer](allocating-the-header-buffer.md).

 

 





